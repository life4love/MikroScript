from PyQt5.QtWidgets import QLineEdit
from Constant import *

CSS_QLineEdit = "BQLineEdit { border-style: solid; border-width:1px; height: 25px; border-color: grey; " + \
                "background: " + COLOR_BG + " ; border-radius: 3px}" + \
                "BQLineEdit:focus {background: white; border: 1px solid grey} "


class BQLineEdit(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setStyleSheet(CSS_QLineEdit)
