from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_data_check(object):
    def setupUi(self, data_check, day_start, drug_List, each_drug, each_drug2, select_meal, updated_data2):
        self.data_check = data_check
        self.select_meal = select_meal
        self.drug_List = drug_List
        self.each_drug = each_drug
        self.each_drug2 = each_drug2
        self.day_start = day_start
        self.updated_data2 = updated_data2

        data_check.setObjectName("data_check")
        data_check.resize(531, 401)
        data_check.setStyleSheet("background-color: rgb(217, 244, 255)")
        self.centralwidget = QtWidgets.QWidget(data_check)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 20, 325, 51))
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
        self.add_back_pushButton.setGeometry(QtCore.QRect(20, 40, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add_back_pushButton.setFont(font)
        self.add_back_pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(166, 0, 0)")
        self.add_back_pushButton.setObjectName("add_back_pushButton")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-10, 80, 551, 20))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
#         self.add_pushButton = QtWidgets.QPushButton(self.centralwidget)
#         self.add_pushButton.setGeometry(QtCore.QRect(430, 40, 81, 31))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         self.add_pushButton.setFont(font)
#         self.add_pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
# "background-color: rgb(81, 179, 85);")
#         self.add_pushButton.setObjectName("add_pushButton")
        data_check.setCentralWidget(self.centralwidget)

        self.retranslateUi(data_check)
        QtCore.QMetaObject.connectSlotsByName(data_check)

        def close_window():
            data_check.close()
            
        self.add_back_pushButton.clicked.connect(close_window)

    def set_data_info(self, drug_id):
        self.drug_id = drug_id
        print(f"data_check {self.updated_data2}")

        connection = sqlite3.connect("medicine.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Drug")
        drugs = cursor.fetchall()
        connection.close()
        print(drugs)

        # เพิ่มโค้ดนี้เพื่อแสดงข้อมูลในหน้า data_check
        label_data = QtWidgets.QLabel(self.centralwidget)
        label_data.setGeometry(QtCore.QRect(20, 120, 300, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        label_data.setFont(font)
        label_data.setText(f"Updated Data: {self.updated_data2}")
        label_data.show()

    def retranslateUi(self, data_check):
        _translate = QtCore.QCoreApplication.translate
        data_check.setWindowTitle(_translate("data_check", "ตรวจสอบความถูกต้อง"))
        self.label.setText(_translate("data_check", "ตรวจสอบความถูกต้อง"))
        self.add_back_pushButton.setText(_translate("data_check", "ย้อนกลับ"))
        # self.add_pushButton.setText(_translate("data_check", "เพิ่มยา"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    data_check = QtWidgets.QMainWindow()
    ui = Ui_data_check()
    ui.setupUi(data_check)
    data_check.show()
    sys.exit(app.exec_())
