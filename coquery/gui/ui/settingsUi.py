# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        SettingsDialog.setObjectName("SettingsDialog")
        SettingsDialog.resize(640, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SettingsDialog.sizePolicy().hasHeightForWidth())
        SettingsDialog.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(SettingsDialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(SettingsDialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout.setContentsMargins(8, 6, 8, 6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.group_case = QtWidgets.QGroupBox(self.tab_2)
        self.group_case.setObjectName("group_case")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.group_case)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.radio_output_case_leave = QtWidgets.QRadioButton(self.group_case)
        self.radio_output_case_leave.setObjectName("radio_output_case_leave")
        self.verticalLayout_4.addWidget(self.radio_output_case_leave)
        self.radio_output_case_lower = QtWidgets.QRadioButton(self.group_case)
        self.radio_output_case_lower.setObjectName("radio_output_case_lower")
        self.verticalLayout_4.addWidget(self.radio_output_case_lower)
        self.radio_output_case_upper = QtWidgets.QRadioButton(self.group_case)
        self.radio_output_case_upper.setObjectName("radio_output_case_upper")
        self.verticalLayout_4.addWidget(self.radio_output_case_upper)
        self.verticalLayout.addWidget(self.group_case)
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.spin_digits = QtWidgets.QSpinBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spin_digits.sizePolicy().hasHeightForWidth())
        self.spin_digits.setSizePolicy(sizePolicy)
        self.spin_digits.setProperty("value", 3)
        self.spin_digits.setObjectName("spin_digits")
        self.horizontalLayout.addWidget(self.spin_digits)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_7.addWidget(self.label_13)
        self.edit_na_string = QtWidgets.QLineEdit(self.groupBox)
        self.edit_na_string.setObjectName("edit_na_string")
        self.horizontalLayout_7.addWidget(self.edit_na_string)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.verticalLayout_7.addLayout(self.horizontalLayout_7)
        self.check_word_wrap = QtWidgets.QCheckBox(self.groupBox)
        self.check_word_wrap.setObjectName("check_word_wrap")
        self.verticalLayout_7.addWidget(self.check_word_wrap)
        self.verticalLayout.addWidget(self.groupBox)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.tabWidget.addTab(self.tab_2, "")
        self.Auto_apply = QtWidgets.QWidget()
        self.Auto_apply.setObjectName("Auto_apply")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.Auto_apply)
        self.verticalLayout_10.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_10.setSpacing(6)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label = QtWidgets.QLabel(self.Auto_apply)
        self.label.setObjectName("label")
        self.verticalLayout_10.addWidget(self.label)
        self.list_auto_apply = QtWidgets.QListWidget(self.Auto_apply)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_auto_apply.sizePolicy().hasHeightForWidth())
        self.list_auto_apply.setSizePolicy(sizePolicy)
        self.list_auto_apply.setObjectName("list_auto_apply")
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.Unchecked)
        self.list_auto_apply.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.Unchecked)
        self.list_auto_apply.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.list_auto_apply.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.Unchecked)
        self.list_auto_apply.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.Unchecked)
        self.list_auto_apply.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.Unchecked)
        self.list_auto_apply.addItem(item)
        self.verticalLayout_10.addWidget(self.list_auto_apply)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem3)
        self.verticalLayout_10.setStretch(2, 1)
        self.tabWidget.addTab(self.Auto_apply, "")
        self.Queries = QtWidgets.QWidget()
        self.Queries.setObjectName("Queries")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Queries)
        self.verticalLayout_2.setContentsMargins(8, 6, 8, 6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.Queries)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.check_regular_expressions = QtWidgets.QCheckBox(self.groupBox_2)
        self.check_regular_expressions.setObjectName("check_regular_expressions")
        self.verticalLayout_8.addWidget(self.check_regular_expressions)
        self.check_ignore_case_query = QtWidgets.QCheckBox(self.groupBox_2)
        self.check_ignore_case_query.setObjectName("check_ignore_case_query")
        self.verticalLayout_8.addWidget(self.check_ignore_case_query)
        self.check_drop_empty_queries = QtWidgets.QCheckBox(self.groupBox_2)
        self.check_drop_empty_queries.setObjectName("check_drop_empty_queries")
        self.verticalLayout_8.addWidget(self.check_drop_empty_queries)
        self.check_remove_duplicates = QtWidgets.QCheckBox(self.groupBox_2)
        self.check_remove_duplicates.setObjectName("check_remove_duplicates")
        self.verticalLayout_8.addWidget(self.check_remove_duplicates)
        self.check_align_quantified = QtWidgets.QCheckBox(self.groupBox_2)
        self.check_align_quantified.setObjectName("check_align_quantified")
        self.verticalLayout_8.addWidget(self.check_align_quantified)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.widget_cache = QtWidgets.QGroupBox(self.Queries)
        self.widget_cache.setObjectName("widget_cache")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_cache)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.check_use_cache = QtWidgets.QCheckBox(self.widget_cache)
        self.check_use_cache.setObjectName("check_use_cache")
        self.horizontalLayout_4.addWidget(self.check_use_cache)
        self.spin_cache_size = QtWidgets.QSpinBox(self.widget_cache)
        self.spin_cache_size.setPrefix("")
        self.spin_cache_size.setMinimum(1)
        self.spin_cache_size.setMaximum(4096)
        self.spin_cache_size.setObjectName("spin_cache_size")
        self.horizontalLayout_4.addWidget(self.spin_cache_size)
        self.widget_used = QtWidgets.QWidget(self.widget_cache)
        self.widget_used.setObjectName("widget_used")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_used)
        self.horizontalLayout_5.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_10 = QtWidgets.QLabel(self.widget_used)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_5.addWidget(self.label_10)
        self.progress_used = QtWidgets.QProgressBar(self.widget_used)
        self.progress_used.setProperty("value", 24)
        self.progress_used.setObjectName("progress_used")
        self.horizontalLayout_5.addWidget(self.progress_used)
        self.horizontalLayout_4.addWidget(self.widget_used)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.button_clear_cache = QtWidgets.QPushButton(self.widget_cache)
        self.button_clear_cache.setObjectName("button_clear_cache")
        self.horizontalLayout_4.addWidget(self.button_clear_cache)
        self.verticalLayout_2.addWidget(self.widget_cache)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem5)
        self.tabWidget.addTab(self.Queries, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setContentsMargins(8, 6, 8, 6)
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.label_sample_context = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_sample_context.sizePolicy().hasHeightForWidth())
        self.label_sample_context.setSizePolicy(sizePolicy)
        self.label_sample_context.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_sample_context.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_sample_context.setObjectName("label_sample_context")
        self.gridLayout.addWidget(self.label_sample_context, 1, 1, 1, 1)
        self.button_figure_font = QtWidgets.QPushButton(self.tab)
        self.button_figure_font.setObjectName("button_figure_font")
        self.gridLayout.addWidget(self.button_figure_font, 2, 2, 1, 1)
        self.button_reset_table = QtWidgets.QPushButton(self.tab)
        self.button_reset_table.setObjectName("button_reset_table")
        self.gridLayout.addWidget(self.button_reset_table, 0, 3, 1, 1)
        self.button_reset_context = QtWidgets.QPushButton(self.tab)
        self.button_reset_context.setObjectName("button_reset_context")
        self.gridLayout.addWidget(self.button_reset_context, 1, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.button_context_font = QtWidgets.QPushButton(self.tab)
        self.button_context_font.setObjectName("button_context_font")
        self.gridLayout.addWidget(self.button_context_font, 1, 2, 1, 1)
        self.button_reset_figure = QtWidgets.QPushButton(self.tab)
        self.button_reset_figure.setObjectName("button_reset_figure")
        self.gridLayout.addWidget(self.button_reset_figure, 2, 3, 1, 1)
        self.label_sample_table = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_sample_table.sizePolicy().hasHeightForWidth())
        self.label_sample_table.setSizePolicy(sizePolicy)
        self.label_sample_table.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_sample_table.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_sample_table.setObjectName("label_sample_table")
        self.gridLayout.addWidget(self.label_sample_table, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.button_table_font = QtWidgets.QPushButton(self.tab)
        self.button_table_font.setObjectName("button_table_font")
        self.gridLayout.addWidget(self.button_table_font, 0, 2, 1, 1)
        self.label_sample_figure = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_sample_figure.sizePolicy().hasHeightForWidth())
        self.label_sample_figure.setSizePolicy(sizePolicy)
        self.label_sample_figure.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_sample_figure.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_sample_figure.setObjectName("label_sample_figure")
        self.gridLayout.addWidget(self.label_sample_figure, 2, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem6, 3, 1, 1, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setRowStretch(3, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_5.setContentsMargins(8, 6, 8, 6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.check_ask_on_quit = QtWidgets.QCheckBox(self.tab_3)
        self.check_ask_on_quit.setObjectName("check_ask_on_quit")
        self.verticalLayout_5.addWidget(self.check_ask_on_quit)
        self.check_save_query_string = QtWidgets.QCheckBox(self.tab_3)
        self.check_save_query_string.setObjectName("check_save_query_string")
        self.verticalLayout_5.addWidget(self.check_save_query_string)
        self.check_save_query_file = QtWidgets.QCheckBox(self.tab_3)
        self.check_save_query_file.setObjectName("check_save_query_file")
        self.verticalLayout_5.addWidget(self.check_save_query_file)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem7)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout_6.setContentsMargins(8, 6, 8, 6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.group_paths = QtWidgets.QGroupBox(self.tab_4)
        self.group_paths.setObjectName("group_paths")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.group_paths)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_8 = QtWidgets.QLabel(self.group_paths)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1)
        self.edit_installer_path = QtWidgets.QLineEdit(self.group_paths)
        self.edit_installer_path.setObjectName("edit_installer_path")
        self.gridLayout_2.addWidget(self.edit_installer_path, 0, 1, 1, 1)
        self.button_installer_path = QtWidgets.QPushButton(self.group_paths)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_installer_path.sizePolicy().hasHeightForWidth())
        self.button_installer_path.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon.fromTheme("folder")
        self.button_installer_path.setIcon(icon)
        self.button_installer_path.setObjectName("button_installer_path")
        self.gridLayout_2.addWidget(self.button_installer_path, 0, 2, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.group_paths)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 2, 0, 1, 1)
        self.edit_cache_path = QtWidgets.QLineEdit(self.group_paths)
        self.edit_cache_path.setObjectName("edit_cache_path")
        self.gridLayout_2.addWidget(self.edit_cache_path, 2, 1, 1, 1)
        self.button_cache_path = QtWidgets.QPushButton(self.group_paths)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_cache_path.sizePolicy().hasHeightForWidth())
        self.button_cache_path.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon.fromTheme("folder")
        self.button_cache_path.setIcon(icon)
        self.button_cache_path.setObjectName("button_cache_path")
        self.gridLayout_2.addWidget(self.button_cache_path, 2, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.group_paths)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 3, 0, 1, 1)
        self.edit_visualizer_path = QtWidgets.QLineEdit(self.group_paths)
        self.edit_visualizer_path.setObjectName("edit_visualizer_path")
        self.gridLayout_2.addWidget(self.edit_visualizer_path, 3, 1, 1, 1)
        self.button_visualizer_path = QtWidgets.QPushButton(self.group_paths)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_visualizer_path.sizePolicy().hasHeightForWidth())
        self.button_visualizer_path.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon.fromTheme("folder")
        self.button_visualizer_path.setIcon(icon)
        self.button_visualizer_path.setObjectName("button_visualizer_path")
        self.gridLayout_2.addWidget(self.button_visualizer_path, 3, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.group_paths)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.edit_binary_path = QtWidgets.QLineEdit(self.group_paths)
        self.edit_binary_path.setObjectName("edit_binary_path")
        self.gridLayout_2.addWidget(self.edit_binary_path, 1, 1, 1, 1)
        self.button_binary_path = QtWidgets.QPushButton(self.group_paths)
        icon = QtGui.QIcon.fromTheme("folder")
        self.button_binary_path.setIcon(icon)
        self.button_binary_path.setObjectName("button_binary_path")
        self.gridLayout_2.addWidget(self.button_binary_path, 1, 2, 1, 1)
        self.verticalLayout_6.addWidget(self.group_paths)
        spacerItem8 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem8)
        self.tabWidget.addTab(self.tab_4, "")
        self.verticalLayout_3.addWidget(self.tabWidget)
        self.buttonBox = QtWidgets.QDialogButtonBox(SettingsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_3.addWidget(self.buttonBox)
        self.label_3.setBuddy(self.spin_digits)
        self.label_13.setBuddy(self.edit_na_string)
        self.label.setBuddy(self.list_auto_apply)
        self.label_8.setBuddy(self.edit_installer_path)
        self.label_11.setBuddy(self.edit_cache_path)
        self.label_9.setBuddy(self.edit_visualizer_path)
        self.label_2.setBuddy(self.edit_binary_path)

        self.retranslateUi(SettingsDialog)
        self.tabWidget.setCurrentIndex(0)
        self.buttonBox.accepted.connect(SettingsDialog.accept)
        self.buttonBox.rejected.connect(SettingsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SettingsDialog)

    def retranslateUi(self, SettingsDialog):
        _translate = QtCore.QCoreApplication.translate
        SettingsDialog.setWindowTitle(_translate("SettingsDialog", "Settings – Coquery"))
        self.group_case.setTitle(_translate("SettingsDialog", "&Case"))
        self.radio_output_case_leave.setText(_translate("SettingsDialog", "Do &not change case"))
        self.radio_output_case_lower.setText(_translate("SettingsDialog", "&Lower case"))
        self.radio_output_case_upper.setText(_translate("SettingsDialog", "&Upper case"))
        self.groupBox.setTitle(_translate("SettingsDialog", "&Display"))
        self.label_3.setText(_translate("SettingsDialog", "Displa&y "))
        self.spin_digits.setSuffix(_translate("SettingsDialog", " digit(s)"))
        self.label_7.setText(_translate("SettingsDialog", "after decimal point"))
        self.label_13.setText(_translate("SettingsDialog", "Placeholder for e&mpty cells:"))
        self.check_word_wrap.setText(_translate("SettingsDialog", " &Word-wrap long lines"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("SettingsDialog", "Results table"))
        self.label.setText(_translate("SettingsDialog", "&Automatically apply:"))
        __sortingEnabled = self.list_auto_apply.isSortingEnabled()
        self.list_auto_apply.setSortingEnabled(False)
        item = self.list_auto_apply.item(0)
        item.setText(_translate("SettingsDialog", "Column visibility"))
        item = self.list_auto_apply.item(1)
        item.setText(_translate("SettingsDialog", "Functions"))
        item = self.list_auto_apply.item(2)
        item.setText(_translate("SettingsDialog", "Substitutions"))
        item = self.list_auto_apply.item(3)
        item.setText(_translate("SettingsDialog", "Stopwords"))
        item = self.list_auto_apply.item(4)
        item.setText(_translate("SettingsDialog", "Filters"))
        item = self.list_auto_apply.item(5)
        item.setText(_translate("SettingsDialog", "Transformations"))
        self.list_auto_apply.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Auto_apply), _translate("SettingsDialog", "Management"))
        self.groupBox_2.setTitle(_translate("SettingsDialog", "&Options"))
        self.check_regular_expressions.setText(_translate("SettingsDialog", "Interpret query strings as &regular expressions"))
        self.check_ignore_case_query.setText(_translate("SettingsDialog", "Ignore &case in query strings"))
        self.check_drop_empty_queries.setText(_translate("SettingsDialog", "&Discard rows for which the query returned no matches"))
        self.check_remove_duplicates.setText(_translate("SettingsDialog", "&Remove duplicates of matched tokens"))
        self.check_align_quantified.setText(_translate("SettingsDialog", "Align &quantified token columns"))
        self.widget_cache.setTitle(_translate("SettingsDialog", "&Cache"))
        self.check_use_cache.setText(_translate("SettingsDialog", "&Use cache, size: "))
        self.spin_cache_size.setSuffix(_translate("SettingsDialog", " MBytes"))
        self.label_10.setText(_translate("SettingsDialog", "Used:"))
        self.progress_used.setFormat(_translate("SettingsDialog", "%v MBytes"))
        self.button_clear_cache.setText(_translate("SettingsDialog", "Clear cache"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Queries), _translate("SettingsDialog", "Queries"))
        self.label_5.setText(_translate("SettingsDialog", "Context font:"))
        self.label_sample_context.setText(_translate("SettingsDialog", "TextLabel"))
        self.button_figure_font.setText(_translate("SettingsDialog", "Change..."))
        self.button_reset_table.setText(_translate("SettingsDialog", "Reset"))
        self.button_reset_context.setText(_translate("SettingsDialog", "Reset"))
        self.label_6.setText(_translate("SettingsDialog", "Default figure font:"))
        self.button_context_font.setText(_translate("SettingsDialog", "Change..."))
        self.button_reset_figure.setText(_translate("SettingsDialog", "Reset"))
        self.label_sample_table.setText(_translate("SettingsDialog", "TextLabel"))
        self.label_4.setText(_translate("SettingsDialog", "Table font:"))
        self.button_table_font.setText(_translate("SettingsDialog", "Change..."))
        self.label_sample_figure.setText(_translate("SettingsDialog", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("SettingsDialog", "Fonts"))
        self.check_ask_on_quit.setText(_translate("SettingsDialog", "Ask if &unsaved results should be saved upon exit"))
        self.check_save_query_string.setText(_translate("SettingsDialog", "Save last query &string in configuration file"))
        self.check_save_query_file.setText(_translate("SettingsDialog", "Save last query &file in configuration file"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("SettingsDialog", "Quitting"))
        self.group_paths.setTitle(_translate("SettingsDialog", "Additional paths"))
        self.label_8.setText(_translate("SettingsDialog", "Cor&pus installers: "))
        self.button_installer_path.setText(_translate("SettingsDialog", "&Browse"))
        self.button_installer_path.setShortcut(_translate("SettingsDialog", "Alt+B"))
        self.label_11.setText(_translate("SettingsDialog", "Query &cache:"))
        self.button_cache_path.setText(_translate("SettingsDialog", "B&rowse"))
        self.button_cache_path.setShortcut(_translate("SettingsDialog", "Alt+B"))
        self.label_9.setText(_translate("SettingsDialog", "&Visualizers:"))
        self.button_visualizer_path.setText(_translate("SettingsDialog", "B&rowse"))
        self.button_visualizer_path.setShortcut(_translate("SettingsDialog", "Alt+B"))
        self.label_2.setText(_translate("SettingsDialog", "&Binary data:"))
        self.button_binary_path.setText(_translate("SettingsDialog", "B&rowse"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("SettingsDialog", "Paths"))


