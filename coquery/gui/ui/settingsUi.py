# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from pyqt_compat import QtCore, QtGui, frameShadow, frameShape

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        SettingsDialog.setObjectName(_fromUtf8("SettingsDialog"))
        SettingsDialog.resize(468, 544)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SettingsDialog.sizePolicy().hasHeightForWidth())
        SettingsDialog.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QtGui.QVBoxLayout(SettingsDialog)
        self.verticalLayout_3.setContentsMargins(4, -1, 4, -1)
        self.verticalLayout_3.setSpacing(8)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.groupBox_2 = QtGui.QGroupBox(SettingsDialog)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_4.setContentsMargins(8, 6, 8, 6)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.spin_digits = QtGui.QSpinBox(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spin_digits.sizePolicy().hasHeightForWidth())
        self.spin_digits.setSizePolicy(sizePolicy)
        self.spin_digits.setProperty("value", 3)
        self.spin_digits.setObjectName(_fromUtf8("spin_digits"))
        self.horizontalLayout.addWidget(self.spin_digits)
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.check_ignore_case = QtGui.QCheckBox(self.groupBox_2)
        self.check_ignore_case.setObjectName(_fromUtf8("check_ignore_case"))
        self.verticalLayout_4.addWidget(self.check_ignore_case)
        self.check_align_quantified = QtGui.QCheckBox(self.groupBox_2)
        self.check_align_quantified.setObjectName(_fromUtf8("check_align_quantified"))
        self.verticalLayout_4.addWidget(self.check_align_quantified)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.group_fonts = QtGui.QGroupBox(SettingsDialog)
        self.group_fonts.setObjectName(_fromUtf8("group_fonts"))
        self.gridLayout_2 = QtGui.QGridLayout(self.group_fonts)
        self.gridLayout_2.setVerticalSpacing(4)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.button_reset_figure = QtGui.QPushButton(self.group_fonts)
        self.button_reset_figure.setObjectName(_fromUtf8("button_reset_figure"))
        self.gridLayout_2.addWidget(self.button_reset_figure, 5, 6, 1, 1)
        self.label_sample_figure = QtGui.QLabel(self.group_fonts)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_sample_figure.sizePolicy().hasHeightForWidth())
        self.label_sample_figure.setSizePolicy(sizePolicy)
        self.label_sample_figure.setFrameShape(frameShape)
        self.label_sample_figure.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_sample_figure.setObjectName(_fromUtf8("label_sample_figure"))
        self.gridLayout_2.addWidget(self.label_sample_figure, 5, 2, 1, 1)
        self.button_figure_font = QtGui.QPushButton(self.group_fonts)
        self.button_figure_font.setObjectName(_fromUtf8("button_figure_font"))
        self.gridLayout_2.addWidget(self.button_figure_font, 5, 4, 1, 1)
        self.button_reset_table = QtGui.QPushButton(self.group_fonts)
        self.button_reset_table.setObjectName(_fromUtf8("button_reset_table"))
        self.gridLayout_2.addWidget(self.button_reset_table, 0, 6, 1, 1)
        self.label_sample_table = QtGui.QLabel(self.group_fonts)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_sample_table.sizePolicy().hasHeightForWidth())
        self.label_sample_table.setSizePolicy(sizePolicy)
        self.label_sample_table.setFrameShape(frameShape)
        self.label_sample_table.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_sample_table.setObjectName(_fromUtf8("label_sample_table"))
        self.gridLayout_2.addWidget(self.label_sample_table, 0, 2, 1, 1)
        self.button_table_font = QtGui.QPushButton(self.group_fonts)
        self.button_table_font.setObjectName(_fromUtf8("button_table_font"))
        self.gridLayout_2.addWidget(self.button_table_font, 0, 4, 1, 1)
        self.label_6 = QtGui.QLabel(self.group_fonts)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_2.addWidget(self.label_6, 5, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.group_fonts)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_sample_context = QtGui.QLabel(self.group_fonts)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_sample_context.sizePolicy().hasHeightForWidth())
        self.label_sample_context.setSizePolicy(sizePolicy)
        self.label_sample_context.setFrameShape(frameShape)
        self.label_sample_context.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_sample_context.setObjectName(_fromUtf8("label_sample_context"))
        self.gridLayout_2.addWidget(self.label_sample_context, 2, 2, 1, 1)
        self.label_5 = QtGui.QLabel(self.group_fonts)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)
        self.button_context_font = QtGui.QPushButton(self.group_fonts)
        self.button_context_font.setObjectName(_fromUtf8("button_context_font"))
        self.gridLayout_2.addWidget(self.button_context_font, 2, 4, 1, 1)
        self.button_reset_context = QtGui.QPushButton(self.group_fonts)
        self.button_reset_context.setObjectName(_fromUtf8("button_reset_context"))
        self.gridLayout_2.addWidget(self.button_reset_context, 2, 6, 1, 1)
        self.verticalLayout_3.addWidget(self.group_fonts)
        self.groupBox_3 = QtGui.QGroupBox(SettingsDialog)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_3.setContentsMargins(8, 6, 8, 6)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.frame_addon_paths = QtGui.QFrame(self.groupBox_3)
        self.frame_addon_paths.setObjectName(_fromUtf8("frame_addon_paths"))
        self.gridLayout = QtGui.QGridLayout(self.frame_addon_paths)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.button_visualizer_path = QtGui.QPushButton(self.frame_addon_paths)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_visualizer_path.sizePolicy().hasHeightForWidth())
        self.button_visualizer_path.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("folder"))
        self.button_visualizer_path.setIcon(icon)
        self.button_visualizer_path.setObjectName(_fromUtf8("button_visualizer_path"))
        self.gridLayout.addWidget(self.button_visualizer_path, 1, 2, 1, 1)
        self.edit_installer_path = QtGui.QLineEdit(self.frame_addon_paths)
        self.edit_installer_path.setObjectName(_fromUtf8("edit_installer_path"))
        self.gridLayout.addWidget(self.edit_installer_path, 0, 1, 1, 1)
        self.button_installer_path = QtGui.QPushButton(self.frame_addon_paths)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_installer_path.sizePolicy().hasHeightForWidth())
        self.button_installer_path.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("folder"))
        self.button_installer_path.setIcon(icon)
        self.button_installer_path.setObjectName(_fromUtf8("button_installer_path"))
        self.gridLayout.addWidget(self.button_installer_path, 0, 2, 1, 1)
        self.edit_visualizer_path = QtGui.QLineEdit(self.frame_addon_paths)
        self.edit_visualizer_path.setObjectName(_fromUtf8("edit_visualizer_path"))
        self.gridLayout.addWidget(self.edit_visualizer_path, 1, 1, 1, 1)
        self.label_9 = QtGui.QLabel(self.frame_addon_paths)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 1, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.frame_addon_paths)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.horizontalLayout_3.addWidget(self.frame_addon_paths)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.groupBox_4 = QtGui.QGroupBox(SettingsDialog)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_2.setContentsMargins(8, 6, 8, 6)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.check_ask_on_quit = QtGui.QCheckBox(self.groupBox_4)
        self.check_ask_on_quit.setObjectName(_fromUtf8("check_ask_on_quit"))
        self.verticalLayout_2.addWidget(self.check_ask_on_quit)
        self.check_save_query_string = QtGui.QCheckBox(self.groupBox_4)
        self.check_save_query_string.setObjectName(_fromUtf8("check_save_query_string"))
        self.verticalLayout_2.addWidget(self.check_save_query_string)
        self.check_save_query_file = QtGui.QCheckBox(self.groupBox_4)
        self.check_save_query_file.setObjectName(_fromUtf8("check_save_query_file"))
        self.verticalLayout_2.addWidget(self.check_save_query_file)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addWidget(self.groupBox_4)
        spacerItem1 = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.buttonBox = QtGui.QDialogButtonBox(SettingsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_3.addWidget(self.buttonBox)
        self.label.setBuddy(self.spin_digits)
        self.label_9.setBuddy(self.edit_visualizer_path)
        self.label_2.setBuddy(self.edit_installer_path)

        self.retranslateUi(SettingsDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), SettingsDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), SettingsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SettingsDialog)

    def retranslateUi(self, SettingsDialog):
        SettingsDialog.setWindowTitle(_translate("SettingsDialog", "Settings – Coquery", None))
        self.groupBox_2.setTitle(_translate("SettingsDialog", "Output options", None))
        self.label.setText(_translate("SettingsDialog", "&Display ", None))
        self.spin_digits.setSuffix(_translate("SettingsDialog", " digit(s)", None))
        self.label_3.setText(_translate("SettingsDialog", "after decimal point", None))
        self.check_ignore_case.setText(_translate("SettingsDialog", "Ignore &case", None))
        self.check_align_quantified.setText(_translate("SettingsDialog", "Align &quantified token columns", None))
        self.group_fonts.setTitle(_translate("SettingsDialog", "Fonts", None))
        self.button_reset_figure.setText(_translate("SettingsDialog", "Reset", None))
        self.label_sample_figure.setText(_translate("SettingsDialog", "TextLabel", None))
        self.button_figure_font.setText(_translate("SettingsDialog", "Change...", None))
        self.button_reset_table.setText(_translate("SettingsDialog", "Reset", None))
        self.label_sample_table.setText(_translate("SettingsDialog", "TextLabel", None))
        self.button_table_font.setText(_translate("SettingsDialog", "Change...", None))
        self.label_6.setText(_translate("SettingsDialog", "Default figure font:", None))
        self.label_4.setText(_translate("SettingsDialog", "Table font:", None))
        self.label_sample_context.setText(_translate("SettingsDialog", "TextLabel", None))
        self.label_5.setText(_translate("SettingsDialog", "Context font:", None))
        self.button_context_font.setText(_translate("SettingsDialog", "Change...", None))
        self.button_reset_context.setText(_translate("SettingsDialog", "Reset", None))
        self.groupBox_3.setTitle(_translate("SettingsDialog", "Additional paths", None))
        self.button_visualizer_path.setText(_translate("SettingsDialog", "B&rowse", None))
        self.button_visualizer_path.setShortcut(_translate("SettingsDialog", "Alt+B", None))
        self.button_installer_path.setText(_translate("SettingsDialog", "&Browse", None))
        self.button_installer_path.setShortcut(_translate("SettingsDialog", "Alt+B", None))
        self.label_9.setText(_translate("SettingsDialog", "&Visualizers:", None))
        self.label_2.setText(_translate("SettingsDialog", "Corpus &installers: ", None))
        self.groupBox_4.setTitle(_translate("SettingsDialog", "Exit options", None))
        self.check_ask_on_quit.setText(_translate("SettingsDialog", "Ask if &unsaved results should be saved upon exit", None))
        self.check_save_query_string.setText(_translate("SettingsDialog", "Save last query &string in configuration file", None))
        self.check_save_query_file.setText(_translate("SettingsDialog", "Save last query &file in configuration file", None))


