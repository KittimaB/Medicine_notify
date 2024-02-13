from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsDropShadowEffect
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QStyle

from each_drug2 import Ui_each_drug2

import sqlite3

class CustomMessageBox(QMessageBox):
    def __init__(self, parent=None):
        super(CustomMessageBox, self).__init__(parent)
        self.setStyleSheet("""
            QMessageBox {
                background-color: white;
                border: 2px solid black;
            }
            QLabel {
                color: black;
            }
        """)

class Ui_each_drug(object):   
    def setupUi(self, each_drug, drug_List):
        self.each_drug = each_drug
        self.drug_List = drug_List
        
        each_drug.setObjectName("each_drug")
        each_drug.resize(683, 400)
        each_drug.setStyleSheet("\n"
"background-color: rgb(23, 73, 110);")
        self.centralwidget = QtWidgets.QWidget(each_drug)
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
        self.img_label.setGeometry(QtCore.QRect(238, 80, 31, 31))
        self.img_label.setText("")
        self.img_label.setPixmap(QtGui.QPixmap(":/icons/each_icon.png"))
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
        self.delete_pushButton = QtWidgets.QPushButton(self.frame)
        self.delete_pushButton.setGeometry(QtCore.QRect(550, 80, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.delete_pushButton.setFont(font)
        self.delete_pushButton.setStyleSheet("border-radius: 9px;\n"
"background-color: rgb(171, 57, 57);\n"
"color: rgb(255, 255, 255);\n"
"")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.delete_pushButton)
        shadow.setBlurRadius(8)
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(0,2)
        self.delete_pushButton.setGraphicsEffect(shadow)
        self.delete_pushButton.setObjectName("delete_pushButton")
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

        self.label_2 = QtWidgets.QTextEdit(self.frame_2)
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
        self.label_2.setCurrentCharFormat(QtGui.QTextCharFormat())
        
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QTextEdit(self.frame_2)
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
        self.label_3.setCurrentCharFormat(QtGui.QTextCharFormat())
        
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.label_3.setObjectName("label_3")

        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(350, 100, 241, 220))
        self.frame_3.setStyleSheet("border-radius: 16px;\n"
"background-color: rgb(236, 236, 236);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.label_3)
        shadow.setBlurRadius(8)
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(0,2)
        self.label_3.setGraphicsEffect(shadow)
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

        self.label_4 = QtWidgets.QTextEdit(self.frame_3)
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
        self.label_4.setCurrentCharFormat(QtGui.QTextCharFormat())
        
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QTextEdit(self.frame_3)
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
        self.label_5.setCurrentCharFormat(QtGui.QTextCharFormat())
        
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
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
        each_drug.setCentralWidget(self.centralwidget)

        

        self.retranslateUi(each_drug)
        QtCore.QMetaObject.connectSlotsByName(each_drug)

        def close_window():
            each_drug.close()

        self.add_back_pushButton.clicked.connect(close_window)

        
        # self.next_pushButton.clicked.connect(self.open_each_drug2)

        def delete_drug():
            drug_name = self.label_2.toPlainText()  # รับชื่อยาจาก Label

            # Use the custom message box
            QMessageBox = CustomMessageBox()
        
            reply = QMessageBox.question(each_drug, 'ลบยา', f'คุณต้องการลบยา "{drug_name}" ใช่หรือไม่?',
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if reply == QtWidgets.QMessageBox.Yes:
                connection = sqlite3.connect("medicine.db")
                cursor = connection.cursor()
                cursor.execute("DELETE FROM Drug WHERE drug_name = ?", (drug_name,))
                connection.commit()
                connection.close()
                each_drug.close()  # ปิดหน้าต่างหลังจากลบเสร็จ
        
        self.delete_pushButton.clicked.connect(delete_drug)

        def save_changes():
            # ตรวจสอบข้อมูลที่ถูกแก้ไขและบันทึกลงฐานข้อมูลหรือตัวแปรที่เหมาะสม
            updated_data = {} 
            updated_data['drug_name'] = self.label_2.toPlainText()
            updated_data['drug_description'] = self.label_3.toPlainText()
            updated_data['drug_remaining'] = self.label_4.toPlainText()
            updated_data['drug_eat'] = self.label_5.toPlainText()

            # ส่งข้อมูลที่ถูกแก้ไขไปยังหน้า each_drug2
            self.open_each_drug2(updated_data)
        
        self.next_pushButton.clicked.connect(save_changes)

        # Set up button press and release styling
        self.add_back_pushButton.pressed.connect(lambda: self.set_button_pressed_style(self.add_back_pushButton))
        self.add_back_pushButton.released.connect(lambda: self.set_button_released_style(self.add_back_pushButton))

        self.delete_pushButton.pressed.connect(lambda: self.set_button_pressed_style(self.delete_pushButton))
        self.delete_pushButton.released.connect(lambda: self.set_button_released_style(self.delete_pushButton))

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
        
    def closeAll(self):
        self.each_drug.close()  # ปิดหน้าต่างที่เป็นส่วนสมาชิกของ Ui_med_pack2

    def open_each_drug2(self,updated_data):
        self.each_drug2_window = QtWidgets.QMainWindow()
        self.each_drug2_ui = Ui_each_drug2()
        self.each_drug2_ui.setupUi(self.each_drug2_window, self.drug_List, self,updated_data)
        print(f"each_drug {updated_data}")
        self.each_drug2_ui.set_drug2_info(self.drug_id)
        self.each_drug2_window.show()

    def set_drug_info(self, drug_name):
        connection = sqlite3.connect("medicine.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Drug WHERE drug_name = ?", (drug_name,))
        drug_info = cursor.fetchone()
        connection.close()

        if drug_info:
            self.drug_id = drug_info[0]
            # drug_info[1] is drug_name
            self.label_2.setPlainText(drug_info[1])
            # drug_info[2] is drug_description
            self.label_3.setPlainText(drug_info[2])
            # drug_info[3] is drug_remaining
            self.label_4.setPlainText(str(drug_info[3]))  # Use str() to convert to string
            # drug_info[4] is drug_eat
            self.label_5.setPlainText(str(drug_info[8]))  # Use str() to convert to string


    def retranslateUi(self, each_drug):
        _translate = QtCore.QCoreApplication.translate
        each_drug.setWindowTitle(_translate("each_drug", "ยาแต่ละตัว"))
        self.label.setText(_translate("each_drug", "ชื่อยา"))
        self.add_back_pushButton.setText(_translate("each_drug", "ย้อนกลับ"))
        #self.edit_pushButton.setText(_translate("each_drug", "แก้ไข"))
        self.delete_pushButton.setText(_translate("each_drug", "ลบ"))
        self.drugName_label.setText(_translate("each_drug", "ชื่อยา"))
        self.drugDescribe_label.setText(_translate("each_drug", "คำอธิบายยา"))
        self.drugOne_label.setText(_translate("each_drug", "จำนวนยาที่กินต่อ 1 มื้อ (เม็ด)"))
        self.drugAll_label.setText(_translate("each_drug", "จำนวนยาทั้งหมดที่มี (เม็ด)"))
        self.next_pushButton.setText(_translate("each_drug", "ถัดไป"))
        self.label_2.setText(_translate("each_drug", "ชื่อยา"))
        self.label_3.setText(_translate("each_drug", "คำอธิบายยา"))
        self.label_4.setText(_translate("each_drug", "ยาทั้งหมด"))
        self.label_5.setText(_translate("each_drug", "ยาที่กิน"))
import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    each_drug = QtWidgets.QMainWindow()
    ui = Ui_each_drug()
    ui.setupUi(each_drug)
    each_drug.show()
    sys.exit(app.exec_())

