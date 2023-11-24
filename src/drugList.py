from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem 
import sqlite3

#ไม่ใช้แล้ว

class Ui_drugList(object):
    def setupUi(self, drugList):
        drugList.setObjectName("drugList")
        drugList.resize(531, 401)
        drugList.setStyleSheet("background-color: rgb(217, 244, 255)")
        self.centralwidget = QtWidgets.QWidget(drugList)
        self.centralwidget.setObjectName("centralwidget")
        self.add_back_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.add_back_pushButton.setGeometry(QtCore.QRect(30, 40, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add_back_pushButton.setFont(font)
        self.add_back_pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(166, 0, 0)")
        self.add_back_pushButton.setObjectName("add_back_pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 20, 221, 51))
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
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-20, 80, 551, 20))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        drugList.setCentralWidget(self.centralwidget)

        self.retranslateUi(drugList)
        QtCore.QMetaObject.connectSlotsByName(drugList)

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 120, 491, 241))
        self.tableWidget.setObjectName("tableWidget")

        def close_window():
            drugList.close()
            
        self.add_back_pushButton.clicked.connect(close_window)


    def retranslateUi(self, drugList):
        _translate = QtCore.QCoreApplication.translate
        drugList.setWindowTitle(_translate("drugList", "รายการยาที่มี"))
        self.add_back_pushButton.setText(_translate("drugList", "ย้อนกลับ"))
        self.label.setText(_translate("drugList", "รายการยาที่มี"))

    
    def load_drugs_from_database(self):

        # ล้างข้อมูลในตาราง
        self.tableWidget.clear()

        # เชื่อมต่อกับฐานข้อมูล SQLite และดึงข้อมูลยาจากตาราง Drug
        connection = sqlite3.connect("medicine.db")
        cursor = connection.cursor()
        cursor.execute("SELECT drug_name, drug_description, drug_amount, drug_eat FROM Drug")
        drugs = cursor.fetchall()
        connection.close()

        # กำหนดหัวข้อคอลัมน์ในตาราง
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(["ชื่อยา", "คำอธิบายยา", "จำนวนยาทั้งหมดที่มี (เม็ด)", "จำนวนยาที่กินต่อ 1 มื้อ (เม็ด)"])
        
        # กำหนดจำนวนแถวในตารางตามจำนวนรายการยาที่ดึงมาจากฐานข้อมูล
        self.tableWidget.setRowCount(len(drugs))

        # แสดงข้อมูลยาในตาราง
        for row, drug in enumerate(drugs):
            for col, data in enumerate(drug):
                item = QTableWidgetItem(str(data))  # Convert data to string before creating QTableWidgetItem
                self.tableWidget.setItem(row, col, item)
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    # สร้าง QMainWindow
    drugList = QtWidgets.QMainWindow()
    ui = Ui_drugList()
    ui.setupUi(drugList)

    # สร้างและกำหนด QTableWidget
    ui.tableWidget = QtWidgets.QTableWidget(ui.centralwidget)
    ui.tableWidget.setGeometry(QtCore.QRect(20, 120, 491, 241))
    ui.tableWidget.setObjectName("tableWidget")

    # เรียกใช้ฟังก์ชัน load_drugs_from_database เพื่อโหลดข้อมูลยาจากฐานข้อมูล
    ui.load_drugs_from_database()
    
    drugList.show()
    sys.exit(app.exec_())
