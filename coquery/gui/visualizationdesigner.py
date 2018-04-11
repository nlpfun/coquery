# -*- coding: utf-8 -*-
"""
visualizationDesigner.py is part of Coquery.

Copyright (c) 2017 Gero Kunter (gero.kunter@coquery.org)

Coquery is released under the terms of the GNU General Public License (v3).
For details, see the file LICENSE that you should have received along
with Coquery. If not, see <http://www.gnu.org/licenses/>.
"""

from __future__ import unicode_literals
from __future__ import division

import imp
import logging
import sys
import os
import glob

from .. import options
from coquery.unicode import utf8
from coquery.defines import (PALETTE_BW,
                             msg_visualization_error,
                             msg_visualization_module_error)

from .pyqt_compat import (QtWidgets, QtCore, QtGui, get_toplevel_window,
                          COLOR_NAMES)

import matplotlib as mpl

from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT)
from matplotlib.backends.backend_qt5 import SubplotToolQt

import pandas as pd
import seaborn as sns

from ..visualizer.visualizer import get_grid_layout
from coquery.visualizer.colorizer import COQ_SINGLE
from .ui.visualizationDesignerUi import Ui_VisualizationDesigner
from . import classes
from .app import get_icon

mpl.use("Qt5Agg")
mpl.rcParams["backend"] = "Qt5Agg"

app = get_toplevel_window()


class MyTool(SubplotToolQt):
    def __init__(self, *args, **kwargs):
        super(MyTool, self).__init__(*args, **kwargs)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            try:
                self.parent().keyPressEvent(event)
            except AttributeError:
                try:
                    self.parent().keyPressEvent(event)
                except AttributeError:
                    pass
        else:
            super(MyTool, self).keyPressEvent(event)

    def functight(self):
        return super(MyTool, self).functight()


class NavigationToolbar(NavigationToolbar2QT):
    """
    See matplotlib/backends/backend_qt5.py for the implementation.
    """
    toolitems = [t for t in NavigationToolbar2QT.toolitems if
                 t[0] not in ("Subplots", "Customize")]

    def __init__(self, canvas, parent, coordinates=True):
        super(NavigationToolbar, self).__init__(canvas, parent, coordinates)

        self._buttons = {}

        for x in self.children():
            if isinstance(x, QtWidgets.QToolButton):
                self._buttons[str(x.text())] = x

        self._buttons["Zoom"].toggled.connect(self.toggle_zoom)
        self._buttons["Pan"].toggled.connect(self.toggle_pan)

        self._zoom = False
        self._pan = False

    def toggle_zoom(self):
        self._zoom = not self._zoom

    def toggle_pan(self):
        self._pan = not self._pan

    def isPanning(self):
        return self._pan

    def isZooming(self):
        return self._zoom


class VisualizationDesigner(QtWidgets.QDialog):
    moduleLoaded = QtCore.Signal(str, str, object)
    allLoaded = QtCore.Signal()
    dataRequested = QtCore.Signal()
    visualizers = {}

    def __init__(self, session, parent=None):
        super(VisualizationDesigner, self).__init__(parent)
        self.session = session
        self.vis = None
        self.df = None
        self._current_color = QtGui.QColor("#55aaff")

        self.ui = Ui_VisualizationDesigner()
        self.ui.setupUi(self)

        self.ui.combo_qualitative.addItem(PALETTE_BW)

        # disable unsupported elements:
        self.ui.radio_custom.hide()
        self.ui.combo_custom.hide()
        self.ui.button_remove_custom.hide()
        self.ui.label_38.hide()
        #self.ui.spin_number.hide()
        #self.ui.label_37.hide()

        self.populate_figure_types()

        self.restore_settings()
        self.display_values()

        self.check_figure_types()
        self.check_wrapping()
        self.check_grid_layout()
        self.check_clear_buttons()
        self._finetune_ui()
        self.change_figure_type()

        self.setup_connections()

        self.dialog = QtWidgets.QWidget()
        self.dialog_layout = QtWidgets.QVBoxLayout(self.dialog)
        self.dialog.resize(self.viewer_size)
        self.dialog.setWindowTitle("<no figure> – Coquery")
        self.dialog.setWindowIcon(get_icon(
            "coquerel_icon.png", small_n_flat=False))
        self.dialog.show()

    def connectDataAvailableSignal(self, signal):
        signal.connect(self.data_available)

    def data_available(self):
        self.ui.button_refresh_data.show()
        new_label = QtWidgets.QApplication.instance().translate(
                "VisualizationDesigner", "<b>New data available</b>", None)
        if len(self.df):
            new_label = "{}<br>{}".format(self.get_label(), new_label)
        self.ui.label_dimensions.setText(new_label)

    def get_label(self):
        if len(self.df):
            label = QtWidgets.QApplication.instance().translate(
                "VisualizationDesigner", "{col} columns, {row} rows", None)
        else:
            label = QtWidgets.QApplication.instance().translate(
                "VisualizationDesigner", "No data available", None)

        label = label.format(col=len(self.categorical) + len(self.numerical),
                             row=len(self.df))
        return label

    def setup_data(self, df, session, alias=None):
        self.blockSignals(True)

        self.ui.table_categorical.clear()
        self.ui.table_numerical.clear()
        self.df = df
        self.session = session
        self.alias = alias or {}
        for i, x in enumerate(df.columns):
            if self.df[x].dtype == bool:
                self.df[x] = self.df[x].astype(str)

        self.populate_variable_lists()
        self.ui.label_dimensions.setText(self.get_label())
        self.check_figure_types()

        self.ui.button_refresh_data.hide()

        self.blockSignals(False)

    def _finetune_ui(self):
        """
        Finetune the UI: set widths, set icons.
        """
        self.ui.list_figures.setDragEnabled(False)
        self.ui.list_figures.setDragDropMode(self.ui.list_figures.NoDragDrop)
        w = app.style().pixelMetric(QtWidgets.QStyle.PM_ScrollBarExtent)
        self.ui.list_figures.setMinimumWidth(180 + w)
        self.ui.list_figures.setMaximumWidth(180 + w)

        icon_size = QtCore.QSize(QtWidgets.QLabel().sizeHint().height(),
                                 QtWidgets.QLabel().sizeHint().height())
        pix_col = get_icon("Select Column").pixmap(icon_size)
        pix_row = get_icon("Select Row").pixmap(icon_size)

        self.ui.icon_columns.setPixmap(pix_col)
        self.ui.icon_rows.setPixmap(pix_row)

        self.ui.button_clear_x.setIcon(get_icon("Clear Symbol"))
        self.ui.button_clear_y.setIcon(get_icon("Clear Symbol"))
        self.ui.button_clear_z.setIcon(get_icon("Clear Symbol"))
        self.ui.button_clear_columns.setIcon(get_icon("Clear Symbol"))
        self.ui.button_clear_rows.setIcon(get_icon("Clear Symbol"))

    def add_figure_type(self, label, icon, vis_class):
        self.figure_types.append((label, icon, vis_class))

    def get_figure_item(self, label, icon, vis_class):
        item = QtWidgets.QListWidgetItem(label)
        try:
            item.setIcon(get_icon(icon, small_n_flat=False))
        except Exception as e:
            item.setIcon(get_icon(icon, size="64x64"))

        size = QtCore.QSize(
            180, 64 + 0 * QtWidgets.QLabel().sizeHint().height())

        item.setSizeHint(size)
        item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEnabled)
        item.setData(QtCore.Qt.UserRole, vis_class)
        return item

    def load_figure_types(self):
        for module_name in find_visualizer_modules():
            module = get_visualizer_module(module_name)
            visualizations = getattr(module, "provided_visualizations", [])
            for vis_class in visualizations:
                name = getattr(vis_class, "name",
                               "Unnamed ({})".format(module_name))
                icon = getattr(vis_class, "icon", "Grid")
                VisualizationDesigner.visualizers[name] = vis_class
                self.moduleLoaded.emit(name, icon, vis_class)
        self.allLoaded.emit()

    def populate_figure_types(self):
        self.figure_types = []
        self.moduleLoaded.connect(self.add_figure_type)
        self.allLoaded.connect(self.check_figure_types)
        #self.figure_loader = QtCore.QThread(self)
        #self.figure_loader.run = self.load_figure_types
        #self.figure_loader.start()
        self.load_figure_types()
        self.allLoaded.emit()

    def populate_variable_lists(self):
        d = self.get_gui_values()
        used = [d[x]
                for x in ["data_x", "data_y", "data_z", "columns", "rows"]
                if x in d and d[x]]

        self.categorical = [col for col in self.df.columns
                            if self.df.dtypes[col] in (object, bool) and
                            col not in used and
                            not col.startswith(("coquery_invisible"))]
        self.numerical = [col for col in self.df.columns
                          if self.df.dtypes[col] in (int, float) and
                          col not in used and
                          not col.startswith(("coquery_invisible"))]

        for col in self.categorical:
            label = self.alias.get(col) or col

            new_item = QtWidgets.QListWidgetItem(label)
            new_item.setData(QtCore.Qt.UserRole, col)
            new_item.setToolTip(new_item.text())
            if label in self.session.Resource.time_features:
                new_item.setIcon(get_icon("Clock"))

            self.ui.table_categorical.addItem(new_item)

        for col in self.numerical:
            label = self.alias.get(col) or col

            new_item = QtWidgets.QListWidgetItem(label)
            new_item.setData(QtCore.Qt.UserRole, col)
            new_item.setToolTip(new_item.text())
            if label in self.session.Resource.time_features:
                new_item.setIcon(get_icon("Clock"))

            self.ui.table_numerical.addItem(new_item)

        if len(self.df):
            # add "row number" variable
            col = "statistics_row_number"
            options.cfg.verbose = True
            label = self.alias.get(col) or col
            options.cfg.verbose = False

            new_item = QtWidgets.QListWidgetItem(label)
            new_item.setData(QtCore.Qt.UserRole, col)
            new_item.setToolTip(new_item.text())

            self.ui.table_numerical.addItem(new_item)

        ## add functions
        #for func in [Freq]:
            #new_item = QtWidgets.QListWidgetItem("{} (generated)".format(
                #func.get_name()))
            #new_item.setData(QtCore.Qt.UserRole,
                                #"func_{}".format(func._name))
            #new_item.setData(
                #QtCore.Qt.FontRole,
                #QtWidgets.QFont(QtWidgets.QLabel().font().family(),
                                #italic=True))
            #self.ui.table_numerical.addItem(new_item)

    def setup_canvas(self, figure):
        if hasattr(self, "canvas"):
            self.dialog_layout.removeWidget(self.canvas)
            self.canvas.hide()
            del self.canvas
        if hasattr(self, "toolbar"):
            self.dialog_layout.removeWidget(self.toolbar)
            self.toolbar.hide()
            del self.toolbar

        # figure canvas:
        self.canvas = FigureCanvas(figure)
        self.canvas.setParent(self)
        self.canvas.setSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                  QtWidgets.QSizePolicy.Expanding)
        self.canvas.updateGeometry()
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.dialog_layout.addWidget(self.toolbar)
        self.dialog_layout.addWidget(self.canvas)

        try:
            _w = self.ui.layout_margins.takeAt(0)
            _w.widget().hide()
            self.ui.layout_margins.removeWidget(_w.widget())
            del _w
        except Exception as e:
            print(e)

        self.tool = MyTool(self.canvas.figure, self)
        opt_text = QtWidgets.QApplication.instance().translate(
            "VisualizationDesigner", "&Optimize margins", None)

        # Someone made the buttons in the tool private in one of the recent
        # versions of matplotlib (2.1, I think). Thank you very much for that.
        # Not.
        if hasattr(self.tool, "resetbutton"):
            self.tool.resetbutton.hide()
            self.tool.donebutton.hide()
            self.tool.tightlayout.setText(opt_text)
        elif hasattr(self.tool, "_widgets"):
            for widget in self.tool._widgets:
                if widget in ("Close", "Reset", "Export values"):
                    self.tool._widgets[widget].hide()
                if widget == "Tight layout":
                    self.tool._widgets[widget].setText(opt_text)

        self.tool.show()
        self.ui.layout_margins.insertWidget(0, self.tool)

    def setup_connections(self):
        """
        Connects the GUI signals to the appropriate slots.
        """

        self.ui.button_refresh_data.clicked.connect(
            lambda: self.dataRequested.emit())

        ## Hook up palette combo boxes:
        #self.ui.combo_qualitative.currentIndexChanged.connect(
            #lambda x: self.change_palette())
        #self.ui.combo_sequential.currentIndexChanged.connect(
            #lambda x: self.change_palette())
        #self.ui.combo_diverging.currentIndexChanged.connect(
            #lambda x: self.change_palette())

        self.ui.combo_qualitative.currentIndexChanged.connect(
            lambda x: self.set_radio(self.ui.radio_qualitative))
        self.ui.combo_sequential.currentIndexChanged.connect(
            lambda x: self.set_radio(self.ui.radio_sequential))
        self.ui.combo_diverging.currentIndexChanged.connect(
            lambda x: self.set_radio(self.ui.radio_diverging))

        # Hook up palette radio buttons:
        self.ui.radio_qualitative.pressed.connect(
            lambda: self.set_radio(self.ui.radio_qualitative))
        self.ui.radio_sequential.pressed.connect(
            lambda: self.set_radio(self.ui.radio_sequential))
        self.ui.radio_diverging.pressed.connect(
            lambda: self.set_radio(self.ui.radio_diverging))
        self.ui.radio_single_color.pressed.connect(
            lambda: self.set_radio(self.ui.radio_single_color))

        # Hook up single color button:
        self.ui.button_change_color.clicked.connect(self.set_color)

        # Hook up reverse checkbox
        self.ui.check_reverse.toggled.connect(
            lambda x: self.change_palette())

        # Hook up number of color spinner
        self.ui.spin_number.valueChanged.connect(
            lambda x: self.change_palette())

        # Hook up clear buttons.
        self.ui.button_clear_x.clicked.connect(self.ui.tray_data_x.clear)
        self.ui.button_clear_y.clicked.connect(self.ui.tray_data_y.clear)
        self.ui.button_clear_z.clicked.connect(self.ui.tray_data_z.clear)
        self.ui.button_clear_rows.clicked.connect(self.ui.tray_rows.clear)
        self.ui.button_clear_columns.clicked.connect(
            self.ui.tray_columns.clear)

        # Change custom figure widgets if necessary:
        self.ui.list_figures.currentItemChanged.connect(
            self.change_figure_type)

        # Hook up checks for figure type.
        # The list of available figure types can change if a data tray has
        # changed, either because a feature was placed in it or if the tray
        # was cleared.
        self.ui.tray_data_x.featureChanged.connect(self.check_figure_types)
        self.ui.tray_data_y.featureChanged.connect(self.check_figure_types)
        self.ui.tray_data_z.featureChanged.connect(self.check_figure_types)
        self.ui.tray_data_x.featureCleared.connect(self.check_figure_types)
        self.ui.tray_data_y.featureCleared.connect(self.check_figure_types)
        self.ui.tray_data_z.featureCleared.connect(self.check_figure_types)

        self.ui.check_hide_unavailable.toggled.connect(
            self.check_figure_types)

        # Hook up checks for clear button enable state.
        # The enable state of clear buttons is checked if the feature in the
        # associated tray has changed or cleared.
        self.ui.tray_data_x.featureChanged.connect(self.check_clear_buttons)
        self.ui.tray_data_y.featureChanged.connect(self.check_clear_buttons)
        self.ui.tray_data_z.featureChanged.connect(self.check_clear_buttons)
        self.ui.tray_columns.featureChanged.connect(self.check_clear_buttons)
        self.ui.tray_rows.featureChanged.connect(self.check_clear_buttons)
        self.ui.tray_data_x.featureCleared.connect(self.check_clear_buttons)
        self.ui.tray_data_y.featureCleared.connect(self.check_clear_buttons)
        self.ui.tray_data_z.featureCleared.connect(self.check_clear_buttons)
        self.ui.tray_columns.featureCleared.connect(self.check_clear_buttons)
        self.ui.tray_rows.featureCleared.connect(self.check_clear_buttons)

        # Hook up checks for column and row trays so that they can't contain
        # duplicates of either the x or the y feature tray:
        self.ui.tray_columns.featureChanged.connect(self.check_duplicates)
        self.ui.tray_rows.featureChanged.connect(self.check_duplicates)

        # Hook up checks for wrapping checkbox enable state.
        # The enable state of the wrapping checkbox is checked if there are
        # changes to the rows and columns tray.
        self.ui.tray_columns.featureCleared.connect(self.check_wrapping)
        self.ui.tray_columns.featureChanged.connect(self.check_wrapping)
        self.ui.tray_rows.featureCleared.connect(self.check_wrapping)
        self.ui.tray_rows.featureChanged.connect(self.check_wrapping)

        # Hook up checks for grid layout enable state.
        # The enable state of the grid layout box is checked if there are
        # changes to the data trays.
        for signal in (self.ui.tray_data_x.featureChanged,
                       self.ui.tray_data_y.featureChanged,
                       self.ui.tray_data_z.featureChanged,
                       self.ui.tray_data_x.featureCleared,
                       self.ui.tray_data_y.featureCleared,
                       self.ui.tray_data_z.featureCleared):
            signal.connect(self.check_grid_layout)

        # Hook up annotation changes:
        for signal in (self.ui.edit_figure_title.textChanged,
                       self.ui.edit_x_label.textChanged,
                       self.ui.edit_y_label.textChanged,
                       self.ui.spin_size_title.valueChanged,
                       self.ui.spin_size_x_label.valueChanged,
                       self.ui.spin_size_y_label.valueChanged,
                       self.ui.spin_size_x_ticklabels.valueChanged,
                       self.ui.spin_size_y_ticklabels.valueChanged,
                       self.ui.combo_font_figure.currentIndexChanged):
            signal.connect(self.add_annotations)

        # (6) changing the legend layout
        self.ui.edit_legend_title.editingFinished.connect(self.change_legend)
        self.ui.check_show_legend.toggled.connect(self.change_legend)
        self.ui.spin_columns.valueChanged.connect(self.change_legend)
        self.ui.spin_size_legend.valueChanged.connect(self.change_legend)
        self.ui.spin_size_legend_entries.valueChanged.connect(
            self.change_legend)

        # Hook up figure plotting.
        # The figure will be plot only upon _explicit_ user actions. User
        # actions are:

        # (1) placing a feature in a tray
        self.ui.tray_data_x.featureChanged.connect(self.plot_figure)
        self.ui.tray_data_y.featureChanged.connect(self.plot_figure)
        self.ui.tray_data_z.featureChanged.connect(self.plot_figure)
        self.ui.tray_columns.featureChanged.connect(self.plot_figure)
        self.ui.tray_rows.featureChanged.connect(self.plot_figure)

        # (2) clicking a clear button
        self.ui.button_clear_x.clicked.connect(self.plot_figure)
        self.ui.button_clear_y.clicked.connect(self.plot_figure)
        self.ui.button_clear_z.clicked.connect(self.plot_figure)
        self.ui.button_clear_rows.clicked.connect(self.plot_figure)
        self.ui.button_clear_columns.clicked.connect(self.plot_figure)

        # (3) changing the wrapping checkbox
        self.ui.check_wrap_layout.toggled.connect(self.plot_figure)

        # (4) selecting a different figure type
        self.ui.list_figures.currentItemChanged.connect(self.plot_figure)

    def change_figure_type(self):
        self.ui.group_custom.hide()

        figure_type = self.ui.list_figures.currentItem()
        if figure_type is None:
            return

        if self.df is None:
            return

        vis_class = VisualizationDesigner.visualizers[
            figure_type.text()]

        #if self.vis is not None:
            #self.vis.updateRequested.disconnect()

        self.vis = vis_class(self.df, self.session)
        self.vis.updateRequested.connect(self.plot_figure)
        self.add_custom_widgets()

    def add_custom_widgets(self):
        for i in reversed(range(self.ui.layout_custom.count())):
            item = self.ui.layout_custom.itemAt(i)
            if isinstance(item, QtWidgets.QLayout):
                for j in reversed(range(item.count())):
                    subitem = item.takeAt(j)
                    if hasattr(subitem, "widget"):
                        widget = subitem.widget()
                        if widget:
                            widget.hide()
                            widget.setParent(None)
                    del subitem
            else:
                item.hide()
            if hasattr(item, "widget"):
                widget = item.widget()
                if widget:
                    widget.hide()
                    widget.setParent(None)
            del item

        widgets = self.vis.get_custom_widgets(**self.get_gui_values())
        if widgets:
            self.ui.group_custom.show()
            for item in widgets:
                if isinstance(item, QtWidgets.QLayout):
                    self.ui.layout_custom.addLayout(item)
                else:
                    self.ui.layout_custom.addWidget(item)

    def check_wrapping(self):
        """
        Activate or deactivate the 'Wrap layout' checkbox. If the checkbox
        is deactivated, also clear the Columns and Rows trays.
        """
        columns = self.ui.tray_columns.data()
        rows = self.ui.tray_rows.data()
        if (columns is None or
                (columns is not None and rows is not None)):
            self._last_wrap_state = self.ui.check_wrap_layout.isChecked()
            self.ui.check_wrap_layout.blockSignals(True)
            self.ui.check_wrap_layout.setChecked(False)
            self.ui.check_wrap_layout.blockSignals(False)
            self.ui.check_wrap_layout.setDisabled(True)
        else:
            self.ui.check_wrap_layout.setDisabled(False)
            if hasattr(self, "_last_wrap_state"):
                self.ui.check_wrap_layout.blockSignals(True)
                self.ui.check_wrap_layout.setChecked(self._last_wrap_state)
                self.ui.check_wrap_layout.blockSignals(False)
                del self._last_wrap_state

    def check_duplicates(self):
        columns = self.ui.tray_columns.data()
        rows = self.ui.tray_rows.data()
        x = self.ui.tray_data_x.data()
        y = self.ui.tray_data_y.data()

        if columns and (columns in [x, y]):
            self.ui.tray_columns.clear()
        if rows and (rows in [x, y]):
            self.ui.tray_rows.clear()

    def check_clear_buttons(self):
        self.ui.button_clear_x.setEnabled(bool(self.ui.tray_data_x.text()))
        self.ui.button_clear_y.setEnabled(bool(self.ui.tray_data_y.text()))
        self.ui.button_clear_z.setEnabled(bool(self.ui.tray_data_z.text()))
        self.ui.button_clear_columns.setEnabled(
            bool(self.ui.tray_columns.text()))
        self.ui.button_clear_rows.setEnabled(bool(self.ui.tray_rows.text()))

    def check_grid_layout(self):
        if self.ui.tray_data_x.text() or self.ui.tray_data_y.text():
            self.ui.group_layout.setEnabled(True)
        else:
            self.ui.group_layout.setEnabled(False)
            if self.ui.tray_columns.text():
                self.ui.tray_columns.clear()
            if self.ui.tray_rows.text():
                self.ui.tray_rows.clear()

    def check_figure_types(self):
        if self.df is None:
            return

        current_item = self.ui.list_figures.currentItem()
        if current_item:
            last_class = current_item.data(QtCore.Qt.UserRole)
        else:
            last_class = None

        data_x = self.ui.tray_data_x.data()
        data_y = self.ui.tray_data_y.data()
        data_z = self.ui.tray_data_z.data()

        hide_unavailable = self.ui.check_hide_unavailable.isChecked()

        self.ui.list_figures.blockSignals(True)

        self.ui.list_figures.clear()

        for label, icon, vis_class in self.figure_types:
            item = self.get_figure_item(label, icon, vis_class)
            visualizer = VisualizationDesigner.visualizers[item.text()]
            if (visualizer.validate_data(data_x, data_y, data_z,
                                         self.df, self.session) and
                    not ((data_x or data_y) and (data_x == data_y))):
                item.setFlags(item.flags() | QtCore.Qt.ItemIsEnabled)
                self.ui.list_figures.addItem(item)
            else:
                item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEnabled)
                if not hide_unavailable:
                    self.ui.list_figures.addItem(item)

        # try to restore last position:
        for i in range(self.ui.list_figures.count()):
            current_item = self.ui.list_figures.item(i)
            vis_class = current_item.data(QtCore.Qt.UserRole)
            if vis_class == last_class:
                self.ui.list_figures.setCurrentItem(current_item)
                break

        self.ui.list_figures.blockSignals(False)

    def show_palette(self):
        self._palette_name = self.get_palette_name()
        self._color_number = self.ui.spin_number.value()
        self.ui.color_test_area.clear()
        name, _, rev = self._palette_name.partition("_")
        if name == COQ_SINGLE:
            rgb = self._current_color.getRgb()[:-1]
            test_palette = [tuple(x / 255 for x in rgb)] * self._color_number
        elif name == PALETTE_BW:
            test_palette = [(0, 0, 0), (1, 1, 1)]
        else:
            test_palette = sns.color_palette(name, self._color_number)
        if rev == "r":
            test_palette = test_palette[::-1]
        for i, (r, g, b) in enumerate(test_palette):
            item = QtWidgets.QListWidgetItem()
            self.ui.color_test_area.addItem(item)
            brush = QtGui.QBrush(QtGui.QColor(
                        int(r * 255), int(g * 255), int(b * 255)))
            item.setBackground(brush)

    def change_palette(self):
        x = self.get_palette_name()
        n = self.ui.spin_number.value()
        if (x != self._palette_name or n != self._color_number):
            self.show_palette()
            self.plot_figure()

    def set_color(self):
        if self._current_color:
            color = QtWidgets.QColorDialog.getColor(self._current_color)
        else:
            color = QtWidgets.QColorDialog.getColor()
        if color.isValid():
            self._current_color = color
            self.change_palette()

    def set_radio(self, radio):
        radio.blockSignals(True)
        if not radio.isChecked():
            radio.setChecked(True)
        self.change_palette()
        radio.blockSignals(False)

    def restore_settings(self):
        def get_or_set_size(key, factor=1.0):
            try:
                size = int(options.settings.value(key, None))
            except TypeError:
                size = None
            if size is None:
                size = int(QtWidgets.QLabel().font().pointSize() * factor)
            return size

        self.resize(640, 400)
        try:
            self.resize(options.settings.value("visualizationdesigner_size"))
        except TypeError:
            pass
        self.viewer_size = options.settings.value(
            "visualizationdesigner_viewer_size")
        self.viewer_size = QtCore.QSize(640, 480)

        self.data_x = options.settings.value(
            "visualizationdesinger_data_x", None)
        self.data_y = options.settings.value(
            "visualizationdesigner_data_y", None)
        self.layout_columns = options.settings.value(
            "visualizationdesigner_layout_columns", None)
        self.layout_rows = options.settings.value(
            "visualizationdesigner_layout_rows", None)
        val = options.settings.value(
            "visualizationdesigner_show_legend", "true")
        val = val == "true"
        self.ui.check_show_legend.setChecked(val)

        val = options.settings.value(
            "visualizationdesigner_hide_unavailable", "true")
        val = val == "true"
        self.ui.check_hide_unavailable.setChecked(val)

        family = options.settings.value(
            "visualizationdesigner_figure_font", None)
        index = self.ui.combo_font_figure.findText(family)
        if family is None or index == -1:
            family = utf8(QtWidgets.QLabel().font().family())
            index = self.ui.combo_font_figure.findText(family)
        self.ui.combo_font_figure.setCurrentIndex(index)

        self.legend_columns = options.settings.value(
            "visualizationdesigner_legend_columns", 1)

        self.ui.spin_size_title.setValue(
            get_or_set_size("visualizationdesigner_size_title", 1.2))
        self.ui.spin_size_x_label.setValue(
            get_or_set_size("visualizationdesigner_size_x_label"))
        self.ui.spin_size_y_label.setValue(
            get_or_set_size("visualizationdesigner_size_y_label"))
        self.ui.spin_size_legend.setValue(
            get_or_set_size("visualizationdesigner_size_legend"))
        self.ui.spin_size_x_ticklabels.setValue(
            get_or_set_size("visualizationdesigner_size_x_ticklabels", 0.8))
        self.ui.spin_size_y_ticklabels.setValue(
            get_or_set_size("visualizationdesigner_size_y_ticklabels", 0.8))
        self.ui.spin_size_legend_entries.setValue(
            get_or_set_size("visualizationdesigner_size_legend_entries", 0.8))

        val = options.settings.value(
            "visualizationdesigner_reverse_palette", "true")
        self._reversed = val == "true"
        self.ui.check_reverse.setChecked(self._reversed)
        val = options.settings.value("visualizationdesigner_color_number", 12)
        self._color_number = int(val)
        self.ui.spin_number.setValue(self._color_number)

        palette = options.settings.value("visualizationdesigner_palette", None)
        if palette is None:
            palette = "Paired"
        for box, radio in (
                (self.ui.combo_qualitative, self.ui.radio_qualitative),
                (self.ui.combo_diverging, self.ui.radio_diverging),
                (self.ui.combo_sequential, self.ui.radio_sequential)):
            if box.findText(palette):
                radio.setChecked(True)
                box.setCurrentIndex(box.findText(palette))
                break
        else:
            self.ui.radio_qualitative.setChecked(True)
            self.ui.combo_qualitative.setCurrentIndex(
                self.ui.combo_qualitative.findText("Paired"))
            palette = "Paired"

        if self._reversed:
            palette = "{}_r".format(palette)
        self._palette_name = palette

    def display_values(self):
        # set up Layout tab:

        # data x
        if self.data_x:
            label = self.alias.get(self.data_x) or self.data_x
        else:
            label = None
        #self.ui.receive_data_x.setText(label)

        # data y
        if self.data_y:
            label = self.alias.get(self.data_y) or self.data_y
        else:
            label = None
        #self.ui.receive_data_y.setText(label)

        # layout columns
        if self.layout_columns:
            label = self.alias.get(self.layout_columns) or self.layout_columns
        else:
            label = None
        #self.ui.receive_columns.setText(label)

        # layout rows
        if self.layout_rows:
            label = self.alias.get(self.layout_rows) or self.layout_rows
        else:
            label = None
        #self.ui.receive_rows.setText(label)

        self.ui.spin_columns.setValue(int(self.legend_columns))
        self.show_palette()

    def get_gui_values(self):
        """
        """
        x = self.ui.tray_data_x.data()
        y = self.ui.tray_data_y.data()
        z = self.ui.tray_data_z.data()

        d = dict(x=x, y=y, z=z,
                 columns=self.ui.tray_columns.data(),
                 rows=self.ui.tray_rows.data(),
                 figure_type=self.ui.list_figures.currentItem(),
                 figure_font=utf8(self.ui.combo_font_figure.currentText()),
                 title=utf8(self.ui.edit_figure_title.text()),
                 xlab=utf8(self.ui.edit_x_label.text()),
                 ylab=utf8(self.ui.edit_y_label.text()),
                 size_title=self.ui.spin_size_title.value(),
                 size_xlab=self.ui.spin_size_x_label.value(),
                 size_ylab=self.ui.spin_size_y_label.value(),
                 size_xticks=self.ui.spin_size_x_ticklabels.value(),
                 size_yticks=self.ui.spin_size_y_ticklabels.value(),
                 session=self.session,
                 palette=self.get_palette_name(),
                 color_number=self.ui.spin_number.value())

        d["levels_x"] = []
        d["levels_y"] = []
        d["levels_z"] = []
        d["range_x"] = None
        d["range_y"] = None
        d["range_z"] = None


        if x:
            # get levels by discarding NAs and then sorting the unique
            # values, using a much more efficient but less transparent
            # variant of sorted(self.df[var].dropna().unique().values():
            d["levels_x"] = sorted(
                set(self.df[x].values[~pd.isnull(self.df[x].values)]))
            d["range_x"] = (self.df[x].min(), self.df[x].max())

        if y:
            d["levels_y"] = sorted(
                set(self.df[y].values[~pd.isnull(self.df[y].values)]))
            d["range_y"] = (self.df[y].min(), self.df[y].max())

        if z:
            d["levels_z"] = sorted(
                set(self.df[z].values[~pd.isnull(self.df[z].values)]))
            d["range_z"] = (self.df[z].min(), self.df[z].max())

        return d

    def get_palette_name(self):
        for ptype in ("qualitative", "sequential", "diverging", "single"):
            if ptype == "single":
                return "{}_{}".format(COQ_SINGLE, self._current_color.name())
            widget_name = "radio_{}".format(ptype)
            widget = getattr(self.ui, widget_name)
            if widget.isChecked():
                combo_name = "combo_{}".format(ptype)
                combo = getattr(self.ui, combo_name)
                pal_name = utf8(combo.currentText())
                break

        if self.ui.check_reverse.isChecked():
            pal_name = "{}_r".format(pal_name)

        return pal_name

    def plot_figure(self):
        logging.info("VIS: plot_figure()")
        values = self.get_gui_values()

        if not values["figure_type"]:
            return

        vis_class = VisualizationDesigner.visualizers[
            values["figure_type"].text()]

        if (self.ui.check_wrap_layout.isChecked()):
            col_wrap, _ = get_grid_layout(
                len(self.df[values["columns"]].unique()))
        else:
            col_wrap = None

        data_columns = [values[x] for
                        x in ["x", "y", "z", "columns", "rows"]
                        if values[x]]
        # remove duplicates:
        data_columns = list(set(data_columns))
        data_columns.append("coquery_invisible_corpus_id")
        aliased_columns = [self.alias.get(x, x) for x in data_columns]

        for x in ["x", "y", "z", "columns", "rows"]:
            values[x] = self.alias.get(values[x], values[x])

        df = self.df[data_columns]
        df.columns = aliased_columns

        logging.info("VIS: Data initialized")
        self.vis = vis_class(df, self.session)
        logging.info("VIS: Visualizer initialized")
        self.grid = self.vis.get_grid(col=values["columns"],
                                      row=values["rows"],
                                      col_wrap=col_wrap,
                                      legend_out=True,
                                      sharex=True, sharey=True)
        logging.info("VIS: Grid initialized")

        self.setup_canvas(self.grid.fig)
        logging.info("VIS: canvas initialized")

        w, h = self.dialog.size().width(), self.dialog.size().height()
        dpi = self.grid.fig.dpi
        self.grid.fig.set_size_inches(w / dpi, h / dpi)

        logging.info("VIS: Grid size {}, {} inches".format(
            w / dpi, h / dpi))

        if options.cfg.experimental:
            self.plot_thread = classes.CoqThread(
                self.run_plot, parent=self, **values)
            self.plot_thread.taskStarted.connect(self.start_plot)
            self.plot_thread.taskFinished.connect(self.finalize_plot)
            self.plot_thread.taskException.connect(self.exception_plot)
            self.vis.moveToThread(self.plot_thread)
            self.plot_thread.start()
        else:
            self.start_plot()
            self.run_plot(**values)
            self.finalize_plot()
        logging.info("VIS: plot_figure() done")

    def start_plot(self):
        logging.info("VIS: start_plot()")
        try:
            self.progress_bar = QtWidgets.QProgressBar()
            self.progress_bar.setRange(0, 0)
            self.progress_bar.show()
            self.dialog_layout.addWidget(self.progress_bar)
        except Exception as e:
            logging.error("VIS: start_plot(), exception {}".format(str(e)))
            raise e
        logging.info("VIS: start_plot() done")

    def run_plot(self, **kwargs):
        logging.info("VIS: run_plot()")
        try:
            self.grid.map_dataframe(self.vis.plot_facet, **kwargs)
        except Exception as e:
            logging.error("VIS: run_plot(), exception {}".format(str(e)))
            raise e
        logging.info("VIS: run_plot() done")

    def finalize_plot(self):
        logging.info("VIS: finalize_plot()")
        try:
            values = self.get_gui_values()
            figure_title = values["figure_type"].text()

            try:
                self.dialog_layout.removeWidget(self.progress_bar)
                self.progress_bar.hide()
                del self.progress_bar
            except AttributeError:
                pass

            self.add_annotations()
            self.change_legend()

            self.grid.fig.tight_layout()

            self.dialog.setWindowTitle("{} – Coquery".format(figure_title))
            self.dialog.show()
            self.dialog.raise_()

            if hasattr(self.vis, "on_pick"):
                self.grid.fig.canvas.mpl_connect(
                    "button_press_event", self.vis.on_pick)
        except Exception as e:
            logging.error("VIS: finalize_plot(), exception {}".format(str(e)))
            raise e
        logging.info("VIS: finalize_plot() done")

    def exception_plot(self, e):
        logging.error(e)
        QtWidgets.QMessageBox.critical(
            self,
            "Error while plotting – Coquery",
            msg_visualization_error.format(str(e)),
            QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)

    def add_annotations(self):
        if self.vis:
            values = self.get_gui_values()
            try:
                self.vis.set_annotations(self.grid, values)
            except Exception as e:
                print("ERROR: ", e)
                logging.error(str(e))
            else:
                self.canvas.draw()

    def change_legend(self):
        if self.vis:
            if self.ui.check_show_legend.isChecked():
                kwargs = dict(
                    grid=self.grid,
                    title=self.ui.edit_legend_title.text() or None,
                    palette=self._palette_name,
                    ncol=self.ui.spin_columns.value(),
                    fontsize=self.ui.spin_size_legend_entries.value(),
                    titlesize=self.ui.spin_size_legend.value())
                self.vis.add_legend(**kwargs)
            else:
                self.vis.hide_legend(self.grid)
            self.canvas.draw()

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Escape:
            self.close()
            self.reject()

    def close(self, *args):
        options.settings.setValue(
            "visualizationdesigner_size", self.size())
        options.settings.setValue(
            "visualizationdesigner_viewer_size", self.viewer_size)
        options.settings.setValue(
            "visualizationdesigner_data_x", self.data_x)
        options.settings.setValue(
            "visualizationdesigner_data_y", self.data_y)
        options.settings.setValue(
            "visualizationdesigner_layout_columns", self.layout_columns)
        options.settings.setValue(
            "visualizationdesigner_layout_rows", self.layout_rows)

        options.settings.setValue(
            "visualizationdesigner_figure_font",
            utf8(self.ui.combo_font_figure.currentText()))

        options.settings.setValue(
            "visualizationdesigner_size_title",
            self.ui.spin_size_title.value())
        options.settings.setValue(
            "visualizationdesigner_size_x_label",
            self.ui.spin_size_x_label.value())
        options.settings.setValue(
            "visualizationdesigner_size_x_ticklabels",
            self.ui.spin_size_x_ticklabels.value())
        options.settings.setValue(
            "visualizationdesigner_size_y_label",
            self.ui.spin_size_y_label.value())
        options.settings.setValue(
            "visualizationdesigner_size_y_ticklabels",
            self.ui.spin_size_y_ticklabels.value())
        options.settings.setValue(
            "visualizationdesigner_size_legend",
            self.ui.spin_size_legend.value())
        options.settings.setValue(
            "visualizationdesigner_size_legend_entries",
            self.ui.spin_size_legend_entries.value())

        val = "true" if self.ui.check_show_legend.isChecked() else "false"
        options.settings.setValue("visualizationdesigner_show_legend", val)

        val = ("true" if self.ui.check_hide_unavailable.isChecked()
               else "false")
        options.settings.setValue(
            "visualizationdesigner_hide_unavailable", val)

        options.settings.setValue("visualizationdesigner_legend_columns",
                                  self.legend_columns)

        val = "true" if self.ui.check_reverse.isChecked() else "false"
        options.settings.setValue("visualizationdesigner_reverse_palette",
                                  val)
        options.settings.setValue("visualizationdesigner_color_number",
                                  self.ui.spin_number.value())

        super(VisualizationDesigner, self).close(*args)

        if not hasattr(self, "canvas") and hasattr(self, "dialog"):
            self.dialog.hide()
            self.dialog.close()
            del self.dialog

    def exec_(self):
        result = super(VisualizationDesigner, self).exec_()

        if result == QtWidgets.QDialog.Accepted:
            self.accept()
            return result
        else:
            return None


def get_visualizer_module(name):
    # try to import the specified visualization module:
    visualizer_path = os.path.join(options.cfg.base_path, "visualizer")
    try:
        find = imp.find_module(name, [visualizer_path])
        module = imp.load_module(name, *find)
        return module
    except Exception as e:
        msg = "{type} in line {line}: {code}".format(
            type=type(e).__name__,
            code=sys.exc_info()[1],
            line=sys.exc_info()[2].tb_lineno)
        logging.error(msg)
        s = msg_visualization_module_error.format(
                module=name,
                msg=msg)
        QtWidgets.QMessageBox.critical(None,
                                       "Visualization error – Coquery", s)
        return None


def find_visualizer_modules():
    """
    Finds the list of potential visualization modules.
    """
    visualizer_path = os.path.join(options.cfg.base_path, "visualizer")

    l = [os.path.splitext(os.path.basename(file_name))[0]
         for file_name in glob.glob(os.path.join(visualizer_path, "*.py"))]
    return l
