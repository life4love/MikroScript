# from PyQt5.QtCore import QRegExp
import time

from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtWidgets import (QLineEdit, QRadioButton, QTabWidget, QWidget, QHBoxLayout,
                             QGridLayout, QLabel, QPlainTextEdit, QCheckBox, QPushButton, QDialog, QFormLayout,
                             QVBoxLayout, QSpacerItem, QSizePolicy, QToolBar, QAction, QToolButton, QGroupBox)
from PyQt5 import QtCore
import math
import datetime
import paramiko
import threading
from netaddr import *
import paramiko.ssh_exception as para
import socket
from fbs_runtime.application_context.PyQt5 import ApplicationContext
from primitive import *

from component.BQLineEdit import BQLineEdit

SSH_PORT = 22
USER = "user"
PASS = "pass"

THREAD = "Session"
DEFAULT_RESULT_TAB = "General"
DEFAULT_SSH = "22"
DEFAULT_TELNET = "23"

class ScriptExecutor:
    def __init__(self):
        self.appctxt = ApplicationContext()
        self.master_layout = QVBoxLayout()

        self.execute = None
        self.multi_credential = {}
        self.credentials = {}
        self.cred_win = None
        if is_env_dev():
            # self.createToolBar()
            self.create_properties()
        else:
            try:
                # self.createToolBar()
                self.create_properties()
            except Exception:
                raise

    def createToolBar(self):

        actSave = QAction(QIcon(self.appctxt.get_resource("outline_save_black_18dp.png")), "&Save")
        actSave.triggered.connect(self.ActionSave)
        actSave.setShortcut(QKeySequence.Save)

        actQuit = QAction(QIcon(self.appctxt.get_resource("outline_exit_to_app_black_18dp.png")), "&Quit")
        actQuit.triggered.connect(self.ActionQuit)
        actQuit.setShortcut(QKeySequence.Quit)

        actExecute = QAction(QIcon(self.appctxt.get_resource("outline_play_circle_outline_black_18dp.png")), "E&xecute")
        actExecute.triggered.connect(self.ActionExecute)
        actExecute.setShortcut(QKeySequence.Refresh)

        actPause = QAction(QIcon(self.appctxt.get_resource("pause_circle_outline-24px.svg")), "Pause")
        actPause.triggered.connect(self.ActionPause)
        actPause.setShortcut(QKeySequence.Refresh)

        actStop = QAction(QIcon(self.appctxt.get_resource("stop-24px.svg")), "Stop")
        actStop.triggered.connect(self.ActionStop)
        actStop.setShortcut(QKeySequence.Refresh)

        actReset = QAction(QIcon(self.appctxt.get_resource("outline_replay_black_18dp.png")), "&Reset")
        actReset.triggered.connect(self.ActionReset)
        actReset.setShortcut(QKeySequence.Replace)

        toolbtnSave = QToolButton()
        toolbtnSave.setDefaultAction(actSave)
        toolbtnSave.setToolTip("Save File")

        toolbtnExecute = QToolButton()
        toolbtnExecute.setDefaultAction(actExecute)
        toolbtnExecute.setToolTip("Execute - F5")

        toolbtnPause = QToolButton()
        toolbtnPause.setDefaultAction(actPause)
        toolbtnPause.setToolTip("Pause")

        toolbtnStop = QToolButton()
        toolbtnStop.setDefaultAction(actStop)
        toolbtnStop.setToolTip("Stop")

        toolbtnReset = QToolButton()
        toolbtnReset.setDefaultAction(actReset)
        toolbtnReset.setToolTip("Reset")

        self.toolBar = QToolBar()
        self.toolBar.addWidget(toolbtnSave)
        self.toolBar.addSeparator()
        self.toolBar.addWidget(toolbtnExecute)
        self.toolBar.addWidget(toolbtnPause)
        self.toolBar.addWidget(toolbtnStop)
        self.toolBar.addWidget(toolbtnReset)
        self.toolBar.setMovable(False)
        self.toolBar.addSeparator()
        hLayout = QHBoxLayout()
        hLayout.addWidget(self.toolBar)
        self.master_layout.addLayout(hLayout)

        # self.addToolBar(self.toolBar)

    def create_properties(self):
        self.host = QLineEdit()
        # self.host.setValidator(self.validateHost)
        # self.host.setInputMask("000.000.000.000-000.000.000.000")

        lblhost = QLabel("&Host* (name, ip-address, ip-range or subnet-mask)")
        lblhost.setBuddy(self.host)
        self.FirstWidget = self.host

        self.portNumber = QLineEdit()
        self.portNumber.setFixedWidth(100)

        self.ssh = QRadioButton("SSH")
        self.telnet = QRadioButton("Telnet")
        self.ssh.toggled.connect(lambda: self.portNumber.setText(DEFAULT_SSH))
        self.telnet.toggled.connect(lambda: self.portNumber.setText(DEFAULT_TELNET))
        self.ssh.setChecked(True)

        self.timeout = QLineEdit()
        self.timeout.setPlaceholderText("Timeout")
        self.timeout.setInputMask("00")
        self.timeout.setText("5")
        self.timeout.setFixedWidth(50)

        self.session = QLineEdit()
        self.session.setPlaceholderText("Session")
        self.session.setInputMask("00")
        self.session.setText("1")
        self.session.setFixedWidth(50)

        self.username = BQLineEdit()
        self.username.setPlaceholderText("Username")

        lblUser = QLabel("&User name*")
        lblUser.setBuddy(self.username)

        self.password = QLineEdit()
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setFixedWidth(250)

        addCredential = QPushButton("+")
        addCredential.clicked.connect(self.multi_credential_dialogue)
        addCredential.setFixedWidth(25)

        self.log = QCheckBox("&Log Execution")
        self.log.setChecked(True)

        self.skipError = QCheckBox("S&kip on Error")
        self.skipError.setChecked(True)

        self.script = QPlainTextEdit()
        self.script.setStyleSheet("{ height: 100px}")

        lblScript = QLabel("&Script*")
        lblScript.setBuddy(self.script)

        self.add_result_tabs()

        hLayout = QHBoxLayout()
        hLayout.addWidget(lblhost)
        hLayout.addWidget(QLabel("Connection type"))
        hLayout.addWidget(QLabel("Port"))



        host_gBox = QGroupBox("")
        vLayout = QVBoxLayout()
        hLayout = QHBoxLayout()
        hLayout.addWidget(self.host)
        hLayout.addWidget(QLabel("Session"))
        hLayout.addWidget(self.session)

        vLayout.addWidget(lblhost)
        vLayout.addLayout(hLayout)

        hLayout = QHBoxLayout()
        hLayout.addWidget(QLabel("Connection type: "))
        hLayout.addWidget(self.ssh)
        hLayout.addWidget(self.telnet)
        hLayout.addWidget(self.portNumber)
        hLayout.addWidget(QLabel("Timeout"))
        hLayout.addWidget(self.timeout)
        vLayout.addLayout(hLayout)
        host_gBox.setLayout(vLayout)
        # self.master_layout.addLayout(hLayout)





        hLayout = QHBoxLayout()
        hLayout.addWidget(lblUser)
        hLayout.addWidget(QLabel("Password"))
        # self.master_layout.addLayout(hLayout)

        cred_gBox = QGroupBox("")
        vLayout = QVBoxLayout()
        hLayout = QHBoxLayout()
        vLayout.addWidget(lblUser)
        vLayout.addWidget(self.username)
        hLayout.addWidget(self.password)
        hLayout.addWidget(addCredential)
        vLayout.addLayout(hLayout)
        cred_gBox.setLayout(vLayout)
        hLayout = QHBoxLayout()
        hLayout.addWidget(cred_gBox)
        hLayout.addWidget(host_gBox)
        self.master_layout.addLayout(hLayout)

        hLayout = QHBoxLayout()
        hLayout.addWidget(lblScript)
        hLayout.addWidget(self.log)
        hLayout.addWidget(self.skipError)
        self.master_layout.addLayout(hLayout)

        hLayout = QHBoxLayout()
        hLayout.addWidget(self.script)
        self.master_layout.addLayout(hLayout)

        hLayout = QHBoxLayout()
        hLayout.addWidget(self.tabview)
        self.master_layout.addLayout(hLayout)


        # self.gridLayout.addWidget(lblScript, 5, 0)
        # self.gridLayout.addWidget(self.log, 5, 2)
        # self.gridLayout.addWidget(self.skipError, 5, 3)
        #
        # self.gridLayout.addWidget(QLabel("Timeout"), 4, 4)
        # self.gridLayout.addWidget(self.timeout, 5, 4)
        #
        # self.gridLayout.addWidget(QLabel("Session"), 4, 5)
        # self.gridLayout.addWidget(self.session, 5, 5)
        #
        # self.gridLayout.addWidget(self.script, 6, 0, 1, 7)
        # self.gridLayout.addWidget(self.tabview, 7, 0, 1, 7)


        # self.gridLayout = QGridLayout()
        # # self.gridLayout.setColumnMinimumWidth(4, 4)
        # self.gridLayout.addWidget(lblhost, 0, 0)
        # self.gridLayout.addWidget(self.host, 1, 0)
        #
        # self.gridLayout.addWidget(QLabel("Connection type"), 0, 2)
        # self.gridLayout.addWidget(self.ssh, 1, 2)
        # self.gridLayout.addWidget(self.telnet, 1, 3)
        #
        # self.gridLayout.addWidget(QLabel("Port number"), 0, 4)
        # self.gridLayout.addWidget(self.portNumber, 1, 4)
        #
        # self.gridLayout.addWidget(lblUser, 2, 0)
        # self.gridLayout.addWidget(self.username, 3, 0)
        #
        # self.gridLayout.addWidget(QLabel("Password"), 2, 2)
        # self.gridLayout.addWidget(self.password, 3, 2)
        # self.gridLayout.addWidget(addCredential, 3, 3)
        #
        # self.gridLayout.addWidget(lblScript, 5, 0)
        # self.gridLayout.addWidget(self.log, 5, 2)
        # self.gridLayout.addWidget(self.skipError, 5, 3)
        #
        # self.gridLayout.addWidget(QLabel("Timeout"), 4, 4)
        # self.gridLayout.addWidget(self.timeout, 5, 4)
        #
        # self.gridLayout.addWidget(QLabel("Session"), 4, 5)
        # self.gridLayout.addWidget(self.session, 5, 5)
        #
        # self.gridLayout.addWidget(self.script, 6, 0, 1, 7)
        # self.gridLayout.addWidget(self.tabview, 7, 0, 1, 7)
        #
        # self.gridLayout.setColumnStretch(0, 1)


    def multi_credential_dialogue(self):
        if self.cred_win == None:
            self.credential_count = 1
            self.cred_win = QDialog(None, QtCore.Qt.WindowTitleHint)
            self.cred_win.setWindowTitle("Credentials")
            self.layout = QVBoxLayout()

            addMore = QPushButton("+")
            addMore.clicked.connect(self.addMoreCredentialObj)
            addMore.setFixedWidth(25)

            button_ok = QPushButton("Ok")
            button_ok.clicked.connect(self.accept_window)

            button_cancel = QPushButton("Cancel")
            button_cancel.clicked.connect(self.close_window)

            hLayout = QHBoxLayout()
            hLayout.addItem(QSpacerItem(80, 10, QSizePolicy.Expanding, QSizePolicy.Expanding))
            self.layout.addLayout(hLayout)

            hLayout = QHBoxLayout()

            hLayout.addWidget(addMore)
            hLayout.addSpacerItem(QSpacerItem(80, 10, QSizePolicy.Expanding, QSizePolicy.Expanding))
            hLayout.addWidget(button_ok)
            hLayout.addWidget(button_cancel)
            self.layout.addLayout(hLayout)

            self.cred_win.setLayout(self.layout)

            self.add_cred_line()

        user = self.username.text().rstrip().lstrip()
        if user != "" or self.password.text() != "":
            self.credentials["1"] = {USER: user, PASS: self.password.text()}

        self.load_credential()
        self.cred_win.exec_()

    def accept_window(self):
        for i in self.multi_credential:
            cred = self.multi_credential[str(i)]
            user = cred[USER]
            pwd  = cred[PASS]
            if user.text() != "" or pwd.text() != "":
                self.credentials[str(i)] = {USER: user.text().lstrip().rstrip(), PASS: pwd.text()}
            elif str(i) in self.credentials:
                del self.credentials[str(i)]
        self.cred_win.accept()

    def load_credential(self):
        for i in self.multi_credential:
            cred = self.multi_credential[str(i)]
            cred[USER].setText(self.credentials[str(i)][USER] if str(i) in self.credentials else "")
            cred[PASS].setText(self.credentials[str(i)][PASS] if str(i) in self.credentials else "")

    def close_window(self):
        self.cred_win.reject()

    def add_cred_line(self):
        self.credential_count += 1
        username = BQLineEdit()
        username.setPlaceholderText("Username")

        password = QLineEdit()
        password.setPlaceholderText("Password")
        password.setEchoMode(QLineEdit.Password)

        hLayout = QHBoxLayout()
        hLayout.addWidget(QLabel("Credential " + ("  " if self.credential_count < 10 else "") + str(self.credential_count) + "      "))
        hLayout.addWidget(username)
        hLayout.addWidget(password)
        hLayout.setProperty("COUNT", self.credential_count)
        self.layout.insertLayout(0 + self.credential_count - 2, hLayout)
        username.setFocus()

        self.multi_credential[str(self.credential_count)] = {USER: username, PASS: password}

    def addMoreCredentialObj(self):
        credObj = self.multi_credential[str(self.credential_count)]
        if credObj[USER].text().rstrip().lstrip() != "" or credObj[PASS].text().rstrip().lstrip() != "":
            self.add_cred_line()
        else:
            credObj[USER].setFocus()

    def getExecutorLayout(self):
        return self.master_layout

    def host_reg_ex(self):
        print("regEx")

    #         regex = "^(?P<all_ip>
    #   (?:[01]?[0-9]{1,2}|2[0-4][0-9]|25[0-5])\.
    #   (?:[01]?[0-9]{1,2}|2[0-4][0-9]|25[0-5])\.
    #   (?:[01]?[0-9]{1,2}|2[0-4][0-9]|25[0-5])\.
    #   (?:[01]?[0-9]{1,2}|2[0-4][0-9]|25[0-5])
    # )$"
    #         ipRange = "(?:[0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])"
    #         regexIp = QRegExp("^" + ipRange
    #                 + "\\." + ipRange
    #                 + "\\." + ipRange
    #                 + "\\." + ipRange + "$")
    #         return self.gridLayout

    def getFirstWidget(self):
        return self.FirstWidget

    def validate_required_fields(self):
        validated = True
        host = self.host.text().lstrip().rstrip()
        user = self.username.text().lstrip().rstrip()
        script = self.script.toPlainText().lstrip().rstrip()
        port = self.portNumber.text().lstrip().rstrip()
        if port == "":
            if self.telnet.isChecked():
                self.portNumber.setText(DEFAULT_TELNET)
            else:
                self.portNumber.setText(DEFAULT_SSH)

        if host == "" or user == "" or script == "":
            validated = False
            self.result.appendPlainText("Mandatory fields are empty. Please specify mandatory fields that are "
                                        "Host, Username or Script.")
            # self.result.appendPlainText("Execution didn't got started.")

        return validated

    def Execute(self):

        if self.validate_required_fields():
            if self.execute is not None and len(self.execute.result) > 0:
                self.execute.destroy()
                self.execute = None

            user = self.username.text().rstrip().lstrip()
            if user != "" or self.password.text() != "":
                self.credentials["1"] = {USER: user, PASS: self.password.text()}
            self.execute = ExecuteScript(self)
            self.result.appendPlainText("Starting Execution")

    def add_result_tabs(self):
        self.tabview = QTabWidget()
        self.result = QPlainTextEdit()
        tab = QWidget()
        tabHBox = QHBoxLayout()
        tabHBox.addWidget(self.result)
        tabHBox.setContentsMargins(1, 1, 1, 1)
        tab.setLayout(tabHBox)
        self.tabview.addTab(tab, "General")

    def get_job_data(self):
        if self.validate_required_fields():
            job_data = {
                "host": self.host.text().lstrip().rstrip(),
                "connection_type": "TELNET" if self.telnet.isChecked() else "SSH",
                "port_number": self.portNumber.text().lstrip().rstrip(),
                "timeout": self.timeout.text(),
                "session": self.session.text(),
                "skip_on_error": self.skipError.isChecked(),
                "log_file": self.log.isChecked(),
                "credential": self.credentials

            }
            return job_data
        return {}

    def ActionPause(self):
        print("Pause")

    def ActionStop(self):
        print("Stop")

    def ActionReset(self):
        print("Reset")

    def ActionQuit(self):
        print("Quit")

    def ActionSave(self):
        print("Save")

    def ActionExecute(self):
        self.Execute()
        # current_tab_index = self.tabview.currentIndex()
        # if current_tab_index >= 0:
        #     tab = self.tabview.currentWidget()
        #     tab.property("OBJECT").Execute()




class ExecuteScript:
    def __init__(self, parent):
        self.parent = parent
        self.result = {}
        self.uneven_ipaddress = False
        self.create_session_thread_dict()

    def add_result_tab(self, session, title):

        result = QPlainTextEdit()
        self.result[title] = result
        tab = QWidget()
        tab.setProperty("SESSION", session)
        tab.setProperty("RESULT_OBJ", result)
        tabHBox = QHBoxLayout()
        tabHBox.addWidget(result)
        tabHBox.setContentsMargins(1, 1, 1, 1)
        tab.setLayout(tabHBox)
        self.parent.tabview.addTab(tab, title)

    def create_session_thread_dict(self):

        session = self.parent.session.text()
        if session.rstrip().lstrip() == "":
            session = 1
        else:
            session = int(session)
            if session == 0:
                session = 1

        h_list = list(dict.fromkeys(self.build_ip_list()))
        length = len(h_list)
        if length > 0:

            session_ip_count = math.ceil(length / session)

            current_ip_count = 0
            thread_count = 0
            ip_list = []
            session_ip_list = {}
            for host in h_list:
                current_ip_count += 1
                if current_ip_count <= session_ip_count:
                    ip_list.append(str(host))
                else:
                    thread_count += 1
                    current_ip_count = 1
                    session_ip_list[THREAD + str(thread_count)] = ip_list
                    session_ip_list["total_thread"] = thread_count
                    ip_list = [str(host)]
            thread_count += 1
            session_ip_list[THREAD + str(thread_count)] = ip_list
            session_ip_list["total_thread"] = thread_count
            self.execute_thread(session_ip_list)

    def execute_thread(self, session_ip_list):
        for i in range(session_ip_list["total_thread"]):
            thread_name = THREAD + str(i + 1)
            self.add_result_tab(i, thread_name)
            th = threading.Thread(target=self.execute_ip_queues,
                                  args=(session_ip_list[thread_name], thread_name))
            th.start()
            # print("Joining the Thread")
            # th.join()

    def get_ports(self):
        port_list = []
        port_numbers = self.parent.portNumber.text().lstrip().rstrip()
        if not port_numbers == "":
            port_list = port_numbers.replace(" ", "")
            port_list = port_list.split(",")

        if len(port_list) == 0:
            port_list.append(DEFAULT_TELNET if self.parent.telnet.isChecked() else DEFAULT_SSH)
        return port_list

    def execute_ip_queues(self, ip_queue, thread_name):
        started_time = datetime.datetime.now()
        if not self.uneven_ipaddress and len(ip_queue) > 0:
            host_addresses = ip_queue[0] + "-" + ip_queue[len(ip_queue) - 1]
        else:
            host_addresses = str(ip_queue)
            host_addresses = host_addresses.replace("'", "")
            host_addresses = host_addresses.replace("[", "")
            host_addresses = host_addresses.replace("]", "")

        self.append_result("IP slot assigned for this session execution are: " + host_addresses, thread_name)
        self.append_result("Session execution started at " + str(started_time) + " second.", thread_name)

        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.load_system_host_keys()
        port_list = self.get_ports()

        for host in ip_queue:
            self.append_result(" ", thread_name)
            self.append_result("Execution started on host: " + host, thread_name)
            for port in port_list:
                if self.execute_host_with_credential(thread_name, client, host, int(port)):
                    break

        client.close()
        end_time = datetime.datetime.now()

        self.append_result("Session execution finished at " + str(end_time) + " second", thread_name)
        # self.append_result("Total time consumed on this session is " + str(round(int(str(end_time - started_time)), 2)) + " seconds",
        #                    thread_name)

    def execute_host_with_credential(self, thread_name, client, host, port):
        for i in self.parent.credentials:
            if self.connect_and_execute_command(thread_name, client, host, port, self.parent.credentials[str(i)], i):
                return True
        return False

    def connect_and_execute_command(self, thread_name, client, ip_address, port, cred, cred_counter):
        # command = "ip address print " \
        #           "\n ip route print" \
        #           '\n  password old-password="" new-password="123456" confirm-new-password="123456"'
        # Tested with this command

        command = self.parent.script.toPlainText()
        cmd_list = command.split("\n")
        try:
            self.append_result(thread_name + " : Connecting host : " + ip_address + " on port: " + str(port) +
                               " with credential " + cred_counter, thread_name)
            username = cred[USER]
            password = cred[PASS]
            timeout = int(self.parent.timeout.text())

            client.connect(hostname=ip_address, port=port, username=username, password=password, timeout=timeout)
            cmd_count = 0
            total_command = len(cmd_list)
            self.success_connection = True
            for cmd in cmd_list:
                cmd_count += 1
                self.append_result(thread_name + " : Executing " + str(cmd_count) + "/" + str(total_command) +
                                   " command on host : " + ip_address + " : " + cmd, thread_name)

                self.append_result(self.execute_command(client, cmd), thread_name)
            return True
        except para.AuthenticationException as auth:
            self.append_result("Wrong username or password to connect " + ip_address + " : " + str(auth), thread_name)
        except para.SSHException as sshEx:
            self.append_result("Unable to establish SSH connection on host " + ip_address + " : " + str(sshEx),
                               thread_name)
        except socket.timeout as timeout:
            self.append_result("Unable to connect host " + ip_address + " : " + str(timeout), thread_name)
        except Exception as e:
            self.append_result("Other Exception occurred on " + ip_address + " : " + str(e), thread_name)
            print("Other Exception occurred on " + ip_address + " : " + str(e), thread_name)
        return False

    def execute_command(self, client, command):
        result = ""
        ssh_stdin, ssh_stdout, ssh_stderr = client.exec_command(command)
        for line in ssh_stdout.readlines():
            result += line
        return result

    def validateHost(self):
        print("Host Validation")

    def build_ip_list(self):
        hostname = self.parent.host.text().lstrip().rstrip()
        # hostname = r"192.168.0.3, 192.168.0.4, 192.168.0.128/29, 192.168.0.10-192.168.0.20, 192.168.0.3"
        # Tested with this hostname
        h_list = []
        host_list = hostname.split(",")
        for host in host_list:
            host = host.lstrip()
            host = host.rstrip()
            if "/" in host:
                lst = self.ip_subnet(host)
                h_list.extend(lst)
            elif "-" in host:
                lst = self.ip_range(host)
                h_list.extend(lst)
            else:
                self.uneven_ipaddress = True
                h_list.append(IPAddress(host))
        return h_list

    def ip_range(self, hostname):
        ip_list = []
        try:
            hosts = hostname.split("-")
            ip_list = list(iter_iprange(hosts[0], hosts[1]))
        except Exception:
            self.append_result("Exception occurred in hostname: " + hostname)

        return ip_list

    def ip_subnet(self, subnet):
        sub = list(IPNetwork(subnet))
        if len(sub) > 0:
            sub.pop(-1)  # removing broadcast address
            sub.pop(0)  # removing network address
        return sub

    def append_result(self, message, title=DEFAULT_RESULT_TAB):
        self.result[title].appendPlainText(message)

    def destroy(self):
        tab_tiles = list(dict.keys(self.result))
        if len(tab_tiles) > 0:
            for title in tab_tiles:
                index = self.get_tab_index_by_title(title)
                if index > 0:
                    tab = self.parent.tabview.widget(index)
                    if tab is not None:
                        tab = None
                        self.parent.tabview.removeTab(index)
        self.result = {}

    def get_tab_index_by_title(self, title):
        count = self.parent.tabview.count()
        for index in range(count):
            if title == self.parent.tabview.tabText(index):
                return index
        return -1

    def remove_tab(self, index):
        tab = self.parent.tabview.widget(index)
        if tab is not None:
            tab = None
            self.parent.tabview.removeTab(index)
