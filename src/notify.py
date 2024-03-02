from Utils import *
from UI_Generate import *
width, height = Scale_Width_Height()

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsDropShadowEffect

class Ui_notify(object):
    def setupUi(self, notify):
        UI_instance.Set(notify)
        show_widget_fullscreen(notify)

        notify.setObjectName("notify")
        notify.resize(int(683 * width), int(400 * height))
        notify.setStyleSheet("\n"
"background-color: rgb(23, 73, 110);")
        self.centralwidget = QtWidgets.QWidget(notify)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(int(190 * width), int(20 * height), int(281 * width), int(51 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(20 * height))
        font.setBold(True)
        font.setWeight(int(75 * width))
        self.label.setFont(font)
        self.label.setStyleSheet("border-radius: 34px;\n"
"color: rgb(23, 73, 110);\n"
"background-color: rgb(255, 255, 255);")
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
        self.img_label = QtWidgets.QLabel(self.label)
        self.img_label.setGeometry(QtCore.QRect(int(50 * width), int(9 * height), int(33 * width), int(31 * height)))
        self.img_label.setText("")
        self.img_label.setPixmap(QtGui.QPixmap(":/icons/notify.png"))
        self.img_label.setScaledContents(True)
        self.img_label.setAlignment(QtCore.Qt.AlignCenter)
        self.img_label.setObjectName("img_label")
        
        # self.close_pushButton = QtWidgets.QPushButton(self.centralwidget)
        # self.close_pushButton.setGeometry(QtCore.QRect(int(420 * width), int(170 * height), int(161 * width), int(161 * height)))
        # font = QtGui.QFont()
        # font.setPointSize(int(20 * height))
        # self.close_pushButton.setFont(font)
        # self.close_pushButton.setStyleSheet("border-radius: 80px;\n"
        #                                 "color: rgb(0, 0, 0);\n"
        #                                 "background-color: rgb(244, 212, 99);\n")
        # # Add drop shadow effect to the button
        # shadow = QGraphicsDropShadowEffect(self.close_pushButton)
        # shadow.setBlurRadius(int(8 * width))
        # shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        # shadow.setOffset(int(0 * width), int(2 * height))
        # self.close_pushButton.setGraphicsEffect(shadow)
        # self.close_pushButton.setObjectName("close_pushButton")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(int(195 * width), int(100 * height), int(275 * width), int(275 * height)))
        self.frame.setStyleSheet("border-radius: 9px;\n"
"background-color: rgb(236, 236, 236);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.frame)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.frame.setGraphicsEffect(shadow)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(int(8 * width), int(10 * height), int(260 * width), int(260 * height)))
        self.frame_2.setStyleSheet("border-radius: 9px;\n"
"background-color: rgb(170, 203, 223);")
        
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.time_name = QtWidgets.QLabel(self.frame_2)
        self.time_name.setGeometry(QtCore.QRect(int(20 * width), int(10 * height), int(211 * width), int(41 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(16 * height))
        font.setBold(False)
        font.setWeight(int(25 * width))
        self.time_name.setFont(font)
        self.time_name.setStyleSheet("border-radius: 16px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.time_name)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.time_name.setGraphicsEffect(shadow)
        self.time_name.setFrameShape(QtWidgets.QFrame.Box)
        self.time_name.setLineWidth(int(1 * width))
        self.time_name.setTextFormat(QtCore.Qt.AutoText)
        self.time_name.setScaledContents(False)
        self.time_name.setAlignment(QtCore.Qt.AlignCenter)
        self.time_name.setWordWrap(True)
        self.time_name.setObjectName("time_name")
        self.meal_name = QtWidgets.QLabel(self.frame_2)
        self.meal_name.setGeometry(QtCore.QRect(int(20 * width), int(60 * height), int(211 * width), int(41 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(16 * height))
        font.setBold(False)
        font.setWeight(int(25 * width))
        self.meal_name.setFont(font)
        self.meal_name.setStyleSheet("border-radius: 16px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.meal_name)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.meal_name.setGraphicsEffect(shadow)
        self.meal_name.setFrameShape(QtWidgets.QFrame.Box)
        self.meal_name.setLineWidth(int(1 * width))
        self.meal_name.setTextFormat(QtCore.Qt.AutoText)
        self.meal_name.setScaledContents(False)
        self.meal_name.setAlignment(QtCore.Qt.AlignCenter)
        self.meal_name.setWordWrap(True)
        self.meal_name.setObjectName("meal_name")
        self.listWidget = QtWidgets.QListWidget(self.frame_2)
        self.listWidget.setGeometry(QtCore.QRect(int(20 * width), int(140 * height), int(211 * width), int(100 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(16 * height))
        font.setWeight(int(25 * width))
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("border-radius: 9px;\n"
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
        self.listWidget.setLineWidth(1)
        self.listWidget.setObjectName("listWidget")

        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(int(20 * width), int(110 * height), int(121 * width), int(31 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(14 * height))
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        
        # self.label_2 = QtWidgets.QLabel(self.centralwidget)
        # self.label_2.setGeometry(QtCore.QRect(410, 120, 200, 31))
        # font = QtGui.QFont()
        # font.setPointSize(16)
        # self.label_2.setFont(font)
        # self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        # self.label_2.setObjectName("label_2")
        notify.setCentralWidget(self.centralwidget)

        unique_drug_names_for_meal = set()  # Use a set to store unique drug names
        unique_drug_names_for_meal.add(f"-A")

        self.listWidget.clear()
        self.listWidget.addItems(list(unique_drug_names_for_meal))  # Add unique drug names to listWidget

        self.retranslateUi(notify)
        QtCore.QMetaObject.connectSlotsByName(notify)

    def retranslateUi(self, notify):
        _translate = QtCore.QCoreApplication.translate
        notify.setWindowTitle(_translate("notify", "แจ้งเตือน"))
        self.label.setText(_translate("notify", "  แจ้งเตือน"))
        # self.close_pushButton.setText(_translate("notify", "ปิดแจ้งเตือน"))
        self.meal_name.setText(_translate("notify", "มื้อเช้า หลังอาหาร"))
        self.time_name.setText(_translate("notify", " เวลา 06:30 น."))
        self.label_2.setText(_translate("notify", "รายการยามีดังนี้"))
        # self.label_2.setText(_translate("notify", "กรุณากดปุ่มด้านล่างนี้"))

import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    notify = QtWidgets.QMainWindow()
    ui = Ui_notify()
    ui.setupUi(notify)
    notify.show()
    sys.exit(app.exec_())
