# -*- coding: utf-8 -*-

import codecs
import pandas as pd

from pyqt_compat import QtCore, QtGui
import stopwordsUi
import queryfilter
import options
from defines import *

class CoqStopWord(QtGui.QListWidgetItem):
    def __init__(self, *args):
        super(CoqStopWord, self).__init__(*args)
        icon = QtGui.qApp.style().standardIcon(QtGui.QStyle.SP_DockWidgetCloseButton)
        self.setIcon(icon)
        brush = QtGui.QBrush(QtGui.QColor("lightcyan"))
        self.setBackground(brush)
        
class CoqStopwordDelegate(QtGui.QStyledItemDelegate):
    def __init__(self, parent=None, *args):
        super(CoqStopwordDelegate, self).__init__(parent, *args)

    def paint(self, painter, option, index):
        painter.save()

        painter.drawPixmap(0, 0, 
                QtGui.qApp.style().standardPixmap(QtGui.QStyle.SP_DockWidgetCloseButton))
        # set background color
        painter.setPen(QtGui.QPen(QtCore.Qt.NoPen))
        if option.state & QtGui.QStyle.State_Selected:
            painter.setBrush(QtGui.QBrush(QtCore.Qt.red))
        else:
            painter.setBrush(QtGui.QBrush(QtGui.QColor("lightcyan")))
        painter.drawRect(option.rect)

        # set text color
        painter.setPen(QtGui.QPen(QtCore.Qt.black))
        value = index.data(QtCore.Qt.DisplayRole)
        painter.drawText(option.rect, QtCore.Qt.AlignLeft, value)
        

        painter.restore()

        
class CoqAddWord(CoqStopWord):
    def __init__(self, *args):
        super(CoqStopWord, self).__init__(*args)
        self.reset()
    
    def reset(self):
        self.setText("Add...")
        
class CoqStopwordList(QtGui.QListWidget):
    def __init__(self, *args):
        super(CoqStopwordList, self).__init__(*args)
        
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.setFlow(QtGui.QListView.TopToBottom)
        self.setProperty("isWrapping", True)
        self.setMovement(QtGui.QListView.Static)
        self.setResizeMode(QtGui.QListView.Adjust)
        self.setSpacing(10)
        self.setFlow(QtGui.QListView.LeftToRight)
        self.setViewMode(QtGui.QListView.IconMode)
        self.setWordWrap(True)
        self.setSelectionRectVisible(True)

        self.itemClicked.connect(self.onClick)
        self.add_item = None
 
        self.setItemDelegate(CoqStopwordDelegate(parent=self))
 
    def onClick(self, item):
        if item == self.add_item:
            #self.add_item.setText("")
            self.openPersistentEditor(self.add_item)
            print("editing")
            self.itemChanged.connect(self.onChange)
            
    def onChange(self, item):
        if item == self.add_item:
            print("change")
            self.itemChanged.disconnect(self.onChange)
            self.closePersistentEditor(self.add_item)
            words = str(self.add_item.text()).split()
            for x in words:
                self.insertItem(self.count() - 1, CoqStopWord(x))
            self.add_item.reset()

    def addAddItem(self, item, *args):
        super(CoqStopwordList, self).addItem(item, *args)
        self.add_item = item

class Stopwords(QtGui.QDialog):
    def __init__(self, filename, default=None, parent=None, icon=None):
        super(Stopwords, self).__init__(parent)
        
        self.ui = stopwordsUi.Ui_Stopwords()
        self.ui.setupUi(self)
        self.ui.horizontalLayout.removeWidget(self.ui.stopword_list)
        self.ui.stopword_list.close()
        #self.ui.stopword_list = CoqStopwordList()
        self.ui.stopword_list = queryfilter.CoqTagBox(label="Add stop word:")
        self.ui.horizontalLayout.insertWidget(0, self.ui.stopword_list)

        self.ui.buttonBox.button(QtGui.QDialogButtonBox.Reset).clicked.connect(self.reset_list)
        self.ui.buttonBox.button(QtGui.QDialogButtonBox.Save).clicked.connect(self.save_list)
        self.ui.buttonBox.button(QtGui.QDialogButtonBox.Open).clicked.connect(self.open_list)
        self.ui.buttonBox.button(QtGui.QDialogButtonBox.Ok).clicked.connect(self.close)

    def reset_list(self):
        response = QtGui.QMessageBox.question(self, "Clear stop word list", msg_clear_stopwords, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if response == QtGui.QMessageBox.Yes:
            self.ui.stopword_list.cloud_area.clear()
    
    def save_list(self):
        name = QtGui.QFileDialog.getSaveFileName(directory=options.cfg.stopwords_file_path)
        if type(name) == tuple:
            name = name[0]
        if name:
            options.cfg.stopwords_file_path = os.path.dirname(name)
            df = pd.DataFrame(options.cfg.stopword_list)
            try:
                df.to_csv(name,
                        index=False, header=False,
                        encoding=options.cfg.output_encoding)
            except IOError as e:
                QtGui.QMessageBox.critical(self, "Disk error", msg_disk_error)
            except (UnicodeEncodeError, UnicodeDecodeError):
                QtGui.QMessageBox.critical(self, "Encoding error", msg_encoding_error)
    
    def open_list(self):
        name = QtGui.QFileDialog.getOpenFileName(directory=options.cfg.stopwords_file_path)
        if type(name) == tuple:
            name = name[0]
        if name:
            options.cfg.stopwords_file_path = os.path.dirname(name)
            self.ui.buttonBox.setEnabled(False)
            try:
                with codecs.open(name, "r", encoding=options.cfg.output_encoding) as input_file:
                    for word in sorted(set(" ".join(input_file.readlines()).split())):
                        if word and not self.ui.stopword_list.hasTag(word):
                            self.ui.stopword_list.addTag(word)
            except IOError as e:
                QtGui.QMessageBox.critical(self, "Disk error", msg_disk_error)
            except (UnicodeEncodeError, UnicodeDecodeError):
                QtGui.QMessageBox.critical(self, "Encoding error", msg_encoding_error)
            finally:
                self.ui.buttonBox.setEnabled(True)
    
    def close(self):
        super(Stopwords, self).close()
        options.cfg.stopword_list = [
            self.ui.stopword_list.cloud_area.itemAt(x).widget().text() for x in range(self.ui.stopword_list.cloud_area.count())]
        super(Stopwords, self).accept()
    
    def accept(self):
        pass

    def keyPressEvent(self, event):
        print("key")
        if event.key() in [QtCore.Qt.Key_Enter, QtCore.Qt.Key_Return]:
            return
        else:
            super(Stopwords, self).keyPressEvent(event)
        
    def set_list(self, l):
        for x in l:
            self.ui.stopword_list.addTag(x)
        
    @staticmethod
    def manage(parent=None, icon=None):
        dialog = Stopwords(parent, icon)
        dialog.set_list(options.cfg.stopword_list)
        result = dialog.exec_()
