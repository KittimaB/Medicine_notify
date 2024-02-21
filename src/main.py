from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsDropShadowEffect
from drug_List import Ui_drug_List
from select_time import Ui_select_time
# from pack_med import Ui_med_pack
from pack import Ui_med_pack
from sortDrug import Ui_sortDrug
from drugTotal import Ui_drugTotal
from wifi import Ui_wifi

import sqlite3

import datetime
from PyQt5.QtCore import QTimer, QLocale

class Ui_Medicine_App(object):
    def setupUi(self, Medicine_App):
        Medicine_App.setObjectName("Medicine_App")
        Medicine_App.resize(683, 400)
        Medicine_App.setStyleSheet("\n"
"background-color: rgb(23, 73, 110);")
        self.centralwidget = QtWidgets.QWidget(Medicine_App)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, -60, 683, 131))
        self.frame.setStyleSheet("border-radius: 40px;\n"
"background-color: rgb(255, 255, 255);\n" )
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.frame)
        shadow.setBlurRadius(8)
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(0,2)
        self.frame.setGraphicsEffect(shadow)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.home_label = QtWidgets.QLabel(self.frame)
        self.home_label.setGeometry(QtCore.QRect(200, 70, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.home_label.setFont(font)
        self.home_label.setStyleSheet("border-radius: 16px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(23, 73, 110);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.home_label)
        shadow.setBlurRadius(8)
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(0,2)
        self.home_label.setGraphicsEffect(shadow)
        self.home_label.setFrameShape(QtWidgets.QFrame.Box)
        self.home_label.setLineWidth(1)
        self.home_label.setTextFormat(QtCore.Qt.AutoText)
        self.home_label.setScaledContents(False)
        self.home_label.setAlignment(QtCore.Qt.AlignCenter)
        self.home_label.setWordWrap(True)
        self.home_label.setObjectName("home_label")
        self.img_home_label = QtWidgets.QLabel(self.frame)
        self.img_home_label.setGeometry(QtCore.QRect(277, 80, 33, 31))
        self.img_home_label.setText("")
        self.img_home_label.setPixmap(QtGui.QPixmap(":/icons/home2_icon.png"))
        self.img_home_label.setScaledContents(True)
        self.img_home_label.setAlignment(QtCore.Qt.AlignCenter)
        self.img_home_label.setObjectName("img_home_label")
        
        self.wifi_pushButton = QtWidgets.QPushButton(self.frame)
        self.wifi_pushButton.setGeometry(QtCore.QRect(590, 76, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.wifi_pushButton.setFont(font)
        self.wifi_pushButton.setStyleSheet("border-radius: 9px;\n"
                                 "color: rgb(0, 0, 0);\n"
                                 "background-color: rgb(255, 255, 255);")
        
        self.img_wifi_label = QtWidgets.QLabel(self.wifi_pushButton)
        self.img_wifi_label.setGeometry(QtCore.QRect(5, 8, 31, 23))
        self.img_wifi_label.setText("")
        self.img_wifi_label.setPixmap(QtGui.QPixmap(":/icons/wifi_icon.png"))
        self.img_wifi_label.setScaledContents(True)
        self.img_wifi_label.setAlignment(QtCore.Qt.AlignCenter)
        self.img_wifi_label.setObjectName("img_wifi_label")

        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(50, 97, 100, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(43, 77, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(205, 90, 271, 281))
        self.frame_2.setStyleSheet("border-radius: 16px;\n"
"background-color: rgb(236, 236, 236);\n")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.frame_2)
        shadow.setBlurRadius(8)
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(0,2)
        self.frame_2.setGraphicsEffect(shadow)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.addDrug_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.addDrug_pushButton.setGeometry(QtCore.QRect(225, 110, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.addDrug_pushButton.setFont(font)
        self.addDrug_pushButton.setStyleSheet("border-radius: 9px;\n"
                                 "color: rgb(0, 0, 0);\n"
                                 "background-color: rgb(255, 255, 255);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.addDrug_pushButton)
        shadow.setBlurRadius(8)
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(0,2)
        self.addDrug_pushButton.setGraphicsEffect(shadow)

        # icon = QtGui.QIcon()                                                                      ไม่ได้ลบไอคอนแบบเก่าแค่คอมเม้นไว้
        # icon.addPixmap(QtGui.QPixmap(":/icons/drug_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.img_druglist_label = QtWidgets.QLabel(self.centralwidget)
        self.img_druglist_label.setGeometry(QtCore.QRect(292, 119, 25, 24))
        self.img_druglist_label.setText("")
        self.img_druglist_label.setPixmap(QtGui.QPixmap(":/icons/druglist_tab.png"))
        self.img_druglist_label.setScaledContents(True)
        self.img_druglist_label.setAlignment(QtCore.Qt.AlignCenter)
        self.img_druglist_label.setObjectName("img_druglist_label")

        # self.addDrug_pushButton.setIcon(icon)
        # self.addDrug_pushButton.setIconSize(QtCore.QSize(20, 40))
        # self.addDrug_pushButton.setAutoDefault(False)
        # self.addDrug_pushButton.setDefault(False)
        # self.addDrug_pushButton.setFlat(False)
        self.addDrug_pushButton.setObjectName("addDrug_pushButton")
        self.setting_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.setting_pushButton.setGeometry(QtCore.QRect(225, 160, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.setting_pushButton.setFont(font)
        self.setting_pushButton.setStyleSheet("border-radius: 9px;\n"
                                 "color: rgb(0, 0, 0);\n"
                                 "background-color: rgb(255, 255, 255);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.setting_pushButton)
        shadow.setBlurRadius(8)
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(0,2)
        self.setting_pushButton.setGraphicsEffect(shadow)
        # icon1 = QtGui.QIcon()
        # icon1.addPixmap(QtGui.QPixmap(":/icons/setting_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.img_selecttime_label = QtWidgets.QLabel(self.centralwidget)
        self.img_selecttime_label.setGeometry(QtCore.QRect(275, 169, 26, 24))
        self.img_selecttime_label.setText("")
        self.img_selecttime_label.setPixmap(QtGui.QPixmap(":/icons/selecttime_tab.png"))
        self.img_selecttime_label.setScaledContents(True)
        self.img_selecttime_label.setAlignment(QtCore.Qt.AlignCenter)
        self.img_selecttime_label.setObjectName("img_selecttime_label")

        # self.setting_pushButton.setIcon(icon1)
        # self.setting_pushButton.setIconSize(QtCore.QSize(20, 40))
        # self.setting_pushButton.setAutoDefault(False)
        # self.setting_pushButton.setDefault(False)
        # self.setting_pushButton.setFlat(False)
        self.setting_pushButton.setObjectName("setting_pushButton")
        self.putDrug_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.putDrug_pushButton.setGeometry(QtCore.QRect(225, 210, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.putDrug_pushButton.setFont(font)
        self.putDrug_pushButton.setStyleSheet("border-radius: 9px;\n"
                                 "color: rgb(0, 0, 0);\n"
                                 "background-color: rgb(255, 255, 255);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.putDrug_pushButton)
        shadow.setBlurRadius(8)
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(0,2)
        self.putDrug_pushButton.setGraphicsEffect(shadow)
        # icon2 = QtGui.QIcon()
        # icon2.addPixmap(QtGui.QPixmap(":/icons/istockphoto-1263011147-170667a.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.img_pack_label = QtWidgets.QLabel(self.centralwidget)
        self.img_pack_label.setGeometry(QtCore.QRect(260, 219, 25, 24))
        self.img_pack_label.setText("")
        self.img_pack_label.setPixmap(QtGui.QPixmap(":/icons/pack_tab.png"))
        self.img_pack_label.setScaledContents(True)
        self.img_pack_label.setAlignment(QtCore.Qt.AlignCenter)
        self.img_pack_label.setObjectName("img_pack_label")

        # self.putDrug_pushButton.setIcon(icon2)
        # self.putDrug_pushButton.setIconSize(QtCore.QSize(20, 50))
        # self.putDrug_pushButton.setAutoDefault(False)
        # self.putDrug_pushButton.setDefault(False)
        # self.putDrug_pushButton.setFlat(False)
        self.putDrug_pushButton.setObjectName("putDrug_pushButton")
        self.alignment_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.alignment_pushButton.setGeometry(QtCore.QRect(225, 260, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.alignment_pushButton.setFont(font)
        self.alignment_pushButton.setStyleSheet("border-radius: 9px;\n"
                                 "color: rgb(0, 0, 0);\n"
                                 "background-color: rgb(255, 255, 255);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.alignment_pushButton)
        shadow.setBlurRadius(8)
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(0,2)
        self.alignment_pushButton.setGraphicsEffect(shadow)
        # icon3 = QtGui.QIcon()
        # icon3.addPixmap(QtGui.QPixmap(":/icons/Industry-Rack-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.img_sort_label = QtWidgets.QLabel(self.centralwidget)
        self.img_sort_label.setGeometry(QtCore.QRect(252, 269, 27, 24))
        self.img_sort_label.setText("")
        self.img_sort_label.setPixmap(QtGui.QPixmap(":/icons/sort_tab.png"))
        self.img_sort_label.setScaledContents(True)
        self.img_sort_label.setAlignment(QtCore.Qt.AlignCenter)
        self.img_sort_label.setObjectName("img_sort_label")

        # self.alignment_pushButton.setIcon(icon3)
        # self.alignment_pushButton.setIconSize(QtCore.QSize(20, 50))
        # self.alignment_pushButton.setAutoDefault(False)
        # self.alignment_pushButton.setDefault(False)
        # self.alignment_pushButton.setFlat(False)
        self.alignment_pushButton.setObjectName("alignment_pushButton")
        self.drugLeft_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.drugLeft_pushButton.setGeometry(QtCore.QRect(225, 310, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.drugLeft_pushButton.setFont(font)
        self.drugLeft_pushButton.setStyleSheet("border-radius: 9px;\n"
                                 "color: rgb(0, 0, 0);\n"
                                 "background-color: rgb(255, 255, 255);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.drugLeft_pushButton)
        shadow.setBlurRadius(8)
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(0,2)
        self.drugLeft_pushButton.setGraphicsEffect(shadow)
        # icon4 = QtGui.QIcon()
        # icon4.addPixmap(QtGui.QPixmap(":/icons/table_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.img_drugleft_label = QtWidgets.QLabel(self.centralwidget)
        self.img_drugleft_label.setGeometry(QtCore.QRect(255, 318, 27, 24))
        self.img_drugleft_label.setText("")
        self.img_drugleft_label.setPixmap(QtGui.QPixmap(":/icons/drugleft_tab.png"))
        self.img_drugleft_label.setScaledContents(True)
        self.img_drugleft_label.setAlignment(QtCore.Qt.AlignCenter)
        self.img_drugleft_label.setObjectName("img_drugleft_label")

        # self.drugLeft_pushButton.setIcon(icon4)
        # self.drugLeft_pushButton.setIconSize(QtCore.QSize(20, 50))
        # self.drugLeft_pushButton.setAutoDefault(False)
        # self.drugLeft_pushButton.setDefault(False)
        # self.drugLeft_pushButton.setFlat(False)
        self.drugLeft_pushButton.setObjectName("drugLeft_pushButton")
        Medicine_App.setCentralWidget(self.centralwidget)

        self.retranslateUi(Medicine_App)
        QtCore.QMetaObject.connectSlotsByName(Medicine_App)
        
        # อัพเดทเวลา
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        
        # Connect to SQLite database
        self.connection = sqlite3.connect("medicine.db")
        self.cursor = self.connection.cursor()

        # Create Drug table
        self.cursor.execute('''   
            CREATE TABLE IF NOT EXISTS Drug (
                "drug_id"	INTEGER,
                "drug_name"	TEXT,
                "drug_description"	TEXT,
                "drug_remaining"	REAL,
                "drug_remaining_meal"	INTEGER,
                "fraction"	REAL,
                "external_drug"	INTEGER,
                "internal_drug"	INTEGER,
                "drug_eat"	REAL,
                "all_drug_recieve"	INTEGER,
                "day_start"	INTEGER,
                "drug_log"	TEXT,
                "drug_new"  REAL,
                "drug_size" REAL,
                PRIMARY KEY("drug_id" AUTOINCREMENT))
        ''')
        
        # Create Meal table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Meal (
                "meal_id"	INTEGER,
                "meal_name"	TEXT,
                "time"	TEXT,
                PRIMARY KEY("meal_id" AUTOINCREMENT)
            )
        ''')

        # Create Drug_handle table 
        ##################### ใช้ระบุว่า ยาตัวนั้นกินมื้อไหนบ้าง ######################## 
        # ทำตารางนี้มาเพื่อแทนที่ meal_state ซึ่งเป็นการเก็บ state โดยรวม
        self.cursor.execute('''       
            CREATE TABLE IF NOT EXISTS Drug_handle (
                "handle_id"	INTEGER,
                "drug_id"	INTEGER,
                "meal_id"	INTEGER,
                FOREIGN KEY("meal_id") REFERENCES "Meal"("meal_id"),
                FOREIGN KEY("drug_id") REFERENCES "Drug"("drug_id"),
                PRIMARY KEY("handle_id" AUTOINCREMENT)
            )
        ''')
        
        # Check if the Meal table is empty, and if so, insert default values
        self.cursor.execute("SELECT COUNT(*) FROM Meal")
        meal_count = self.cursor.fetchone()[0]
        
        ############################### ปลื้มแก้ ######################################    
        if meal_count == 0:
            self.cursor.execute("INSERT INTO Meal (meal_name, time) VALUES (?, ?)",
                                ("มื้อเช้า ก่อนอาหาร", "06:00"))
            self.cursor.execute("INSERT INTO Meal (meal_name, time) VALUES (?, ?)",
                                ("มื้อเช้า หลังอาหาร", "06:30"))
            self.cursor.execute("INSERT INTO Meal (meal_name, time) VALUES (?, ?)",
                                ("มื้อเที่ยง ก่อนอาหาร", "12:00"))
            self.cursor.execute("INSERT INTO Meal (meal_name, time) VALUES (?, ?)",
                                ("มื้อเที่ยง หลังอาหาร", "12:30"))
            self.cursor.execute("INSERT INTO Meal (meal_name, time) VALUES (?, ?)",
                                ("มื้อเย็น ก่อนอาหาร", "18:00"))
            self.cursor.execute("INSERT INTO Meal (meal_name, time) VALUES (?, ?)",
                                ("มื้อเย็น หลังอาหาร", "18:30"))
            self.cursor.execute("INSERT INTO Meal (meal_name, time) VALUES (?, ?)",
                                ("มื้อก่อนนอน", "20:30"))

        self.connection.commit()
        
        self.addDrug_pushButton.clicked.connect(self.open_drug_List_page)
        self.setting_pushButton.clicked.connect(self.open_select_time_page)
        self.putDrug_pushButton.clicked.connect(self.open_pack_page)
        self.alignment_pushButton.clicked.connect(self.open_sortdrug_page)
        self.drugLeft_pushButton.clicked.connect(self.open_drugTotal_page)
        self.wifi_pushButton.clicked.connect(self.open_wifi_page)

        # Set up button press and release styling
        self.addDrug_pushButton.pressed.connect(lambda: self.set_button_pressed_style(self.addDrug_pushButton))
        self.addDrug_pushButton.released.connect(lambda: self.set_button_released_style(self.addDrug_pushButton))

        self.setting_pushButton.pressed.connect(lambda: self.set_button_pressed_style(self.setting_pushButton))
        self.setting_pushButton.released.connect(lambda: self.set_button_released_style(self.setting_pushButton))

        self.putDrug_pushButton.pressed.connect(lambda: self.set_button_pressed_style(self.putDrug_pushButton))
        self.putDrug_pushButton.released.connect(lambda: self.set_button_released_style(self.putDrug_pushButton))

        self.alignment_pushButton.pressed.connect(lambda: self.set_button_pressed_style(self.alignment_pushButton))
        self.alignment_pushButton.released.connect(lambda: self.set_button_released_style(self.alignment_pushButton))

        self.drugLeft_pushButton.pressed.connect(lambda: self.set_button_pressed_style(self.drugLeft_pushButton))
        self.drugLeft_pushButton.released.connect(lambda: self.set_button_released_style(self.drugLeft_pushButton))

        
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
            "background-color: rgb(255, 255, 255);"
        )
        
    ###################### เวลา #############################
    def update_time(self):
        current_datetime = datetime.datetime.now()
        current_time = current_datetime.strftime("%H:%M:%S")
        current_date = current_datetime.strftime("%a, %d %b %Y")
        
        self.label.setText(current_time)
        self.label_3.setText(current_date)

    ###################### หน้าคลังยา #############################  
    def open_drug_List_page(self):
        self.drug_List_window = QtWidgets.QMainWindow()
        self.ui_drug_List = Ui_drug_List()
        self.ui_drug_List.setupUi(self.drug_List_window)
        self.drug_List_window.show()

        def close_drug_List_window():
            self.drug_List_window.close()
        
        self.ui_drug_List.add_back_pushButton.clicked.connect(close_drug_List_window)

    ###################### หน้าตั้งเวลามื้อยา ############################# 
    def open_select_time_page(self):
        self.select_time_window = QtWidgets.QMainWindow()
        self.ui_select_time = Ui_select_time()
        self.ui_select_time.setupUi(self.select_time_window)
        self.select_time_window.show()
        
        def close_select_time_window():
            self.select_time_window.close()
        
        self.ui_select_time.add_back_pushButton.clicked.connect(close_select_time_window)
        
    # ###################### หน้าวิธีบรรจุยา #############################                                            อันเก่า
    # def open_pack_page(self):
    #     self.pack_window = QtWidgets.QMainWindow()
    #     self.ui_pack = Ui_med_pack()
    #     self.ui_pack.setupUi(self.pack_window)
    #     self.pack_window.show()
        
    #     def close_pack_window():
    #         self.pack_window.close()
            
    #     self.ui_pack.pack_back_pushButton.clicked.connect(close_pack_window)
        
        ##################### หน้าคำแนะนำการใส่ยา ############################# 
    def open_pack_page(self):
        self.pack_window = QtWidgets.QMainWindow()
        self.ui_pack = Ui_med_pack()
        self.ui_pack.setupUi(self.pack_window)
        self.pack_window.show()
        
        def close_pack_window():
            self.pack_window.close()
            
        self.ui_pack.add_back_pushButton.clicked.connect(close_pack_window)

    ###################### หน้าวิธีจัดเรียงยาตามผัง ############################# 
    def open_sortdrug_page(self):
        self.sortdrug_window = QtWidgets.QMainWindow()
        self.ui_sortdrug = Ui_sortDrug()
        self.ui_sortdrug.setupUi(self.sortdrug_window)
        self.sortdrug_window.show()
        
        def close_sortdrug_window():
            self.sortdrug_window.close()
            
        self.ui_sortdrug.add_back_pushButton.clicked.connect(close_sortdrug_window)
    
    ##################### หน้าจำนวนมื้อยาคงเหลือ ############################# 
    def open_drugTotal_page(self):
        self.drugTotal_window = QtWidgets.QMainWindow()
        self.ui_drugTotal = Ui_drugTotal()
        self.ui_drugTotal.setupUi(self.drugTotal_window)
        self.drugTotal_window.show()
        
        def close_drugTotal_window():
            self.drugTotal_window.close()
            
        self.ui_drugTotal.add_back_pushButton.clicked.connect(close_drugTotal_window)


    ##################### หน้าwifi ############################# 
    def open_wifi_page(self):
        self.wifi_window = QtWidgets.QMainWindow()
        self.ui_wifi = Ui_wifi()
        self.ui_wifi.setupUi(self.wifi_window)
        self.wifi_window.show()
        
        def close_wifi_window():
            self.wifi_window.close()
            
        self.ui_wifi.add_back_pushButton.clicked.connect(close_wifi_window)


    def retranslateUi(self, Medicine_App):
        _translate = QtCore.QCoreApplication.translate
        Medicine_App.setWindowTitle(_translate("Medicine_App", "หน้าหลัก"))
        self.addDrug_pushButton.setText(_translate("Medicine_App", "  คลังยา"))
        self.home_label.setText(_translate("Medicine_App", "     หน้าหลัก"))
        self.setting_pushButton.setText(_translate("Medicine_App", "  ตั้งเวลามื้อยา"))
        self.putDrug_pushButton.setText(_translate("Medicine_App", "  คำแนะนำการใส่ยา"))
        self.alignment_pushButton.setText(_translate("Medicine_App", "  วิธีเรียงกล่องบรรจุยา"))
        self.drugLeft_pushButton.setText(_translate("Medicine_App", "  จำนวนยาคงเหลือ"))
        self.wifi_pushButton.setText(_translate("Medicine_App", ""))

    
        self.img_wifi_label.raise_()
        
import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Medicine_App = QtWidgets.QMainWindow()
    ui = Ui_Medicine_App()
    ui.setupUi(Medicine_App)
    # Set the locale to English
    english_locale = QLocale(QLocale.English)
    QLocale.setDefault(english_locale)
    Medicine_App.show()
    sys.exit(app.exec_())