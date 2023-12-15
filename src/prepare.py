

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_prepare(object):
    def setupUi(self, prepare):
        prepare.setObjectName("prepare")
        prepare.resize(531, 401)
        prepare.setStyleSheet("background-color: rgb(217, 244, 255)")
        self.centralwidget = QtWidgets.QWidget(prepare)
        self.centralwidget.setObjectName("centralwidget")
        self.prepare_label = QtWidgets.QLabel(self.centralwidget)
        self.prepare_label.setGeometry(QtCore.QRect(130, 20, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.prepare_label.setFont(font)
        self.prepare_label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.prepare_label.setFrameShape(QtWidgets.QFrame.Box)
        self.prepare_label.setLineWidth(1)
        self.prepare_label.setTextFormat(QtCore.Qt.AutoText)
        self.prepare_label.setScaledContents(False)
        self.prepare_label.setAlignment(QtCore.Qt.AlignCenter)
        self.prepare_label.setWordWrap(True)
        self.prepare_label.setObjectName("prepare_label")
        self.add_back_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.add_back_pushButton.setGeometry(QtCore.QRect(30, 40, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add_back_pushButton.setFont(font)
        self.add_back_pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(166, 0, 0)")
        self.add_back_pushButton.setObjectName("add_back_pushButton")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-10, 90, 551, 20))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 120, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(35, 160, 131, 191))
        self.listWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.listWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.listWidget.setLineWidth(1)
        self.listWidget.setObjectName("listWidget")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(190, 110, 20, 261))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setObjectName("line_2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(220, 150, 291, 211))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(290, 120, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.next_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.next_pushButton.setGeometry(QtCore.QRect(440, 40, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.next_pushButton.setFont(font)
        self.next_pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.next_pushButton.setObjectName("next_pushButton")
        prepare.setCentralWidget(self.centralwidget)

        self.retranslateUi(prepare)
        QtCore.QMetaObject.connectSlotsByName(prepare)

        def close_window():
            prepare.close()
            
        self.add_back_pushButton.clicked.connect(close_window)

    def retranslateUi(self, prepare):
        _translate = QtCore.QCoreApplication.translate
        prepare.setWindowTitle(_translate("prepare", "เตรียมบอล"))
        self.prepare_label.setText(_translate("prepare", "เตรียมบอล"))
        self.add_back_pushButton.setText(_translate("prepare", "ย้อนกลับ"))
        self.label.setText(_translate("prepare", "รายชื่อยาที่ต้องเตรียม"))
        self.label_2.setText(_translate("prepare", "วางตามช่องที่แสดง"))
        self.next_pushButton.setText(_translate("prepare", "ถัดไป"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    prepare = QtWidgets.QMainWindow()
    ui = Ui_prepare()
    ui.setupUi(prepare)
    prepare.show()
    sys.exit(app.exec_())
