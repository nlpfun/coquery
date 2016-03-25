# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'corpusInstaller.ui'
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

class Ui_CorpusInstaller(object):
    def setupUi(self, CorpusInstaller):
        CorpusInstaller.setObjectName(_fromUtf8("CorpusInstaller"))
        CorpusInstaller.resize(640, 480)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CorpusInstaller.sizePolicy().hasHeightForWidth())
        CorpusInstaller.setSizePolicy(sizePolicy)
        CorpusInstaller.setModal(True)
        self.verticalLayout_3 = QtGui.QVBoxLayout(CorpusInstaller)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.frame = QtGui.QFrame(CorpusInstaller)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(frameShape)
        self.frame.setFrameShadow(frameShadow)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout.setMargin(10)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.corpus_description = QtGui.QLabel(self.frame)
        self.corpus_description.setWordWrap(True)
        self.corpus_description.setObjectName(_fromUtf8("corpus_description"))
        self.verticalLayout.addWidget(self.corpus_description)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setVerticalSpacing(10)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.box_build_options = QtGui.QGroupBox(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.box_build_options.sizePolicy().hasHeightForWidth())
        self.box_build_options.setSizePolicy(sizePolicy)
        self.box_build_options.setObjectName(_fromUtf8("box_build_options"))
        self.gridLayout = QtGui.QGridLayout(self.box_build_options)
        self.gridLayout.setMargin(10)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.input_path = QtGui.QLineEdit(self.box_build_options)
        self.input_path.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_path.sizePolicy().hasHeightForWidth())
        self.input_path.setSizePolicy(sizePolicy)
        self.input_path.setObjectName(_fromUtf8("input_path"))
        self.gridLayout.addWidget(self.input_path, 1, 0, 1, 1)
        self.label_8 = QtGui.QLabel(self.box_build_options)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 1)
        self.layout_nltk = QtGui.QHBoxLayout()
        self.layout_nltk.setObjectName(_fromUtf8("layout_nltk"))
        self.use_pos_tagging = QtGui.QCheckBox(self.box_build_options)
        self.use_pos_tagging.setText(_fromUtf8(""))
        self.use_pos_tagging.setObjectName(_fromUtf8("use_pos_tagging"))
        self.layout_nltk.addWidget(self.use_pos_tagging)
        self.label_pos_tagging = QtGui.QLabel(self.box_build_options)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_pos_tagging.sizePolicy().hasHeightForWidth())
        self.label_pos_tagging.setSizePolicy(sizePolicy)
        self.label_pos_tagging.setText(_fromUtf8(""))
        self.label_pos_tagging.setWordWrap(True)
        self.label_pos_tagging.setObjectName(_fromUtf8("label_pos_tagging"))
        self.layout_nltk.addWidget(self.label_pos_tagging)
        self.gridLayout.addLayout(self.layout_nltk, 2, 0, 1, 1)
        self.button_input_path = QtGui.QPushButton(self.box_build_options)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_input_path.sizePolicy().hasHeightForWidth())
        self.button_input_path.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("folder"))
        self.button_input_path.setIcon(icon)
        self.button_input_path.setObjectName(_fromUtf8("button_input_path"))
        self.gridLayout.addWidget(self.button_input_path, 1, 1, 1, 1)
        self.widget_ngram = QtGui.QWidget(self.box_build_options)
        self.widget_ngram.setObjectName(_fromUtf8("widget_ngram"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget_ngram)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.check_ngram = QtGui.QCheckBox(self.widget_ngram)
        self.check_ngram.setText(_fromUtf8(""))
        self.check_ngram.setObjectName(_fromUtf8("check_ngram"))
        self.horizontalLayout_3.addWidget(self.check_ngram)
        self.label_2 = QtGui.QLabel(self.widget_ngram)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.spin_n = QtGui.QSpinBox(self.widget_ngram)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spin_n.sizePolicy().hasHeightForWidth())
        self.spin_n.setSizePolicy(sizePolicy)
        self.spin_n.setMinimum(2)
        self.spin_n.setProperty("value", 2)
        self.spin_n.setObjectName(_fromUtf8("spin_n"))
        self.horizontalLayout_3.addWidget(self.spin_n)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label_ngram_info = QtGui.QLabel(self.widget_ngram)
        self.label_ngram_info.setObjectName(_fromUtf8("label_ngram_info"))
        self.horizontalLayout_3.addWidget(self.label_ngram_info)
        self.horizontalLayout_3.setStretch(3, 1)
        self.gridLayout.addWidget(self.widget_ngram, 3, 0, 1, 1)
        self.gridLayout_2.addWidget(self.box_build_options, 1, 1, 1, 1)
        self.radio_only_module = QtGui.QRadioButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radio_only_module.sizePolicy().hasHeightForWidth())
        self.radio_only_module.setSizePolicy(sizePolicy)
        self.radio_only_module.setText(_fromUtf8(""))
        self.radio_only_module.setObjectName(_fromUtf8("radio_only_module"))
        self.gridLayout_2.addWidget(self.radio_only_module, 3, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.frame)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_2.addWidget(self.label_6, 3, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.frame)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 0, 1, 1, 1)
        self.radio_complete = QtGui.QRadioButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radio_complete.sizePolicy().hasHeightForWidth())
        self.radio_complete.setSizePolicy(sizePolicy)
        self.radio_complete.setText(_fromUtf8(""))
        self.radio_complete.setChecked(True)
        self.radio_complete.setObjectName(_fromUtf8("radio_complete"))
        self.gridLayout_2.addWidget(self.radio_complete, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.verticalLayout_3.addWidget(self.frame)
        spacerItem1 = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.progress_box = QtGui.QFrame(CorpusInstaller)
        self.progress_box.setFrameShape(frameShape)
        self.progress_box.setFrameShadow(frameShadow)
        self.progress_box.setObjectName(_fromUtf8("progress_box"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.progress_box)
        self.verticalLayout_2.setMargin(10)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(self.progress_box)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.progress_general = QtGui.QProgressBar(self.progress_box)
        self.progress_general.setMinimum(0)
        self.progress_general.setMaximum(9)
        self.progress_general.setProperty("value", 0)
        self.progress_general.setObjectName(_fromUtf8("progress_general"))
        self.verticalLayout_2.addWidget(self.progress_general)
        self.progress_bar = QtGui.QProgressBar(self.progress_box)
        self.progress_bar.setProperty("value", 0)
        self.progress_bar.setFormat(_fromUtf8(""))
        self.progress_bar.setObjectName(_fromUtf8("progress_bar"))
        self.verticalLayout_2.addWidget(self.progress_bar)
        self.verticalLayout_3.addWidget(self.progress_box)
        self.buttonBox = QtGui.QDialogButtonBox(CorpusInstaller)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Yes)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_3.addWidget(self.buttonBox)
        self.label_pos_tagging.setBuddy(self.use_pos_tagging)
        self.label_2.setBuddy(self.check_ngram)

        self.retranslateUi(CorpusInstaller)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), CorpusInstaller.reject)
        QtCore.QMetaObject.connectSlotsByName(CorpusInstaller)

    def retranslateUi(self, CorpusInstaller):
        CorpusInstaller.setWindowTitle(_translate("CorpusInstaller", "Corpus Installer – Coquery", None))
        self.corpus_description.setText(_translate("CorpusInstaller", "<html><head/><body><p><span style=\" font-weight:600;\">Corpus installer</span></p><p>You have requested to install \'<span style=\" font-weight:600;\">{}\'</span> using the database connection \'{}\'.</p></body></html>", None))
        self.label_8.setText(_translate("CorpusInstaller", "Path to corpus data files:", None))
        self.button_input_path.setText(_translate("CorpusInstaller", "Browse", None))
        self.button_input_path.setShortcut(_translate("CorpusInstaller", "Alt+B", None))
        self.label_2.setText(_translate("CorpusInstaller", "&Generate lookup table for multi-item query strings,", None))
        self.spin_n.setSuffix(_translate("CorpusInstaller", " items", None))
        self.spin_n.setPrefix(_translate("CorpusInstaller", "up to ", None))
        self.label_ngram_info.setToolTip(_translate("CorpusInstaller", "<html><head/><body><p>A lookup table for multi-item queries is an additional database table. For each token in the corpus, this table also contains information on the <span style=\" font-style:italic;\">n</span> following tokens. Using a lookup table can greatly speed up queries that consist of more than one query item. However, it also greatly increases the disk space required for the corpus database, and it increases the time required to install the corpus.</p><p>Lookup tables are recommended for the larger corpora such as the BNC, COCA, or COHA.</p><p>Note that even if you do not generate a lookup table for multi-item query strings, you can still use query strings that consist of more than one query item, or that are longer than the lookup table. However, in these cases, the query may be relatively slow.</p><p>For a detailed description of multi-token lookup tables, see:</p><p>Davies, Mark. Semantically-based queries with a joint <span style=\" font-style:italic;\">BNC/WordNet</span> database. In Facchinetti, Roberta (ed.). <span style=\" font-style:italic;\">Corpus linguistics 25 years on.</span> 149–168. Amsterdam: Rodopi.</p></body></html>", None))
        self.label_ngram_info.setText(_translate("CorpusInstaller", "?", None))
        self.label_6.setText(_translate("CorpusInstaller", "Only install corpus module (e.g. if you have a network database server)", None))
        self.label_5.setText(_translate("CorpusInstaller", "Install corpus data and corpus module (if you have a local database server)", None))
        self.label.setText(_translate("CorpusInstaller", "Installing...", None))
        self.progress_general.setFormat(_translate("CorpusInstaller", "Stage %v of %m", None))


