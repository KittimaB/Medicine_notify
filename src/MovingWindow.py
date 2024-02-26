
from Utils import *
from UI_Generate import *
width, height = Scale_Width_Height()

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt, QTimer

class MovingWindow(QMainWindow):
    def __init__(self):
        super(MovingWindow, self).__init__()

        self.initUI()

    def initUI(self):
        UI_instance.Set(MovingWindow)
        # self.showFullScreen()
        # กำหนดขนาดหน้าต่าง
        self.resize(int(683 * width), int(400 * height))
        self.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.setWindowTitle('Moving Window')

        # สร้าง QLabel เพื่อแสดงข้อความ
        font = QtGui.QFont()
        font.setPointSize(int(30 * height))
        font.setBold(True)
        font.setWeight(int(75 * width))
        self.label = QLabel('Medicine Box', self)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setGeometry(QtCore.QRect(int(190 * width), int(20 * height), int(281 * width), int(51 * height)))
        self.label.setAlignment(Qt.AlignCenter)

        # กำหนดตัวแปรที่ใช้เก็บข้อมูลตำแหน่งปัจจุบันของหน้าต่าง
        self.current_pos_x = 0
        self.current_pos_y = 0
        self.move_direction_x = 1  # 1 หรือ -1 เพื่อกำหนดทิศทางการเคลื่อนที่
        self.move_direction_y = 1  # 1 หรือ -1 เพื่อกำหนดทิศทางการเคลื่อนที่

        # ใช้ QTimer เพื่อเรียกฟังก์ชันที่เคลื่อนที่หน้าต่างทุกๆ 100 มิลลิวินาที
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.move_window)
        self.timer.start(100)

    def move_window(self):
        # เคลื่อนที่หน้าต่างซ้าย-ขวา
        self.current_pos_x += self.move_direction_x * 5
        if self.current_pos_x >= self.width() or self.current_pos_x <= 0:
            self.move_direction_x *= -1

        # เคลื่อนที่หน้าต่างขึ้น-ลง
        self.current_pos_y += self.move_direction_y * 5
        if self.current_pos_y >= self.height() or self.current_pos_y <= 0:
            self.move_direction_y *= -1

        self.label.move(self.current_pos_x, self.current_pos_y)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MovingWindow()
    window.show()
    sys.exit(app.exec_())

