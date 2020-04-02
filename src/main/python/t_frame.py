from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QFrame, QVBoxLayout, QLabel

import primitive


class TaskFrame(QFrame):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(200, 50)
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Plain)
        self.setStyleSheet(primitive.CSS_FRAME)

    def add_frame(self, name):

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
