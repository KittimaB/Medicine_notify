from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
# from each_drug import Ui_each_drug
from PyQt5.QtWidgets import QCalendarWidget, QMessageBox
# from select_meal import Ui_select_meal
import sqlite3
from PyQt5.QtCore import QTimer, QLocale
import sys

class Ui_drug_List(object):
    def __init__(self):
        self.drug_List = None  # Initialize med_pack as an instance variable
        
    def setupUi(self, drug_List):
        self.drug_List = drug_List
        drug_List.setObjectName("drug_List")
        drug_List.resize(531, 401)
        drug_List.setStyleSheet("background-color: rgb(217, 244, 255)")
        self.centralwidget = QtWidgets.QWidget(drug_List)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-10, 80, 551, 20))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 20, 141, 51))
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
        self.add_back_pushButton.setGeometry(QtCore.QRect(30, 40, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add_back_pushButton.setFont(font)
        self.add_back_pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(166, 0, 0)")
        self.add_back_pushButton.setObjectName("add_back_pushButton")
        self.add_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.add_pushButton.setGeometry(QtCore.QRect(410, 40, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add_pushButton.setFont(font)
        self.add_pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(81, 179, 85);")
        self.add_pushButton.setObjectName("add_pushButton")
        drug_List.setCentralWidget(self.centralwidget)

        self.retranslateUi(drug_List)
        QtCore.QMetaObject.connectSlotsByName(drug_List)

        self.drug_list_widget = QtWidgets.QListWidget(self.centralwidget)
        self.drug_list_widget.setGeometry(QtCore.QRect(20, 120, 491, 261))
        self.update_drug_list()  # เรียกใช้ฟังก์ชันเพื่อแสดงรายการยาในคลังยา

        # Connect the itemClicked signal to handle_drug_item_click method
        self.drug_list_widget.itemClicked.connect(self.handle_drug_item_click) #คลิกชื่อยาแล้วเปิดหน้าeach_drug

        def close_window():
            drug_List.close()
            
        # self.add_back_pushButton.clicked.connect(self.open_drug_list_again)
        self.add_back_pushButton.clicked.connect(close_window)
            
        self.add_pushButton.clicked.connect(self.open_add_drug)

    # def open_add_drug(self):
    #         self.add_drug_window = QtWidgets.QMainWindow()
    #         self.add_drug_ui = Ui_Add_drug()
    #         self.add_drug_ui.setupUi(self.add_drug_window)
    #         self.add_drug_window.show()
    #         # if self.add_drug_window.close():
    #         #     self.update_drug_list()

    def handle_drug_item_click(self, item):
        # Get the text of the clicked item (drug name)
        drug_name = item.text()

        # Open the each_drug window with the selected drug
        self.each_drug_window = QtWidgets.QMainWindow()             ###
        self.each_drug_ui = Ui_each_drug()                          ###
        
        self.each_drug_ui.setupUi(self.each_drug_window, self)      ###
        
        # Set drug info for the each_drug window
        self.each_drug_ui.set_drug_info(drug_name)

        # Pass the drug name to the each_drug window
        self.each_drug_ui.label.setText(drug_name)
        self.each_drug_ui.showMedEach(self.each_drug_window)       ###
        self.each_drug_window.show()                     ###
        
    ###################################################################################################################################
        
    #     # ปุ่มย้อนกลับ

    #     self.pack_back_pushButton.clicked.connect(self.closeMedPack)
        
    #     # ปุ่มถัดไป
        
    #     # self.next_pushButton.clicked.connect(self.showMedPack2)
        
    # # def showMedPack2(self):     # ฟังก์ชันไปหน้าถัดไป
    # #     # self.med_pack2 = QtWidgets.QMainWindow()
    # #     # self.ui2 = Ui_med_pack2()
    # #     # self.ui2.setupUi(self.med_pack2, self)
    # #     self.ui2.showMedPack(self.med_pack2)
    # #     self.med_pack2.show()
        
    # def closeMedPack(self):     # ฟังก์ชันย้อนกลับ
    #     self.med_pack.close()
        
    ###################################################################################################################################
        
        # self.select_meal_window = QtWidgets.QMainWindow()
        # self.select_meal_ui = Ui_select_meal()
        # self.select_meal_ui.setupUi(self.select_meal_window)
        
        # # Set drug info for the select_meal window
        # self.select_meal_ui.set_drug_info(drug_name)

        # Pass the drug name to the select_meal window
        # self.select_meal_ui.label.setText(drug_name)
        #self.select_meal_window.show()
        
    def closeAll(self):
        self.drug_List.close()

    def open_add_drug(self):
        self.add_drug_window = QtWidgets.QMainWindow()
        self.add_drug_ui = Ui_Add_drug()
        self.add_drug_ui.setupUi(self.add_drug_window, self)
        self.add_drug_window.show()

    def update_drug_list(self):
        connection = sqlite3.connect("medicine.db")
        cursor = connection.cursor()
        cursor.execute("SELECT drug_name FROM Drug")
        drugs = cursor.fetchall()
        connection.close()

        # Clear existing items in the drug list widget
        self.drug_list_widget.clear()

        # Add new items to the drug list widget
        for drug in drugs:
            self.drug_list_widget.addItem(drug[0])
            
    def retranslateUi(self, drug_List):
        _translate = QtCore.QCoreApplication.translate
        drug_List.setWindowTitle(_translate("drug_List", "คลังยา"))
        self.label.setText(_translate("drug_List", "คลังยา"))
        self.add_back_pushButton.setText(_translate("drug_List", "ย้อนกลับ"))
        self.add_pushButton.setText(_translate("drug_List", "เพิ่มยา"))
        
############################################################################################################

class Ui_each_drug(object):   
    def setupUi(self, each_drug, drug_List):
        self.drug_List = drug_List
        
        each_drug.setObjectName("each_drug")
        each_drug.resize(531, 401)
        each_drug.setStyleSheet("background-color: rgb(217, 244, 255)")
        self.centralwidget = QtWidgets.QWidget(each_drug)
        self.centralwidget.setObjectName("centralwidget")
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
        self.add_back_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.add_back_pushButton.setGeometry(QtCore.QRect(30, 40, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add_back_pushButton.setFont(font)
        self.add_back_pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(166, 0, 0)")
        self.add_back_pushButton.setObjectName("add_back_pushButton")
#         self.edit_pushButton = QtWidgets.QPushButton(self.centralwidget)
#         self.edit_pushButton.setGeometry(QtCore.QRect(380, 40, 61, 31))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         self.edit_pushButton.setFont(font)
#         self.edit_pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
# "background-color: rgb(85, 170, 127);")
#         self.edit_pushButton.setObjectName("edit_pushButton")
        self.delete_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.delete_pushButton.setGeometry(QtCore.QRect(430, 40, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.delete_pushButton.setFont(font)
        self.delete_pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.delete_pushButton.setObjectName("delete_pushButton")
        self.drugName_label = QtWidgets.QLabel(self.centralwidget)
        self.drugName_label.setGeometry(QtCore.QRect(20, 120, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.drugName_label.setFont(font)
        self.drugName_label.setObjectName("drugName_label")
        self.drugDescribe_label = QtWidgets.QLabel(self.centralwidget)
        self.drugDescribe_label.setGeometry(QtCore.QRect(20, 150, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.drugDescribe_label.setFont(font)
        self.drugDescribe_label.setObjectName("drugDescribe_label")
        self.drugOne_label = QtWidgets.QLabel(self.centralwidget)
        self.drugOne_label.setGeometry(QtCore.QRect(20, 210, 261, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.drugOne_label.setFont(font)
        self.drugOne_label.setObjectName("drugOne_label")
        self.drugAll_label = QtWidgets.QLabel(self.centralwidget)
        self.drugAll_label.setGeometry(QtCore.QRect(20, 180, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.drugAll_label.setFont(font)
        self.drugAll_label.setObjectName("drugAll_label")
        self.next_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.next_pushButton.setGeometry(QtCore.QRect(410, 280, 85, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.next_pushButton.setFont(font)
        self.next_pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.next_pushButton.setObjectName("next_pushButton")
        self.label_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 120, 351, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setLineWidth(1)
        self.label_2.setCurrentCharFormat(QtGui.QTextCharFormat())
        
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(140, 150, 301, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setLineWidth(1)
        self.label_3.setCurrentCharFormat(QtGui.QTextCharFormat())
        
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(250, 180, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_4.setFrameShape(QtWidgets.QFrame.Box)
        self.label_4.setLineWidth(1)
        self.label_4.setCurrentCharFormat(QtGui.QTextCharFormat())
        
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QTextEdit(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(270, 210, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_5.setFrameShape(QtWidgets.QFrame.Box)
        self.label_5.setLineWidth(1)
        self.label_5.setCurrentCharFormat(QtGui.QTextCharFormat())
        
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.label_5.setObjectName("label_5")
        each_drug.setCentralWidget(self.centralwidget)

        self.retranslateUi(each_drug)
        QtCore.QMetaObject.connectSlotsByName(each_drug)

        def close_window():
            each_drug.close()

        self.add_back_pushButton.clicked.connect(close_window)

        
        self.next_pushButton.clicked.connect(self.open_each_drug2)

        def delete_drug():
            drug_name = self.label_2.text()  # รับชื่อยาจาก Label
            reply = QtWidgets.QMessageBox.question(each_drug, 'ลบยา', f'คุณต้องการลบยา "{drug_name}" ใช่หรือไม่?',
                                                   QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
            if reply == QtWidgets.QMessageBox.Yes:
                connection = sqlite3.connect("medicine.db")
                cursor = connection.cursor()
                cursor.execute("DELETE FROM Drug WHERE drug_name = ?", (drug_name,))
                connection.commit()
                connection.close()
                each_drug.close()  # ปิดหน้าต่างหลังจากลบเสร็จ
        
        self.delete_pushButton.clicked.connect(delete_drug)
        
    ###################################################################################################################################
        
    def closeAll(self):
        self.each_drug.close()  # ปิดหน้าต่างที่เป็นส่วนสมาชิกของ Ui_med_pack2
        
    def showMedEach(self, each_drug):
        self.each_drug = each_drug  # บันทึกตัวแปรเข้าสมาชิกของคลาส
        
        
    ###################################################################################################################################

    def open_each_drug2(self):
        #drug_name = self.label_2.text()
        self.each_drug2_window = QtWidgets.QMainWindow()
        self.each_drug2_ui = Ui_each_drug2()
        self.each_drug2_ui.setupUi(self.each_drug2_window, self.drug_List, self)
        self.each_drug2_ui.showMedEach2(self.each_drug2_window)
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
            # drug_info[3] is drug_amount
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
        self.drugName_label.setText(_translate("each_drug", "ชื่อยา : "))
        self.drugDescribe_label.setText(_translate("each_drug", "คำอธิบายยา : "))
        self.drugOne_label.setText(_translate("each_drug", "จำนวนยาที่กินต่อ 1 มื้อ (เม็ด) : "))
        self.drugAll_label.setText(_translate("each_drug", "จำนวนยาทั้งหมดที่มี (เม็ด) :"))
        self.next_pushButton.setText(_translate("each_drug", "ถัดไป"))
        self.label_2.setText(_translate("each_drug", "ชื่อยา"))
        self.label_3.setText(_translate("each_drug", "คำอธิบายยา"))
        self.label_4.setText(_translate("each_drug", "ยาทั้งหมด"))
        self.label_5.setText(_translate("each_drug", "ยาที่กิน"))
        
############################################################################################################

class Ui_each_drug2(object):
    def setupUi(self, each_drug2, drug_List, each_drug):
        self.drug_List = drug_List
        self.each_drug = each_drug
        
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
        # self.delete_pushButton = QtWidgets.QPushButton(self.centralwidget)
        # self.delete_pushButton.setGeometry(QtCore.QRect(430, 40, 71, 31))
        # font = QtGui.QFont()
        # font.setPointSize(12)
        # self.delete_pushButton.setFont(font)
        # self.delete_pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        # self.delete_pushButton.setObjectName("delete_pushButton")
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

        self.next_pushButton.clicked.connect(self.open_day_start)
        
    def showMedEach2(self, each_drug2):
        self.each_drug2 = each_drug2

    def open_day_start(self):
        self.day_start_window = QtWidgets.QMainWindow()
        self.day_start_ui = Ui_day_start()
        self.day_start_ui.setupUi(self.day_start_window, self.drug_List, self.each_drug, self)
        self.day_start_ui.set_day_info(self.drug_id)
        self.day_start_window.show()

    def set_drug2_info(self, drug_id):
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
            if drug_new is not None:
                drug_remaining_with_new = drug_remaining + drug_new
            else:
                drug_remaining_with_new = drug_remaining

            # Update the modified values back to the list
            drug_info_list[9] = drug_remaining_with_new

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
        
##################################################################################################################################

class Ui_day_start(object):
    def setupUi(self, day_start, drug_List, each_drug, each_drug2):
        self.day_start = day_start
        self.drug_List = drug_List
        self.each_drug = each_drug
        self.each_drug2 = each_drug2
        
        day_start.setObjectName("day_start")
        day_start.resize(531, 401)
        day_start.setStyleSheet("background-color: rgb(217, 244, 255)")
        self.centralwidget = QtWidgets.QWidget(day_start)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 20, 320, 51))
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
        self.add_back_pushButton.setGeometry(QtCore.QRect(30, 40, 71, 31))
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
        self.next_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.next_pushButton.setGeometry(QtCore.QRect(420, 320, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.next_pushButton.setFont(font)
        self.next_pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.next_pushButton.setObjectName("next_pushButton")
        day_start.setCentralWidget(self.centralwidget)

        self.calendar_widget = QCalendarWidget(self.centralwidget)
        self.calendar_widget.setGeometry(QtCore.QRect(125, 105, 271, 191))
        self.calendar_widget.setObjectName("calendarWidget")

        self.label_date = QtWidgets.QLabel(self.centralwidget)
        self.label_date.setGeometry(QtCore.QRect(125, 320, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_date.setFont(font)
        self.label_date.setAlignment(QtCore.Qt.AlignCenter)
        self.label_date.setObjectName("label_date")

        self.calendar_widget.selectionChanged.connect(self.update_selected_date)

        self.retranslateUi(day_start)
        QtCore.QMetaObject.connectSlotsByName(day_start)

        def close_window():
            day_start.close()

        self.add_back_pushButton.clicked.connect(close_window)

        self.next_pushButton.clicked.connect(self.open_select_meal)

        # Initialize variable to track if the date has been selected
        self.date_selected = False

    def update_selected_date(self):
        english_locale = QLocale(QLocale.English)
        QLocale.setDefault(english_locale)
        selected_date = self.calendar_widget.selectedDate()
        
        # Convert the selected date to the desired format
        formatted_date = selected_date.toString("dd-MM-yyyy")
        # Set the label text to the formatted date
        self.label_date.setText(formatted_date)
        # Enable further date changes
        self.calendar_widget.setEnabled(True)
        # Update the variable to indicate that the date has been selected
        self.date_selected = True

    def set_day_info(self, drug_id):
        self.drug_id = drug_id

    def open_select_meal(self):
        if self.date_selected:
            # Save the selected date to the database
            selected_date = self.calendar_widget.selectedDate().toString("yyyy-MM-dd")
            self.save_date_to_database(selected_date, self.drug_id)

            # Open the select_meal window
            self.select_meal_window = QtWidgets.QMainWindow()
            self.select_meal_ui = Ui_select_meal()
            self.select_meal_ui.setupUi(self.select_meal_window, self.drug_List, self.each_drug, self.each_drug2, self)
            self.select_meal_ui.set_meal_info(self.drug_id)
            self.select_meal_window.show()

            # Disable the calendar after proceeding
            self.calendar_widget.setEnabled(False)
        else:
            QMessageBox.warning(self.centralwidget, "เลือกวัน", "กรุณาเลือกวันก่อนดำเนินการถัดไป")
            
    def closeAll(self):
        self.each_drug.closeAll()
        self.each_drug2.closeAll()
        self.day_start.close()  # ปิดหน้าต่างที่เป็นส่วนสมาชิกของ Ui_med_pack2
    
    def save_date_to_database(self, selected_date, drug_id):
        # Connect to SQLite database
        connection = sqlite3.connect("medicine.db")
        cursor = connection.cursor()

        # Check if a record already exists
        cursor.execute("SELECT * FROM Drug")
        existing_record = cursor.fetchall()
        # print(existing_record)

        if existing_record:
            # Update the existing record
            cursor.execute("UPDATE Drug SET day_start = ? WHERE drug_id = ?", (selected_date, drug_id))
        
        # Commit changes and close connection
        connection.commit()
        connection.close()

    def retranslateUi(self, day_start):
        _translate = QtCore.QCoreApplication.translate
        day_start.setWindowTitle(_translate("day_start", "วันที่เริ่มรับประทานยา"))
        self.label.setText(_translate("day_start", "วันที่เริ่มรับประทานยา"))
        self.add_back_pushButton.setText(_translate("day_start", "ย้อนกลับ"))
        self.next_pushButton.setText(_translate("day_start", "ถัดไป"))
        self.label_date.setText("เลือกวันที่เริ่มรับประทานยา")
        
##################################################################################################################################
        
class Ui_select_meal(object):

    def setupUi(self, select_meal, drug_List, each_drug, each_drug2, day_start):
        self.select_meal = select_meal
        self.drug_List = drug_List
        self.each_drug = each_drug
        self.each_drug2 = each_drug2
        self.day_start = day_start
        
        select_meal.setObjectName("select_meal")
        select_meal.resize(531, 401)
        select_meal.setStyleSheet("background-color: rgb(217, 244, 255)")
        self.centralwidget = QtWidgets.QWidget(select_meal)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-10, 90, 1201, 16))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.meal_label = QtWidgets.QLabel(self.centralwidget)
        self.meal_label.setGeometry(QtCore.QRect(170, 20, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.meal_label.setFont(font)
        self.meal_label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.meal_label.setFrameShape(QtWidgets.QFrame.Box)
        self.meal_label.setLineWidth(1)
        self.meal_label.setTextFormat(QtCore.Qt.AutoText)
        self.meal_label.setScaledContents(False)
        self.meal_label.setAlignment(QtCore.Qt.AlignCenter)
        self.meal_label.setWordWrap(True)
        self.meal_label.setObjectName("meal_label")
        self.back_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.back_pushButton.setGeometry(QtCore.QRect(30, 40, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.back_pushButton.setFont(font)
        self.back_pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(166, 0, 0)")
        self.back_pushButton.setObjectName("back_pushButton")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(-10, 280, 1201, 20))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(350, 110, 20, 171))
        self.line_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_4.setLineWidth(3)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setObjectName("line_4")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(170, 110, 20, 171))
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setLineWidth(3)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setObjectName("line_3")
        self.bbed_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.bbed_checkBox.setGeometry(QtCore.QRect(200, 310, 61, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bbed_checkBox.sizePolicy().hasHeightForWidth())
        self.bbed_checkBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bbed_checkBox.setFont(font)
        self.bbed_checkBox.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.bbed_checkBox.setText("")
        self.bbed_checkBox.setTristate(False)
        self.bbed_checkBox.setObjectName("bbed_checkBox")
        self.bb_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.bb_checkBox.setGeometry(QtCore.QRect(20, 140, 61, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bb_checkBox.sizePolicy().hasHeightForWidth())
        self.bb_checkBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bb_checkBox.setFont(font)
        self.bb_checkBox.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.bb_checkBox.setText("")
        self.bb_checkBox.setTristate(False)
        self.bb_checkBox.setObjectName("bb_checkBox")
        self.ab_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.ab_checkBox.setGeometry(QtCore.QRect(20, 200, 61, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ab_checkBox.sizePolicy().hasHeightForWidth())
        self.ab_checkBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ab_checkBox.setFont(font)
        self.ab_checkBox.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.ab_checkBox.setText("")
        self.ab_checkBox.setTristate(False)
        self.ab_checkBox.setObjectName("ab_checkBox")
        self.bb_label = QtWidgets.QLabel(self.centralwidget)
        self.bb_label.setGeometry(QtCore.QRect(50, 160, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.bb_label.setFont(font)
        self.bb_label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bb_label.setFrameShape(QtWidgets.QFrame.Box)
        self.bb_label.setLineWidth(1)
        self.bb_label.setTextFormat(QtCore.Qt.AutoText)
        self.bb_label.setScaledContents(False)
        self.bb_label.setAlignment(QtCore.Qt.AlignCenter)
        self.bb_label.setWordWrap(True)
        self.bb_label.setObjectName("bb_label")
        self.b_label = QtWidgets.QLabel(self.centralwidget)
        self.b_label.setGeometry(QtCore.QRect(20, 120, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.b_label.setFont(font)
        self.b_label.setAlignment(QtCore.Qt.AlignCenter)
        self.b_label.setObjectName("b_label")
        self.ab_label = QtWidgets.QLabel(self.centralwidget)
        self.ab_label.setGeometry(QtCore.QRect(50, 220, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.ab_label.setFont(font)
        self.ab_label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ab_label.setFrameShape(QtWidgets.QFrame.Box)
        self.ab_label.setLineWidth(1)
        self.ab_label.setTextFormat(QtCore.Qt.AutoText)
        self.ab_label.setScaledContents(False)
        self.ab_label.setAlignment(QtCore.Qt.AlignCenter)
        self.ab_label.setWordWrap(True)
        self.ab_label.setObjectName("ab_label")
        self.al_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.al_checkBox.setGeometry(QtCore.QRect(200, 200, 61, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.al_checkBox.sizePolicy().hasHeightForWidth())
        self.al_checkBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.al_checkBox.setFont(font)
        self.al_checkBox.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.al_checkBox.setText("")
        self.al_checkBox.setTristate(False)
        self.al_checkBox.setObjectName("al_checkBox")
        self.bl_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.bl_checkBox.setGeometry(QtCore.QRect(200, 140, 61, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bl_checkBox.sizePolicy().hasHeightForWidth())
        self.bl_checkBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bl_checkBox.setFont(font)
        self.bl_checkBox.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.bl_checkBox.setText("")
        self.bl_checkBox.setTristate(False)
        self.bl_checkBox.setObjectName("bl_checkBox")
        self.bl_label = QtWidgets.QLabel(self.centralwidget)
        self.bl_label.setGeometry(QtCore.QRect(230, 160, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.bl_label.setFont(font)
        self.bl_label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bl_label.setFrameShape(QtWidgets.QFrame.Box)
        self.bl_label.setLineWidth(1)
        self.bl_label.setTextFormat(QtCore.Qt.AutoText)
        self.bl_label.setScaledContents(False)
        self.bl_label.setAlignment(QtCore.Qt.AlignCenter)
        self.bl_label.setWordWrap(True)
        self.bl_label.setObjectName("bl_label")
        self.al_label = QtWidgets.QLabel(self.centralwidget)
        self.al_label.setGeometry(QtCore.QRect(230, 220, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.al_label.setFont(font)
        self.al_label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.al_label.setFrameShape(QtWidgets.QFrame.Box)
        self.al_label.setLineWidth(1)
        self.al_label.setTextFormat(QtCore.Qt.AutoText)
        self.al_label.setScaledContents(False)
        self.al_label.setAlignment(QtCore.Qt.AlignCenter)
        self.al_label.setWordWrap(True)
        self.al_label.setObjectName("al_label")
        self.l_label = QtWidgets.QLabel(self.centralwidget)
        self.l_label.setGeometry(QtCore.QRect(210, 120, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.l_label.setFont(font)
        self.l_label.setAlignment(QtCore.Qt.AlignCenter)
        self.l_label.setObjectName("l_label")
        self.ad_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.ad_checkBox.setGeometry(QtCore.QRect(380, 200, 61, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ad_checkBox.sizePolicy().hasHeightForWidth())
        self.ad_checkBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ad_checkBox.setFont(font)
        self.ad_checkBox.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.ad_checkBox.setText("")
        self.ad_checkBox.setTristate(False)
        self.ad_checkBox.setObjectName("ad_checkBox")
        self.bd_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.bd_checkBox.setGeometry(QtCore.QRect(380, 140, 61, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bd_checkBox.sizePolicy().hasHeightForWidth())
        self.bd_checkBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bd_checkBox.setFont(font)
        self.bd_checkBox.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.bd_checkBox.setText("")
        self.bd_checkBox.setTristate(False)
        self.bd_checkBox.setObjectName("bd_checkBox")
        self.bd_label = QtWidgets.QLabel(self.centralwidget)
        self.bd_label.setGeometry(QtCore.QRect(410, 160, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.bd_label.setFont(font)
        self.bd_label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bd_label.setFrameShape(QtWidgets.QFrame.Box)
        self.bd_label.setLineWidth(1)
        self.bd_label.setTextFormat(QtCore.Qt.AutoText)
        self.bd_label.setScaledContents(False)
        self.bd_label.setAlignment(QtCore.Qt.AlignCenter)
        self.bd_label.setWordWrap(True)
        self.bd_label.setObjectName("bd_label")
        self.ad_label = QtWidgets.QLabel(self.centralwidget)
        self.ad_label.setGeometry(QtCore.QRect(410, 220, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.ad_label.setFont(font)
        self.ad_label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ad_label.setFrameShape(QtWidgets.QFrame.Box)
        self.ad_label.setLineWidth(1)
        self.ad_label.setTextFormat(QtCore.Qt.AutoText)
        self.ad_label.setScaledContents(False)
        self.ad_label.setAlignment(QtCore.Qt.AlignCenter)
        self.ad_label.setWordWrap(True)
        self.ad_label.setObjectName("ad_label")
        self.d_label = QtWidgets.QLabel(self.centralwidget)
        self.d_label.setGeometry(QtCore.QRect(380, 120, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.d_label.setFont(font)
        self.d_label.setAlignment(QtCore.Qt.AlignCenter)
        self.d_label.setObjectName("d_label")
        self.bed_label = QtWidgets.QLabel(self.centralwidget)
        self.bed_label.setGeometry(QtCore.QRect(110, 300, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bed_label.setFont(font)
        self.bed_label.setAlignment(QtCore.Qt.AlignCenter)
        self.bed_label.setObjectName("bed_label")
        self.bbed_label = QtWidgets.QLabel(self.centralwidget)
        self.bbed_label.setGeometry(QtCore.QRect(230, 330, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.bbed_label.setFont(font)
        self.bbed_label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bbed_label.setFrameShape(QtWidgets.QFrame.Box)
        self.bbed_label.setLineWidth(1)
        self.bbed_label.setTextFormat(QtCore.Qt.AutoText)
        self.bbed_label.setScaledContents(False)
        self.bbed_label.setAlignment(QtCore.Qt.AlignCenter)
        self.bbed_label.setWordWrap(True)
        self.bbed_label.setObjectName("bbed_label")
        self.next_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.next_pushButton.setGeometry(QtCore.QRect(410, 330, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.next_pushButton.setFont(font)
        self.next_pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 127);")
        self.next_pushButton.setObjectName("next_pushButton")
        select_meal.setCentralWidget(self.centralwidget)

        self.retranslateUi(select_meal)
        QtCore.QMetaObject.connectSlotsByName(select_meal)
        def close_window():
            select_meal.close()

        self.back_pushButton.clicked.connect(close_window)
        # self.next_pushButton.clicked.connect(close_window)

        # ในส่วนนี้เราเพิ่มการเชื่อมต่อกับเมธอด save_checkbox_states ในปุ่มย้อนกลับ
        self.next_pushButton.clicked.connect(self.save_checkbox_states_and_close)
        self.next_pushButton.clicked.connect(self.closeAll)

        # เพิ่มการเชื่อมต่อฐานข้อมูล SQLite3
        self.conn = sqlite3.connect("medicine.db")
        self.cursor = self.conn.cursor()


        QtCore.QMetaObject.connectSlotsByName(select_meal)
    
    def closeAll(self):
        self.each_drug.closeAll()
        self.each_drug2.closeAll()
        self.day_start.closeAll()  # ปิดหน้าต่างที่เป็นส่วนสมาชิกของ Ui_med_pack2
        self.select_meal.close()
        

    def set_meal_info(self, drug_id):
        self.drug_id = drug_id

        # print("drug_id: ",drug_id)
        
        # Check which meal_id is associated with the given drug_id
        self.cursor.execute('SELECT meal_id FROM Drug_handle WHERE drug_id = ?', (drug_id,))
        data = self.cursor.fetchall()

        # load ค่าจากฐานข้อมูลมาแสดงค่าใน Checkbox
        for meal_id in data:
            # print(meal_id)
            if meal_id == (1,):
                self.bb_checkBox.setChecked(True)

            elif meal_id == (2,):
                self.ab_checkBox.setChecked(True)
                
            elif meal_id == (3,):
                self.bl_checkBox.setChecked(True)
               
            elif meal_id == (4,):
                self.al_checkBox.setChecked(True)
               
            elif meal_id == (5,):
                self.bd_checkBox.setChecked(True)
               
            elif meal_id == (6,):
                self.ad_checkBox.setChecked(True)
               
            elif meal_id == (7,):
                self.bbed_checkBox.setChecked(True)


        # Print or use the associated meal_ids as needed
        # print("Associated meal_ids:", associated_meal_ids)

    def save_checkbox_states_and_close(self):
        self.save_checkbox_states()
        # QtWidgets.qApp.closeAllWindows()
        # # app = QtWidgets.QApplication(sys.argv)
        # drug_List = QtWidgets.QMainWindow()
        # ui = Ui_drug_List()
        # ui.setupUi(drug_List)
        # drug_List.show()
        
        # sys.exit(app.exec_())
        # อาจต้องสร้างฟังก์ชันในฟังก์ชัน
        
        
        # from main import Ui_Medicine_App  # version ใช้ไปก่อน จริงๆต้องimport drug_List แต่ยังไม่ได้ทำอัปเดทเลยยังไม่สามารถรู้ได้ในทันที
        # self.drug_list_again_window = QtWidgets.QMainWindow()
        # self.drug_list_again_ui = Ui_Medicine_App()
        # self.drug_list_again_ui.setupUi(self.drug_list_again_window)
        # self.drug_list_again_window.show()
        
        # for widget in QtWidgets.qApp.topLevelWidgets():
        #     print(self)
        #     if isinstance(widget, QtWidgets.QMainWindow) and widget is not self:
        #         print(widget)
        #         widget.close()
        #     else:
        #         print("not close" if isinstance(widget, Ui_drug_List) else "Ui_drug_list not closed")
        #         drug_List = QtWidgets.QMainWindow()
        #         ui = Ui_drug_List()
        #         ui.setupUi(drug_List)
        #         drug_List.show()
        #     print('\n')
                
    def save_checkbox_states(self):
        checkbox_states = {
            "bb_checkBox": self.bb_checkBox.isChecked(),
            "ab_checkBox": self.ab_checkBox.isChecked(),
            "bl_checkBox": self.bl_checkBox.isChecked(),
            "al_checkBox": self.al_checkBox.isChecked(),
            "bd_checkBox": self.bd_checkBox.isChecked(),
            "ad_checkBox": self.ad_checkBox.isChecked(),
            "bbed_checkBox": self.bbed_checkBox.isChecked()
        }

        # Iterate through checkbox states
        for checkbox_name, state in checkbox_states.items():
            # print(f"{checkbox_name}: {state}")

            # Determine meal_id based on checkbox_name
            meal_id = None
            if "bb_checkBox" in checkbox_name:
                meal_id = 1
            elif "ab_checkBox" in checkbox_name:
                meal_id = 2
            elif "bl_checkBox" in checkbox_name:
                meal_id = 3
            elif "al_checkBox" in checkbox_name:
                meal_id = 4
            elif "bd_checkBox" in checkbox_name:
                meal_id = 5
            elif "ad_checkBox" in checkbox_name:
                meal_id = 6
            elif "bbed_checkBox" in checkbox_name:
                meal_id = 7

            # Check if the record already exists
            self.cursor.execute('''
                SELECT * FROM Drug_handle
                WHERE drug_id = ? AND meal_id = ?
            ''', (self.drug_id, meal_id))

            existing_data = self.cursor.fetchone()

            if state:
                # Insert the record if it doesn't exist
                if not existing_data:
                    self.cursor.execute('''
                        INSERT INTO Drug_handle (drug_id, meal_id)
                        VALUES (?, ?)
                    ''', (self.drug_id, meal_id))
                    # print(f"Inserted: drug_id={self.drug_id}, meal_id={meal_id}")
                else:
                    pass
            else:
                # Delete the record if it exists
                if existing_data:
                    self.cursor.execute('''
                        DELETE FROM Drug_handle
                        WHERE drug_id = ? AND meal_id = ?
                    ''', (self.drug_id, meal_id))
                    # print(f"Deleted: drug_id={self.drug_id}, meal_id={meal_id}")
                else:
                    # print(f"Skipped: Record doesn't exist - drug_id={self.drug_id}, meal_id={meal_id}")
                    pass

        self.conn.commit()

            # if existing_data:
            #     # อัปเดตข้อมูล
            #     self.cursor.execute('''
            #         UPDATE Drug_handle
            #         SET meal_state = ?
            #         WHERE meal_id = ?
            #     ''', (state, meal_id))
            # else:
            #     # ถ้าไม่มีข้อมูล ให้เพิ่มข้อมูลใหม่
            #     self.cursor.execute('''
            #         INSERT INTO Meal (meal_id, meal_state, time)
            #         VALUES (?, ?, ?)
            #     ''', (meal_id, state, ""))

        # self.conn.commit()
    
    def retranslateUi(self, select_meal):
        _translate = QtCore.QCoreApplication.translate
        select_meal.setWindowTitle(_translate("select_meal", "เลือกมื้อ"))
        self.meal_label.setText(_translate("select_meal", "เลือกมื้อยาที่ต้องการ"))
        self.back_pushButton.setText(_translate("select_meal", "ย้อนกลับ"))
        self.bb_label.setText(_translate("select_meal", "ก่อน อาหาร"))
        self.b_label.setText(_translate("select_meal", "มื้อเช้า"))
        self.ab_label.setText(_translate("select_meal", "หลัง อาหาร"))
        self.bl_label.setText(_translate("select_meal", "ก่อน อาหาร"))
        self.al_label.setText(_translate("select_meal", "หลัง อาหาร"))
        self.l_label.setText(_translate("select_meal", "มื้อเที่ยง"))
        self.bd_label.setText(_translate("select_meal", "ก่อน อาหาร"))
        self.ad_label.setText(_translate("select_meal", "หลัง อาหาร"))
        self.d_label.setText(_translate("select_meal", "มื้อเย็น"))
        self.bed_label.setText(_translate("select_meal", "มื้อก่อนนอน"))
        self.bbed_label.setText(_translate("select_meal", "ก่อนนอน"))
        self.next_pushButton.setText(_translate("select_meal", "เสร็จสิ้น"))


class NumericOnlyTextEdit(QtWidgets.QTextEdit):
    def keyPressEvent(self, event):
        # Allow only numeric characters and certain key events (e.g., Backspace)
        if event.key() == QtCore.Qt.Key_Backspace or event.text().isdigit():
            super().keyPressEvent(event)
        else:
            event.ignore()

class Ui_Add_drug(object):

    def setupUi(self, Add_drug, drug_List):
        self.Add_drug = Add_drug
        self.drug_List = drug_List
        
        Add_drug.setObjectName("Add_drug")
        Add_drug.resize(531, 401)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../.designer/Resources/drug_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Add_drug.setWindowIcon(icon)
        Add_drug.setStyleSheet("background-color: rgb(217, 244, 255)")
        self.centralwidget = QtWidgets.QWidget(Add_drug)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 20, 191, 51))
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
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 30, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setLineWidth(1)
        self.label_2.setText("")
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setPixmap(QtGui.QPixmap(":/icons/drug_icon.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-10, 90, 551, 20))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.drugName_label = QtWidgets.QLabel(self.centralwidget)
        self.drugName_label.setGeometry(QtCore.QRect(30, 130, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.drugName_label.setFont(font)
        self.drugName_label.setObjectName("drugName_label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 160, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit.setFrameShape(QtWidgets.QFrame.Box)
        self.textEdit.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textEdit.setObjectName("textEdit")
        self.drugDescribe_label = QtWidgets.QLabel(self.centralwidget)
        self.drugDescribe_label.setGeometry(QtCore.QRect(30, 210, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.drugDescribe_label.setFont(font)
        self.drugDescribe_label.setObjectName("drugDescribe_label")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(20, 240, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setAccessibleName("")
        self.textEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_2.setFrameShape(QtWidgets.QFrame.Box)
        self.textEdit_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textEdit_2.setObjectName("textEdit_2")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(250, 109, 20, 211))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setObjectName("line_2")
        self.drugAll_label = QtWidgets.QLabel(self.centralwidget)
        self.drugAll_label.setGeometry(QtCore.QRect(280, 130, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.drugAll_label.setFont(font)
        self.drugAll_label.setAlignment(QtCore.Qt.AlignCenter)
        self.drugAll_label.setObjectName("drugAll_label")
        self.saveDrug_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveDrug_pushButton.setGeometry(QtCore.QRect(220, 330, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.saveDrug_pushButton.setFont(font)
        self.saveDrug_pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 127);")
        self.saveDrug_pushButton.setObjectName("saveDrug_pushButton")
        #self.listHave_pushButton = QtWidgets.QPushButton(self.centralwidget)
        #self.listHave_pushButton.setGeometry(QtCore.QRect(370, 40, 141, 31))
        #font = QtGui.QFont()
        #font.setPointSize(12)
        #self.listHave_pushButton.setFont(font)
        #self.listHave_pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        #self.listHave_pushButton.setObjectName("listHave_pushButton")
        self.add_back_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.add_back_pushButton.setGeometry(QtCore.QRect(30, 40, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add_back_pushButton.setFont(font)
        self.add_back_pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(166, 0, 0)")
        self.add_back_pushButton.setObjectName("add_back_pushButton")
        self.drugOne_label = QtWidgets.QLabel(self.centralwidget)
        self.drugOne_label.setGeometry(QtCore.QRect(280, 210, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.drugOne_label.setFont(font)
        self.drugOne_label.setAlignment(QtCore.Qt.AlignCenter)
        self.drugOne_label.setObjectName("drugOne_label")

        self.textEdit_3 = NumericOnlyTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(280, 160, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit_3.setFont(font)
        self.textEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_3.setFrameShape(QtWidgets.QFrame.Box)
        self.textEdit_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textEdit_3.setObjectName("textEdit_3")


        self.textEdit_4 = NumericOnlyTextEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(280, 240, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit_4.setFont(font)
        self.textEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_4.setFrameShape(QtWidgets.QFrame.Box)
        self.textEdit_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textEdit_4.setObjectName("textEdit_4")
        Add_drug.setCentralWidget(self.centralwidget)

        self.retranslateUi(Add_drug)
        QtCore.QMetaObject.connectSlotsByName(Add_drug)
        Add_drug.setTabOrder(self.textEdit, self.textEdit_2)
        Add_drug.setTabOrder(self.textEdit_2, self.saveDrug_pushButton)

        self.add_back_pushButton.clicked.connect(self.closeAll)

        #Add_drug.setTabOrder(self.saveDrug_pushButton, self.listHave_pushButton)
        #Add_drug.setTabOrder(self.listHave_pushButton, self.add_back_pushButton)

        

        #def open_drug_list():
        #    drug_list_window = QtWidgets.QMainWindow()
        #    drug_list_ui = Ui_drugList()
        #    drug_list_ui.setupUi(drug_list_window)
        #    drug_list_ui.load_drugs_from_database()  # เรียกฟังก์ชันนี้เมื่อเปิดหน้ารายการยา
        #    drug_list_window.show()
            
        #self.listHave_pushButton.clicked.connect(open_drug_list) 

        
        # เชื่อมต่อกับฟังก์ชัน save_drug                                                                      
        self.saveDrug_pushButton.clicked.connect(self.save_drug)


    def save_drug(self):
        drug_name = self.textEdit.toPlainText()
        drug_description = self.textEdit_2.toPlainText()
        drug_amount = self.textEdit_3.toPlainText()
        drug_eat = self.textEdit_4.toPlainText()
        
        if not drug_name.strip():
            error_dialog = QtWidgets.QDialog(self.centralwidget)
            error_dialog.setWindowTitle("ผิดพลาด")
            error_dialog.setModal(True)
            error_dialog.move(200, 200)
            error_dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)

            # Create and configure QLabel for the error message
            error_label = QtWidgets.QLabel("กรุณาระบุชื่อยา", error_dialog)
            font = QtGui.QFont()
            font.setPointSize(12)
            error_label.setFont(font)
            error_label.setAlignment(QtCore.Qt.AlignCenter)

            # Create and configure OK button
            ok_button = QtWidgets.QPushButton("ตกลง", error_dialog)
            ok_button_font = QtGui.QFont()
            ok_button_font.setPointSize(12)
            ok_button.setFont(ok_button_font)

            # Set background color for the dialog
            error_dialog.setStyleSheet("background-color: rgb(255, 241, 129); border-radius: 30px;")

            # Set button background and text color
            ok_button.setStyleSheet("background-color: rgb(85, 170, 127); color: white; border: none; border-radius: 15px;")

            # Set QDialog layout
            layout = QtWidgets.QVBoxLayout()
            layout.addWidget(error_label)
            layout.addWidget(ok_button)
            error_dialog.setLayout(layout)

            # Connect the OK button's click event to close the error_dialog
            ok_button.clicked.connect(error_dialog.accept)

            # Show the QDialog
            error_dialog.exec_()
            return  # Do not proceed with saving
        self.update_drug_list

        connection = sqlite3.connect("medicine.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO Drug (drug_name, drug_description, drug_amount, drug_eat) VALUES (?, ?, ?, ?)", (drug_name, drug_description, drug_amount, drug_eat))
        connection.commit()
        connection.close()

        #  # เพิ่มเรียกใช้ฟังก์ชัน update_drug_list เพื่ออัพเดตรายการยาในหน้าคลังยา
        # self.update_drug_list()

        # สร้าง QDialog และกำหนดสไตล์
        message_dialog = QtWidgets.QDialog(self.centralwidget)
        message_dialog.setWindowTitle("บันทึกสำเร็จ")
        message_dialog.setModal(True)
        message_dialog.move(150, 200)
        message_dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)

        # Create and configure QLabel
        message_label = QtWidgets.QLabel(message_dialog)
        message_label.setText("บันทึกข้อมูลยาเรียบร้อยแล้ว")
        font = QtGui.QFont()
        font.setPointSize(12)
        message_label.setFont(font)
        message_label.setAlignment(QtCore.Qt.AlignCenter)

        # Create and configure OK button
        ok_button = QtWidgets.QPushButton(message_dialog)
        ok_button.setText("ตกลง")
        ok_button_font = QtGui.QFont()
        ok_button_font.setPointSize(12)
        ok_button.setFont(ok_button_font)

        # Set background color for the dialog
        message_dialog.setStyleSheet("background-color: rgb(255, 241, 129); border-radius: 30px;")

        # Set button background and text color
        ok_button.setStyleSheet("background-color: rgb(85, 170, 127); color: white; border: none; border-radius: 15px;")

        # Set QDialog layout
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(message_label)
        layout.addWidget(ok_button)
        message_dialog.setLayout(layout)

        # Connect the OK button's click event to close the dialog
        ok_button.clicked.connect(message_dialog.accept)

        # Show the QDialog
        message_dialog.exec_()
        
        # ล้างข้อมูลใน textEdit, textEdit_2, textEdit_3, textEdit_4
        self.textEdit.clear()
        self.textEdit_2.clear()
        self.textEdit_3.clear()
        self.textEdit_4.clear()
        
    def closeAll(self):
        self.drug_List.closeAll()
        self.Add_drug.close()

    def retranslateUi(self, Add_drug):
        _translate = QtCore.QCoreApplication.translate
        Add_drug.setWindowTitle(_translate("Add_drug", "เพิ่มยา"))
        self.label.setText(_translate("Add_drug", "   เพิ่มยา"))
        self.drugName_label.setText(_translate("Add_drug", "ชื่อยา"))
        self.drugDescribe_label.setText(_translate("Add_drug", "คำอธิบายยา"))
        self.drugAll_label.setText(_translate("Add_drug", "จำนวนยาทั้งหมดที่มี (เม็ด)"))
        self.saveDrug_pushButton.setText(_translate("Add_drug", "บันทึกยา"))
        #self.listHave_pushButton.setText(_translate("Add_drug", "รายการยาที่มี"))
        self.add_back_pushButton.setText(_translate("Add_drug", "หน้าหลัก"))
        self.drugOne_label.setText(_translate("Add_drug", "จำนวนยาที่กินต่อ 1 มื้อ (เม็ด)"))
        
import resources_rc

##################################################################################################################################

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("medicine.db")
    if not db.open():
        print("Cannot establish a database connection.")
        sys.exit(1)
        
    drug_List = QtWidgets.QMainWindow()
    ui = Ui_drug_List()
    ui.setupUi(drug_List)
    drug_List.show()
    sys.exit(app.exec_())
