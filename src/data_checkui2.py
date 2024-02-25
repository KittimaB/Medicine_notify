from Utils import *
from UI_Generate import *
width, height = Scale_Width_Height()

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sqlite3

from data_checkui3 import Ui_data_check3

class Ui_data_check2(object):
    def setupUi(self, data_check2):
        UI_instance.Set(data_check2)
        show_widget_fullscreen(data_check2)

        self.data_check2 = data_check2
        self.drug_List = drug_list_instance.Get()
        self.each_drug = each_drug_instance.Get()
        self.each_drug2 = each_drug_2_instance.Get()
        self.day_start = day_start_instance.Get()
        self.select_meal = select_meal_instance.Get()
        self.data_check1 = data_checkui1_instance.Get()
        self.updated_data2 = drug_Update_2_instance.Get()

        data_check2.setObjectName("data_check2")
        data_check2.resize(int(683 * width), int(400 * height))
        data_check2.setStyleSheet("\n"
"background-color: rgb(23, 73, 110);")
        self.centralwidget = QtWidgets.QWidget(data_check2)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(int(0 * width), int(-60 * height), int(683 * width), int(131 * height)))
        self.frame.setStyleSheet("border-radius: 40px;\n"
"background-color: rgb(255, 255, 255);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.frame)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.frame.setGraphicsEffect(shadow)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(int(200 * width), int(70 * height), int(281 * width), int(51 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(14 * height))
        font.setBold(True)
        font.setWeight(int(75 * width))
        self.label.setFont(font)
        self.label.setStyleSheet("border-radius: 16px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(23, 73, 110);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.label)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.label.setGraphicsEffect(shadow)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setLineWidth(int(1 * width))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.img_label = QtWidgets.QLabel(self.frame)
        self.img_label.setGeometry(QtCore.QRect(int(225 * width), int(80 * height), int(33 * width), int(31 * height)))
        self.img_label.setText("")
        self.img_label.setPixmap(QtGui.QPixmap(":/icons/check.png"))
        self.img_label.setScaledContents(True)
        self.img_label.setAlignment(QtCore.Qt.AlignCenter)
        self.img_label.setObjectName("img_label")
        self.add_back_pushButton = QtWidgets.QPushButton(self.frame)
        self.add_back_pushButton.setGeometry(QtCore.QRect(int(50 * width), int(80 * height), int(81 * width), int(31 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        self.add_back_pushButton.setFont(font)
        self.add_back_pushButton.setStyleSheet("border-radius: 9px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(244, 212, 99);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.add_back_pushButton)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.add_back_pushButton.setGraphicsEffect(shadow)
        self.add_back_pushButton.setObjectName("add_back_pushButton")
        self.drugName_label = QtWidgets.QLabel(self.centralwidget)
        self.drugName_label.setGeometry(QtCore.QRect(int(50 * width), int(77 * height), int(250 * width), int(21 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        self.drugName_label.setFont(font)
        self.drugName_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.drugName_label.setObjectName("drugName_label")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(int(350 * width), int(100 * height), int(241 * width), int(220 * height)))
        self.frame_3.setStyleSheet("border-radius: 16px;\n"
"background-color: rgb(236, 236, 236);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.frame_3)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.frame_3.setGraphicsEffect(shadow)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.drugStill = QtWidgets.QLabel(self.frame_3)
        self.drugStill.setGeometry(QtCore.QRect(int(-30 * width), int(20 * height), int(251 * width), int(21 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        self.drugStill.setFont(font)
        self.drugStill.setAlignment(QtCore.Qt.AlignCenter)
        self.drugStill.setObjectName("drugStill")
        self.drugGot = QtWidgets.QLabel(self.frame_3)
        self.drugGot.setGeometry(QtCore.QRect(int(-25 * width), int(110 * height), int(261 * width), int(21 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        self.drugGot.setFont(font)
        self.drugGot.setAlignment(QtCore.Qt.AlignCenter)
        self.drugGot.setObjectName("drugGot")
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        self.label_7.setGeometry(QtCore.QRect(int(10 * width), int(50 * height), int(221 * width), int(41 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        font.setBold(False)
        font.setWeight(int(25 * width))
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("border-radius: 9px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.label_7)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.label_7.setGraphicsEffect(shadow)
        self.label_7.setFrameShape(QtWidgets.QFrame.Box)
        self.label_7.setLineWidth(int(1 * width))
        self.label_7.setTextFormat(QtCore.Qt.AutoText)
        self.label_7.setScaledContents(False)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame_3)
        self.label_8.setGeometry(QtCore.QRect(int(10 * width), int(140 * height), int(221 * width), int(41 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        font.setBold(False)
        font.setWeight(int(25 * width))
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("border-radius: 9px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.label_8)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.label_8.setGraphicsEffect(shadow)
        self.label_8.setFrameShape(QtWidgets.QFrame.Box)
        self.label_8.setLineWidth(int(1 * width))
        self.label_8.setTextFormat(QtCore.Qt.AutoText)
        self.label_8.setScaledContents(False)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName("label_8")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(int(100 * width), int(100 * height), int(231 * width), int(220 * height)))
        self.frame_2.setStyleSheet("border-radius: 16px;\n"
"background-color: rgb(236, 236, 236);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.frame_2)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.frame_2.setGraphicsEffect(shadow)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.drugSize = QtWidgets.QLabel(self.frame_2)
        self.drugSize.setGeometry(QtCore.QRect(int(10 * width), int(20 * height), int(191 * width), int(21 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        self.drugSize.setFont(font)
        self.drugSize.setObjectName("drugSize")
        self.drugNew = QtWidgets.QLabel(self.frame_2)
        self.drugNew.setGeometry(QtCore.QRect(int(10 * width), int(110 * height), int(211 * width), int(21 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        self.drugNew.setFont(font)
        self.drugNew.setObjectName("drugNew")
        self.size_label = QtWidgets.QLabel(self.frame_2)
        self.size_label.setGeometry(QtCore.QRect(int(10 * width), int(50 * height), int(211 * width), int(41 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        font.setBold(False)
        font.setWeight(int(25 * width))
        self.size_label.setFont(font)
        self.size_label.setStyleSheet("border-radius: 9px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.size_label)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.size_label.setGraphicsEffect(shadow)
        self.size_label.setFrameShape(QtWidgets.QFrame.Box)
        self.size_label.setLineWidth(int(1 * width))
        self.size_label.setTextFormat(QtCore.Qt.AutoText)
        self.size_label.setScaledContents(False)
        self.size_label.setAlignment(QtCore.Qt.AlignCenter)
        self.size_label.setWordWrap(True)
        self.size_label.setObjectName("size_label")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(int(10 * width), int(140 * height), int(211 * width), int(41 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        font.setBold(False)
        font.setWeight(int(25 * width))
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("border-radius: 9px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.label_6)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.label_6.setGraphicsEffect(shadow)
        self.label_6.setFrameShape(QtWidgets.QFrame.Box)
        self.label_6.setLineWidth(int(1 * width))
        self.label_6.setTextFormat(QtCore.Qt.AutoText)
        self.label_6.setScaledContents(False)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.next_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.next_pushButton.setGeometry(QtCore.QRect(int(510 * width), int(330 * height), int(81 * width), int(31 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        self.next_pushButton.setFont(font)
        self.next_pushButton.setStyleSheet("border-radius: 9px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(227, 151, 61);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.next_pushButton)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.next_pushButton.setGraphicsEffect(shadow)
        self.next_pushButton.setObjectName("next_pushButton")
        data_check2.setCentralWidget(self.centralwidget)

        self.retranslateUi(data_check2)
        self.set_data_info2(drug_ID_instance.Get())
        QtCore.QMetaObject.connectSlotsByName(data_check2)
            
        self.add_back_pushButton.clicked.connect(self.backpage)
        self.next_pushButton.clicked.connect(lambda: self.open_data_check3())
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

    def backpage(self):
        from data_checkui1 import Ui_data_check1
        backpage_form = UI_Genarate()
        backpage_form.widgetSet(UI_instance.Get(), Ui_data_check1)

    def open_data_check3(self):
        drug_Update_2_instance.Set({'drug_id': self.drug_id, **self.updated_data2})
        data_checkui2_instance.Set(self)
        data_checkui1_instance.Set(self.data_check1)
        select_meal_instance.Set(self.select_meal)
        day_start_instance.Set(self.day_start)
        each_drug_2_instance.Set(self.each_drug2)
        each_drug_2_instance.Set(self.each_drug)
        drug_list_instance.Set(self.drug_List)

        data_check3_form = UI_Genarate()
        data_check3_form.widgetSet(UI_instance.Get(), Ui_data_check3)
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
        self.drugNew.setText(_translate("data_check2", "จำนวนยาใหม่ที่ได้รับมา (เม็ด)"))
        self.size_label.setText(_translate("data_check2", "ขนาดเม็ดยา"))
        self.label_6.setText(_translate("data_check2", "จำนวนยาใหม่ที่ได้รับมา"))
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
