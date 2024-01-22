from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QCalendarWidget, QMessageBox
from select_meal import Ui_select_meal
from PyQt5.QtCore import QLocale
import sqlite3

class Ui_day_start(object):
    def setupUi(self, day_start, drug_List, each_drug, each_drug2, updated_data2):
        self.day_start = day_start
        self.drug_List = drug_List
        self.each_drug = each_drug
        self.each_drug2 = each_drug2
        self.updated_data2 = updated_data2
        
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
        self.next_pushButton.setGeometry(QtCore.QRect(420, 330, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.next_pushButton.setFont(font)
        self.next_pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.next_pushButton.setObjectName("next_pushButton")
        day_start.setCentralWidget(self.centralwidget)

        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(100, 100, 341, 221))
        self.calendarWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.calendarWidget.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setSelectionMode(QtWidgets.QCalendarWidget.SingleSelection)
        self.calendarWidget.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.ShortDayNames)
        self.calendarWidget.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendarWidget.setObjectName("calendarWidget")
        
        self.label_date = QtWidgets.QLabel(self.centralwidget)
        self.label_date.setGeometry(QtCore.QRect(125, 330, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_date.setFont(font)
        self.label_date.setAlignment(QtCore.Qt.AlignCenter)
        self.label_date.setObjectName("label_date")
        self.label_date.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))

        self.calendarWidget.selectionChanged.connect(self.update_selected_date)

        # Set the minimum date to the current date
        current_date = QtCore.QDate.currentDate()
        self.calendarWidget.setMinimumDate(current_date)

        self.retranslateUi(day_start)
        QtCore.QMetaObject.connectSlotsByName(day_start)

        def close_window():
            day_start.close()

        self.add_back_pushButton.clicked.connect(close_window)

        def save_changes():
            updated_data2 = self.updated_data2

            # If the user hasn't selected a date, use the current date
            if not self.date_selected:
                current_date = QtCore.QDate.currentDate()
                self.label_date.setText(current_date.toString("dddd d MMMM yyyy"))
                updated_data2['day_start'] = self.label_date.text()
            # else:
            #     updated_data2['day_start'] = self.label_date.text()

            # ส่งข้อมูลที่ถูกแก้ไขไปยังหน้าต่อไป
            self.open_select_meal(self.updated_data2)

        # def save_changes():                                                                  แบบเดิม
        #     updated_data2 = self.updated_data2
        #     updated_data2['day_start'] = self.label_date.text()


        #     # ส่งข้อมูลที่ถูกแก้ไขไปยังหน้าต่อไป
        #     self.open_select_meal(self.updated_data2)
        
        self.next_pushButton.clicked.connect(save_changes)
        # self.next_pushButton.clicked.connect(self.closeAll)

        # Initialize variable to track if the date has been selected
        self.date_selected = False

    def update_selected_date(self):
        selected_date = self.calendarWidget.selectedDate()
        
        # Check if the selected date is not in the past
        if selected_date >= QtCore.QDate.currentDate():
            self.label_date.setText(selected_date.toString("dddd d MMMM yyyy"))
            # Enable further date changes
            self.calendarWidget.setEnabled(True)
            # Update the variable to indicate that the date has been selected
            self.date_selected = True
        else:
            # Show a warning message and reset the selected date
            QMessageBox.warning(self.centralwidget, "เลือกวัน", "ไม่สามารถเลือกวันที่ผ่านมาได้")
            self.calendarWidget.setSelectedDate(QtCore.QDate.currentDate())

        if not self.date_selected:
            current_date = QtCore.QDate.currentDate()
            self.label_date.setText(current_date.toString("dddd d MMMM yyyy"))
            self.calendarWidget.setEnabled(True)
           
        



    def set_day_info(self, drug_id):
        self.drug_id = drug_id
        print(f"day_start {self.updated_data2}")

    def open_select_meal(self, updated_data2):
        if self.date_selected:
            # Save the selected date to the database
            selected_date = self.calendarWidget.selectedDate().toString("dd-MM-yyyy")
            self.save_date_to_database(selected_date, self.drug_id)

            # Open the select_meal window
            self.select_meal_window = QtWidgets.QMainWindow()
            self.select_meal_ui = Ui_select_meal()
            self.select_meal_ui.setupUi(self.select_meal_window, self.drug_List, self.each_drug, self.each_drug2, self, updated_data2)
            self.select_meal_ui.set_meal_info(self.drug_id)
            self.select_meal_window.show()

            
            self.calendarWidget.setEnabled(True)
        else:
            # Save the selected date to the database
            selected_date = self.calendarWidget.selectedDate().toString("dd-MM-yyyy")
            self.save_date_to_database(selected_date, self.drug_id)

            # Open the select_meal window
            self.select_meal_window = QtWidgets.QMainWindow()
            self.select_meal_ui = Ui_select_meal()
            self.select_meal_ui.setupUi(self.select_meal_window, self.drug_List, self.each_drug, self.each_drug2, self, updated_data2)
            self.select_meal_ui.set_meal_info(self.drug_id)
            self.select_meal_window.show()

            
            self.calendarWidget.setEnabled(True)

            # QMessageBox.warning(self.centralwidget, "เลือกวัน", "กรุณาเลือกวันก่อนดำเนินการถัดไป")
            
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
        current_date = QtCore.QDate.currentDate()
        self.label_date.setText(current_date.toString("dddd d MMMM yyyy"))
        # self.label_date.setText("เลือกวันที่เริ่มรับประทานยา")          

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    day_start = QtWidgets.QMainWindow()
    ui = Ui_day_start()
    ui.setupUi(day_start)
    day_start.show()
    sys.exit(app.exec_())