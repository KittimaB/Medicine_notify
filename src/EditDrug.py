from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Edit_drug(object):
    def setupUi(self, Edit_drug):
        Edit_drug.setObjectName("Edit_drug")
        Edit_drug.resize(531, 401)
        Edit_drug.setStyleSheet("background-color: rgb(217, 244, 255)")
        self.centralwidget = QtWidgets.QWidget(Edit_drug)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-10, 90, 551, 20))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 20, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
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
        self.add_back_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.add_back_pushButton.setGeometry(QtCore.QRect(30, 40, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add_back_pushButton.setFont(font)
        self.add_back_pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(166, 0, 0)")
        self.add_back_pushButton.setObjectName("add_back_pushButton")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(20, 241, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setAccessibleName("")
        self.textEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_2.setFrameShape(QtWidgets.QFrame.Box)
        self.textEdit_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textEdit_2.setObjectName("textEdit_2")
        self.drugName_label = QtWidgets.QLabel(self.centralwidget)
        self.drugName_label.setGeometry(QtCore.QRect(30, 131, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.drugName_label.setFont(font)
        self.drugName_label.setObjectName("drugName_label")
        self.drugDescribe_label = QtWidgets.QLabel(self.centralwidget)
        self.drugDescribe_label.setGeometry(QtCore.QRect(30, 211, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.drugDescribe_label.setFont(font)
        self.drugDescribe_label.setObjectName("drugDescribe_label")
        self.drugOne_label = QtWidgets.QLabel(self.centralwidget)
        self.drugOne_label.setGeometry(QtCore.QRect(280, 211, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.drugOne_label.setFont(font)
        self.drugOne_label.setAlignment(QtCore.Qt.AlignCenter)
        self.drugOne_label.setObjectName("drugOne_label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 161, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit.setFrameShape(QtWidgets.QFrame.Box)
        self.textEdit.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textEdit.setObjectName("textEdit")
        self.saveDrug_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveDrug_pushButton.setGeometry(QtCore.QRect(220, 331, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.saveDrug_pushButton.setFont(font)
        self.saveDrug_pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 127);")
        self.saveDrug_pushButton.setObjectName("saveDrug_pushButton")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(280, 161, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit_3.setFont(font)
        self.textEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_3.setFrameShape(QtWidgets.QFrame.Box)
        self.textEdit_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textEdit_3.setObjectName("textEdit_3")
        self.drugAll_label = QtWidgets.QLabel(self.centralwidget)
        self.drugAll_label.setGeometry(QtCore.QRect(280, 131, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.drugAll_label.setFont(font)
        self.drugAll_label.setAlignment(QtCore.Qt.AlignCenter)
        self.drugAll_label.setObjectName("drugAll_label")
        self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(280, 241, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit_4.setFont(font)
        self.textEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_4.setFrameShape(QtWidgets.QFrame.Box)
        self.textEdit_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textEdit_4.setObjectName("textEdit_4")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(250, 110, 20, 211))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setObjectName("line_2")
        Edit_drug.setCentralWidget(self.centralwidget)

        self.retranslateUi(Edit_drug)
        QtCore.QMetaObject.connectSlotsByName(Edit_drug)

        def close_window():
            Edit_drug.close()

        self.add_back_pushButton.clicked.connect(close_window)

    def retranslateUi(self, Edit_drug):
        _translate = QtCore.QCoreApplication.translate
        Edit_drug.setWindowTitle(_translate("Edit_drug", "แก้ไขยา"))
        self.label.setText(_translate("Edit_drug", "แก้ไขยา"))
        self.add_back_pushButton.setText(_translate("Edit_drug", "ย้อนกลับ"))
        self.drugName_label.setText(_translate("Edit_drug", "ชื่อยา"))
        self.drugDescribe_label.setText(_translate("Edit_drug", "คำอธิบายยา"))
        self.drugOne_label.setText(_translate("Edit_drug", "จำนวนยาที่กินต่อ 1 มื้อ (เม็ด)"))
        self.saveDrug_pushButton.setText(_translate("Edit_drug", "บันทึกยา"))
        self.drugAll_label.setText(_translate("Edit_drug", "จำนวนยาทั้งหมดที่มี (เม็ด)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Edit_drug = QtWidgets.QMainWindow()
    ui = Ui_Edit_drug()
    ui.setupUi(Edit_drug)
    Edit_drug.show()
    sys.exit(app.exec_())
