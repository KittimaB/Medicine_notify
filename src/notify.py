

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsDropShadowEffect

class Ui_notify(object):
    def setupUi(self, notify):
        notify.setObjectName("notify")
        notify.resize(683, 400)
        notify.setStyleSheet("\n"
"background-color: rgb(23, 73, 110);")
        self.centralwidget = QtWidgets.QWidget(notify)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 20, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("border-radius: 16px;\n"
"color: rgb(23, 73, 110);\n"
"background-color: rgb(255, 255, 255);")
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
        self.img_label = QtWidgets.QLabel(self.label)
        self.img_label.setGeometry(QtCore.QRect(50, 9, 33, 31))
        self.img_label.setText("")
        self.img_label.setPixmap(QtGui.QPixmap(":/icons/notify.png"))
        self.img_label.setScaledContents(True)
        self.img_label.setAlignment(QtCore.Qt.AlignCenter)
        self.img_label.setObjectName("img_label")
        
        self.close_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.close_pushButton.setGeometry(QtCore.QRect(420, 170, 161, 161))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.close_pushButton.setFont(font)
        self.close_pushButton.setStyleSheet("border-radius: 80px;\n"
                                        "color: rgb(0, 0, 0);\n"
                                        "background-color: rgb(244, 212, 99);\n")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.close_pushButton)
        shadow.setBlurRadius(8)
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(0,2)
        self.close_pushButton.setGraphicsEffect(shadow)
        self.close_pushButton.setObjectName("close_pushButton")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(50, 100, 271, 271))
        self.frame.setStyleSheet("border-radius: 9px;\n"
"background-color: rgb(236, 236, 236);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.frame)
        shadow.setBlurRadius(8)
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(0,2)
        self.frame.setGraphicsEffect(shadow)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.meal_name = QtWidgets.QLabel(self.frame)
        self.meal_name.setGeometry(QtCore.QRect(30, 20, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.meal_name.setFont(font)
        self.meal_name.setStyleSheet("border-radius: 9px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.meal_name)
        shadow.setBlurRadius(8)
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(0,2)
        self.meal_name.setGraphicsEffect(shadow)
        self.meal_name.setFrameShape(QtWidgets.QFrame.Box)
        self.meal_name.setLineWidth(1)
        self.meal_name.setTextFormat(QtCore.Qt.AutoText)
        self.meal_name.setScaledContents(False)
        self.meal_name.setAlignment(QtCore.Qt.AlignCenter)
        self.meal_name.setWordWrap(True)
        self.meal_name.setObjectName("meal_name")
        self.listWidget = QtWidgets.QListWidget(self.frame)
        self.listWidget.setGeometry(QtCore.QRect(30, 80, 211, 161))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("border-radius: 9px;\n"
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
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(410, 120, 200, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        notify.setCentralWidget(self.centralwidget)

        self.retranslateUi(notify)
        QtCore.QMetaObject.connectSlotsByName(notify)

    def retranslateUi(self, notify):
        _translate = QtCore.QCoreApplication.translate
        notify.setWindowTitle(_translate("notify", "แจ้งเตือน"))
        self.label.setText(_translate("notify", "  แจ้งเตือน"))
        self.close_pushButton.setText(_translate("notify", "ปิดแจ้งเตือน"))
        self.meal_name.setText(_translate("notify", "ชื่อมื้ออาหาร"))
        self.label_2.setText(_translate("notify", "กรุณากดปุ่มด้านล่างนี้"))

import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    notify = QtWidgets.QMainWindow()
    ui = Ui_notify()
    ui.setupUi(notify)
    notify.show()
    sys.exit(app.exec_())
