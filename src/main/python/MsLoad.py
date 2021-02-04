from fbs_runtime.application_context.PyQt5 import ApplicationContext
from MsUiDesign import MsUiDesign

import sys
import json


import sqlite3
from functools import partial
from datetime import datetime
from PyQt5.QtGui import QIcon, QKeySequence, QLinearGradient, QImage, QPixmap
from PyQt5.QtCore import Qt
from Constant import *
from PyQt5.QtWidgets import (QStatusBar, QTabWidget, QMainWindow,
                             QToolBar, QToolButton, QDockWidget, QAction,
                             QApplication, QStyleFactory, QWidget, QPushButton, QGraphicsView, QListView, QHBoxLayout,
                             QVBoxLayout, QFrame, QLabel, QScrollArea, QAbstractScrollArea, QGroupBox, QDialog,
                             QSpacerItem, QSizePolicy, QTreeView, QMessageBox, QComboBox)

from ScriptExecutor import ScriptExecutor
import CSS
# from CustumTabWidget import CustomTabWidget
from component.BQLineEdit import BQLineEdit
from save_window import SaveWindow




RESOURCE_FILE_PATH = "../resources/"

FRAME_SIZE = 73

NAME = "name"
_ID = "id"
JOB_DATA = "job_data"


class MsLoad(MsUiDesign):
    def __init__(self, parent=None):
        super(MsLoad, self).__init__(parent)
        # self.conn = sqlite3.connect("MikroScript.db")

