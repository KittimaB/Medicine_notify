from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsDropShadowEffect
import sqlite3

class Ui_drugTotal(object):
    def setupUi(self, drugTotal):
        drugTotal.setObjectName("drugTotal")
        drugTotal.resize(683, 400)
        drugTotal.setStyleSheet("\n"
"background-color: rgb(23, 73, 110);")
        self.centralwidget = QtWidgets.QWidget(drugTotal)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, -60, 683, 131))
        self.frame.setStyleSheet("border-radius: 40px;\n"
"background-color: rgb(255, 255, 255);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.frame)
        shadow.setBlurRadius(8)
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(0,2)
        self.frame.setGraphicsEffect(shadow)
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
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.label)
        shadow.setBlurRadius(8)
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(0,2)
        self.label.setGraphicsEffect(shadow)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setLineWidth(1)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.img_label = QtWidgets.QLabel(self.frame)
        self.img_label.setGeometry(QtCore.QRect(238, 80, 33, 31))
        self.img_label.setText("")
        self.img_label.setPixmap(QtGui.QPixmap(":/icons/drugleft_icon.png"))
        self.img_label.setScaledContents(True)
        self.img_label.setAlignment(QtCore.Qt.AlignCenter)
        self.img_label.setObjectName("img_label")
        self.add_back_pushButton = QtWidgets.QPushButton(self.frame)
        self.add_back_pushButton.setGeometry(QtCore.QRect(50, 80, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add_back_pushButton.setFont(font)
        self.add_back_pushButton.setStyleSheet("border-radius: 9px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(244, 212, 99);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.add_back_pushButton)
        shadow.setBlurRadius(8)
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(0,2)
        self.add_back_pushButton.setGraphicsEffect(shadow)
        self.add_back_pushButton.setObjectName("add_back_pushButton")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(90, 90, 512, 261))
        self.frame_2.setStyleSheet("border-radius: 9px;\n"
"background-color: rgb(236, 236, 236);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.frame_2)
        shadow.setBlurRadius(8)
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(0,2)
        self.frame_2.setGraphicsEffect(shadow)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        drugTotal.setCentralWidget(self.centralwidget)


        self.retranslateUi(drugTotal)
        QtCore.QMetaObject.connectSlotsByName(drugTotal)

        def close_window():
            drugTotal.close()
            
        self.add_back_pushButton.clicked.connect(close_window)

        # สร้างและกำหนด QTableWidget
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(107, 105, 480, 230))
        self.tableWidget.setObjectName("tableWidget")

        # กำหนดหัวข้อคอลัมน์ในตาราง
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(["ชื่อยา", "จำนวนยาคงเหลือในเครื่อง", "จำนวนยาคงเหลือนอกเครื่อง"])

        # Set the width of the columns
        self.tableWidget.setColumnWidth(0, 150)  # Adjust the width as needed
        self.tableWidget.setColumnWidth(1, 150)  # Adjust the width as needed
        self.tableWidget.setColumnWidth(2, 150)  # Adjust the width as needed

         # Set the background color of the table to white and text color to black
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);")
        
        # กำหนดจำนวนแถวในตารางตามจำนวนรายการยาที่ดึงมาจากฐานข้อมูล
        self.tableWidget.setRowCount(7)

         # Set up button press and release styling
        self.add_back_pushButton.pressed.connect(lambda: self.set_button_pressed_style(self.add_back_pushButton))
        self.add_back_pushButton.released.connect(lambda: self.set_button_released_style(self.add_back_pushButton))

        self.load_drug_data()

    def load_drug_data(self):
        connection = sqlite3.connect("medicine.db")
        cursor = connection.cursor()
        cursor.execute('''
            SELECT drug_name, external_drug, internal_drug, drug_eat FROM Drug 
        ''')

        # Fetch all rows from the result set
        drug_data = cursor.fetchall()

        # Set the number of rows in the table equal to the number of records
        self.tableWidget.setRowCount(len(drug_data))

        # Populate the table with the retrieved data
        for row_num, row_data in enumerate(drug_data):
            for col_num, col_data in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem()

                # If calculating for external_drug or internal_drug columns, apply the formula
                if col_num == 1 or col_num == 2:
                    drug_eat = row_data[3]  #  ตรงกับตำแหน่งที่สี่ คือ drug_eat

                    # Check for None values before performing multiplication
                    if col_data is not None and drug_eat is not None:
                        # Set the text with the desired format
                        item.setText(f"{col_data} มื้อ ({col_data * drug_eat} เม็ด)")
                    else:
                        item.setText("N/A")  # Or any default value you prefer
                else:
                    # For other columns, directly set the text
                    item.setText(str(col_data))

                self.tableWidget.setItem(row_num, col_num, item)

    def set_button_pressed_style(self, button):
        button.setStyleSheet(
            "border-radius: 9px;\n"
            "color: rgb(0, 0, 0);\n"
            "background-color: rgb(200, 200, 200);"  # Change color when pressed
        )

    def set_button_released_style(self, button):
        button.setStyleSheet(
            "border-radius: 9px;\n"
            "color: rgb(255, 255, 255);\n"
            "background-color: rgb(85, 170, 127);"
        )


        

    def retranslateUi(self, drugTotal):
        _translate = QtCore.QCoreApplication.translate
        drugTotal.setWindowTitle(_translate("drugTotal", "จำนวนยาคงเหลือ"))
        self.add_back_pushButton.setText(_translate("drugTotal", "ย้อนกลับ"))
        self.label.setText(_translate("drugTotal", "           จำนวนมื้อยาคงเหลือ   "))

import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    drugTotal = QtWidgets.QMainWindow()
    ui = Ui_drugTotal()
    ui.setupUi(drugTotal)
    drugTotal.show()
    sys.exit(app.exec_())
