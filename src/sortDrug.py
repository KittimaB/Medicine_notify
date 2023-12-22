from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget
from prepare import Ui_prepare
import sqlite3

class CircularColorItem(QtWidgets.QWidget):
    def __init__(self, color, text, parent=None):
        super().__init__(parent)
        self.color = color
        self.text = text

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing, True)
        painter.setBrush(QtGui.QBrush(self.color))
        painter.drawEllipse(self.rect())

        font = painter.font()
        font.setPointSize(8)
        painter.setFont(font)
        painter.drawText(self.rect(), QtCore.Qt.AlignCenter, self.text)

class Ui_sortDrug(object):
    def setupUi(self, sortDrug):
        sortDrug.setObjectName("sortDrug")
        sortDrug.setEnabled(True)
        sortDrug.resize(531, 401)
        sortDrug.setStyleSheet("background-color: rgb(217, 244, 255)")
        self.centralwidget = QtWidgets.QWidget(sortDrug)
        self.centralwidget.setObjectName("centralwidget")
        self.add_back_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.add_back_pushButton.setGeometry(QtCore.QRect(30, 31, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add_back_pushButton.setFont(font)
        self.add_back_pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(166, 0, 0)")
        self.add_back_pushButton.setObjectName("add_back_pushButton")
        self.sort_label = QtWidgets.QLabel(self.centralwidget)
        self.sort_label.setGeometry(QtCore.QRect(130, 11, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.sort_label.setFont(font)
        self.sort_label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.sort_label.setFrameShape(QtWidgets.QFrame.Box)
        self.sort_label.setLineWidth(1)
        self.sort_label.setTextFormat(QtCore.Qt.AutoText)
        self.sort_label.setScaledContents(False)
        self.sort_label.setAlignment(QtCore.Qt.AlignCenter)
        self.sort_label.setWordWrap(True)
        self.sort_label.setObjectName("sort_label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-10, 62, 551, 20))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.next_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.next_pushButton.setGeometry(QtCore.QRect(440, 31, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.next_pushButton.setFont(font)
        self.next_pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.next_pushButton.setObjectName("next_pushButton")
        sortDrug.setCentralWidget(self.centralwidget)

        # Set up the table widget
        self.setup_table_widget()

        self.retranslateUi(sortDrug)
        QtCore.QMetaObject.connectSlotsByName(sortDrug)

        def close_window():
            sortDrug.close()
            
        self.add_back_pushButton.clicked.connect(close_window)

        self.next_pushButton.clicked.connect(self.open_prepare)
        
        self.sort_handle()

    def open_prepare(self):
        self.prepare_window = QtWidgets.QMainWindow()
        self.prepare_ui = Ui_prepare()
        self.prepare_ui.setupUi(self.prepare_window)
        self.prepare_window.show()
            
    def get_color_text_mapping(meal_ids):
        color_mapping = {
            1: (255, 255, 102),  # เช้าก่อน (Yellow)
            2: (255, 192, 203),  # เช้าหลัง (Pink)
            3: (178, 255, 102),  # เที่ยงก่อน (Green)
            4: (255, 178, 102),  # เที่ยงหลัง (Orange)
            5: (102, 255, 255),  # เย็นก่อน (Blue)
            6: (204, 153, 255),  # เย็นหลัง (Purple)
            7: (255, 102, 102)   # ก่อนนอน (Red)
        }

        return {color_mapping[meal_id]: f"Meal {meal_id}" for meal_id in meal_ids}

    def setup_table_widget(self):
        # สร้างและกำหนด QTableWidget
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(25, 76, 483, 316))                         
        self.tableWidget.setObjectName("tableWidget")
        row_max = 6
        col_max = 6

        # กำหนดหัวข้อคอลัมน์ในตาราง
        self.tableWidget.setColumnCount(col_max)
        self.tableWidget.setHorizontalHeaderLabels(["Column 1", "Column 2", "Column 3", "Column 4", "Column 5", "Column 6"])
        
        # กำหนดจำนวนแถวในตารางตามจำนวนรายการยาที่ดึงมาจากฐานข้อมูล
        self.tableWidget.setRowCount(row_max)

        cell_size = 58  # You can adjust this value as needed
        for col_idx in range(col_max):
            self.tableWidget.setColumnWidth(col_idx, cell_size)
        for row_idx in range(row_max):
            self.tableWidget.setRowHeight(row_idx, cell_size)

        # Set up the color-text associations using RGB tuples
        color_text_mapping = {
            (255, 255, 102): "เช้าก่อน",    # สีเหลือง
            (255, 192, 203): "เช้าหลัง",    # สีชมพู
            (178, 255, 102): "เที่ยงก่อน",   # สีเขียว
            (255, 178, 102): "เที่ยงหลัง",   # สีส้ม
            (102, 255, 255): "เย็นก่อน",    # สีฟ้า
            (204, 153, 255): "เย็นหลัง",    # สีม่วง
            (255, 102, 102): "ก่อนนอน"    # สีแดง
        }

        color_index = 0

        for row in range(row_max):
            for col in range(col_max):
                # color = (255, 255, 0)  # Default color is yellow
                if color_index < len(color_text_mapping):
                    color = list(color_text_mapping.keys())[color_index]

                circular_item = CircularColorItem(QtGui.QColor(*color), color_text_mapping[color])
                self.tableWidget.setCellWidget(row, col, circular_item)

                color_index = (color_index + 1) % len(color_text_mapping)  # Rotate colors
                
    def sort_handle(self):
        connection = sqlite3.connect("medicine.db")
        cursor = connection.cursor()

        query = '''
        SELECT  h.drug_id, drug_name, drug_description, drug_remaining, drug_remaining_meal, fraction, external_drug, internal_drug, drug_eat, all_drug_recieve, day_start, drug_log, 
                h.meal_id, meal_name, time
            FROM Drug_handle AS h
            LEFT JOIN Drug AS d ON h.drug_id = d.drug_id
            LEFT JOIN Meal AS m ON h.meal_id = m.meal_id
        '''

        cursor.execute(query)
        drug_info_list = cursor.fetchall()
        

        for drug_info in drug_info_list:
            drug_id, drug_name, drug_description, drug_remaining, drug_remaining_meal, fraction, external_drug, internal_drug, drug_eat, all_drug_recieve, day_start, drug_log, meal_id, meal_name, time = drug_info

            
            drug_remaining_meal = drug_remaining / drug_eat                 # คำนวณจำนวนมื้อทั้งหมดที่คงเหลือทั้งหมด
            drug_remaining_meal = int(drug_remaining_meal)                  # แปลงเป็นจำนวนเต็ม
            fraction = drug_remaining % drug_eat                            # คำนวณจำนวนเศษยาที่ไม่ลงตัวกับจำนวนยาที่กิน
            external_drug = int(drug_remaining_meal)                        # แปลงเป็นจำนวนเต็ม
            
            # Update external_drug with drug_remaining
            cursor.execute(f"UPDATE Drug SET drug_remaining_meal = {drug_remaining_meal}, fraction = {fraction}, external_drug = {external_drug}, internal_drug = 0 WHERE drug_id = {drug_id}")
            connection.commit()

            # Fetch updated drug information after the update
            cursor.execute(f"SELECT * FROM Drug WHERE drug_id = {drug_id}")
            updated_drug_info = cursor.fetchone()
            drug_id, drug_name, drug_description, drug_remaining, drug_remaining_meal, fraction, external_drug, internal_drug, drug_eat, all_drug_recieve, day_start, drug_log = updated_drug_info

            # Display updated drug and meal information
            print(f"Drug: {drug_id}, {drug_name}, {drug_description}, {drug_remaining}, {drug_remaining_meal}, {fraction}, {external_drug}, {internal_drug}, {drug_eat}, {all_drug_recieve}, {day_start}, {drug_log}")
            print(f"Meal: {meal_id}, {meal_name}, {time}")
            print(f"ยา: {drug_name} และรับประทาน{meal_name}")
            print("=============================================================================")
        print("\n")
        connection.close()
        
        check_meal = 1
        slot = 1
        
        
        while(slot <= 30):
            connection = sqlite3.connect("medicine.db")
            cursor = connection.cursor()
            query = '''
                SELECT  h.drug_id, drug_name, drug_description, drug_remaining, drug_remaining_meal, fraction, external_drug, internal_drug, drug_eat, all_drug_recieve, day_start, drug_log, 
                        h.meal_id, meal_name, time
                    FROM Drug_handle AS h
                    LEFT JOIN Drug AS d ON h.drug_id = d.drug_id
                    LEFT JOIN Meal AS m ON h.meal_id = m.meal_id
                WHERE h.meal_id = ?
                '''
                    
            cursor.execute(query, (check_meal,))   
            drug_info_list = cursor.fetchall()
            
            if drug_info_list:
                print(f"ลำดับ: {slot}, ยา{drug_info_list[0][13]}\n")
                print("ประกอบไปด้วย")
                have_drug = False
                for drug_info in drug_info_list:
                    drug_id, drug_name, drug_description, drug_remaining, drug_remaining_meal, fraction, external_drug, internal_drug, drug_eat, all_drug_recieve, day_start, drug_log, meal_id, meal_name, time = drug_info

                    
                    if external_drug != 0:
                        print(f"- {drug_name}")
                        
                        # print(f"    มื้อยานอกเครื่อง:{external_drug} (ก่อน update)")
                        # print(f"    มื้อยาในเครื่อง:{internal_drug} (ก่อน update)")
                        # print("-----------------------")
                        
                        external_drug -= 1
                        internal_drug += 1
                        
                        cursor.execute(f"UPDATE Drug SET external_drug = {external_drug}, internal_drug = {internal_drug} WHERE drug_id = {drug_id}")
                        connection.commit()
                        
                        print(f"    มื้อยานอกเครื่อง:{external_drug} (หลัง update)")
                        print(f"    มื้อยาในเครื่อง:{internal_drug} (หลัง update)")
                        
                        have_drug = True
                    else:
                        print("     หมด")
                        
                        
                    
                print("============================================================================")
                
                if have_drug:
                    slot += 1
                check_meal += 1
                
            else:
                check_meal += 1
                
            if check_meal > 7:
                check_meal = 1
            
        connection.close()



    def retranslateUi(self, sortDrug):
        _translate = QtCore.QCoreApplication.translate
        sortDrug.setWindowTitle(_translate("sortDrug", "วิธีเรียงกล่องบรรจุยา"))
        self.add_back_pushButton.setText(_translate("sortDrug", "ย้อนกลับ"))
        self.sort_label.setText(_translate("sortDrug", "วิธีเรียงกล่องบรรจุยา"))
        self.next_pushButton.setText(_translate("prepare", "ถัดไป"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    sortDrug = QtWidgets.QMainWindow()
    ui = Ui_sortDrug()
    ui.setupUi(sortDrug)
    sortDrug.show()
    sys.exit(app.exec_())
