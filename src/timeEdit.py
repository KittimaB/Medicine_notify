from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_time_Edit(object):
    def __init__(self):
        self.meal_label_text = ""
        
    def setupUi(self, time_Edit):
        time_Edit.setObjectName("time_Edit")
        time_Edit.resize(531, 401)
        time_Edit.setStyleSheet("background-color: rgb(217, 244, 255)")
        self.centralwidget = QtWidgets.QWidget(time_Edit)
        self.centralwidget.setObjectName("centralwidget")
        self.add_back_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.add_back_pushButton.setGeometry(QtCore.QRect(40, 50, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add_back_pushButton.setFont(font)
        self.add_back_pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(166, 0, 0)")
        self.add_back_pushButton.setObjectName("add_back_pushButton")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 90, 1201, 16))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 20, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setLineWidth(1)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.timeEdit_label = QtWidgets.QLabel(self.centralwidget)
        self.timeEdit_label.setGeometry(QtCore.QRect(30, 120, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.timeEdit_label.setFont(font)
        self.timeEdit_label.setAlignment(QtCore.Qt.AlignCenter)
        self.timeEdit_label.setObjectName("timeEdit_label")
        self.timeEdit_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.timeEdit_pushButton.setGeometry(QtCore.QRect(230, 280, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.timeEdit_pushButton.setFont(font)
        self.timeEdit_pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.timeEdit_pushButton.setObjectName("timeEdit_pushButton")
        self.timeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit.setGeometry(QtCore.QRect(190, 200, 171, 51))
        self.timeEdit.setObjectName("timeEdit")
        time_Edit.setCentralWidget(self.centralwidget)

        self.retranslateUi(time_Edit)
        QtCore.QMetaObject.connectSlotsByName(time_Edit)

        self.label.setText(self.meal_label_text)

        def close_window():
            time_Edit.close()

        self.add_back_pushButton.clicked.connect(close_window)

    def retranslateUi(self, time_Edit):
        _translate = QtCore.QCoreApplication.translate
        time_Edit.setWindowTitle(_translate("time_Edit", "ตั้งเวลา"))
        self.add_back_pushButton.setText(_translate("time_Edit", "ย้อนกลับ"))
        self.label.setText(_translate("time_Edit", "มื้อเช้า ก่อนอาหาร"))
        self.timeEdit_label.setText(_translate("time_Edit", "เลือกเวลาที่ต้องการ"))
        self.timeEdit_pushButton.setText(_translate("time_Edit", "ยืนยัน"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    time_Edit = QtWidgets.QMainWindow()
    ui = Ui_time_Edit()
    ui.setupUi(time_Edit)
    time_Edit.show()
    sys.exit(app.exec_())
