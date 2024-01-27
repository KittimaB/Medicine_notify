import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import random
import sqlite3
import string

class Ui_encrypt_check(object):
    def setupUi(self, encrypt_check, drug_List, each_drug, each_drug2, day_start, select_meal, data_check, updated_data2):
        self.encrypt_check = encrypt_check
        self.drug_List = drug_List
        self.each_drug = each_drug
        self.each_drug2 = each_drug2
        self.day_start = day_start
        self.select_meal = select_meal
        self.data_check = data_check
        self.updated_data2 = updated_data2

        encrypt_check.setObjectName("encrypt_check")
        encrypt_check.resize(531, 401)
        encrypt_check.setStyleSheet("background-color: rgb(217, 244, 255)")
        self.centralwidget = QtWidgets.QWidget(encrypt_check)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 120, 181, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setLineWidth(1)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-10, 80, 551, 20))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.add_back_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.add_back_pushButton.setGeometry(QtCore.QRect(30, 40, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add_back_pushButton.setFont(font)
        self.add_back_pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(166, 0, 0)")
        self.add_back_pushButton.setObjectName("add_back_pushButton")

        self.label_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(240, 160, 181, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_3.setObjectName("label_3")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 20, 281, 51))
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
        self.set_code_label = QtWidgets.QLabel(self.centralwidget)
        self.set_code_label.setGeometry(QtCore.QRect(110, 123, 115, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.set_code_label.setFont(font)
        self.set_code_label.setObjectName("set_code_label")
        self.fill_code_label = QtWidgets.QLabel(self.centralwidget)
        self.fill_code_label.setGeometry(QtCore.QRect(104, 164, 130, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.fill_code_label.setFont(font)
        self.fill_code_label.setObjectName("fill_code_label")
        self.next_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.next_pushButton.setGeometry(QtCore.QRect(230, 200, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.next_pushButton.setFont(font)
        self.next_pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 127);\n"
"")
        self.next_pushButton.setObjectName("next_pushButton")
        encrypt_check.setCentralWidget(self.centralwidget)

        self.retranslateUi(encrypt_check)
        QtCore.QMetaObject.connectSlotsByName(encrypt_check)

        def close_window():
            encrypt_check.close()

        self.add_back_pushButton.clicked.connect(close_window)

        self.updated_data2 = updated_data2

        # Generate a random code with both numbers and letters
        characters = string.ascii_letters + string.digits
        self.generated_code = ''.join(random.choice(characters) for _ in range(6))
        self.label_2.setText(f"{self.generated_code}")

        def check_code():
            # Get the user-entered code
            user_code = self.label_3.toPlainText().strip()

            # Check if the user-entered code matches the generated code
            if user_code == self.generated_code:
                # Code is correct, update the database with the received data
                connection = sqlite3.connect("medicine.db")
                cursor = connection.cursor()

                update_query = '''
                    UPDATE Drug
                    SET drug_name = ?,
                        drug_description = ?,
                        drug_remaining = ?,
                        drug_eat = ?,
                        drug_new = ?
                    WHERE drug_id = ?
                '''
                cursor.execute(update_query, (
                    self.updated_data2['drug_name'],
                    self.updated_data2['drug_description'],
                    self.updated_data2['drug_remaining'],
                    self.updated_data2['drug_eat'],
                    self.updated_data2['drug_new'],
                    self.updated_data2['drug_id']
                ))

                

                connection.commit()
                connection.close()
                
                
            else:
                # Code is incorrect, prompt the user to enter the correct code
                QMessageBox.warning(self.centralwidget, "รหัสไม่ถูกต้อง", "กรุณากรอกรหัสให้ถูกต้อง")

        self.next_pushButton.clicked.connect(check_code)
        self.next_pushButton.clicked.connect(self.closeAll)

    # def closeAll(self):
    #     self.each_drug.closeAll()
    #     self.each_drug2.closeAll()
    #     self.day_start.closeAll() 
    #     self.select_meal.closeAll()
    #     self.data_check.closeAll()
    #     self.encrypt_check.close()

    def closeAll(self):
        self.each_drug.closeAll()
        self.each_drug2.closeAll()
        self.select_meal.closeAll()
        self.data_check.closeAll()
        self.encrypt_check.close()

    def retranslateUi(self, encrypt_check):
        _translate = QtCore.QCoreApplication.translate
        encrypt_check.setWindowTitle(_translate("encrypt_check", "ยืนยันการแก้ไข"))
        self.label_2.setText(_translate("encrypt_check", "รหัสที่กำหนด"))
        self.add_back_pushButton.setText(_translate("encrypt_check", "ย้อนกลับ"))
        self.label_3.setText(_translate("encrypt_check", ""))
        self.label.setText(_translate("encrypt_check", "ยืนยันการแก้ไข"))
        self.set_code_label.setText(_translate("encrypt_check", "รหัสตรวจสอบ : "))
        self.fill_code_label.setText(_translate("encrypt_check", " กรุณากรอกรหัส: "))
        self.next_pushButton.setText(_translate("encrypt_check", "ยืนยัน"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    encrypt_check = QtWidgets.QMainWindow()
    ui = Ui_encrypt_check()
    ui.setupUi(encrypt_check)
    encrypt_check.show()
    sys.exit(app.exec_())
