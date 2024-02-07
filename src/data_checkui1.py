
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsDropShadowEffect
# from encrypt_check import Ui_encrypt_check
from data_checkui2 import Ui_data_check2
import sqlite3
class Ui_data_check1(object):
    def setupUi(self, data_check1, drug_List, each_drug, each_drug2, day_start, select_meal, updated_data2):
        self.data_check1 = data_check1
        self.drug_List = drug_List
        self.each_drug = each_drug
        self.each_drug2 = each_drug2
        self.day_start = day_start
        self.select_meal = select_meal
        self.updated_data2 = updated_data2

        data_check1.setObjectName("data_check1")
        data_check1.resize(683, 400)
        data_check1.setStyleSheet("\n"
"background-color: rgb(23, 73, 110);")
        self.centralwidget = QtWidgets.QWidget(data_check1)
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
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(100, 100, 231, 220))
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
        self.drugName_label = QtWidgets.QLabel(self.frame_2)
        self.drugName_label.setGeometry(QtCore.QRect(10, 20, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.drugName_label.setFont(font)
        self.drugName_label.setObjectName("drugName_label")
        self.drugDescribe_label = QtWidgets.QLabel(self.frame_2)
        self.drugDescribe_label.setGeometry(QtCore.QRect(10, 110, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.drugDescribe_label.setFont(font)
        self.drugDescribe_label.setObjectName("drugDescribe_label")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border-radius: 9px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.label_2)
        shadow.setBlurRadius(8)
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(0,2)
        self.label_2.setGraphicsEffect(shadow)
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setLineWidth(1)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(10, 140, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border-radius: 9px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.label_3)
        shadow.setBlurRadius(8)
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(0,2)
        self.label_3.setGraphicsEffect(shadow)
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setLineWidth(1)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(350, 100, 241, 220))
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
        self.drugAll_label = QtWidgets.QLabel(self.frame_3)
        self.drugAll_label.setGeometry(QtCore.QRect(-30, 20, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.drugAll_label.setFont(font)
        self.drugAll_label.setAlignment(QtCore.Qt.AlignCenter)
        self.drugAll_label.setObjectName("drugAll_label")
        self.drugOne_label = QtWidgets.QLabel(self.frame_3)
        self.drugOne_label.setGeometry(QtCore.QRect(-25, 110, 261, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.drugOne_label.setFont(font)
        self.drugOne_label.setAlignment(QtCore.Qt.AlignCenter)
        self.drugOne_label.setObjectName("drugOne_label")
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setGeometry(QtCore.QRect(10, 50, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("border-radius: 9px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.label_4)
        shadow.setBlurRadius(8)
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(0,2)
        self.label_4.setGraphicsEffect(shadow)
        self.label_4.setFrameShape(QtWidgets.QFrame.Box)
        self.label_4.setLineWidth(1)
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setScaledContents(False)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setGeometry(QtCore.QRect(10, 140, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("border-radius: 9px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.label_5)
        shadow.setBlurRadius(8)
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(0,2)
        self.label_5.setGraphicsEffect(shadow)
        self.label_5.setFrameShape(QtWidgets.QFrame.Box)
        self.label_5.setLineWidth(1)
        self.label_5.setTextFormat(QtCore.Qt.AutoText)
        self.label_5.setScaledContents(False)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.next_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.next_pushButton.setGeometry(QtCore.QRect(510, 330, 81, 31))
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
        data_check1.setCentralWidget(self.centralwidget)

        self.retranslateUi(data_check1)
        QtCore.QMetaObject.connectSlotsByName(data_check1)

        def close_window():
            data_check1.close()
            
        self.add_back_pushButton.clicked.connect(close_window)
        # self.next_pushButton.clicked.connect(lambda: self.open_encrypt_check(updated_data2))
        self.next_pushButton.clicked.connect(lambda: self.open_data_check2(updated_data2))

#     def open_encrypt_check(self,updated_data2):
#         self.encrypt_check_window = QtWidgets.QMainWindow()
#         self.encrypt_check_ui = Ui_encrypt_check()
#         self.encrypt_check_ui.setupUi(self.encrypt_check_window, self.drug_List, self.each_drug, self.each_drug2, self.day_start, self.select_meal, self, {'drug_id': self.drug_id, **updated_data2})
#         self.encrypt_check_window.show()
        
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


    def open_data_check2(self,updated_data2):
        self.data_check2_window = QtWidgets.QMainWindow()
        self.data_check2_ui = Ui_data_check2()
        self.data_check2_ui.setupUi(self.data_check2_window, self.drug_List, self.each_drug, self.each_drug2, self.day_start, self.select_meal, self, {'drug_id': self.drug_id, **updated_data2})
        self.data_check2_ui.set_data_info2(self.drug_id)
        self.data_check2_window.show()
        

    def set_data_info1(self, drug_id):
        self.drug_id = drug_id
        print(f"data_check1 {self.updated_data2}")

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
        self.label_2.setText(f"{self.updated_data2['drug_name']}")
        self.label_3.setText(f"{self.updated_data2['drug_description']}")
        self.label_4.setText(f"{self.updated_data2['drug_remaining']}")
        self.label_5.setText(f"{self.updated_data2['drug_eat']}")

        # self.label_6.setText(f"{self.updated_data2['drug_new']}")
        # self.label_7.setText(f"{self.updated_data2['drug_remaining_meal']}")
        # self.label_8.setText(f"{self.updated_data2['all_drug_recieve']}")
        # self.label_9.setText(f"{self.updated_data2['day_start']}")               ใช้

        #  # Clear the listWidget before adding new items
        # self.listWidget.clear()                                                  ใช้

        # # Add meal selection data to the listWidget
        # meal_data = self.updated_data2.get('meals', [])
        # print(f"Meal Data: {meal_data}")
        # self.listWidget.addItems(meal_data)

        #  # Add fetched meal data to the listWidget
        # meal_names = [item[0] for item in meal_data]                             ใช้
        # self.listWidget.addItems(meal_names)

    def closeAll(self):
        self.each_drug.closeAll()
        self.each_drug2.closeAll()
        self.select_meal.closeAll()
        self.data_check1.close()

    def retranslateUi(self, data_check1):
        _translate = QtCore.QCoreApplication.translate
        data_check1.setWindowTitle(_translate("data_check1", "ตรวจสอบความถูกต้อง"))
        self.label.setText(_translate("data_check1", "ตรวจสอบความถูกต้อง"))
        self.add_back_pushButton.setText(_translate("data_check1", "ย้อนกลับ"))
        self.drugName_label.setText(_translate("data_check1", "ชื่อยา"))
        self.drugDescribe_label.setText(_translate("data_check1", "คำอธิบายยา"))
        self.label_2.setText(_translate("data_check1", "ชื่อยา"))
        self.label_3.setText(_translate("data_check1", "คำอธิบายยา"))
        self.drugAll_label.setText(_translate("data_check1", "จำนวนยาทั้งหมดที่มี (เม็ด)"))
        self.drugOne_label.setText(_translate("data_check1", "จำนวนยาที่กินต่อ 1 มื้อ (เม็ด)"))
        self.label_4.setText(_translate("data_check1", "ยาทั้งหมด"))
        self.label_5.setText(_translate("data_check1", "ยาที่กิน"))
        self.next_pushButton.setText(_translate("data_check1", "ถัดไป"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    data_check1 = QtWidgets.QMainWindow()
    ui = Ui_data_check1()
    ui.setupUi(data_check1)
    data_check1.show()
    sys.exit(app.exec_())
