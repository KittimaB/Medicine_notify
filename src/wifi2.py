from Utils import *
from UI_Generate import *
width, height = Scale_Width_Height()

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

class Ui_wifi2(object):
    def setupUi(self, wifi2):
        UI_instance.Set(wifi2)
        show_widget_fullscreen(wifi2)

        wifi2.setObjectName("wifi2")
        wifi2.resize(int(683 * width), int(400 * height))
        wifi2.setStyleSheet("\n"
"background-color: rgb(23, 73, 110);")
        self.centralwidget = QtWidgets.QWidget(wifi2)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(int(0 * width), int(-60 * height), int(683 * width), int(131 * height)))
        self.frame.setStyleSheet("border-radius: 40px;\n"
"background-color: rgb(255, 255, 255);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.frame)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.frame.setGraphicsEffect(shadow)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(int(200 * width), int(70 * height), int(281 * width), int(51 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(14 * height))
        font.setBold(True)
        font.setWeight(int(75 * width))
        self.label.setFont(font)
        self.label.setStyleSheet("border-radius: 16px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(23, 73, 110);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.label)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.label.setGraphicsEffect(shadow)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setLineWidth(int(1 * width))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.img_wifi_label = QtWidgets.QLabel(self.frame)
        self.img_wifi_label.setGeometry(QtCore.QRect(int(283 * width), int(81 * height), int(30 * width), int(26 * height)))
        self.img_wifi_label.setText("")
        self.img_wifi_label.setPixmap(QtGui.QPixmap(":/icons/wifi_tab.png"))
        self.img_wifi_label.setScaledContents(True)
        self.img_wifi_label.setAlignment(QtCore.Qt.AlignCenter)
        self.img_wifi_label.setObjectName("img_wifi_label")
        self.add_back_pushButton = QtWidgets.QPushButton(self.frame)
        self.add_back_pushButton.setGeometry(QtCore.QRect(int(50 * width), int(80 * height), int(81 * width), int(31 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        self.add_back_pushButton.setFont(font)
        self.add_back_pushButton.setStyleSheet("border-radius: 9px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(244, 212, 99);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.add_back_pushButton)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.add_back_pushButton.setGraphicsEffect(shadow)
        self.add_back_pushButton.setObjectName("add_back_pushButton")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(int(200 * width), int(90 * height), int(291 * width), int(261 * height)))
        self.frame_2.setStyleSheet("border-radius: 16px;\n"
"background-color: rgb(236, 236, 236);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.frame_2)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.frame_2.setGraphicsEffect(shadow)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(int(10 * width), int(10 * height), int(271 * width), int(201 * height)))
        self.frame_3.setStyleSheet("border-radius: 9px;\n"
"background-color: rgb(170, 203, 223);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.name_wifi = QtWidgets.QLabel(self.frame_3)
        self.name_wifi.setGeometry(QtCore.QRect(int(30 * width), int(10 * height), int(191 * width), int(21 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        self.name_wifi.setFont(font)
        self.name_wifi.setObjectName("name_wifi")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(int(30 * width), int(40 * height), int(211 * width), int(41 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        font.setBold(False)
        font.setWeight(int(25 * width))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border-radius: 9px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.label_2)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.label_2.setGraphicsEffect(shadow)
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setLineWidth(int(1 * width))
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setGeometry(QtCore.QRect(int(30 * width), int(130 * height), int(211 * width), int(41 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        font.setBold(False)
        font.setWeight(int(25 * width))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border-radius: 9px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.label_3)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.label_3.setGraphicsEffect(shadow)
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setLineWidth(int(1 * width))
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.password = QtWidgets.QLabel(self.frame_3)
        self.password.setGeometry(QtCore.QRect(int(30 * width), int(100 * height), int(211 * width), int(21 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        self.password.setFont(font)
        self.password.setObjectName("password")
        self.next_pushButton = QtWidgets.QPushButton(self.frame_2)
        self.next_pushButton.setGeometry(QtCore.QRect(int(100 * width), int(220 * height), int(91 * width), int(31 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        self.next_pushButton.setFont(font)
        self.next_pushButton.setStyleSheet("border-radius: 9px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 127);\n"
"")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.next_pushButton)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.next_pushButton.setGraphicsEffect(shadow)
        self.next_pushButton.setObjectName("next_pushButton")
        wifi2.setCentralWidget(self.centralwidget)

        self.retranslateUi(wifi2)
        QtCore.QMetaObject.connectSlotsByName(wifi2)

        self.add_back_pushButton.clicked.connect(self.backpage)

         # Set up button press and release styling
        self.add_back_pushButton.pressed.connect(lambda: self.set_button_pressed_style(self.add_back_pushButton))
        self.add_back_pushButton.released.connect(lambda: self.set_button_released_style(self.add_back_pushButton))

        self.next_pushButton.pressed.connect(lambda: self.set_button_pressed_style(self.next_pushButton))
        self.next_pushButton.released.connect(lambda: self.set_button_released_style(self.next_pushButton))


    def set_button_pressed_style(self, button):
        button.setStyleSheet(
            "border-radius: 9px;\n"
            "color: rgb(0, 0, 0);\n"
            "background-color: rgb(200, 200, 200);"  # Change color when pressed
        )

    def set_button_released_style(self, button):
        button.setStyleSheet(
            "border-radius: 9px;\n"
            "color: rgb(255, 255, 255);\n"
            "background-color: rgb(85, 170, 127);"
        )
    def backpage(self):
        from main import Ui_Medicine_App
        backpage_form = UI_Genarate()
        backpage_form.widgetSet(UI_instance.Get(), Ui_Medicine_App)
        
    def retranslateUi(self, wifi2):
        _translate = QtCore.QCoreApplication.translate
        wifi2.setWindowTitle(_translate("wifi2", "Wi-Fi"))
        self.label.setText(_translate("wifi2", "Wi-Fi"))
        self.add_back_pushButton.setText(_translate("wifi2", "ย้อนกลับ"))
        self.name_wifi.setText(_translate("wifi2", "ชื่อ Wi-Fi"))
        self.label_2.setText(_translate("wifi2", "  Wi-Fi"))
        self.label_3.setText(_translate("wifi2", "กรุณากรอกรหัส"))
        self.password.setText(_translate("wifi2", "กรุณากรอกรหัสผ่าน"))
        self.next_pushButton.setText(_translate("wifi2", "ยืนยัน"))

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    wifi2 = QtWidgets.QMainWindow()
    ui = Ui_wifi2()
    ui.setupUi(wifi2)
    wifi2.show()
    sys.exit(app.exec_())
