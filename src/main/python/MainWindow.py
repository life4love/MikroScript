import json
import sqlite3
from datetime import datetime
from PyQt5.QtGui import QIcon, QKeySequence, QLinearGradient, QImage, QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QStatusBar, QTabWidget, QMainWindow,
                             QToolBar, QToolButton, QDockWidget, QAction,
                             QApplication, QStyleFactory, QWidget, QPushButton, QGraphicsView, QListView, QHBoxLayout,
                             QVBoxLayout, QFrame, QLabel, QScrollArea, QAbstractScrollArea, QGroupBox, QDialog,
                             QSpacerItem, QSizePolicy, QTreeView)
from fbs_runtime.application_context.PyQt5 import ApplicationContext

from ScriptExecutor import ScriptExecutor
import primitive
# from CustumTabWidget import CustomTabWidget
from component.BQLineEdit import BQLineEdit
from save_window import SaveWindow

RESOURCE_FILE_PATH = "../resources/"

FRAME_SIZE = 73

NAME = "name"
_ID = "id"
JOB_DATA = "job_data"

class MainWindowGui(QMainWindow):
    def __init__(self, parent=None):
        self.appctxt = ApplicationContext()
        super(MainWindowGui, self).__init__(parent)
        self.setWindowTitle("MikroScript")
        self.setStyleSheet(primitive.CSS_BASE)
        self.resize(1128, 768)
        self.setMinimumSize(800,600)
        self.setWindowIcon(QIcon(self.appctxt.get_resource("favicon.png")))

        self.tabCtr = 0
        self.tabview = QTabWidget()
        self.tabview.setStyleSheet(primitive.CSS_TAB)

        self.conn = sqlite3.connect("MikroScript.db")

        self.changeStyle('Windows')
        self.createMenuBar()
        self.tree_dock_widget()
        # self.card_dock_widget()
        self.create_dock_widget_area()
        # self.createBottomArea()

        # mainLayout = QGridLayout()
        # # mainLayout.addLayout(self.TopArea   , 0, 0, 1, 3)
        # # mainLayout.addLayout(self.LeftArea  , 1, 0, 1, 1)
        # mainLayout.addLayout(self.RightArea , 1, 1, 1, 2)
        # # mainLayout.addLayout(self.BottomArea, 2, 0, 1, 3)
        # # mainLayout.addWidget(self.topLeftGroupBox, 1, 0)
        # # mainLayout.addWidget(self.topRightGroupBox, 1, 1)
        # # mainLayout.addWidget(self.bottomLeftTabWidget, 2, 0)
        # # mainLayout.addWidget(self.bottomRightGroupBox, 2, 1)
        # # mainLayout.addWidget(self.progressBar, 3, 0, 1, 2)
        # # mainLayout.setRowStretch(1, 1)
        # mainLayout.setColumnStretch(1, 1)
        # mainLayout.setColumnStretch(2, 1)

        # self.plusButton.setFixedSize(20, 20)  # Small Fixed size
        addButton = QPushButton(QIcon(self.appctxt.get_resource("add-24px.svg")), "")
        addButton.clicked.connect(self.ActionNew)

        self.tabview.setMovable(True)
        self.tabview.setTabsClosable(True)
        self.tabview.tabCloseRequested.connect(self.removeTab)
        self.tabview.setCornerWidget(addButton)
        # self.tabview = CustomTabWidget()
        self.setCentralWidget(self.tabview)
        self.ActionNew()

    def ActionNew(self):

        try:
            self.tabCtr += 1
            tab = QWidget()
            tab.setStyleSheet(primitive.CSS_TAB_BASE)
            # tab.setStyleSheet("{ border-style: solid; background-color:#FBFBFB }")
            center = ScriptExecutor()
            result = center.getExecutorLayout()

            tab.setLayout(result)
            tab.setProperty("OBJECT", center)
            tab.setProperty("TAB_CTR", self.tabCtr)
            tab.setProperty("NAME", "")
            tab.setProperty("_ID", 0)
            # center.getFirstWidget().setFocus(Qt.ActiveWindowFocusReason)
            self.tabview.addTab(tab, "Untitled " + str(self.tabCtr))
            self.tabview.setCurrentWidget(tab)
            center.host.setFocus()
        except Exception:
            raise

    def removeTab(self, index):
        tab = self.tabview.widget(index)
        if tab is not None:
            tab = None
            self.tabview.removeTab(index)

    def createMenuBar(self):

        actNew = QAction(QIcon(self.appctxt.get_resource("outline_insert_drive_file_black_18dp.png")), "&New")
        actNew.triggered.connect(self.ActionNew)
        actNew.setShortcut(QKeySequence.New)

        # actOpen = QAction(QIcon(self.appctxt.get_resource("outline_folder_black_18dp.png")), "&Open")
        # actOpen.triggered.connect(self.ActionOpen)
        # actOpen.setShortcut(QKeySequence.Open)

        actSave = QAction(QIcon(self.appctxt.get_resource("outline_save_black_18dp.png")), "&Save")
        actSave.triggered.connect(self.ActionSave)
        actSave.setShortcut(QKeySequence.Save)

        actQuit = QAction(QIcon(self.appctxt.get_resource("outline_exit_to_app_black_18dp.png")), "&Quit")
        actQuit.triggered.connect(self.ActionQuit)
        actQuit.setShortcut(QKeySequence.Quit)

        self.actExecute = QAction(QIcon(self.appctxt.get_resource("outline_play_circle_outline_black_18dp.png")), "E&xecute")
        self.actExecute.triggered.connect(self.ActionExecute)
        self.actExecute.setShortcut(QKeySequence.Refresh)

        actPause = QAction(QIcon(self.appctxt.get_resource("pause_circle_outline-24px.svg")), "Pause")
        actPause.triggered.connect(self.ActionPause)
        actPause.setShortcut(QKeySequence.Refresh)

        actStop = QAction(QIcon(self.appctxt.get_resource("stop-24px.svg")), "Stop")
        actStop.triggered.connect(self.ActionStop)
        actStop.setShortcut(QKeySequence.Refresh)

        actReset = QAction(QIcon(self.appctxt.get_resource("outline_replay_black_18dp.png")), "&Reset")
        actReset.triggered.connect(self.ActionReset)
        actReset.setShortcut(QKeySequence.Replace)

        # actCut = QAction(QIcon(self.appctxt.get_resource("outline_file_copy_black_18dp.png")), "Cu&t")
        # actCut.setShortcut(QKeySequence.Cut)
        #
        # actCopy = QAction(QIcon(self.appctxt.get_resource("outline_insert_drive_file_black_18dp.png")), "&Copy")
        # actCopy.setShortcut(QKeySequence.Copy)
        #
        # actPaste = QAction(QIcon(self.appctxt.get_resource("outline_insert_drive_file_black_18dp.png")), "&Paste")
        # actPaste.setShortcut(QKeySequence.Paste)

        # actAbout = QAction("&About")


        # menuFile = self.menuBar().addMenu("&File")
        # menuFile.addAction(actNew)
        # # menuFile.addAction(actOpen)
        # menuFile.addAction(actSave)
        # menuFile.addSeparator()
        # menuFile.addAction(actQuit)

        # menuEdit = self.menuBar().addMenu("&Edit")
        # menuEdit.addAction(actCut)
        # menuEdit.addAction(actCopy)
        # menuEdit.addAction(actPaste)

        # menuView = self.menuBar().addMenu("&View")
        # menuRun = self.menuBar().addMenu("&Run")
        # menuRun.addAction(self.actExecute)
        # menuWin = self.menuBar().addMenu("&Window")

        # menuHelp = self.menuBar().addMenu("Help")
        # menuHelp.addAction(actAbout)

        ###################################################################

        toolbtnNew = QToolButton()
        toolbtnNew.setDefaultAction(actNew)
        toolbtnNew.setToolTip("New Job - CTRL + N")

        # toolbtnOpen = QToolButton()
        # toolbtnOpen.setDefaultAction(actOpen)
        # toolbtnOpen.setToolTip("Open File")

        toolbtnSave = QToolButton()
        toolbtnSave.setDefaultAction(actSave)
        toolbtnSave.setToolTip("Save File")

        toolbtnExecute = QToolButton()
        toolbtnExecute.setDefaultAction(self.actExecute)
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

        # styleComboBox = QComboBox()
        # styleComboBox.addItems(QStyleFactory.keys())

        # styleLabel = QLabel("&Style:")
        # styleLabel.setBuddy(styleComboBox)
        # styleComboBox.activated[str].connect(self.changeStyle)

        self.toolBar = QToolBar()
        self.toolBar.addWidget(toolbtnNew)
        # toolBar.addWidget(toolbtnOpen)
        self.toolBar.addWidget(toolbtnSave)
        self.toolBar.addSeparator()
        self.toolBar.addWidget(toolbtnExecute)
        self.toolBar.addWidget(toolbtnPause)
        self.toolBar.addWidget(toolbtnStop)
        self.toolBar.addWidget(toolbtnReset)
        self.toolBar.setMovable(False)
        self.toolBar.addSeparator()
        # toolBar.addWidget(styleLabel)
        # toolBar.addWidget(styleComboBox)
        self.addToolBar(self.toolBar)

    def build_job_frame(self, name):
        job_frame = QFrame()
        # job_frame.   connect(self.load_job)
        job_frame.setMinimumSize(220, 50)

        job_frame.setFrameShape(QFrame.StyledPanel)
        job_frame.setFrameShadow(QFrame.Plain)
        job_frame.setStyleSheet(primitive.CSS_FRAME)


        layout = QVBoxLayout()
        layout.addWidget(QLabel(name))
        # layout.addWidget(QPushButton(QIcon(self.appctxt.get_resource("outline_play_circle_outline_black_18dp.png")), ""))

        img = QImage(self.appctxt.get_resource("outline_play_circle_outline_black_18dp.png"))
        lbl_img = QLabel("")
        lbl_img.setPixmap(QPixmap.fromImage(img))
        # lbl_img.resize(img.width(), img.height())

        job_frame.setLayout(layout)
        # count = self.dock_layout.count()
        self.dock_layout.addWidget(job_frame)
        self.groupBox.setMinimumHeight(self.groupBox.sizeHint().height() + FRAME_SIZE)
        return job_frame

    def tree_dock_widget(self):
        self.dock_widget = QTreeView()


    def card_dock_widget(self):

        self.dock_layout = QVBoxLayout()

        self.groupBox = QGroupBox("")
        self.groupBox.setLayout(self.dock_layout)
        self.groupBox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # groupBox.setMinimumWidth(250)
        # groupBox.setMinimumHeight(500)


        self.dock_widget = QScrollArea()
        self.dock_widget.setWidget(self.groupBox)
        self.dock_widget.setWidgetResizable(True)
        self.dock_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)

    def create_dock_widget_area(self):
        docWidget = QDockWidget("Script Jobs")
        docWidget.setWidget(self.dock_widget)
        # docWidget.setLayout(layout)
        docWidget.DockWidgetFeatures(QDockWidget.DockWidgetVerticalTitleBar)
        docWidget.setFloating(False)
        self.addDockWidget(Qt.LeftDockWidgetArea, docWidget, Qt.Vertical)

    def createBottomArea(self):
        status = QStatusBar()
        self.setStatusBar(status)

    def ActionOpen(self):
        print("Open")

    def ActionSave(self):
        self.create_table()
        current_tab_index = self.tabview.currentIndex()
        if current_tab_index >= 0:
            tab = self.tabview.currentWidget()
            job_data = tab.property("OBJECT").get_job_data()
            if len(job_data) > 0:
                if tab.property("NAME") == "":
                    win = SaveWindow()
                    if win.is_accepted():
                        name = win.get_name()
                        _id = self.get_id()
                        tab.setToolTip(name)
                        tab.setWindowTitle(name)
                        tab.setProperty("NAME", name)
                        tab.setProperty("_ID", _id)
                        string = "insert into jobs (id, name, jobs_data, created_on) values (?, ?, ?, ?)"
                        values = [_id, name, json.dumps(job_data), datetime.now()]
                        self.build_job_frame(name)
                        self.conn.execute(string, values)
                        self.conn.commit()
                else:
                    string = "update jobs set name = ?, jobs_data = ?, updated_on = ? where id = ?"
                    values = [tab.property("NAME"), json.dumps(job_data), datetime.now(), tab.property("_ID")]
                    self.conn.execute(string, values)
                    self.conn.commit()

    def ActionExecute(self):
        current_tab_index = self.tabview.currentIndex()
        if current_tab_index >= 0:
            tab = self.tabview.currentWidget()
            tab.property("OBJECT").Execute()

    def ActionPause(self):
        print("Pause")

    def ActionStop(self):
        print("Stop")

    def ActionReset(self):
        print("Reset")

    def ActionQuit(self):
        print("Quit")

    def changeStyle(self, styleName):
        QApplication.setStyle(QStyleFactory.create(styleName))
        # self.changePalette()

    def create_table(self):

        cursor = self.conn.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='Jobs' ''')

        # if the count is 1, then table exists
        if not cursor.fetchone()[0] == 1:
            string = "create table Jobs (id INT PRIMARY KEY NOT NULL, name text, jobs_data json, " \
                     "created_on CURRENT_TIMESTAMP, " \
                     "updated_on CURRENT_TIMESTAMP )"

            self.conn.execute(string)
            print("Create Statement:", string)

    def get_id(self):
        cursor = self.conn.execute(''' SELECT MAX(id) as id FROM jobs  ''')
        _id = cursor.fetchone()[0] + 1
        cursor.close()
        return _id

    def get_job_list(self,):
        string = "select id, name, jobs_data from Jobs order by id"
        cursor = self.conn.execute(string)
        for rec in cursor:
            frame = self.build_job_frame(rec[1])
            frame.setProperty(_ID, rec[0])
            frame.setProperty(NAME, rec[1])
            frame.setProperty(JOB_DATA, rec[2])

    def load_job(self):
        print("Frame Event Called")

