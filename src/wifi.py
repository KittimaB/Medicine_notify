from Utils import Scale_Width_Height, show_widget_fullscreen

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsDropShadowEffect


class Ui_wifi(object):
    def setupUi(self, wifi):
        wifi.setObjectName("wifi")
        wifi.resize(683, 400)
        wifi.setStyleSheet("\n"
"background-color: rgb(23, 73, 110);")
        self.centralwidget = QtWidgets.QWidget(wifi)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(200, 90, 291, 261))
        self.frame_2.setStyleSheet("border-radius: 16px;\n"
"background-color: rgb(236, 236, 236);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.frame_2)
        shadow.setBlurRadius(8)
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(0,2)
        self.frame_2.setGraphicsEffect(shadow)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.listWidget = QtWidgets.QListWidget(self.frame_2)
        self.listWidget.setGeometry(QtCore.QRect(20, 50, 251, 181))
        self.listWidget.setStyleSheet("border-radius: 4px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.listWidget)
        shadow.setBlurRadius(8)
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(0,2)
        self.listWidget.setGraphicsEffect(shadow)
        self.listWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.listWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.listWidget.setLineWidth(1)
        self.listWidget.setObjectName("listWidget")
        self.name_wifi = QtWidgets.QLabel(self.frame_2)
        self.name_wifi.setGeometry(QtCore.QRect(20, 20, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.name_wifi.setFont(font)
        self.name_wifi.setObjectName("name_wifi")

        self.reload_pushButton = QtWidgets.QPushButton(self.frame_2)
        self.reload_pushButton.setGeometry(QtCore.QRect(230, 12, 40, 37))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.reload_pushButton.setFont(font)
        self.reload_pushButton.setStyleSheet("border-radius: 9px;\n"
                                 "color: rgb(0, 0, 0);\n"
                                 "background-color: rgb(236, 236, 236);")
        self.img_label = QtWidgets.QLabel(self.reload_pushButton)
        self.img_label.setGeometry(QtCore.QRect(5, 5, 30, 26))
        self.img_label.setText("")
        self.img_label.setPixmap(QtGui.QPixmap(":/icons/reload.png"))
        self.img_label.setScaledContents(True)
        self.img_label.setAlignment(QtCore.Qt.AlignCenter)
        self.img_label.setObjectName("img_label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, -60, 683, 131))
        self.frame.setStyleSheet("border-radius: 40px;\n"
"background-color: rgb(255, 255, 255);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.frame)
        shadow.setBlurRadius(8)
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(0,2)
        self.frame.setGraphicsEffect(shadow)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(200, 70, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("border-radius: 16px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(23, 73, 110);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.label)
        shadow.setBlurRadius(8)
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(0,2)
        self.label.setGraphicsEffect(shadow)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setLineWidth(1)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.img_label = QtWidgets.QLabel(self.frame)
        self.img_label.setGeometry(QtCore.QRect(283, 81, 30, 26))
        self.img_label.setText("")
        self.img_label.setPixmap(QtGui.QPixmap(":/icons/wifi_tab.png"))
        self.img_label.setScaledContents(True)
        self.img_label.setAlignment(QtCore.Qt.AlignCenter)
        self.img_label.setObjectName("img_label")
        self.add_back_pushButton = QtWidgets.QPushButton(self.frame)
        self.add_back_pushButton.setGeometry(QtCore.QRect(50, 80, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add_back_pushButton.setFont(font)
        self.add_back_pushButton.setStyleSheet("border-radius: 9px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(244, 212, 99);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.add_back_pushButton)
        shadow.setBlurRadius(8)
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(0,2)
        self.add_back_pushButton.setGraphicsEffect(shadow)
        self.add_back_pushButton.setObjectName("add_back_pushButton")
        wifi.setCentralWidget(self.centralwidget)

        self.retranslateUi(wifi)
        QtCore.QMetaObject.connectSlotsByName(wifi)

        def close_window():
            wifi.close()

        self.add_back_pushButton.clicked.connect(close_window)

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

    def retranslateUi(self, wifi):
        _translate = QtCore.QCoreApplication.translate
        wifi.setWindowTitle(_translate("wifi", "Wi-Fi"))
        self.name_wifi.setText(_translate("wifi", "ชื่อ Wi-Fi"))
        self.label.setText(_translate("wifi", "  Wi-Fi"))
        self.add_back_pushButton.setText(_translate("wifi", "ย้อนกลับ"))
        self.reload_pushButton.setText(_translate("wifi", ""))

        self.img_label.raise_()

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    wifi = QtWidgets.QMainWindow()
    ui = Ui_wifi()
    ui.setupUi(wifi)
    wifi.show()
    sys.exit(app.exec_())
