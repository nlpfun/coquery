# -*- coding: utf-8 -*-

"""
MySQLOptions.py is part of Coquery.

Copyright (c) 2015 Gero Kunter (gero.kunter@coquery.org)

Coquery is released under the terms of the GNU General Public License.
For details, see the file LICENSE that you should have received along 
with Coquery. If not, see <http://www.gnu.org/licenses/>.
"""

from __future__ import division
from __future__ import unicode_literals

import argparse
import socket
import re
import string
import sys

from pyqt_compat import QtCore, QtGui
import mysqlConfigurationUi

import sqlwrap
from errors import *
import QtProgress


def check_valid_host(s):
    """
    Check if a string is a valid host name or a valid IP address.
    
    The check involves three steps. First, it is checked if the string
    represents a valid IPv6 address by opening a IP6V socket. Then, the 
    same check is performed for IPv4 adresses. Finally, the string is 
    checked for formal appropriateness as a hostname.
    
    Parameters
    ----------
    s : string
        A string representing either an IP address or a host name
    
    Returns
    -------
    b : bool
        True if the string is valid as a host name or IP address, and False
        otherwise.
    """

    def is_valid_ipv4_address(address):
        try:
            socket.inet_pton(socket.AF_INET, address)
        except AttributeError: 
            try:
                socket.inet_aton(address)
            except socket.error:
                return False
            return address.count('.') == 3
        except socket.error:
            return False
        return True

    def is_valid_ipv6_address(address):
        try:
            socket.inet_pton(socket.AF_INET6, address)
        except (socket.error, AttributeError):  # not a valid address
            return False
        return True

    def is_valid_hostname(s):
        if len(s) > 255:
            return False
        # strings must contain at least one letter, otherwise they should be
        # considered ip addresses
        if not any([x in string.ascii_letters for x in s]):
            return
        if s.endswith("."):
            s= s[:-1] # strip exactly one dot from the right, if present
        allowed = re.compile("(?!-)[A-Z\d-]{1,63}(?<!-)$", re.IGNORECASE)
        return all(allowed.match(x) for x in s.split("."))

    if is_valid_ipv6_address(s):
        return True
    if is_valid_ipv4_address(s):
        return True
    if is_valid_hostname(s):
        return True
    return False

class MySQLOptions(QtGui.QDialog):
    noConnection = QtCore.Signal(Exception)
    accessDenied = QtCore.Signal(Exception)
    connected = QtCore.Signal()
    
    def __init__(self, name, config_dict, host="127.0.0.1", port=3306, user="mysql", password="mysql", parent=None):
        
        super(MySQLOptions, self).__init__(parent)
        
        self.default_host = host
        self.default_port = port
        self.default_user = user
        self.default_password = password
    
        self.current_server = name
        self.config_dict = config_dict
        
        self.ui = mysqlConfigurationUi.Ui_MySQLConfig()
        self.ui.setupUi(self)
        
        self.ui.buttonBox.button(QtGui.QDialogButtonBox.Ok).setEnabled(False)

        # set up button signals
        self.ui.button_create_user.clicked.connect(self.create_user)
        self.ui.button_add.clicked.connect(self.add_configuration)
        self.ui.button_replace.clicked.connect(self.replace_configuration)
        self.ui.button_remove.clicked.connect(self.remove_configuration)
        
        # set up connection signals:
        self.noConnection.connect(lambda x: self.update_connection("noConnection", x))
        self.accessDenied.connect(lambda x: self.update_connection("accessDenied", x))
        self.connected.connect(lambda: self.update_connection("connected"))
        self.state = None
        
        # set the validator for the configuration name QLineEdit so that
        # only an alphanumeric string (including '_') can be entered:
        self.ui.configuration_name.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[A-Za-z0-9_]*")))
        
        # fill tree widget with existing server configurations:
        for x in sorted(self.config_dict):
            current_item = QtGui.QTreeWidgetItem()
            current_item.setText(0, x)
            self.ui.tree_configuration.insertTopLevelItem(0, current_item)
        
        self.set_configuration(self.get_configuration())
        self.update_configuration(False)

        self.ui.tree_configuration.itemActivated.connect(self.apply_configuration)
        self.ui.configuration_name.textChanged.connect(lambda: self.update_configuration(False))

        self.ui.hostname.textChanged.connect(lambda: self.update_configuration(True))
        self.ui.user.textChanged.connect(lambda: self.update_configuration(True))
        self.ui.password.textChanged.connect(lambda: self.update_configuration(True))
        self.ui.port.valueChanged.connect(lambda: self.update_configuration(True))
        self.ui.radio_local.clicked.connect(lambda: self.update_configuration(True))
        self.ui.radio_remote.clicked.connect(lambda: self.update_configuration(True))

    def update_connection(self, state, exc=None):
        if state == "noConnection":
            self.ui.label_connection.setText("Could not connect to a MySQL server.<br/>{}".format(exc))
            self.ui.button_status.setStyleSheet('QPushButton {background-color: red; color: red;}')
        elif state == "accessDenied":
            self.ui.label_connection.setText("A MySQL server was found, but access was denied. Check the user name and password, or create a new MySQL user.")
            self.ui.button_status.setStyleSheet('QPushButton {background-color: yellow; color: yellow;}')
        elif state == "connected": 
            self.ui.button_status.setStyleSheet('QPushButton {background-color: green; color: green;}')
            self.ui.label_connection.setText("Coquery is successfully connected to the MySQL server.")
        self.state = state
        try:
            self.timer.stop()
        except AttributeError: 
            pass
        self.check_buttons()

    def check_buttons(self):
        # disable all buttons by default:
        self.ui.button_add.setEnabled(False)
        self.ui.button_replace.setEnabled(False)
        self.ui.button_remove.setEnabled(False)
        self.ui.buttonBox.button(QtGui.QDialogButtonBox.Ok).setEnabled(False)
        
        name = str(self.ui.configuration_name.text())

        # exit if no configuration name has been entered:
        if not name:
            return

        # enable either the Add or the Remove button, depending on whether
        # there is already a configuration with the current name:
        if self.state == "connected":
            if name not in self.config_dict:
                self.ui.button_add.setEnabled(True)
            else:
                # only enable Replace button if current values are different
                # from the stored values:
                d = self.get_values()
                if (d["host"] != self.config_dict[name]["host"] or
                    d["port"] != self.config_dict[name]["port"] or
                    d["user"] != self.config_dict[name]["user"] or
                    d["password"] != self.config_dict[name]["password"]):
                    self.ui.button_replace.setEnabled(True)
                else:
                    # Enable the Ok button:
                    self.ui.buttonBox.button(QtGui.QDialogButtonBox.Ok).setEnabled(True)
                    
                # Select item in tree:
                self.current_item = self.ui.tree_configuration.findItems(name, QtCore.Qt.MatchExactly, 0)[0]
                self.ui.tree_configuration.insertTopLevelItem(0, self.current_item)
                self.ui.tree_configuration.setCurrentItem(self.current_item)
                self.current_item.setSelected(True)
                
                # Also, enable the Remove button:
                self.ui.button_remove.setEnabled(True)

    def apply_configuration(self, item):
        self.current_configuration = self.config_dict[str(item.text(0))]
        self.current_configuration["name"] = str(item.text(0))
        self.set_configuration(self.current_configuration)
        self.update_configuration(True)
            
    def set_configuration(self, d):
        self.ui.configuration_name.setText(d["name"])

        if d["host"] == "127.0.0.1":
            self.ui.radio_local.setChecked(True)
        else:
            self.ui.radio_remote.setChecked(True)
            self.ui.hostname.setText(d["host"])
        
        self.ui.user.setText(d["user"])
        self.ui.password.setText(d["password"])
        self.ui.port.setValue(int(d["port"]))
        
    def get_configuration(self):
        if self.current_server in self.config_dict:
            # Select the current configuration in the tree:
            self.current_item = self.ui.tree_configuration.findItems(self.current_server, QtCore.Qt.MatchExactly, 0)[0]
            self.ui.tree_configuration.setCurrentItem(self.current_item)
            self.current_item.setSelected(True)                
            return self.config_dict[self.current_server]
        else:
            return {
                "name": "Default",
                "host": self.default_host,
                "port": self.default_port,
                "user": self.default_user,
                "password": self.default_password}
    
    def get_values(self):
        d = dict()
        d["name"] = str(self.ui.configuration_name.text())
        d["host"] = self.get_hostname()
        d["port"] = int(self.ui.port.text())
        d["user"] = str(self.ui.user.text())
        d["password"] = str(self.ui.password.text())
        return d
    
    def add_configuration(self):
        name = str(self.ui.configuration_name.text())
        self.config_dict[name] = self.get_values()
        self.current_item = QtGui.QTreeWidgetItem()
        self.current_item.setText(0, name)
        self.ui.tree_configuration.insertTopLevelItem(0, self.current_item)
        self.ui.tree_configuration.setCurrentItem(self.current_item)
        self.current_item.setSelected(True)
        self.check_buttons()
    
    def remove_configuration(self):
        name = str(self.ui.configuration_name.text())
        current_item = self.ui.tree_configuration.findItems(name, QtCore.Qt.MatchExactly, 0)[0]
        self.ui.tree_configuration.takeTopLevelItem(
            self.ui.tree_configuration.indexOfTopLevelItem(current_item))
        self.config_dict.pop(name)
        self.check_buttons()
    
    def replace_configuration(self):
        name = str(self.ui.configuration_name.text())
        self.config_dict[name] = self.get_values()

    def get_hostname(self):
        if self.ui.radio_local.isChecked():
            hostname = "127.0.0.1"
        else:
            hostname = str(self.ui.hostname.text())
            if hostname == "localhost":
                hostname == "127.0.0.1"
        if hostname == "127.0.0.1":
            self.ui.radio_local.setChecked(True)
            self.ui.hostname.setText("")
            self.ui.hostname.setEnabled(False)
        else:
            self.ui.radio_local.setChecked(False)
            self.ui.hostname.setEnabled(True)
        return hostname

    def create_user(self):
        import createuser
        name = str(self.ui.user.text())
        password = str(self.ui.password.text())
        create_data = createuser.CreateUser.get(name, password, self)

        hostname = self.get_hostname()

        if create_data:
            root_name, root_password, name, password = create_data
            try:
                DB = sqlwrap.SqlDB(
                    hostname,
                    self.ui.port.value(),
                    root_name,
                    root_password)
            except SQLInitializationError:
                QtGui.QMessageBox.critical(self, "Access as root failed", "<p>A root access to the MySQL server could not be established.</p><p>Please check the MySQL root name and the MySQL root password, and try again to create a user.") 
                return
            S = """
            CREATE USER '{user}'@'{hostname}' IDENTIFIED BY '{password}';
            GRANT ALL PRIVILEGES ON * . * TO '{user}'@'{hostname}';
            FLUSH PRIVILEGES;""".format(
                user=name, password=password, hostname=hostname)
            try:
                DB.Cur.execute(S)
            except:
                QtGui.QMessageBox.critical(self, "Error creating user", "Apologies – the user named '{}' could not be created on the MySQL server.".format(name))
                return
            else:
                QtGui.QMessageBox.information(self, "User created", "The user named '{}' has successfully been created on the MySQL server.".format(name))
            finally:
                DB.close()
            self.ui.user.setText(name)
            self.ui.password.setText(password)
            self.check_connection()
            
    def update_configuration(self, connection_changed):
        self.configuration_changed = connection_changed
        if connection_changed or self.state == None:
            self.current_connection = self.check_connection()
        self.check_buttons()
            
    def check_connection(self):
        """ Check if a connection to a MySQL server can be established using
        the settings from the GUI. Return True if a connection can be
        established, or True if not. Also, set up the connection indicator
        accordingly."""

        hostname = self.get_hostname()
        if hostname == "127.0.0.1":
            self.ui.radio_local.setChecked(True)
            self.ui.hostname.setText("")
            self.ui.hostname.setEnabled(False)
        else:
            self.ui.radio_local.setChecked(False)
            self.ui.hostname.setEnabled(True)

        if check_valid_host(hostname):
            self.probe_thread = QtProgress.ProgressThread(lambda: self.probe_host(hostname), self)
            self.ui.button_status.setStyleSheet('QPushButton {background-color: grey; color: grey;}')
            self.timer = QtCore.QTimer()
            self.timer.timeout.connect(self.update_timeout)
            self.timeout_remain = 60
            self.timer.start(1000)
            self.probe_thread.start()
        else:
            self.noConnection.emit(Exception("Invalid hostname or invalid IP address"))
        
    def update_timeout(self):
        try:
            if self.probe_thread.isRunning() and self.timeout_remain >= 0:
                self.timeout_remain = self.timeout_remain - 1
                self.ui.label_connection.setText(
                    "Testing connection (timeout in {} seconds)...".format(self.timeout_remain))
        except AttributeError:
            pass
        
    def probe_host(self, hostname):
        try:
            DB = sqlwrap.SqlDB(
                Host=hostname,
                Port=self.ui.port.value(),
                User=str(self.ui.user.text()),
                connect_timeout=60,
                Password=str(self.ui.password.text()))
            DB.Cur.execute("SELECT VERSION()")
            x = DB.Cur.fetchone()
            DB.close()
        except SQLInitializationError as e:
            if "access denied" in str(e).lower():
                self.accessDenied.emit(e)
            else:
                self.noConnection.emit(e)
        else:
            self.connected.emit()
    
    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Escape:
            self.reject()

    def accept(self):
        self.current_server = str(self.ui.tree_configuration.currentItem().text(0))
        super(MySQLOptions, self).accept()

    def exec_(self):
        super(MySQLOptions, self).exec_()
        if self.ui.tree_configuration.currentItem():
            return str(self.ui.tree_configuration.currentItem().text(0))
        else:
            return None
        
    @staticmethod
    def choose(configuration_name, configuration_dict, parent=None):
        dialog = MySQLOptions(configuration_name, configuration_dict, parent=parent)
        return dialog.exec_()

def main():
    app = QtGui.QApplication(sys.argv)
    viewer = MySQLOptions.choose(None, {})
    viewer.exec_()
    
if __name__ == "__main__":
    main()
    