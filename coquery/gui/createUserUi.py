# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'createUser.ui'
#
# Created: Mon Sep 21 19:42:48 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from pyqt_compat import QtCore, QtGui, frameShadow

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

class Ui_CreateUser(object):
    def setupUi(self, CreateUser):
        CreateUser.setObjectName(_fromUtf8("CreateUser"))
        CreateUser.resize(586, 569)
        self.verticalLayout_2 = QtGui.QVBoxLayout(CreateUser)
        self.verticalLayout_2.setSpacing(16)
        self.verticalLayout_2.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.frame = QtGui.QFrame(CreateUser)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(frameShadow)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.root_name = QtGui.QLineEdit(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.root_name.sizePolicy().hasHeightForWidth())
        self.root_name.setSizePolicy(sizePolicy)
        self.root_name.setText(_fromUtf8(""))
        self.root_name.setObjectName(_fromUtf8("root_name"))
        self.gridLayout.addWidget(self.root_name, 0, 1, 1, 1)
        self.root_password = QtGui.QLineEdit(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.root_password.sizePolicy().hasHeightForWidth())
        self.root_password.setSizePolicy(sizePolicy)
        self.root_password.setText(_fromUtf8(""))
        self.root_password.setEchoMode(QtGui.QLineEdit.PasswordEchoOnEdit)
        self.root_password.setObjectName(_fromUtf8("root_password"))
        self.gridLayout.addWidget(self.root_password, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.label_7 = QtGui.QLabel(self.frame)
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout.addWidget(self.label_7)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.new_password = QtGui.QLineEdit(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.new_password.sizePolicy().hasHeightForWidth())
        self.new_password.setSizePolicy(sizePolicy)
        self.new_password.setText(_fromUtf8(""))
        self.new_password.setEchoMode(QtGui.QLineEdit.PasswordEchoOnEdit)
        self.new_password.setObjectName(_fromUtf8("new_password"))
        self.gridLayout_2.addWidget(self.new_password, 1, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.frame)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.new_name = QtGui.QLineEdit(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.new_name.sizePolicy().hasHeightForWidth())
        self.new_name.setSizePolicy(sizePolicy)
        self.new_name.setText(_fromUtf8(""))
        self.new_name.setObjectName(_fromUtf8("new_name"))
        self.gridLayout_2.addWidget(self.new_name, 0, 1, 1, 1)
        self.new_password_check = QtGui.QLineEdit(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.new_password_check.sizePolicy().hasHeightForWidth())
        self.new_password_check.setSizePolicy(sizePolicy)
        self.new_password_check.setText(_fromUtf8(""))
        self.new_password_check.setEchoMode(QtGui.QLineEdit.PasswordEchoOnEdit)
        self.new_password_check.setObjectName(_fromUtf8("new_password_check"))
        self.gridLayout_2.addWidget(self.new_password_check, 2, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.frame)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.check_show_passwords = QtGui.QCheckBox(self.frame)
        self.check_show_passwords.setObjectName(_fromUtf8("check_show_passwords"))
        self.verticalLayout.addWidget(self.check_show_passwords)
        self.verticalLayout_2.addWidget(self.frame)
        self.buttonBox = QtGui.QDialogButtonBox(CreateUser)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(CreateUser)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), CreateUser.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), CreateUser.reject)
        QtCore.QMetaObject.connectSlotsByName(CreateUser)
        CreateUser.setTabOrder(self.root_name, self.root_password)
        CreateUser.setTabOrder(self.root_password, self.new_name)
        CreateUser.setTabOrder(self.new_name, self.new_password)
        CreateUser.setTabOrder(self.new_password, self.new_password_check)
        CreateUser.setTabOrder(self.new_password_check, self.check_show_passwords)
        CreateUser.setTabOrder(self.check_show_passwords, self.buttonBox)

    def retranslateUi(self, CreateUser):
        CreateUser.setWindowTitle(_translate("CreateUser", "Create a new MySQL user – Coquery", None))
        self.label.setText(_translate("CreateUser", "<html><head/><body><p>In order to create a new MySQL user and provide it with the required database privileges, you need to provide the <span style=\" font-weight:600;\">MySQL root user</span> and <span style=\" font-weight:600;\">MySQL root password</span>. Do not use your system root or administrator account credentials.</p></body></html>", None))
        self.label_2.setText(_translate("CreateUser", "Root password:", None))
        self.label_3.setText(_translate("CreateUser", "Root user:", None))
        self.label_7.setText(_translate("CreateUser", "<html><head/><body><p>Enter a user name and a password. This user will be granted all privileges that are required to create, query, modify, and delete MySQL databases and tables. This user will not have the privilege to create or modify the priviledges of other users.</p></body></html>", None))
        self.label_4.setText(_translate("CreateUser", "Password:", None))
        self.label_5.setText(_translate("CreateUser", "New user name:", None))
        self.label_6.setText(_translate("CreateUser", "Retype password::", None))
        self.check_show_passwords.setText(_translate("CreateUser", "Show passwords", None))


