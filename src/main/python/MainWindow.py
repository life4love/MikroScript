from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QStatusBar, QListView, QLabel, QTabWidget, QMainWindow,
                             QToolBar, QToolButton, QDockWidget, QAction,
                             QComboBox, QApplication, QStyleFactory, QWidget)
from ScriptExecutor import ScriptExecutor
from fbs_runtime.application_context.PyQt5 import ApplicationContext

RESOURCE_FILE_PATH = "../resources/"

class MainWindowGui(QMainWindow):
    def __init__(self, parent=None):
        self.appctxt = ApplicationContext()
        super(MainWindowGui, self).__init__(parent)
        self.setWindowTitle("MikroScript V2.0")
        self.resize(1128, 768)
        self.setMinimumSize(800,600)
        self.setWindowIcon(QIcon(self.appctxt.get_resource("favicon.png")))
        self.tabCtr = 0

        self.createMenuBar()
        self.createLeftArea()
        self.createBottomArea()

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

        self.tabview = QTabWidget()
        self.tabview.setMovable(True)
        self.tabview.setTabsClosable(True)
        self.tabview.tabCloseRequested.connect(self.removeTab)
        # self.tabview.setShortcut(QKeySequence.close)
        self.setCentralWidget(self.tabview)
        self.ActionNew()

    def ActionNew(self):

        try:
            self.tabCtr += 1
            tab = QWidget()
            center = ScriptExecutor()
            result = center.getExecutorLayout()
            tab.setLayout(result)
            tab.setProperty("OBJECT", center)
            tab.setProperty("TAB_CTR", self.tabCtr)
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

        actOpen = QAction(QIcon(self.appctxt.get_resource("outline_folder_black_18dp.png")), "&Open")
        actOpen.triggered.connect(self.ActionOpen)
        actOpen.setShortcut(QKeySequence.Open)

        actSave = QAction(QIcon(self.appctxt.get_resource("outline_save_black_18dp.png")), "&Save")
        actSave.triggered.connect(self.ActionSave)
        actSave.setShortcut(QKeySequence.Save)

        actQuit = QAction(QIcon(self.appctxt.get_resource("outline_exit_to_app_black_18dp.png")), "&Quit")
        actQuit.triggered.connect(self.ActionQuit)
        actQuit.setShortcut(QKeySequence.Quit)

        actExecute = QAction(QIcon(self.appctxt.get_resource("outline_play_circle_outline_black_18dp.png")), "E&xecute")
        actExecute.triggered.connect(self.ActionExecute)
        actExecute.setShortcut(QKeySequence.Refresh)

        actReset = QAction(QIcon(self.appctxt.get_resource("outline_replay_black_18dp.png")), "&Reset")
        actReset.triggered.connect(self.ActionReset)
        actReset.setShortcut(QKeySequence.Replace)

        actCut = QAction(QIcon(self.appctxt.get_resource("outline_file_copy_black_18dp.png")), "Cu&t")
        actCut.setShortcut(QKeySequence.Cut)

        actCopy = QAction(QIcon(self.appctxt.get_resource("outline_insert_drive_file_black_18dp.png")), "&Copy")
        actCopy.setShortcut(QKeySequence.Copy)

        actPaste = QAction(QIcon(self.appctxt.get_resource("outline_insert_drive_file_black_18dp.png")), "&Paste")
        actPaste.setShortcut(QKeySequence.Paste)

        actAbout = QAction("&About")

        menuFile = self.menuBar().addMenu("&File")
        menuFile.addAction(actNew)
        menuFile.addAction(actOpen)
        menuFile.addAction(actSave)
        menuFile.addSeparator()
        menuFile.addAction(actQuit)

        menuEdit = self.menuBar().addMenu("&Edit")
        menuEdit.addAction(actCut)
        menuEdit.addAction(actCopy)
        menuEdit.addAction(actPaste)

        menuView = self.menuBar().addMenu("&View")
        menuRun = self.menuBar().addMenu("&Run")
        menuRun.addAction(actExecute)
        menuWin = self.menuBar().addMenu("&Window")

        menuHelp = self.menuBar().addMenu("Help")
        menuHelp.addAction(actAbout)

        ###################################################################

        toolbtnNew = QToolButton()
        toolbtnNew.setDefaultAction(actNew)
        toolbtnNew.setToolTip("New File")

        toolbtnOpen = QToolButton()
        toolbtnOpen.setDefaultAction(actOpen)
        toolbtnOpen.setToolTip("Open File")

        toolbtnSave = QToolButton()
        toolbtnSave.setDefaultAction(actSave)
        toolbtnSave.setToolTip("Save File")

        toolbtnExecute = QToolButton()
        toolbtnExecute.setDefaultAction(actExecute)
        toolbtnExecute.setToolTip("Execute - F5")

        toolbtnReset = QToolButton()
        toolbtnReset.setDefaultAction(actReset)
        toolbtnReset.setToolTip("Reset")

        styleComboBox = QComboBox()
        styleComboBox.addItems(QStyleFactory.keys())

        styleLabel = QLabel("&Style:")
        styleLabel.setBuddy(styleComboBox)
        styleComboBox.activated[str].connect(self.changeStyle)

        toolBar = QToolBar()
        toolBar.addWidget(toolbtnNew)
        toolBar.addWidget(toolbtnOpen)
        toolBar.addWidget(toolbtnSave)
        toolBar.addSeparator()
        toolBar.addWidget(toolbtnExecute)
        toolBar.addWidget(toolbtnReset)
        toolBar.setMovable(False)
        toolBar.addSeparator()
        toolBar.addWidget(styleLabel)
        toolBar.addWidget(styleComboBox)

        self.addToolBar(toolBar)

        self.changeStyle('Fusion')

    def createLeftArea(self):
        listView = QListView()
        # tabBar = QTabBar()
        # tabBar.addTab("Execution")
        # tabBar.addTab("Reporting")
        # LeftArea = QVBoxLayout()
        # LeftArea.(tabBar)
        docWidget = QDockWidget("Script Jobs")
        docWidget.setWidget(listView)
        docWidget.DockWidgetFeatures(QDockWidget.DockWidgetVerticalTitleBar)
        docWidget.setFloating(False)
        self.addDockWidget(Qt.LeftDockWidgetArea, docWidget, Qt.Vertical)

    def createBottomArea(self):
        status = QStatusBar()
        self.setStatusBar(status)

    def ActionOpen(self):
        print("Open")

    def ActionSave(self):
        print("Save")

    def ActionExecute(self):
        current_tab_index = self.tabview.currentIndex()
        if current_tab_index >= 0:
            tab = self.tabview.currentWidget()
            tab.property("OBJECT").Execute()

    def ActionReset(self):
        print("Reset")

    def ActionQuit(self):
        print("Quit")

    def changeStyle(self, styleName):
        QApplication.setStyle(QStyleFactory.create(styleName))
        # self.changePalette()
