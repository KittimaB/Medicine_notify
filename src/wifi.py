from Utils import *
from UI_Generate import *
width, height = Scale_Width_Height()

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

class Ui_wifi(object):
    def setupUi(self, wifi):
        UI_instance.Set(wifi)
        show_widget_fullscreen(wifi)

        wifi.setObjectName("wifi")
        wifi.resize(int(683 * width), int(400 * height))
        wifi.setStyleSheet("\n"
"background-color: rgb(23, 73, 110);")
        self.centralwidget = QtWidgets.QWidget(wifi)
        self.centralwidget.setObjectName("centralwidget")
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
        self.listWidget = QtWidgets.QListWidget(self.frame_2)
        self.listWidget.setGeometry(QtCore.QRect(int(20 * width), int(50 * height), int(251 * width), int(181 * height)))
        self.listWidget.setStyleSheet("border-radius: 4px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.listWidget)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.listWidget.setGraphicsEffect(shadow)
        self.listWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.listWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.listWidget.setLineWidth(int(1 * width))
        self.listWidget.setObjectName("listWidget")
        self.name_wifi = QtWidgets.QLabel(self.frame_2)
        self.name_wifi.setGeometry(QtCore.QRect(int(20 * width), int(20 * height), int(191 * width), int(21 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        self.name_wifi.setFont(font)
        self.name_wifi.setObjectName("name_wifi")

        self.reload_pushButton = QtWidgets.QPushButton(self.frame_2)
        self.reload_pushButton.setGeometry(QtCore.QRect(int(230 * width), int(12 * height), int(40 * width), int(37 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(10 * height))
        font.setBold(True)
        font.setWeight(int(75 * width))
        self.reload_pushButton.setFont(font)
        self.reload_pushButton.setStyleSheet("border-radius: 9px;\n"
                                 "color: rgb(0, 0, 0);\n"
                                 "background-color: rgb(236, 236, 236);")
        self.img_reload_label = QtWidgets.QLabel(self.reload_pushButton)
        self.img_reload_label.setGeometry(QtCore.QRect(int(5 * width), int(5 * height), int(28 * width), int(26 * height)))
        self.img_reload_label.setText("")
        self.img_reload_label.setPixmap(QtGui.QPixmap(":/icons/reload.png"))
        self.img_reload_label.setScaledContents(True)
        self.img_reload_label.setAlignment(QtCore.Qt.AlignCenter)
        self.img_reload_label.setObjectName("img_reload_label")
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
        wifi.setCentralWidget(self.centralwidget)

        self.retranslateUi(wifi)
        QtCore.QMetaObject.connectSlotsByName(wifi)

        self.add_back_pushButton.clicked.connect(self.backpage)

         # Set up button press and release styling
        self.add_back_pushButton.pressed.connect(lambda: self.set_button_pressed_style(self.add_back_pushButton))
        self.add_back_pushButton.released.connect(lambda: self.set_button_released_style(self.add_back_pushButton))

        self.reload_pushButton.pressed.connect(lambda: self.set_button_pressed_style(self.reload_pushButton))
        self.reload_pushButton.released.connect(lambda: self.set_button_released_style(self.reload_pushButton))

    def set_button_pressed_style(self, button):
        button.setStyleSheet(
            "border-radius: 9px;\n"
            "color: rgb(0, 0, 0);\n"
            "background-color: rgb(200, 200, 200);"  # Change color when pressed
        )

    def set_button_released_style(self, button):
        button.setStyleSheet(
            "border-radius: 9px;\n"
            "color: rgb(0, 0, 0);\n"
            "background-color: rgb(236, 236, 236);"
        )
    def backpage(self):
        from main import Ui_Medicine_App
        backpage_form = UI_Genarate()
        backpage_form.widgetSet(UI_instance.Get(), Ui_Medicine_App)
        
    def retranslateUi(self, wifi):
        _translate = QtCore.QCoreApplication.translate
        wifi.setWindowTitle(_translate("wifi", "Wi-Fi"))
        self.name_wifi.setText(_translate("wifi", "ชื่อ Wi-Fi"))
        self.label.setText(_translate("wifi", "  Wi-Fi"))
        self.add_back_pushButton.setText(_translate("wifi", "ย้อนกลับ"))
        self.reload_pushButton.setText(_translate("wifi", ""))

        self.img_reload_label.raise_()

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    wifi = QtWidgets.QMainWindow()
    ui = Ui_wifi()
    ui.setupUi(wifi)
    wifi.show()
    sys.exit(app.exec_())
