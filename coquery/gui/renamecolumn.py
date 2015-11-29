# -*- coding: utf-8 -*-
"""
renamecolumn.py is part of Coquery.

Copyright (c) 2015 Gero Kunter (gero.kunter@coquery.org)

Coquery is released under the terms of the GNU General Public License.
For details, see the file LICENSE that you should have received along 
with Coquery. If not, see <http://www.gnu.org/licenses/>.
"""

from __future__ import division
from __future__ import unicode_literals

from pyqt_compat import QtCore, QtGui

import sys
import re
import renameColumnUi

try:
    import options
except ImportError:
    pass

def func_regexp(x, s):
    match = re.search("({})".format(s), x)
    if match:
        return match.group(1)
    else:
        return ""

def func_match(x, s):
    match = re.search('({})'.format(s), x)
    if match:
        return "yes"
    else:
        return "no"

class RenameColumnDialog(QtGui.QDialog):
    def __init__(self, header_name, current_name, parent=None):
        
        super(RenameColumnDialog, self).__init__(parent)

        self.ui = renameColumnUi.Ui_Dialog()
        self.ui.setupUi(self)


        if not current_name:
            current_name = header_name

        self.ui.label.setText(str(self.ui.label.text()).format(header_name))
        self.ui.edit_column_name.setText(current_name)
        self.ui.buttonBox.button(QtGui.QDialogButtonBox.Reset).clicked.connect(
            lambda x: self.ui.edit_column_name.setText(header_name))
        
    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Escape:
            self.reject()
            
    def closeEvent(self, *args):
        try:
            options.cfg.rename_column_height = self.height()
            options.cfg.rename_column_width = self.width()        
        except NameError:
            pass
        
    @staticmethod
    def get_name(header, name, parent=None):
        
        dialog = RenameColumnDialog(header, name, parent=parent)        
        dialog.setVisible(True)
        result = dialog.exec_()
        if result == QtGui.QDialog.Accepted:
            value = str(dialog.ui.edit_column_name.text())
            return value
        else:
            return name

def main():
    app = QtGui.QApplication(sys.argv)
    print(RenameColumnDialog.get_name('MATCH(\'^\\\'|"\', PhonStrsDISC)', 
                                      'MATCH(\'^\\\'|"\', PhonStrsDISC)'))
    
if __name__ == "__main__":
    main()
    