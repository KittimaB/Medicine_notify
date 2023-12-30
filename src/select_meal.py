from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
# อันนี้ของเรา
class Ui_select_meal(object):
    def open_drug_list_again(self):
        from main import Ui_Medicine_App  # version ใช้ไปก่อน จริงๆต้องimport drug_List แต่ยังไม่ได้ทำอัปเดทเลยยังไม่สามารถรู้ได้ในทันที
        self.drug_list_again_window = QtWidgets.QMainWindow()
        self.drug_list_again_ui = Ui_Medicine_App()
        self.drug_list_again_ui.setupUi(self.drug_list_again_window)
        self.drug_list_again_window.show()

    def setupUi(self, select_meal):
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
        self.next_pushButton.clicked.connect(self.open_drug_list_again)

        # ในส่วนนี้เราเพิ่มการเชื่อมต่อกับเมธอด save_checkbox_states ในปุ่มย้อนกลับ
        self.back_pushButton.clicked.connect(self.save_checkbox_states_and_close)

        # เพิ่มการเชื่อมต่อฐานข้อมูล SQLite3
        self.conn = sqlite3.connect("medicine.db")
        self.cursor = self.conn.cursor()
        

        # เช็คว่ามีข้อมูลในตาราง Meal หรือยัง
        self.cursor.execute('SELECT COUNT(*) FROM Meal')
        count = self.cursor.fetchone()[0]

        if count == 0:
            # สร้างรายชื่อของมื้อ
            meal_names = [
                "มื้อเช้า ก่อนอาหาร",
                "มื้อเช้า หลังอาหาร",
                "มื้อเที่ยง ก่อนอาหาร",
                "มื้อเที่ยง หลังอาหาร",
                "มื้อเย็น ก่อนอาหาร",
                "มื้อเย็น หลังอาหาร",
                "มื้อก่อนนอน"
            ]

            # เพิ่มรายชื่อมื้อลงในตาราง Meal
            for meal_name in meal_names:
                self.cursor.execute('INSERT INTO Meal (meal_name) VALUES (?)', (meal_name,))

            self.conn.commit()

        # Load checkbox states from the database
        self.load_checkbox_states()

        QtCore.QMetaObject.connectSlotsByName(select_meal)

    def set_meal_info(self, drug_id):
        self.drug_id = drug_id

        print("drug_id: ",drug_id)
        
        # Check which meal_id is associated with the given drug_id
        self.cursor.execute('SELECT meal_id FROM Drug_handle WHERE drug_id = ?', (drug_id,))
        associated_meal_ids = [row[0] for row in self.cursor.fetchall()]

        # Print or use the associated meal_ids as needed
        print("Associated meal_ids:", associated_meal_ids)

    def save_checkbox_states_and_close(self):
        self.save_checkbox_states()

    def load_checkbox_states(self):
        # โหลด checkbox_states จากฐานข้อมูล SQLite3
        self.cursor.execute('SELECT meal_id FROM Drug_handle')
        data = self.cursor.fetchall()

        for meal_id in data:
            if meal_id == 1:
                self.bb_checkBox.setChecked(True)

            elif meal_id == 2:
                self.ab_checkBox.setChecked(True)
                
            elif meal_id == 3:
                self.bl_checkBox.setChecked(True)
               
            elif meal_id == 4:
                self.al_checkBox.setChecked(True)
               
            elif meal_id == 5:
                self.bd_checkBox.setChecked(True)
               
            elif meal_id == 6:
                self.ad_checkBox.setChecked(True)
               
            elif meal_id == 7:
                self.bbed_checkBox.setChecked(True)
                
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

        # บันทึก checkbox_states ลงในฐานข้อมูล SQLite3
        for checkbox_name, state in checkbox_states.items():
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

            # ตรวจสอบว่ามีข้อมูลในฐานข้อมูลหรือไม่
            self.cursor.execute('SELECT * FROM Meal WHERE meal_id = ?', (meal_id,))
            existing_data = self.cursor.fetchone()


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

        self.conn.commit()


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
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    select_meal = QtWidgets.QMainWindow()
    ui = Ui_select_meal()
    ui.setupUi(select_meal)
    select_meal.show()
    sys.exit(app.exec_())




# from PyQt5 import QtCore, QtGui, QtWidgets
# import sqlite3

# class Ui_select_meal(object):
#     def open_drug_list_again(self):
#         from main import Ui_Medicine_App  # version ใช้ไปก่อน จริงๆต้องimport drug_List แต่ยังไม่ได้ทำอัปเดทเลยยังไม่สามารถรู้ได้ในทันที
#         self.drug_list_again_window = QtWidgets.QMainWindow()
#         self.drug_list_again_ui = Ui_Medicine_App()
#         self.drug_list_again_ui.setupUi(self.drug_list_again_window)
#         self.drug_list_again_window.show()

#     def setupUi(self, select_meal):
#         select_meal.setObjectName("select_meal")
#         select_meal.resize(531, 401)
#         select_meal.setStyleSheet("background-color: rgb(217, 244, 255)")
#         self.centralwidget = QtWidgets.QWidget(select_meal)
#         self.centralwidget.setObjectName("centralwidget")
#         self.line = QtWidgets.QFrame(self.centralwidget)
#         self.line.setGeometry(QtCore.QRect(-10, 90, 1201, 16))
#         self.line.setFrameShadow(QtWidgets.QFrame.Plain)
#         self.line.setLineWidth(3)
#         self.line.setFrameShape(QtWidgets.QFrame.HLine)
#         self.line.setObjectName("line")
#         self.meal_label = QtWidgets.QLabel(self.centralwidget)
#         self.meal_label.setGeometry(QtCore.QRect(170, 20, 211, 61))
#         font = QtGui.QFont()
#         font.setPointSize(16)
#         font.setBold(True)
#         font.setWeight(75)
#         self.meal_label.setFont(font)
#         self.meal_label.setStyleSheet("background-color: rgb(255, 255, 255);")
#         self.meal_label.setFrameShape(QtWidgets.QFrame.Box)
#         self.meal_label.setLineWidth(1)
#         self.meal_label.setTextFormat(QtCore.Qt.AutoText)
#         self.meal_label.setScaledContents(False)
#         self.meal_label.setAlignment(QtCore.Qt.AlignCenter)
#         self.meal_label.setWordWrap(True)
#         self.meal_label.setObjectName("meal_label")
#         self.back_pushButton = QtWidgets.QPushButton(self.centralwidget)
#         self.back_pushButton.setGeometry(QtCore.QRect(30, 40, 91, 41))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         self.back_pushButton.setFont(font)
#         self.back_pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
# "background-color: rgb(166, 0, 0)")
#         self.back_pushButton.setObjectName("back_pushButton")
#         self.line_2 = QtWidgets.QFrame(self.centralwidget)
#         self.line_2.setGeometry(QtCore.QRect(-10, 280, 1201, 20))
#         self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
#         self.line_2.setLineWidth(3)
#         self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
#         self.line_2.setObjectName("line_2")
#         self.line_4 = QtWidgets.QFrame(self.centralwidget)
#         self.line_4.setGeometry(QtCore.QRect(350, 110, 20, 171))
#         self.line_4.setFrameShadow(QtWidgets.QFrame.Plain)
#         self.line_4.setLineWidth(3)
#         self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
#         self.line_4.setObjectName("line_4")
#         self.line_3 = QtWidgets.QFrame(self.centralwidget)
#         self.line_3.setGeometry(QtCore.QRect(170, 110, 20, 171))
#         self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
#         self.line_3.setLineWidth(3)
#         self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
#         self.line_3.setObjectName("line_3")
#         self.bbed_checkBox = QtWidgets.QCheckBox(self.centralwidget)
#         self.bbed_checkBox.setGeometry(QtCore.QRect(200, 310, 61, 71))
#         sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
#         sizePolicy.setHorizontalStretch(0)
#         sizePolicy.setVerticalStretch(0)
#         sizePolicy.setHeightForWidth(self.bbed_checkBox.sizePolicy().hasHeightForWidth())
#         self.bbed_checkBox.setSizePolicy(sizePolicy)
#         font = QtGui.QFont()
#         font.setPointSize(14)
#         self.bbed_checkBox.setFont(font)
#         self.bbed_checkBox.setFocusPolicy(QtCore.Qt.WheelFocus)
#         self.bbed_checkBox.setText("")
#         self.bbed_checkBox.setTristate(False)
#         self.bbed_checkBox.setObjectName("bbed_checkBox")
#         self.bb_checkBox = QtWidgets.QCheckBox(self.centralwidget)
#         self.bb_checkBox.setGeometry(QtCore.QRect(20, 140, 61, 71))
#         sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
#         sizePolicy.setHorizontalStretch(0)
#         sizePolicy.setVerticalStretch(0)
#         sizePolicy.setHeightForWidth(self.bb_checkBox.sizePolicy().hasHeightForWidth())
#         self.bb_checkBox.setSizePolicy(sizePolicy)
#         font = QtGui.QFont()
#         font.setPointSize(14)
#         self.bb_checkBox.setFont(font)
#         self.bb_checkBox.setFocusPolicy(QtCore.Qt.WheelFocus)
#         self.bb_checkBox.setText("")
#         self.bb_checkBox.setTristate(False)
#         self.bb_checkBox.setObjectName("bb_checkBox")
#         self.ab_checkBox = QtWidgets.QCheckBox(self.centralwidget)
#         self.ab_checkBox.setGeometry(QtCore.QRect(20, 200, 61, 71))
#         sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
#         sizePolicy.setHorizontalStretch(0)
#         sizePolicy.setVerticalStretch(0)
#         sizePolicy.setHeightForWidth(self.ab_checkBox.sizePolicy().hasHeightForWidth())
#         self.ab_checkBox.setSizePolicy(sizePolicy)
#         font = QtGui.QFont()
#         font.setPointSize(14)
#         self.ab_checkBox.setFont(font)
#         self.ab_checkBox.setFocusPolicy(QtCore.Qt.WheelFocus)
#         self.ab_checkBox.setText("")
#         self.ab_checkBox.setTristate(False)
#         self.ab_checkBox.setObjectName("ab_checkBox")
#         self.bb_label = QtWidgets.QLabel(self.centralwidget)
#         self.bb_label.setGeometry(QtCore.QRect(50, 160, 91, 31))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         font.setBold(False)
#         font.setWeight(50)
#         self.bb_label.setFont(font)
#         self.bb_label.setStyleSheet("background-color: rgb(255, 255, 255);")
#         self.bb_label.setFrameShape(QtWidgets.QFrame.Box)
#         self.bb_label.setLineWidth(1)
#         self.bb_label.setTextFormat(QtCore.Qt.AutoText)
#         self.bb_label.setScaledContents(False)
#         self.bb_label.setAlignment(QtCore.Qt.AlignCenter)
#         self.bb_label.setWordWrap(True)
#         self.bb_label.setObjectName("bb_label")
#         self.b_label = QtWidgets.QLabel(self.centralwidget)
#         self.b_label.setGeometry(QtCore.QRect(20, 120, 131, 31))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         self.b_label.setFont(font)
#         self.b_label.setAlignment(QtCore.Qt.AlignCenter)
#         self.b_label.setObjectName("b_label")
#         self.ab_label = QtWidgets.QLabel(self.centralwidget)
#         self.ab_label.setGeometry(QtCore.QRect(50, 220, 91, 31))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         font.setBold(False)
#         font.setWeight(50)
#         self.ab_label.setFont(font)
#         self.ab_label.setStyleSheet("background-color: rgb(255, 255, 255);")
#         self.ab_label.setFrameShape(QtWidgets.QFrame.Box)
#         self.ab_label.setLineWidth(1)
#         self.ab_label.setTextFormat(QtCore.Qt.AutoText)
#         self.ab_label.setScaledContents(False)
#         self.ab_label.setAlignment(QtCore.Qt.AlignCenter)
#         self.ab_label.setWordWrap(True)
#         self.ab_label.setObjectName("ab_label")
#         self.al_checkBox = QtWidgets.QCheckBox(self.centralwidget)
#         self.al_checkBox.setGeometry(QtCore.QRect(200, 200, 61, 71))
#         sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
#         sizePolicy.setHorizontalStretch(0)
#         sizePolicy.setVerticalStretch(0)
#         sizePolicy.setHeightForWidth(self.al_checkBox.sizePolicy().hasHeightForWidth())
#         self.al_checkBox.setSizePolicy(sizePolicy)
#         font = QtGui.QFont()
#         font.setPointSize(14)
#         self.al_checkBox.setFont(font)
#         self.al_checkBox.setFocusPolicy(QtCore.Qt.WheelFocus)
#         self.al_checkBox.setText("")
#         self.al_checkBox.setTristate(False)
#         self.al_checkBox.setObjectName("al_checkBox")
#         self.bl_checkBox = QtWidgets.QCheckBox(self.centralwidget)
#         self.bl_checkBox.setGeometry(QtCore.QRect(200, 140, 61, 71))
#         sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
#         sizePolicy.setHorizontalStretch(0)
#         sizePolicy.setVerticalStretch(0)
#         sizePolicy.setHeightForWidth(self.bl_checkBox.sizePolicy().hasHeightForWidth())
#         self.bl_checkBox.setSizePolicy(sizePolicy)
#         font = QtGui.QFont()
#         font.setPointSize(14)
#         self.bl_checkBox.setFont(font)
#         self.bl_checkBox.setFocusPolicy(QtCore.Qt.WheelFocus)
#         self.bl_checkBox.setText("")
#         self.bl_checkBox.setTristate(False)
#         self.bl_checkBox.setObjectName("bl_checkBox")
#         self.bl_label = QtWidgets.QLabel(self.centralwidget)
#         self.bl_label.setGeometry(QtCore.QRect(230, 160, 91, 31))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         font.setBold(False)
#         font.setWeight(50)
#         self.bl_label.setFont(font)
#         self.bl_label.setStyleSheet("background-color: rgb(255, 255, 255);")
#         self.bl_label.setFrameShape(QtWidgets.QFrame.Box)
#         self.bl_label.setLineWidth(1)
#         self.bl_label.setTextFormat(QtCore.Qt.AutoText)
#         self.bl_label.setScaledContents(False)
#         self.bl_label.setAlignment(QtCore.Qt.AlignCenter)
#         self.bl_label.setWordWrap(True)
#         self.bl_label.setObjectName("bl_label")
#         self.al_label = QtWidgets.QLabel(self.centralwidget)
#         self.al_label.setGeometry(QtCore.QRect(230, 220, 91, 31))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         font.setBold(False)
#         font.setWeight(50)
#         self.al_label.setFont(font)
#         self.al_label.setStyleSheet("background-color: rgb(255, 255, 255);")
#         self.al_label.setFrameShape(QtWidgets.QFrame.Box)
#         self.al_label.setLineWidth(1)
#         self.al_label.setTextFormat(QtCore.Qt.AutoText)
#         self.al_label.setScaledContents(False)
#         self.al_label.setAlignment(QtCore.Qt.AlignCenter)
#         self.al_label.setWordWrap(True)
#         self.al_label.setObjectName("al_label")
#         self.l_label = QtWidgets.QLabel(self.centralwidget)
#         self.l_label.setGeometry(QtCore.QRect(210, 120, 131, 31))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         self.l_label.setFont(font)
#         self.l_label.setAlignment(QtCore.Qt.AlignCenter)
#         self.l_label.setObjectName("l_label")
#         self.ad_checkBox = QtWidgets.QCheckBox(self.centralwidget)
#         self.ad_checkBox.setGeometry(QtCore.QRect(380, 200, 61, 71))
#         sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
#         sizePolicy.setHorizontalStretch(0)
#         sizePolicy.setVerticalStretch(0)
#         sizePolicy.setHeightForWidth(self.ad_checkBox.sizePolicy().hasHeightForWidth())
#         self.ad_checkBox.setSizePolicy(sizePolicy)
#         font = QtGui.QFont()
#         font.setPointSize(14)
#         self.ad_checkBox.setFont(font)
#         self.ad_checkBox.setFocusPolicy(QtCore.Qt.WheelFocus)
#         self.ad_checkBox.setText("")
#         self.ad_checkBox.setTristate(False)
#         self.ad_checkBox.setObjectName("ad_checkBox")
#         self.bd_checkBox = QtWidgets.QCheckBox(self.centralwidget)
#         self.bd_checkBox.setGeometry(QtCore.QRect(380, 140, 61, 71))
#         sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
#         sizePolicy.setHorizontalStretch(0)
#         sizePolicy.setVerticalStretch(0)
#         sizePolicy.setHeightForWidth(self.bd_checkBox.sizePolicy().hasHeightForWidth())
#         self.bd_checkBox.setSizePolicy(sizePolicy)
#         font = QtGui.QFont()
#         font.setPointSize(14)
#         self.bd_checkBox.setFont(font)
#         self.bd_checkBox.setFocusPolicy(QtCore.Qt.WheelFocus)
#         self.bd_checkBox.setText("")
#         self.bd_checkBox.setTristate(False)
#         self.bd_checkBox.setObjectName("bd_checkBox")
#         self.bd_label = QtWidgets.QLabel(self.centralwidget)
#         self.bd_label.setGeometry(QtCore.QRect(410, 160, 91, 31))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         font.setBold(False)
#         font.setWeight(50)
#         self.bd_label.setFont(font)
#         self.bd_label.setStyleSheet("background-color: rgb(255, 255, 255);")
#         self.bd_label.setFrameShape(QtWidgets.QFrame.Box)
#         self.bd_label.setLineWidth(1)
#         self.bd_label.setTextFormat(QtCore.Qt.AutoText)
#         self.bd_label.setScaledContents(False)
#         self.bd_label.setAlignment(QtCore.Qt.AlignCenter)
#         self.bd_label.setWordWrap(True)
#         self.bd_label.setObjectName("bd_label")
#         self.ad_label = QtWidgets.QLabel(self.centralwidget)
#         self.ad_label.setGeometry(QtCore.QRect(410, 220, 91, 31))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         font.setBold(False)
#         font.setWeight(50)
#         self.ad_label.setFont(font)
#         self.ad_label.setStyleSheet("background-color: rgb(255, 255, 255);")
#         self.ad_label.setFrameShape(QtWidgets.QFrame.Box)
#         self.ad_label.setLineWidth(1)
#         self.ad_label.setTextFormat(QtCore.Qt.AutoText)
#         self.ad_label.setScaledContents(False)
#         self.ad_label.setAlignment(QtCore.Qt.AlignCenter)
#         self.ad_label.setWordWrap(True)
#         self.ad_label.setObjectName("ad_label")
#         self.d_label = QtWidgets.QLabel(self.centralwidget)
#         self.d_label.setGeometry(QtCore.QRect(380, 120, 131, 31))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         self.d_label.setFont(font)
#         self.d_label.setAlignment(QtCore.Qt.AlignCenter)
#         self.d_label.setObjectName("d_label")
#         self.bed_label = QtWidgets.QLabel(self.centralwidget)
#         self.bed_label.setGeometry(QtCore.QRect(110, 300, 131, 31))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         self.bed_label.setFont(font)
#         self.bed_label.setAlignment(QtCore.Qt.AlignCenter)
#         self.bed_label.setObjectName("bed_label")
#         self.bbed_label = QtWidgets.QLabel(self.centralwidget)
#         self.bbed_label.setGeometry(QtCore.QRect(230, 330, 91, 31))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         font.setBold(False)
#         font.setWeight(50)
#         self.bbed_label.setFont(font)
#         self.bbed_label.setStyleSheet("background-color: rgb(255, 255, 255);")
#         self.bbed_label.setFrameShape(QtWidgets.QFrame.Box)
#         self.bbed_label.setLineWidth(1)
#         self.bbed_label.setTextFormat(QtCore.Qt.AutoText)
#         self.bbed_label.setScaledContents(False)
#         self.bbed_label.setAlignment(QtCore.Qt.AlignCenter)
#         self.bbed_label.setWordWrap(True)
#         self.bbed_label.setObjectName("bbed_label")
#         self.next_pushButton = QtWidgets.QPushButton(self.centralwidget)
#         self.next_pushButton.setGeometry(QtCore.QRect(410, 330, 91, 31))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         self.next_pushButton.setFont(font)
#         self.next_pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
# "background-color: rgb(85, 170, 127);")
#         self.next_pushButton.setObjectName("next_pushButton")
#         select_meal.setCentralWidget(self.centralwidget)

#         self.retranslateUi(select_meal)
#         QtCore.QMetaObject.connectSlotsByName(select_meal)

#         def close_window():
#             select_meal.close()

#         self.back_pushButton.clicked.connect(close_window)
#         self.next_pushButton.clicked.connect(self.open_drug_list_again)

#         # ในส่วนนี้เราเพิ่มการเชื่อมต่อกับเมธอด save_checkbox_states ในปุ่มย้อนกลับ
#         self.back_pushButton.clicked.connect(self.save_checkbox_states_and_close)

#         # เพิ่มการเชื่อมต่อฐานข้อมูล SQLite3
#         self.conn = sqlite3.connect("medicine.db")
#         self.cursor = self.conn.cursor()
        
#         # สร้างตาราง Meal ถ้ายังไม่มี
#         self.cursor.execute('''
#             CREATE TABLE IF NOT EXISTS Meal (
#                 meal_id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 meal_name TEXT,
#                 time TEXT
#             )
#         ''')

#         # # เช็คว่ามีข้อมูลในตาราง Meal หรือยัง
#         # self.cursor.execute('SELECT COUNT(*) FROM Meal')
#         # count = self.cursor.fetchone()[0]

#         # if count == 0:
#         #     # สร้างรายชื่อของมื้อ
#         #     meal_names = [
#         #         "มื้อเช้า ก่อนอาหาร",
#         #         "มื้อเช้า หลังอาหาร",
#         #         "มื้อเที่ยง ก่อนอาหาร",
#         #         "มื้อเที่ยง หลังอาหาร",
#         #         "มื้อเย็น ก่อนอาหาร",
#         #         "มื้อเย็น หลังอาหาร",
#         #         "มื้อก่อนนอน"
#         #     ]

#         #     # เพิ่มรายชื่อมื้อลงในตาราง Meal
#         #     for meal_name in meal_names:
#         #         self.cursor.execute('INSERT INTO Meal (meal_name) VALUES (?)', (meal_name,))

#         #     self.conn.commit()

#         # # Load checkbox states from the database
#         # # self.load_checkbox_states()
        
#         # query = '''
#         # SELECT h.drug_id, drug_name, drug_description, drug_amount, drug_eat,
#         #        h.meal_id, meal_name, time
#         #     FROM Drug_handle AS h
#         #     LEFT JOIN Drug AS d ON h.drug_id = d.drug_id
#         #     LEFT JOIN Meal AS m ON h.meal_id = m.meal_id
#         # '''
        
#         # self.cursor.execute(query)
#         # data = self.cursor.fetchall()
        
#         # for row in data:
#         #     drug_id, drug_name, drug_description, drug_amount, drug_eat, meal_id, meal_name, time = row
#         #     # ทำต่อไปตามความต้องการ เช่น แสดงผลลัพธ์ทาง GUI หรือทำประมวลผลเพิ่มเติม
#         #     if drug_name is not None and meal_name is not None:
#         #         print(f"Drug: {drug_id}, {drug_name}, {drug_description}, {drug_amount}, {drug_eat}")
#         #         print(f"Meal: {meal_id}, {meal_name}, {time}")
#         #     else:
#         #         print("Error: Invalid data found.")

#         QtCore.QMetaObject.connectSlotsByName(select_meal)

#     def save_checkbox_states_and_close(self):
#         self.save_checkbox_states()
        
#     ####################################### แก้ไขโค้ดในส่วนนี้ด้วยจากปลื้ม ###########################################    

#     # def load_checkbox_states(self):
#     #     # Load checkbox_states from the database
#     #     self.cursor.execute('SELECT h.drug_id, h.meal_id FROM Drug_handle AS h LEFT JOIN Drug AS d ON h.drug_id = d.drug_id LEFT JOIN Meal AS m on h.meal_id = m.meal_id')
#     #     data = self.cursor.fetchall()

#     #     for drug_id, meal_id in data:
#     #         if meal_id == 1:
#     #             self.bb_checkBox.setChecked(1)
#     #         elif meal_id == 2:
#     #             self.ab_checkBox.setChecked(1)
#     #         elif meal_id == 3:
#     #             self.bl_checkBox.setChecked(1)
#     #         elif meal_id == 4:
#     #             self.al_checkBox.setChecked(1)
#     #         elif meal_id == 5:
#     #             self.bd_checkBox.setChecked(1)
#     #         elif meal_id == 6:
#     #             self.ad_checkBox.setChecked(1)
#     #         elif meal_id == 7:
#     #             self.bbed_checkBox.setChecked(1)

                
#     def save_checkbox_states(self):
#         checkbox_states = {
#             "bb_checkBox": self.bb_checkBox.isChecked(),
#             "ab_checkBox": self.ab_checkBox.isChecked(),
#             "bl_checkBox": self.bl_checkBox.isChecked(),
#             "al_checkBox": self.al_checkBox.isChecked(),
#             "bd_checkBox": self.bd_checkBox.isChecked(),
#             "ad_checkBox": self.ad_checkBox.isChecked(),
#             "bbed_checkBox": self.bbed_checkBox.isChecked()
#         }

#         # # Save checkbox_states to the database
#         # for checkbox_name, state in checkbox_states.items():
#         #     meal_id = None
#         #     if "bb_checkBox" in checkbox_name:
#         #         meal_id = 1
#         #     elif "ab_checkBox" in checkbox_name:
#         #         meal_id = 2
#         #     elif "bl_checkBox" in checkbox_name:
#         #         meal_id = 3
#         #     elif "al_checkBox" in checkbox_name:
#         #         meal_id = 4
#         #     elif "bd_checkBox" in checkbox_name:
#         #         meal_id = 5
#         #     elif "ad_checkBox" in checkbox_name:
#         #         meal_id = 6
#         #     elif "bbed_checkBox" in checkbox_name:
#         #         meal_id = 7

#             # Check if there is an existing record
#             # self.cursor.execute('SELECT * FROM Drug_handle WHERE meal_id = ? AND drug_id = ?', (meal_id, drug_id))
#             # existing_data = self.cursor.fetchone()

#             # if existing_data:
#             #     # Update the existing record
#             #     self.cursor.execute('''
#             #         UPDATE Drug_handle
#             #         SET state = ?
#             #         WHERE meal_id = ? AND h.drug_id = ?
#             #     ''', (state, meal_id, drug_id))
#             # else:
#             #     # If no existing record, insert a new one
#             #     self.cursor.execute('''
#             #         INSERT INTO Drug_handle (meal_id, drug_id, state)
#             #         VALUES (?, ?, ?)
#             #     ''', (meal_id, drug_id, state))

#         # self.conn.commit()


#     def set_drug_info(self, drug_name):
#         connection = sqlite3.connect("medicine.db")
#         cursor = connection.cursor()

#         query = '''
#         SELECT h.drug_id, drug_name, drug_description, drug_remaining, drug_eat,
#             h.meal_id, meal_name, time
#             FROM Drug_handle AS h
#             LEFT JOIN Drug AS d ON h.drug_id = d.drug_id
#             LEFT JOIN Meal AS m ON h.meal_id = m.meal_id
#             WHERE d.drug_name = ?
#         '''

#         cursor.execute(query, (drug_name,))
#         drug_info_list = cursor.fetchall()
#         connection.close()

#         for drug_info in drug_info_list:
#             drug_id, drug_name, drug_description, drug_remaining, drug_eat, meal_id, meal_name, time = drug_info

#             # Display drug and meal information
#             print(f"Drug: {drug_id}, {drug_name}, {drug_description}, {drug_remaining}, {drug_eat}")
#             print(f"Meal: {meal_id}, {meal_name}, {time}")

#             # Check the meal_id and set the corresponding checkbox
#             if meal_id == 1:
#                 self.bb_checkBox.setChecked(True)
#             elif meal_id == 2:
#                 self.ab_checkBox.setChecked(True)
#             elif meal_id == 3:
#                 self.bl_checkBox.setChecked(True)
#             elif meal_id == 4:
#                 self.al_checkBox.setChecked(True)
#             elif meal_id == 5:
#                 self.bd_checkBox.setChecked(True)
#             elif meal_id == 6:
#                 self.ad_checkBox.setChecked(True)
#             elif meal_id == 7:
#                 self.bbed_checkBox.setChecked(True)
            
#             # self.set_value.setText(str(drug_info[0]))
#         #     # drug_info[1] คือ drug_name
#         #     self.label_2.setText(drug_info[1])
#         #     # drug_info[2] คือ drug_description
#         #     self.label_3.setText(drug_info[2])
#         #     # drug_info[3] คือ drug_amount
#         #     self.label_4.setText(f"{drug_info[3]}")
#         #     # drug_info[4] คือ drug_eat
#         #     self.label_5.setText(f"{drug_info[4]}")

#     def retranslateUi(self, select_meal):
#         _translate = QtCore.QCoreApplication.translate
#         select_meal.setWindowTitle(_translate("select_meal", "เลือกมื้อ"))
#         self.meal_label.setText(_translate("select_meal", "เลือกมื้อยาที่ต้องการ"))
#         self.back_pushButton.setText(_translate("select_meal", "ย้อนกลับ"))
#         self.bb_label.setText(_translate("select_meal", "ก่อน อาหาร"))
#         self.b_label.setText(_translate("select_meal", "มื้อเช้า"))
#         self.ab_label.setText(_translate("select_meal", "หลัง อาหาร"))
#         self.bl_label.setText(_translate("select_meal", "ก่อน อาหาร"))
#         self.al_label.setText(_translate("select_meal", "หลัง อาหาร"))
#         self.l_label.setText(_translate("select_meal", "มื้อเที่ยง"))
#         self.bd_label.setText(_translate("select_meal", "ก่อน อาหาร"))
#         self.ad_label.setText(_translate("select_meal", "หลัง อาหาร"))
#         self.d_label.setText(_translate("select_meal", "มื้อเย็น"))
#         self.bed_label.setText(_translate("select_meal", "มื้อก่อนนอน"))
#         self.bbed_label.setText(_translate("select_meal", "ก่อนนอน"))
#         self.next_pushButton.setText(_translate("select_meal", "เสร็จสิ้น"))
# import resources_rc


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     select_meal = QtWidgets.QMainWindow()
#     ui = Ui_select_meal()
#     ui.setupUi(select_meal)
#     select_meal.show()
#     sys.exit(app.exec_())



