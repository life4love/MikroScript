from PyQt5.QtWidgets import QDialog, QVBoxLayout, QPushButton, QHBoxLayout, QSpacerItem, QSizePolicy, QLabel, QComboBox
from PyQt5.QtCore import Qt

from component.BQLineEdit import BQLineEdit
import CSS

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

        labelJobName = QLabel("Job Name")

        # Updated by Pinkesh Shah on 11-May-20 to set minimum size
        # Start Region
        labelJobName.setFixedSize(70, 10)
        # End Region

        hLayout.addWidget(labelJobName)
        hLayout.addWidget(self.name)
        layout.addLayout(hLayout)

        # Updated by Pinkesh Shah on 11-May-20 to add device selection for the user
        # Start Region
        hLayout = QHBoxLayout()

        labelDevice = QLabel("Select Device")
        labelDevice.setFixedSize(70, 10)

        self.dropDownDevices = QComboBox()
        self.dropDownDevices.addItems(["Mikrotik", "Others"])
        self.dropDownDevices.setMinimumWidth(50)
        self.dropDownDevices.setStyleSheet(CSS.CSS_COMBOBOX)

        hLayout.addWidget(labelDevice)
        hLayout.addWidget(self.dropDownDevices)
        layout.addLayout(hLayout)
        # End Region

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

    # Updated by Pinkesh Shah on 11-May-20 to return device selection
    # Start Region
    def get_device_name(self):
        return self.dropDownDevices.currentText()
    # End Region
