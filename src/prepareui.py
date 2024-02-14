

from PyQt5 import QtCore, QtGui, QtWidgets
# ไม่ใช้แล้ว

class Ui_prepare(object):
    def setupUi(self, prepare):
        prepare.setObjectName("prepare")
        prepare.resize(683, 400)
        prepare.setStyleSheet("\n"
"background-color: rgb(23, 73, 110);")
        self.centralwidget = QtWidgets.QWidget(prepare)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, -60, 683, 131))
        self.frame.setStyleSheet("border-radius: 40px;\n"
"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.prepare_label = QtWidgets.QLabel(self.frame)
        self.prepare_label.setGeometry(QtCore.QRect(200, 70, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.prepare_label.setFont(font)
        self.prepare_label.setStyleSheet("border-radius: 16px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(23, 73, 110);")
        self.prepare_label.setFrameShape(QtWidgets.QFrame.Box)
        self.prepare_label.setLineWidth(1)
        self.prepare_label.setTextFormat(QtCore.Qt.AutoText)
        self.prepare_label.setScaledContents(False)
        self.prepare_label.setAlignment(QtCore.Qt.AlignCenter)
        self.prepare_label.setWordWrap(True)
        self.prepare_label.setObjectName("prepare_label")
        self.add_back_pushButton = QtWidgets.QPushButton(self.frame)
        self.add_back_pushButton.setGeometry(QtCore.QRect(50, 80, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add_back_pushButton.setFont(font)
        self.add_back_pushButton.setStyleSheet("border-radius: 9px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(244, 212, 99);")
        self.add_back_pushButton.setObjectName("add_back_pushButton")
        self.next_pushButton = QtWidgets.QPushButton(self.frame)
        self.next_pushButton.setGeometry(QtCore.QRect(540, 80, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.next_pushButton.setFont(font)
        self.next_pushButton.setStyleSheet("border-radius: 9px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(227, 151, 61);")
        self.next_pushButton.setObjectName("next_pushButton")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(30, 80, 201, 301))
        self.frame_2.setStyleSheet("border-radius: 16px;\n"
"background-color: rgb(236, 236, 236);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(10, 10, 181, 281))
        self.frame_3.setStyleSheet("border-radius: 9px;\n"
"background-color: rgb(170, 203, 223);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setGeometry(QtCore.QRect(20, 10, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.listWidget = QtWidgets.QListWidget(self.frame_3)
        self.listWidget.setGeometry(QtCore.QRect(10, 40, 161, 231))
        self.listWidget.setStyleSheet("border-radius: 9px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.listWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.listWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.listWidget.setLineWidth(1)
        self.listWidget.setObjectName("listWidget")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(250, 80, 401, 301))
        self.frame_4.setStyleSheet("border-radius: 16px;\n"
"background-color: rgb(236, 236, 236);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setGeometry(QtCore.QRect(30, 10, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(260, 120, 381, 251))
        self.tableWidget.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        prepare.setCentralWidget(self.centralwidget)

        self.retranslateUi(prepare)
        QtCore.QMetaObject.connectSlotsByName(prepare)

    def retranslateUi(self, prepare):
        _translate = QtCore.QCoreApplication.translate
        prepare.setWindowTitle(_translate("prepare", "เตรียมบอล"))
        self.prepare_label.setText(_translate("prepare", "กล่องบรรจุยา"))
        self.add_back_pushButton.setText(_translate("prepare", "ย้อนกลับ"))
        self.next_pushButton.setText(_translate("prepare", "ถัดไป"))
        self.label.setText(_translate("prepare", "รายชื่อยาที่ต้องเตรียม"))
        self.label_2.setText(_translate("prepare", "วางตามช่องที่แสดง"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    prepare = QtWidgets.QMainWindow()
    ui = Ui_prepare()
    ui.setupUi(prepare)
    prepare.show()
    sys.exit(app.exec_())
