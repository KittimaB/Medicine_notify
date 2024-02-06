

from PyQt5 import QtCore, QtGui, QtWidgets
# ไม่ใช้แล้ว

class Ui_drug_List(object):
    def setupUi(self, drug_List):
        drug_List.setObjectName("drug_List")
        drug_List.resize(531, 401)
        drug_List.setStyleSheet("\n"
"background-color: rgb(23, 73, 110);")
        self.centralwidget = QtWidgets.QWidget(drug_List)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, -60, 531, 131))
        self.frame.setStyleSheet("border-radius: 40px;\n"
"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(180, 70, 171, 51))
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
        self.add_back_pushButton.setGeometry(QtCore.QRect(50, 80, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add_back_pushButton.setFont(font)
        self.add_back_pushButton.setStyleSheet("border-radius: 9px;\n"
"color: rgb(0, 0, 0);\n"
"border-color:rgb(0, 0, 0);\n"
"background-color: rgb(244, 212, 99);")
        self.add_back_pushButton.setObjectName("add_back_pushButton")
        self.add_pushButton = QtWidgets.QPushButton(self.frame)
        self.add_pushButton.setGeometry(QtCore.QRect(410, 80, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add_pushButton.setFont(font)
        self.add_pushButton.setStyleSheet("border-radius: 9px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 127);")
        self.add_pushButton.setObjectName("add_pushButton")
        drug_List.setCentralWidget(self.centralwidget)

        self.retranslateUi(drug_List)
        QtCore.QMetaObject.connectSlotsByName(drug_List)

    def retranslateUi(self, drug_List):
        _translate = QtCore.QCoreApplication.translate
        drug_List.setWindowTitle(_translate("drug_List", "คลังยา"))
        self.label.setText(_translate("drug_List", "คลังยา"))
        self.add_back_pushButton.setText(_translate("drug_List", "ย้อนกลับ"))
        self.add_pushButton.setText(_translate("drug_List", "เพิ่มยา"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    drug_List = QtWidgets.QMainWindow()
    ui = Ui_drug_List()
    ui.setupUi(drug_List)
    drug_List.show()
    sys.exit(app.exec_())
