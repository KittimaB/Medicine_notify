
from PyQt5 import QtCore, QtGui, QtWidgets
#  ไม่ใช้แล้ว

class Ui_encrypt_check(object):
    def setupUi(self, encrypt_check):
        encrypt_check.setObjectName("encrypt_check")
        encrypt_check.resize(683, 400)
        encrypt_check.setStyleSheet("\n"
"background-color: rgb(23, 73, 110);")
        self.centralwidget = QtWidgets.QWidget(encrypt_check)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, -60, 683, 131))
        self.frame.setStyleSheet("border-radius: 40px;\n"
"background-color: rgb(255, 255, 255);")
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
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setLineWidth(1)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.add_back_pushButton = QtWidgets.QPushButton(self.frame)
        self.add_back_pushButton.setGeometry(QtCore.QRect(50, 80, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add_back_pushButton.setFont(font)
        self.add_back_pushButton.setStyleSheet("border-radius: 9px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(244, 212, 99);")
        self.add_back_pushButton.setObjectName("add_back_pushButton")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(200, 90, 291, 261))
        self.frame_2.setStyleSheet("border-radius: 16px;\n"
"background-color: rgb(236, 236, 236);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(10, 10, 271, 201))
        self.frame_3.setStyleSheet("border-radius: 9px;\n"
"background-color: rgb(170, 203, 223);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.set_code_label = QtWidgets.QLabel(self.frame_3)
        self.set_code_label.setGeometry(QtCore.QRect(30, 10, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.set_code_label.setFont(font)
        self.set_code_label.setObjectName("set_code_label")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(30, 40, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border-radius: 9px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setLineWidth(1)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setGeometry(QtCore.QRect(30, 130, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border-radius: 9px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setLineWidth(1)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.drugName_label_2 = QtWidgets.QLabel(self.frame_3)
        self.drugName_label_2.setGeometry(QtCore.QRect(30, 100, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.drugName_label_2.setFont(font)
        self.drugName_label_2.setObjectName("drugName_label_2")
        self.next_pushButton = QtWidgets.QPushButton(self.frame_2)
        self.next_pushButton.setGeometry(QtCore.QRect(100, 220, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.next_pushButton.setFont(font)
        self.next_pushButton.setStyleSheet("border-radius: 9px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 127);\n"
"")
        self.next_pushButton.setObjectName("next_pushButton")
        encrypt_check.setCentralWidget(self.centralwidget)

        self.retranslateUi(encrypt_check)
        QtCore.QMetaObject.connectSlotsByName(encrypt_check)

    def retranslateUi(self, encrypt_check):
        _translate = QtCore.QCoreApplication.translate
        encrypt_check.setWindowTitle(_translate("encrypt_check", "ยืนยันการแก้ไข"))
        self.label.setText(_translate("encrypt_check", "ยืนยันการแก้ไข"))
        self.add_back_pushButton.setText(_translate("encrypt_check", "ย้อนกลับ"))
        self.set_code_label.setText(_translate("encrypt_check", "รหัสตรวจสอบ"))
        self.label_2.setText(_translate("encrypt_check", "รหัสที่กำหนด"))
        self.label_3.setText(_translate("encrypt_check", "กรุณากรอกรหัส"))
        self.drugName_label_2.setText(_translate("encrypt_check", "กรุณากรอกรหัส"))
        self.next_pushButton.setText(_translate("encrypt_check", "ยืนยัน"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    encrypt_check = QtWidgets.QMainWindow()
    ui = Ui_encrypt_check()
    ui.setupUi(encrypt_check)
    encrypt_check.show()
    sys.exit(app.exec_())
