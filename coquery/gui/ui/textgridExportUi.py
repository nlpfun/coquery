# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'textgridExport.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TextgridExport(object):
    def setupUi(self, TextgridExport):
        TextgridExport.setObjectName("TextgridExport")
        TextgridExport.resize(640, 480)
        self.verticalLayout = QtWidgets.QVBoxLayout(TextgridExport)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(TextgridExport)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.edit_output_path = QtWidgets.QLineEdit(self.groupBox)
        self.edit_output_path.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edit_output_path.sizePolicy().hasHeightForWidth())
        self.edit_output_path.setSizePolicy(sizePolicy)
        self.edit_output_path.setAccessibleDescription("")
        self.edit_output_path.setObjectName("edit_output_path")
        self.gridLayout.addWidget(self.edit_output_path, 0, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.button_output_path = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_output_path.sizePolicy().hasHeightForWidth())
        self.button_output_path.setSizePolicy(sizePolicy)
        self.button_output_path.setObjectName("button_output_path")
        self.gridLayout.addWidget(self.button_output_path, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.edit_file_prefix = QtWidgets.QLineEdit(self.groupBox)
        self.edit_file_prefix.setObjectName("edit_file_prefix")
        self.horizontalLayout_4.addWidget(self.edit_file_prefix)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.tabWidget = QtWidgets.QTabWidget(TextgridExport)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_5.addWidget(self.label_8)
        self.list_columns = CoqListSelect(self.tab)
        self.list_columns.setObjectName("list_columns")
        self.verticalLayout_5.addWidget(self.list_columns)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.radio_one_per_match = QtWidgets.QRadioButton(self.tab_2)
        self.radio_one_per_match.setObjectName("radio_one_per_match")
        self.verticalLayout_6.addWidget(self.radio_one_per_match)
        self.radio_one_per_file = QtWidgets.QRadioButton(self.tab_2)
        self.radio_one_per_file.setObjectName("radio_one_per_file")
        self.verticalLayout_6.addWidget(self.radio_one_per_file)
        self.line = QtWidgets.QFrame(self.tab_2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_6.addWidget(self.line)
        self.check_remember = QtWidgets.QCheckBox(self.tab_2)
        self.check_remember.setObjectName("check_remember")
        self.verticalLayout_6.addWidget(self.check_remember)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.check_copy_sounds = QtWidgets.QCheckBox(self.tab_3)
        self.check_copy_sounds.setText("")
        self.check_copy_sounds.setObjectName("check_copy_sounds")
        self.gridLayout_3.addWidget(self.check_copy_sounds, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.edit_sound_path = QtWidgets.QLineEdit(self.tab_3)
        self.edit_sound_path.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edit_sound_path.sizePolicy().hasHeightForWidth())
        self.edit_sound_path.setSizePolicy(sizePolicy)
        self.edit_sound_path.setAccessibleDescription("")
        self.edit_sound_path.setObjectName("edit_sound_path")
        self.horizontalLayout_2.addWidget(self.edit_sound_path)
        self.button_sound_path = QtWidgets.QPushButton(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_sound_path.sizePolicy().hasHeightForWidth())
        self.button_sound_path.setSizePolicy(sizePolicy)
        self.button_sound_path.setObjectName("button_sound_path")
        self.horizontalLayout_2.addWidget(self.button_sound_path)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab_3)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 0, 1, 1, 1)
        self.groupbox = QtWidgets.QGroupBox(self.tab_3)
        self.groupbox.setObjectName("groupbox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupbox)
        self.gridLayout_4.setContentsMargins(6, 6, 6, 6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_2 = QtWidgets.QLabel(self.groupbox)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupbox)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 0, 1, 1, 1)
        self.spin_left_padding = QtWidgets.QDoubleSpinBox(self.groupbox)
        self.spin_left_padding.setDecimals(3)
        self.spin_left_padding.setMaximum(999.999)
        self.spin_left_padding.setSingleStep(0.1)
        self.spin_left_padding.setObjectName("spin_left_padding")
        self.gridLayout_4.addWidget(self.spin_left_padding, 0, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem2, 0, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupbox)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 0, 4, 1, 1)
        self.spin_right_padding = QtWidgets.QDoubleSpinBox(self.groupbox)
        self.spin_right_padding.setDecimals(3)
        self.spin_right_padding.setMaximum(999.999)
        self.spin_right_padding.setSingleStep(0.1)
        self.spin_right_padding.setObjectName("spin_right_padding")
        self.gridLayout_4.addWidget(self.spin_right_padding, 0, 5, 1, 1)
        self.gridLayout_3.addWidget(self.groupbox, 2, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 3, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.buttonBox = QtWidgets.QDialogButtonBox(TextgridExport)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.label_7.setBuddy(self.edit_file_prefix)
        self.label.setBuddy(self.edit_output_path)
        self.label_4.setBuddy(self.check_copy_sounds)
        self.label_5.setBuddy(self.spin_left_padding)
        self.label_6.setBuddy(self.spin_right_padding)

        self.retranslateUi(TextgridExport)
        self.tabWidget.setCurrentIndex(0)
        self.buttonBox.rejected.connect(TextgridExport.reject)
        self.buttonBox.accepted.connect(TextgridExport.accept)
        QtCore.QMetaObject.connectSlotsByName(TextgridExport)

    def retranslateUi(self, TextgridExport):
        _translate = QtCore.QCoreApplication.translate
        TextgridExport.setWindowTitle(_translate("TextgridExport", "Export to text grids – Coquery"))
        self.groupBox.setTitle(_translate("TextgridExport", "Save as text grid files"))
        self.edit_output_path.setPlaceholderText(_translate("TextgridExport", "Input path name"))
        self.label_7.setText(_translate("TextgridExport", "Fi&le prefix:"))
        self.button_output_path.setText(_translate("TextgridExport", "&Browse"))
        self.button_output_path.setShortcut(_translate("TextgridExport", "Alt+B"))
        self.label.setText(_translate("TextgridExport", "&Output path:"))
        self.label_8.setText(_translate("TextgridExport", "Select the columns that will be included as tiers in the text grids."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("TextgridExport", "&Columns"))
        self.radio_one_per_match.setText(_translate("TextgridExport", "Create one text grid for each &match"))
        self.radio_one_per_file.setText(_translate("TextgridExport", "Create one &text grid for each source file"))
        self.check_remember.setText(_translate("TextgridExport", "&Remember original time in a point tier"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("TextgridExport", "Text &grids"))
        self.edit_sound_path.setPlaceholderText(_translate("TextgridExport", "Input path name"))
        self.button_sound_path.setText(_translate("TextgridExport", "&Browse"))
        self.button_sound_path.setShortcut(_translate("TextgridExport", "Alt+B"))
        self.label_4.setText(_translate("TextgridExport", "&Copy matching sound files to output path:"))
        self.groupbox.setTitle(_translate("TextgridExport", "Add audio context"))
        self.label_5.setText(_translate("TextgridExport", "&Before:"))
        self.spin_left_padding.setSuffix(_translate("TextgridExport", " seconds"))
        self.label_6.setText(_translate("TextgridExport", "&After:"))
        self.spin_right_padding.setSuffix(_translate("TextgridExport", " seconds"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("TextgridExport", "&Sound files"))

from ..listselect import CoqListSelect

