# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addFilter.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from coquery.gui.pyqt_compat import QtCore, QtGui, frameShadow, frameShape

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

class Ui_FiltersDialog(object):
    def setupUi(self, FiltersDialog):
        FiltersDialog.setObjectName(_fromUtf8("FiltersDialog"))
        FiltersDialog.resize(640, 480)
        self.verticalLayout_4 = QtGui.QVBoxLayout(FiltersDialog)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.widget_filters = QtGui.QWidget(FiltersDialog)
        self.widget_filters.setObjectName(_fromUtf8("widget_filters"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.widget_filters)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.table_filters = QtGui.QTableWidget(self.widget_filters)
        self.table_filters.setShowGrid(False)
        self.table_filters.setColumnCount(1)
        self.table_filters.setObjectName(_fromUtf8("table_filters"))
        self.table_filters.setRowCount(0)
        self.table_filters.horizontalHeader().setVisible(False)
        self.table_filters.horizontalHeader().setStretchLastSection(True)
        self.table_filters.verticalHeader().setVisible(False)
        self.verticalLayout_3.addWidget(self.table_filters)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.line = QtGui.QFrame(self.widget_filters)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout.addWidget(self.line)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_2 = QtGui.QLabel(self.widget_filters)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_5.addWidget(self.label_2)
        self.list_columns = QtGui.QListWidget(self.widget_filters)
        self.list_columns.setObjectName(_fromUtf8("list_columns"))
        self.verticalLayout_5.addWidget(self.list_columns)
        self.check_before_transformation = QtGui.QCheckBox(self.widget_filters)
        self.check_before_transformation.setObjectName(_fromUtf8("check_before_transformation"))
        self.verticalLayout_5.addWidget(self.check_before_transformation)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_3 = QtGui.QLabel(self.widget_filters)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.radio_OP_EQ = QtGui.QRadioButton(self.widget_filters)
        self.radio_OP_EQ.setChecked(True)
        self.radio_OP_EQ.setObjectName(_fromUtf8("radio_OP_EQ"))
        self.verticalLayout.addWidget(self.radio_OP_EQ)
        self.radio_OP_NE = QtGui.QRadioButton(self.widget_filters)
        self.radio_OP_NE.setObjectName(_fromUtf8("radio_OP_NE"))
        self.verticalLayout.addWidget(self.radio_OP_NE)
        self.radio_OP_LT = QtGui.QRadioButton(self.widget_filters)
        self.radio_OP_LT.setObjectName(_fromUtf8("radio_OP_LT"))
        self.verticalLayout.addWidget(self.radio_OP_LT)
        self.radio_OP_LE = QtGui.QRadioButton(self.widget_filters)
        self.radio_OP_LE.setObjectName(_fromUtf8("radio_OP_LE"))
        self.verticalLayout.addWidget(self.radio_OP_LE)
        self.radio_OP_GT = QtGui.QRadioButton(self.widget_filters)
        self.radio_OP_GT.setObjectName(_fromUtf8("radio_OP_GT"))
        self.verticalLayout.addWidget(self.radio_OP_GT)
        self.radio_OP_GE = QtGui.QRadioButton(self.widget_filters)
        self.radio_OP_GE.setObjectName(_fromUtf8("radio_OP_GE"))
        self.verticalLayout.addWidget(self.radio_OP_GE)
        self.radio_OP_MATCH = QtGui.QRadioButton(self.widget_filters)
        self.radio_OP_MATCH.setObjectName(_fromUtf8("radio_OP_MATCH"))
        self.verticalLayout.addWidget(self.radio_OP_MATCH)
        self.radio_OP_NMATCH = QtGui.QRadioButton(self.widget_filters)
        self.radio_OP_NMATCH.setObjectName(_fromUtf8("radio_OP_NMATCH"))
        self.verticalLayout.addWidget(self.radio_OP_NMATCH)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.line_2 = QtGui.QFrame(self.widget_filters)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.horizontalLayout.addWidget(self.line_2)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(self.widget_filters)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.edit_value = QtGui.QLineEdit(self.widget_filters)
        self.edit_value.setObjectName(_fromUtf8("edit_value"))
        self.verticalLayout_2.addWidget(self.edit_value)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.button_add = QtGui.QPushButton(self.widget_filters)
        self.button_add.setObjectName(_fromUtf8("button_add"))
        self.verticalLayout_2.addWidget(self.button_add)
        self.button_remove = QtGui.QPushButton(self.widget_filters)
        self.button_remove.setObjectName(_fromUtf8("button_remove"))
        self.verticalLayout_2.addWidget(self.button_remove)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout.setStretch(0, 1)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addWidget(self.widget_filters)
        self.buttonBox = QtGui.QDialogButtonBox(FiltersDialog)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_4.addWidget(self.buttonBox)
        self.label_2.setBuddy(self.list_columns)
        self.label_3.setBuddy(self.radio_OP_EQ)
        self.label.setBuddy(self.edit_value)

        self.retranslateUi(FiltersDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), FiltersDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), FiltersDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(FiltersDialog)

    def retranslateUi(self, FiltersDialog):
        FiltersDialog.setWindowTitle(_translate("FiltersDialog", "Summary filters – Coquery", None))
        self.label_2.setText(_translate("FiltersDialog", "&Column:", None))
        self.check_before_transformation.setText(_translate("FiltersDialog", "&Apply before transformation", None))
        self.label_3.setText(_translate("FiltersDialog", "&Relation:", None))
        self.radio_OP_EQ.setText(_translate("FiltersDialog", "equals", None))
        self.radio_OP_NE.setText(_translate("FiltersDialog", "does not equal", None))
        self.radio_OP_LT.setText(_translate("FiltersDialog", "is less than", None))
        self.radio_OP_LE.setText(_translate("FiltersDialog", "is less or equal than", None))
        self.radio_OP_GT.setText(_translate("FiltersDialog", "is greater than", None))
        self.radio_OP_GE.setText(_translate("FiltersDialog", "is greater or equal than", None))
        self.radio_OP_MATCH.setText(_translate("FiltersDialog", "matches", None))
        self.radio_OP_NMATCH.setText(_translate("FiltersDialog", "does not match", None))
        self.label.setText(_translate("FiltersDialog", "&Value:", None))
        self.button_add.setText(_translate("FiltersDialog", "&Add", None))
        self.button_remove.setText(_translate("FiltersDialog", "&Remove", None))


