# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'visualizer.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Visualizer(object):
    def setupUi(self, Visualizer):
        Visualizer.setObjectName("Visualizer")
        Visualizer.resize(800, 600)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Visualizer)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(Visualizer)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setObjectName("frame_2")
        self.navigation_layout = QtWidgets.QHBoxLayout(self.frame_2)
        self.navigation_layout.setContentsMargins(6, 0, 6, 0)
        self.navigation_layout.setObjectName("navigation_layout")
        self.horizontalLayout_3.addWidget(self.frame_2)
        self.verticalLayout_2.addWidget(self.frame)
        self.frame_placeholder = QtWidgets.QFrame(Visualizer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_placeholder.sizePolicy().hasHeightForWidth())
        self.frame_placeholder.setSizePolicy(sizePolicy)
        self.frame_placeholder.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_placeholder.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_placeholder.setObjectName("frame_placeholder")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_placeholder)
        self.verticalLayout_3.setContentsMargins(6, 8, 6, 8)
        self.verticalLayout_3.setSpacing(16)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.frame_placeholder)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.progress_bar = QtWidgets.QProgressBar(self.frame_placeholder)
        self.progress_bar.setProperty("value", 24)
        self.progress_bar.setObjectName("progress_bar")
        self.verticalLayout_4.addWidget(self.progress_bar)
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.verticalLayout_2.addWidget(self.frame_placeholder)
        self.box_visualize = QtWidgets.QFrame(Visualizer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.box_visualize.sizePolicy().hasHeightForWidth())
        self.box_visualize.setSizePolicy(sizePolicy)
        self.box_visualize.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.box_visualize.setFrameShadow(QtWidgets.QFrame.Raised)
        self.box_visualize.setObjectName("box_visualize")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.box_visualize)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2.addWidget(self.box_visualize)
        self.box_visualize.raise_()
        self.frame.raise_()
        self.frame_placeholder.raise_()

        self.retranslateUi(Visualizer)
        QtCore.QMetaObject.connectSlotsByName(Visualizer)

    def retranslateUi(self, Visualizer):
        _translate = QtCore.QCoreApplication.translate
        Visualizer.setWindowTitle(_translate("Visualizer", "Data visualization – Coquery"))
        self.label.setText(_translate("Visualizer", "Visualizing... "))


