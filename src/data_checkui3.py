
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsDropShadowEffect
from encrypt_check import Ui_encrypt_check
import sqlite3

class Ui_data_check3(object):
    def setupUi(self, data_check3, drug_List, each_drug, each_drug2, day_start, select_meal, data_check1, data_check2, updated_data2):
   
        self.data_check3 = data_check3
        self.drug_List = drug_List
        self.each_drug = each_drug
        self.each_drug2 = each_drug2
        self.day_start = day_start
        self.select_meal = select_meal
        self.data_check1 = data_check1
        self.data_check2 = data_check2
        self.updated_data2 = updated_data2
        data_check3.setObjectName("data_check3")
        data_check3.resize(683, 400)
        data_check3.setStyleSheet("\n"
"background-color: rgb(23, 73, 110);")
        self.centralwidget = QtWidgets.QWidget(data_check3)
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
        self.drugName_label = QtWidgets.QLabel(self.centralwidget)
        self.drugName_label.setGeometry(QtCore.QRect(50, 77, 250, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.drugName_label.setFont(font)
        self.drugName_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.drugName_label.setObjectName("drugName_label")
        self.next_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.next_pushButton.setGeometry(QtCore.QRect(510, 250, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.next_pushButton.setFont(font)
        self.next_pushButton.setStyleSheet("border-radius: 9px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(227, 151, 61);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.next_pushButton)
        shadow.setBlurRadius(8)
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(0,2)
        self.next_pushButton.setGraphicsEffect(shadow)
        self.next_pushButton.setObjectName("next_pushButton")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(100, 100, 231, 220))
        self.frame_3.setStyleSheet("border-radius: 16px;\n"
"background-color: rgb(236, 236, 236);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.frame_3)
        shadow.setBlurRadius(8)
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(0,2)
        self.frame_3.setGraphicsEffect(shadow)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.drugDescribe_label_2 = QtWidgets.QLabel(self.frame_3)
        self.drugDescribe_label_2.setGeometry(QtCore.QRect(20, 20, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.drugDescribe_label_2.setFont(font)
        self.drugDescribe_label_2.setObjectName("drugDescribe_label_2")
        self.listWidget = QtWidgets.QListWidget(self.frame_3)
        self.listWidget.setGeometry(QtCore.QRect(20, 50, 185, 150))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.listWidget.setFont(font)
        self.listWidget.setAutoFillBackground(False)
        self.listWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.listWidget)
        shadow.setBlurRadius(8)
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(0,2)
        self.listWidget.setGraphicsEffect(shadow)
        self.listWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.listWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.listWidget.setLineWidth(2)
        self.listWidget.setMidLineWidth(0)
        self.listWidget.setObjectName("listWidget")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(350, 100, 241, 120))
        self.frame_2.setStyleSheet("border-radius: 16px;\n"
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
        self.day_start = QtWidgets.QLabel(self.frame_2)
        self.day_start.setGeometry(QtCore.QRect(10, 20, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.day_start.setFont(font)
        self.day_start.setObjectName("day_start")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(10, 50, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("border-radius: 9px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.label_9)
        shadow.setBlurRadius(8)
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(0,2)
        self.label_9.setGraphicsEffect(shadow)
        self.label_9.setFrameShape(QtWidgets.QFrame.Box)
        self.label_9.setLineWidth(1)
        self.label_9.setTextFormat(QtCore.Qt.AutoText)
        self.label_9.setScaledContents(False)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName("label_9")
        data_check3.setCentralWidget(self.centralwidget)

        self.retranslateUi(data_check3)
        QtCore.QMetaObject.connectSlotsByName(data_check3)

        def close_window():
            data_check3.close()
            
        self.add_back_pushButton.clicked.connect(close_window)
        self.next_pushButton.clicked.connect(lambda: self.open_encrypt_check(updated_data2))
        # self.next_pushButton.clicked.connect(self.closeAll)

         # Set up button press and release styling
        self.add_back_pushButton.pressed.connect(lambda: self.set_button_pressed_style(self.add_back_pushButton))
        self.add_back_pushButton.released.connect(lambda: self.set_button_released_style(self.add_back_pushButton))

        self.next_pushButton.pressed.connect(lambda: self.set_button_pressed_style(self.next_pushButton))
        self.next_pushButton.released.connect(lambda: self.set_button_released_style(self.next_pushButton))


    def set_button_pressed_style(self, button):
        button.setStyleSheet(
            "border-radius: 9px;\n"
            "color: rgb(0, 0, 0);\n"
            "background-color: rgb(200, 200, 200);"  # Change color when pressed
        )

    def set_button_released_style(self, button):
        button.setStyleSheet(
            "border-radius: 9px;\n"
            "color: rgb(0, 0, 0);\n"
            "background-color: rgb(227, 151, 61);"
        )

    def open_encrypt_check(self,updated_data2):
        self.encrypt_check_window = QtWidgets.QMainWindow()
        self.encrypt_check_ui = Ui_encrypt_check()
        self.encrypt_check_ui.setupUi(self.encrypt_check_window, self.drug_List, self.each_drug, self.each_drug2, self.day_start, self.select_meal, self.data_check1, self.data_check2, self, {'drug_id': self.drug_id, **updated_data2})
        self.encrypt_check_window.show()
        

    def set_data_info3(self, drug_id):
        self.drug_id = drug_id
        print(f"data_check3 {self.updated_data2}")
        self.drugName_label.setText(f"ชื่อยา: {self.updated_data2['drug_name']}")

        # Fetch meal data for the given drug_id from the database
        connection = sqlite3.connect("medicine.db")
        cursor = connection.cursor()

        query = '''
            SELECT Meal.meal_name
            FROM Meal
            JOIN Drug_handle ON Meal.meal_id = Drug_handle.meal_id
            WHERE Drug_handle.drug_id = ?
        '''
        cursor.execute(query, (self.drug_id,))
        meal_data = cursor.fetchall()

        connection.close()
        
        # cursor.execute("SELECT * FROM Drug")
        # drugs = cursor.fetchall()
        # connection.close()
        # print(drugs)


        # Set the data in the labels and listWidget
        self.label_9.setText(f"{self.updated_data2['day_start']}")

         # Clear the listWidget before adding new items
        self.listWidget.clear()

        # # Add meal selection data to the listWidget
        # meal_data = self.updated_data2.get('meals', [])
        # print(f"Meal Data: {meal_data}")
        # self.listWidget.addItems(meal_data)

         # Add fetched meal data to the listWidget
        meal_names = [item[0] for item in meal_data]
        self.listWidget.addItems(meal_names)

    def closeAll(self):
        self.each_drug.closeAll()
        self.each_drug2.closeAll()
        self.select_meal.closeAll()
        self.data_check1.closeAll()
        self.data_check2.closeAll()
        self.data_check3.close()

    def retranslateUi(self, data_check3):
        _translate = QtCore.QCoreApplication.translate
        data_check3.setWindowTitle(_translate("data_check3", "ตรวจสอบความถูกต้อง"))
        self.label.setText(_translate("data_check3", "ตรวจสอบความถูกต้อง"))
        self.add_back_pushButton.setText(_translate("data_check3", "ย้อนกลับ"))
        self.drugName_label.setText(_translate("data_check3", "ชื่อยา:"))
        self.next_pushButton.setText(_translate("data_check3", "ถัดไป"))
        self.drugDescribe_label_2.setText(_translate("data_check3", "มื้อยาที่รับประทาน"))
        self.day_start.setText(_translate("data_check3", "วันแรกที่เริ่มรับประทานยา"))
        self.label_9.setText(_translate("data_check3", "วันที่"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    data_check3 = QtWidgets.QMainWindow()
    ui = Ui_data_check3()
    ui.setupUi(data_check3)
    data_check3.show()
    sys.exit(app.exec_())