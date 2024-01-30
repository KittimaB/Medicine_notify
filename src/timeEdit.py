from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_time_Edit(object):
    def __init__(self):
        self.meal_label_text = ""
        self.connection = sqlite3.connect("medicine.db")

    def convert_thai_to_arabic(self, thai_numeral):
        thai_to_arabic_mapping = {
            '๐': '0',
            '๑': '1',
            '๒': '2',
            '๓': '3',
            '๔': '4',
            '๕': '5',
            '๖': '6',
            '๗': '7',
            '๘': '8',
            '๙': '9'
        }

        arabic_numeral = ''.join(thai_to_arabic_mapping.get(char, char) for char in thai_numeral)
        return arabic_numeral


        
    def setupUi(self, time_Edit):
        time_Edit.setObjectName("time_Edit")
        time_Edit.resize(531, 401)
        time_Edit.setStyleSheet("background-color: rgb(217, 244, 255)")
        self.centralwidget = QtWidgets.QWidget(time_Edit)
        self.centralwidget.setObjectName("centralwidget")
        self.add_back_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.add_back_pushButton.setGeometry(QtCore.QRect(40, 50, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add_back_pushButton.setFont(font)
        self.add_back_pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(166, 0, 0)")
        self.add_back_pushButton.setObjectName("add_back_pushButton")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 90, 1201, 16))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 20, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
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
        self.timeEdit_label = QtWidgets.QLabel(self.centralwidget)
        self.timeEdit_label.setGeometry(QtCore.QRect(30, 120, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.timeEdit_label.setFont(font)
        self.timeEdit_label.setAlignment(QtCore.Qt.AlignCenter)
        self.timeEdit_label.setObjectName("timeEdit_label")
        self.timeEdit_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.timeEdit_pushButton.setGeometry(QtCore.QRect(230, 280, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.timeEdit_pushButton.setFont(font)
        self.timeEdit_pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.timeEdit_pushButton.setObjectName("timeEdit_pushButton")
        self.timeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit.setGeometry(QtCore.QRect(190, 200, 171, 51))
        self.timeEdit.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.timeEdit.setObjectName("timeEdit")
        time_Edit.setCentralWidget(self.centralwidget)

        self.retranslateUi(time_Edit)
        QtCore.QMetaObject.connectSlotsByName(time_Edit)

        self.label.setText(self.meal_label_text)

        def close_window():
            time_Edit.close()

        self.add_back_pushButton.clicked.connect(close_window)

        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT time FROM Meal WHERE meal_name = ?", (self.meal_label_text,))
            result = cursor.fetchone()
            print(result)

            if result:
                stored_time_thai = result[0]
                stored_time_arabic = self.convert_thai_to_arabic(stored_time_thai)
                stored_qtime = QtCore.QTime.fromString(stored_time_arabic, "HH:mm")
                self.timeEdit.setTime(stored_qtime)
        except Exception as e:
            QtWidgets.QMessageBox.critical(time_Edit, "Error", f"เกิดข้อผิดพลาดในการดึงข้อมูล: {str(e)}")

        def save_time():
            selected_time = self.timeEdit.time().toString("HH:mm")
            print(selected_time)
            meal_name = self.meal_label_text

            try:
                cursor = self.connection.cursor()
                cursor.execute("UPDATE Meal SET time = ? WHERE meal_name = ?", (selected_time, meal_name))
                self.connection.commit()
                QtWidgets.QMessageBox.information(time_Edit, "Success", "เวลาถูกบันทึกเรียบร้อยแล้ว")

                # Retrieve the updated time from the database
                cursor.execute("SELECT time FROM Meal WHERE meal_name = ?", (meal_name,))
                result = cursor.fetchone()

                if result:
                    stored_time_thai = result[0]
                    stored_time_arabic = self.convert_thai_to_arabic(stored_time_thai)
                    stored_qtime = QtCore.QTime.fromString(stored_time_arabic, "HH:mm")
                    self.timeEdit.setTime(stored_qtime)
                    print(f"Updated time in QTimeEdit: {stored_time_arabic}")

            except Exception as e:
                QtWidgets.QMessageBox.critical(time_Edit, "Error", f"เกิดข้อผิดพลาด: {str(e)}")



        self.timeEdit_pushButton.clicked.connect(save_time)
        

    def retranslateUi(self, time_Edit):
        _translate = QtCore.QCoreApplication.translate
        time_Edit.setWindowTitle(_translate("time_Edit", "ตั้งเวลา"))
        self.add_back_pushButton.setText(_translate("time_Edit", "ย้อนกลับ"))
        self.label.setText(_translate("time_Edit", "มื้อเช้า ก่อนอาหาร"))
        self.timeEdit_label.setText(_translate("time_Edit", "เลือกเวลาที่ต้องการ"))
        self.timeEdit_pushButton.setText(_translate("time_Edit", "ยืนยัน"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    time_Edit = QtWidgets.QMainWindow()

    locale = QtCore.QLocale(QtCore.QLocale.English)
    QtCore.QLocale.setDefault(locale)
    
    ui = Ui_time_Edit()
    ui.setupUi(time_Edit)
    time_Edit.show()
    sys.exit(app.exec_())
