from PyQt5.QtWidgets import QLineEdit
CSS_QLineEdit = "BQLineEdit { border-style: solid; border-width:1px; height: 25px; border-color: grey; " + \
                "background: white; border-radius: 3px}" + \
                "BQLineEdit:focus {border: 2px solid #FF6B09} "


class BQLineEdit(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setStyleSheet(CSS_QLineEdit)
