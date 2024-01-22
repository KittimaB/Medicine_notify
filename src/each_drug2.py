from PyQt5 import QtCore, QtGui, QtWidgets
from day_start import Ui_day_start
import sqlite3

class Ui_each_drug2(object):
    def setupUi(self, each_drug2, drug_List, each_drug, updated_data):
        self.each_drug2 = each_drug2
        self.drug_List = drug_List
        self.each_drug = each_drug
        self.updated_data = updated_data
        
        each_drug2.setObjectName("each_drug2")
        each_drug2.resize(531, 401)
        each_drug2.setStyleSheet("background-color: rgb(217, 244, 255)")
        self.centralwidget = QtWidgets.QWidget(each_drug2)
        self.centralwidget.setObjectName("centralwidget")
        self.label_6 = QtWidgets.QTextEdit(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(270, 120, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_6.setFrameShape(QtWidgets.QFrame.Box)
        self.label_6.setLineWidth(1)
        self.label_6.setCurrentCharFormat(QtGui.QTextCharFormat())
       
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.label_6.setObjectName("label_6")
        self.next_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.next_pushButton.setGeometry(QtCore.QRect(410, 280, 85, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.next_pushButton.setFont(font)
        self.next_pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.next_pushButton.setObjectName("next_pushButton")
        self.drugStill = QtWidgets.QLabel(self.centralwidget)
        self.drugStill.setGeometry(QtCore.QRect(20, 150, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.drugStill.setFont(font)
        self.drugStill.setObjectName("drugStill")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-10, 90, 551, 20))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 20, 201, 51))
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
        self.drugNew = QtWidgets.QLabel(self.centralwidget)
        self.drugNew.setGeometry(QtCore.QRect(20, 120, 245, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.drugNew.setFont(font)
        self.drugNew.setObjectName("drugNew")
        self.drugGot = QtWidgets.QLabel(self.centralwidget)
        self.drugGot.setGeometry(QtCore.QRect(20, 180, 245, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.drugGot.setFont(font)
        self.drugGot.setObjectName("drugGot")
        self.add_back_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.add_back_pushButton.setGeometry(QtCore.QRect(30, 40, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add_back_pushButton.setFont(font)
        self.add_back_pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(166, 0, 0)")
        self.add_back_pushButton.setObjectName("add_back_pushButton")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(270, 150, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_7.setFrameShape(QtWidgets.QFrame.Box)
        self.label_7.setLineWidth(1)
        self.label_7.setTextFormat(QtCore.Qt.AutoText)
        self.label_7.setScaledContents(False)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(270, 180, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_8.setFrameShape(QtWidgets.QFrame.Box)
        self.label_8.setLineWidth(1)
        self.label_8.setTextFormat(QtCore.Qt.AutoText)
        self.label_8.setScaledContents(False)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName("label_8")
        each_drug2.setCentralWidget(self.centralwidget)

        self.retranslateUi(each_drug2)
        QtCore.QMetaObject.connectSlotsByName(each_drug2)

        def close_window():
            each_drug2.close()

        self.add_back_pushButton.clicked.connect(close_window)

        # self.next_pushButton.clicked.connect(self.open_day_start)

        def save_changes():
            # ตรวจสอบข้อมูลที่ถูกแก้ไขและบันทึกลงฐานข้อมูลหรือตัวแปรที่เหมาะสม
            updated_data2 = self.updated_data
            updated_data2['drug_new'] = self.label_6.toPlainText()
            updated_data2['drug_remaining_meal'] = self.label_7.text()
            updated_data2['all_drug_recieve'] = self.label_8.text()

            # ส่งข้อมูลที่ถูกแก้ไขไปยังหน้าต่อไป
            self.open_day_start(updated_data2)

        self.next_pushButton.clicked.connect(save_changes)

    def open_day_start(self, updated_data2):
        self.day_start_window = QtWidgets.QMainWindow()
        self.day_start_ui = Ui_day_start()
        self.day_start_ui.setupUi(self.day_start_window, self.drug_List, self.each_drug, self, updated_data2)
        print(f"each_drug2 ครั้งที่ 2 {updated_data2}")
        self.day_start_ui.set_day_info(self.drug_id)
        self.day_start_window.show()

    def set_drug2_info(self, drug_id):
        print(f"each_drug2 {self.updated_data}")
        self.drug_id = drug_id
        # print(drug_id)
        connection = sqlite3.connect("medicine.db")
        cursor = connection.cursor()
        query = '''
            SELECT * FROM Drug WHERE drug_id = ?
            '''
        cursor.execute(query, (drug_id,))  
        drug_info = cursor.fetchone()

        if drug_info:
            # Convert the tuple to a list for modification
            drug_info_list = list(drug_info)

            # Modify the values as needed
            drug_info_list[12] = 0

            # Check for None values before performing the division
            drug_remaining, drug_eat = drug_info_list[3], drug_info_list[8]
            if drug_remaining is not None and drug_eat is not None and drug_eat != 0:
                drug_remaining_meal = int(drug_remaining / drug_eat)
            else:
                drug_remaining_meal = 0

            # Update the modified values back to the list
            drug_info_list[4] = drug_remaining_meal

            # Additional modification
            drug_new = drug_info_list[12]
            all_drug_recieve =int(drug_info_list[9])
            if drug_new is not None:
                all_drug_recieve = all_drug_recieve + drug_new
            else:
                all_drug_recieve = all_drug_recieve

            # Update the modified values back to the list
            drug_info_list[9] = all_drug_recieve

            # Convert the list back to a tuple
            drug_info = tuple(drug_info_list)

            self.drug_id = drug_info[0]
            self.label.setText(drug_info[1])
            self.label_6.setText(f"{drug_info[12]}")
            self.label_7.setText(f"{drug_info[4]}")
            self.label_8.setText(f"{drug_info[9]}")

        # print(drug_info)
        
    def closeAll(self):
        self.each_drug.closeAll()
        self.each_drug2.close()  # ปิดหน้าต่างที่เป็นส่วนสมาชิกของ Ui_med_pack2

    def retranslateUi(self, each_drug2):
        _translate = QtCore.QCoreApplication.translate
        each_drug2.setWindowTitle(_translate("each_drug2", "ยาแต่ละตัว"))
        self.label_6.setText(_translate("each_drug2", "ยาที่ได้รับมาใหม่"))
        self.next_pushButton.setText(_translate("each_drug2", "ถัดไป"))
        self.drugStill.setText(_translate("each_drug2", "จำนวนมื้อยาคงเหลือ (มื้อ) :"))
        self.label.setText(_translate("each_drug2", "ชื่อยา"))
        self.drugNew.setText(_translate("each_drug2", "จำนวนยาที่ได้รับมาใหม่ (เม็ด) :"))
        self.drugGot.setText(_translate("each_drug2", "จำนวนยาที่ได้รับมาแล้ว (เม็ด) :"))
        self.add_back_pushButton.setText(_translate("each_drug2", "ย้อนกลับ"))
        self.label_7.setText(_translate("each_drug2", "ยาคงเหลือ"))
        # self.delete_pushButton.setText(_translate("each_drug2", "ลบ"))
        self.label_8.setText(_translate("each_drug2", "ยาที่ได้รับมาแล้ว"))
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    each_drug2 = QtWidgets.QMainWindow()
    ui = Ui_each_drug2()
    ui.setupUi(each_drug2)
    each_drug2.show()
    sys.exit(app.exec_())