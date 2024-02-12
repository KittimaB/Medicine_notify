
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsDropShadowEffect
from data_checkui3 import Ui_data_check3
import sqlite3

class Ui_data_check2(object):
    def setupUi(self, data_check2,drug_List, each_drug, each_drug2, day_start, select_meal, data_check1, updated_data2):

        self.data_check2 = data_check2
        self.drug_List = drug_List
        self.each_drug = each_drug
        self.each_drug2 = each_drug2
        self.day_start = day_start
        self.select_meal = select_meal
        self.data_check1 = data_check1
        self.updated_data2 = updated_data2

        data_check2.setObjectName("data_check2")
        data_check2.resize(683, 400)
        data_check2.setStyleSheet("\n"
"background-color: rgb(23, 73, 110);")
        self.centralwidget = QtWidgets.QWidget(data_check2)
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
        self.img_label.setGeometry(QtCore.QRect(225, 80, 33, 31))
        self.img_label.setText("")
        self.img_label.setPixmap(QtGui.QPixmap(":/icons/check.png"))
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
        self.drugName_label = QtWidgets.QLabel(self.centralwidget)
        self.drugName_label.setGeometry(QtCore.QRect(50, 77, 250, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.drugName_label.setFont(font)
        self.drugName_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.drugName_label.setObjectName("drugName_label")
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
        self.drugStill = QtWidgets.QLabel(self.frame_3)
        self.drugStill.setGeometry(QtCore.QRect(-30, 20, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.drugStill.setFont(font)
        self.drugStill.setAlignment(QtCore.Qt.AlignCenter)
        self.drugStill.setObjectName("drugStill")
        self.drugGot = QtWidgets.QLabel(self.frame_3)
        self.drugGot.setGeometry(QtCore.QRect(-25, 110, 261, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.drugGot.setFont(font)
        self.drugGot.setAlignment(QtCore.Qt.AlignCenter)
        self.drugGot.setObjectName("drugGot")
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        self.label_7.setGeometry(QtCore.QRect(10, 50, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("border-radius: 9px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.label_7)
        shadow.setBlurRadius(8)
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(0,2)
        self.label_7.setGraphicsEffect(shadow)
        self.label_7.setFrameShape(QtWidgets.QFrame.Box)
        self.label_7.setLineWidth(1)
        self.label_7.setTextFormat(QtCore.Qt.AutoText)
        self.label_7.setScaledContents(False)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame_3)
        self.label_8.setGeometry(QtCore.QRect(10, 140, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("border-radius: 9px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.label_8)
        shadow.setBlurRadius(8)
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(0,2)
        self.label_8.setGraphicsEffect(shadow)
        self.label_8.setFrameShape(QtWidgets.QFrame.Box)
        self.label_8.setLineWidth(1)
        self.label_8.setTextFormat(QtCore.Qt.AutoText)
        self.label_8.setScaledContents(False)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName("label_8")
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
        self.drugSize = QtWidgets.QLabel(self.frame_2)
        self.drugSize.setGeometry(QtCore.QRect(10, 20, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.drugSize.setFont(font)
        self.drugSize.setObjectName("drugSize")
        self.drugNew = QtWidgets.QLabel(self.frame_2)
        self.drugNew.setGeometry(QtCore.QRect(10, 110, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.drugNew.setFont(font)
        self.drugNew.setObjectName("drugNew")
        self.size_label = QtWidgets.QLabel(self.frame_2)
        self.size_label.setGeometry(QtCore.QRect(10, 50, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.size_label.setFont(font)
        self.size_label.setStyleSheet("border-radius: 9px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.size_label)
        shadow.setBlurRadius(8)
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(0,2)
        self.size_label.setGraphicsEffect(shadow)
        self.size_label.setFrameShape(QtWidgets.QFrame.Box)
        self.size_label.setLineWidth(1)
        self.size_label.setTextFormat(QtCore.Qt.AutoText)
        self.size_label.setScaledContents(False)
        self.size_label.setAlignment(QtCore.Qt.AlignCenter)
        self.size_label.setWordWrap(True)
        self.size_label.setObjectName("size_label")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(10, 140, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("border-radius: 9px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.label_6)
        shadow.setBlurRadius(8)
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(0,2)
        self.label_6.setGraphicsEffect(shadow)
        self.label_6.setFrameShape(QtWidgets.QFrame.Box)
        self.label_6.setLineWidth(1)
        self.label_6.setTextFormat(QtCore.Qt.AutoText)
        self.label_6.setScaledContents(False)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
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
        data_check2.setCentralWidget(self.centralwidget)

        self.retranslateUi(data_check2)
        QtCore.QMetaObject.connectSlotsByName(data_check2)

        def close_window():
            data_check2.close()
            
        self.add_back_pushButton.clicked.connect(close_window)
        self.next_pushButton.clicked.connect(lambda: self.open_data_check3(updated_data2))
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


    def open_data_check3(self,updated_data2):
        self.data_check3_window = QtWidgets.QMainWindow()
        self.data_check3_ui = Ui_data_check3()
        self.data_check3_ui.setupUi(self.data_check3_window, self.drug_List, self.each_drug, self.each_drug2, self.day_start, self.select_meal, self.data_check1, self, {'drug_id': self.drug_id, **updated_data2})
        self.data_check3_ui.set_data_info3(self.drug_id)
        self.data_check3_window.show()
        

    def set_data_info2(self, drug_id):
        self.drug_id = drug_id
        print(f"data_check2 {self.updated_data2}")
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
       

        # Set the data in the labels and listWidget
        self.size_label.setText(f"{self.updated_data2['drug_size']}")
        self.label_6.setText(f"{self.updated_data2['drug_new']}")
        self.label_7.setText(f"{self.updated_data2['drug_remaining_meal']}")
        self.label_8.setText(f"{self.updated_data2['all_drug_recieve']}")

    def closeAll(self):
        self.each_drug.closeAll()
        self.each_drug2.closeAll()
        self.select_meal.closeAll()
        self.data_check1.closeAll()
        self.data_check2.close()

    def retranslateUi(self, data_check2):
        _translate = QtCore.QCoreApplication.translate
        data_check2.setWindowTitle(_translate("data_check2", "ตรวจสอบความถูกต้อง"))
        self.label.setText(_translate("data_check2", "        ตรวจสอบความถูกต้อง  "))
        self.add_back_pushButton.setText(_translate("data_check2", "ย้อนกลับ"))
        self.drugName_label.setText(_translate("data_check2", "ชื่อยา"))
        self.drugStill.setText(_translate("data_check2", "จำนวนมื้อยาคงเหลือ (มื้อ)"))
        self.drugGot.setText(_translate("data_check2", "จำนวนยาที่ได้รับมาแล้ว (เม็ด)"))
        self.label_7.setText(_translate("data_check2", "ยาคงเหลือ"))
        self.label_8.setText(_translate("data_check2", "ยาที่ได้รับมาแล้ว"))
        self.drugSize.setText(_translate("data_check2", "ขนาดเม็ดยา (มิลลิเมตร)"))
        self.drugNew.setText(_translate("data_check2", "จำนวนยาที่ได้รับมาใหม่ (เม็ด)"))
        self.size_label.setText(_translate("data_check2", ""))
        self.label_6.setText(_translate("data_check2", "ยาที่ได้รับมาใหม่"))
        self.next_pushButton.setText(_translate("data_check2", "ถัดไป"))

import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    data_check2 = QtWidgets.QMainWindow()
    ui = Ui_data_check2()
    ui.setupUi(data_check2)
    data_check2.show()
    sys.exit(app.exec_())
