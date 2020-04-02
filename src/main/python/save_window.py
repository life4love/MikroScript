from PyQt5.QtWidgets import QDialog, QVBoxLayout, QPushButton, QHBoxLayout, QSpacerItem, QSizePolicy, QLabel
from PyQt5.QtCore import Qt

from component.BQLineEdit import BQLineEdit

class SaveWindow(QDialog):
    def __init__(self):
        # super(SaveWindow, self).__init__()
        super().__init__(None, Qt.WindowTitleHint)

        self.accepted = False
        self.setWindowTitle("Please define Job Name")
        layout = QVBoxLayout()
        self.setMinimumSize(400, 100)

        self.name = BQLineEdit()
        self.name.setPlaceholderText("Job Name")
        # self.name.setMinimumWidth(50)

        button_ok = QPushButton("Ok")
        button_ok.clicked.connect(self.action_accept)

        button_cancel = QPushButton("Cancel")
        button_cancel.clicked.connect(lambda: self.reject())

        # hLayout = QHBoxLayout()
        # hLayout.addItem(QSpacerItem(80, 10, QSizePolicy.Expanding, QSizePolicy.Expanding))
        # layout.addLayout(hLayout)

        hLayout = QHBoxLayout()
        hLayout.addWidget(QLabel("Job Name"))
        hLayout.addWidget(self.name)
        layout.addLayout(hLayout)

        hLayout = QHBoxLayout()
        hLayout.addSpacerItem(QSpacerItem(80, 10, QSizePolicy.Expanding, QSizePolicy.Expanding))
        hLayout.addWidget(button_ok)
        hLayout.addWidget(button_cancel)
        layout.addLayout(hLayout)

        self.setLayout(layout)

        self.exec_()

    def action_accept(self):
        name = self.name.text().lstrip().rstrip()
        if name != "":
            self.accepted = True
            self.accept()

    def get_name(self):
        return self.name.text().lstrip().rstrip()

    def is_accepted(self):
        return self.accepted

