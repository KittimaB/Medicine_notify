from Utils import *
from UI_Generate import *
width, height = Scale_Width_Height()

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sqlite3

row_max = 5     # แถวของกล่องยา                                  # กำหนดจำนวน row ของยา
col_max = 8     # จำนวนลูกบอลที่ใส่ได้ในแต่ละแถว                      # กำหนดจำนวน col ของยา
current_ball_index = 0
class CircularColorItem(QtWidgets.QWidget):
    def __init__(self, color, text, parent=None):
        super().__init__(parent)
        self.color = color
        self.text = text["text"]
        self.enabled = text["enabled"]

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing, True)
        if self.enabled:
            painter.setBrush(QtGui.QBrush(self.color))
        else:
            painter.setBrush(QtGui.QBrush(QtGui.QColor(200, 200, 200)))  # You can adjust this color as needed
        painter.drawEllipse(self.rect())

        font = painter.font()
        font.setPointSize(int(8 * height))
        painter.setFont(font)
        painter.drawText(self.rect(), QtCore.Qt.AlignCenter, self.text)


class Ui_prepare(object):
    def setupUi(self, prepare):
        UI_instance.Set(prepare)
        show_widget_fullscreen(prepare)

        prepare.setObjectName("prepare")
        prepare.resize(int(683 * width), int(400 * height))
        prepare.setStyleSheet("\n"
"background-color: rgb(23, 73, 110);")
        self.centralwidget = QtWidgets.QWidget(prepare)
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
        self.prepare_label = QtWidgets.QLabel(self.frame)
        self.prepare_label.setGeometry(QtCore.QRect(int(200 * width), int(70 * height), int(281 * width), int(51 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(14 * height))
        font.setBold(True)
        font.setWeight(int(75 * width))
        self.prepare_label.setFont(font)
        self.prepare_label.setStyleSheet("border-radius: 16px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(23, 73, 110);")
         # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.prepare_label)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.prepare_label.setGraphicsEffect(shadow)
        self.prepare_label.setFrameShape(QtWidgets.QFrame.Box)
        self.prepare_label.setLineWidth(int(1 * width))
        self.prepare_label.setTextFormat(QtCore.Qt.AutoText)
        self.prepare_label.setScaledContents(False)
        self.prepare_label.setAlignment(QtCore.Qt.AlignCenter)
        self.prepare_label.setWordWrap(True)
        self.prepare_label.setObjectName("prepare_label")
        self.img_label = QtWidgets.QLabel(self.frame)
        self.img_label.setGeometry(QtCore.QRect(int(250 * width), int(80 * height), int(37 * width), int(31 * height)))
        self.img_label.setText("")
        self.img_label.setPixmap(QtGui.QPixmap(":/icons/sort_icon.png"))
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
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(int(30 * width), int(80 * height), int(201 * width), int(301 * height)))
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
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(int(10 * width), int(10 * height), int(181 * width), int(281 * height)))
        self.frame_3.setStyleSheet("border-radius: 9px;\n"
"background-color: rgb(170, 203, 223);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setGeometry(QtCore.QRect(int(20 * width), int(10 * height), int(151 * width), int(21 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.listWidget = QtWidgets.QListWidget(self.frame_3)
        self.listWidget.setGeometry(QtCore.QRect(int(10 * width), int(40 * height), int(161 * width), int(231 * height)))
        self.listWidget.setStyleSheet("border-radius: 9px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.listWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.listWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.listWidget.setLineWidth(int(1 * width))
        self.listWidget.setObjectName("listWidget")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(int(250 * width), int(80 * height), int(401 * width), int(301 * height)))
        self.frame_4.setStyleSheet("border-radius: 16px;\n"
"background-color: rgb(236, 236, 236);")
         # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.frame_4)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.frame_4.setGraphicsEffect(shadow)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setGeometry(QtCore.QRect(int(30 * width), int(10 * height), int(191 * width), int(21 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.previous_pushButton = QtWidgets.QPushButton(self.frame_4)
        self.previous_pushButton.setGeometry(QtCore.QRect(int(210 * width), int(5 * height), int(71 * width), int(31 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        self.previous_pushButton.setFont(font)
        self.previous_pushButton.setStyleSheet("border-radius: 9px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(115, 172, 131);")
         # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.previous_pushButton)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.previous_pushButton.setGraphicsEffect(shadow)
        self.previous_pushButton.setObjectName("previous_pushButton")
        self.next_pushButton = QtWidgets.QPushButton(self.frame_4)
        self.next_pushButton.setGeometry(QtCore.QRect(int(300 * width), int(5 * height), int(71 * width), int(31 * height)))
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

        prepare.setCentralWidget(self.centralwidget)

        # Set up the table widget
        self.setup_table_widget()

        self.selected_ball_index = -1

        self.retranslateUi(prepare)
        QtCore.QMetaObject.connectSlotsByName(prepare)

        self.add_back_pushButton.clicked.connect(self.backpage)

        # Set up button press and release styling
        self.add_back_pushButton.pressed.connect(lambda: self.set_button_pressed_style(self.add_back_pushButton))
        self.add_back_pushButton.released.connect(lambda: self.set_button_released_style(self.add_back_pushButton))

        self.next_pushButton.pressed.connect(lambda: self.set_button_pressed_style(self.next_pushButton))
        self.next_pushButton.released.connect(lambda: self.set_button_released_style(self.next_pushButton))

        self.previous_pushButton.pressed.connect(lambda: self.set_button_pressed_style2(self.previous_pushButton))
        self.previous_pushButton.released.connect(lambda: self.set_button_released_style2(self.previous_pushButton))

        # self.next_pushButton.clicked.connect(self.next_pushButton_clicked)                                                           ตรงนี้
        # self.add_back_pushButton.clicked.connect(self.add_back_pushButton_clicked)

        self.previous_pushButton.clicked.connect(self.move_to_previous_ball)
        self.next_pushButton.clicked.connect(self.move_to_next_ball)

         # Add a counter for the "ถัดไป" button press
        self.next_button_press_count = 0

        # self.sort_handle()
        # self.update_ball_colors()

    # def next_pushButton_clicked(self):
    #     global current_ball_index
    #     current_ball_index = (current_ball_index + 1) % (row_max * col_max)                                                          ตรงนี้
    #     self.sort_handle()

    # def add_back_pushButton_clicked(self):
    #     global current_ball_index
    #     current_ball_index = (current_ball_index - 1) % (row_max * col_max)
    #     self.sort_handle()
        
    
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

    def set_button_pressed_style2(self, button):
        button.setStyleSheet(
            "border-radius: 9px;\n"
            "color: rgb(0, 0, 0);\n"
            "background-color: rgb(200, 200, 200);"  # Change color when pressed
        )

    def set_button_released_style2(self, button):
        button.setStyleSheet(
            "border-radius: 9px;\n"
            "color: rgb(0, 0, 0);\n"
            "background-color: rgb(115, 172, 131);"
        )

    def move_to_previous_ball(self):
        if self.next_button_press_count > 0:
            self.next_button_press_count -= 1
            self.update_ball_colors()

    def backpage(self):
        from sortDrug import Ui_sortDrug
        backpage_form = UI_Genarate()
        backpage_form.widgetSet(UI_instance.Get(), Ui_sortDrug)

    def move_to_next_ball(self):
        if self.next_button_press_count >= 40:
            # Display a warning message after 40 presses
            QtWidgets.QMessageBox.warning(self.centralwidget, "คำเตือน", "คุณได้กดปุ่มถัดไปเกินจำนวนที่กำหนด")
            return

        self.next_button_press_count += 1
        self.update_ball_colors()

    def update_ball_colors(self):
        connection = sqlite3.connect("medicine.db")
        cursor = connection.cursor()
        query = '''
            SELECT  h.drug_id, drug_name, drug_description, drug_remaining, drug_remaining_meal, fraction, external_drug, internal_drug, drug_eat, all_drug_recieve, day_start, drug_log, drug_new, drug_size,
                    h.meal_id, meal_name, time
                FROM Drug_handle AS h
                LEFT JOIN Drug AS d ON h.drug_id = d.drug_id
                LEFT JOIN Meal AS m ON h.meal_id = m.meal_id
            '''

        cursor.execute(query)
        drug_info_list = cursor.fetchall()
        connection.close()

        if drug_info_list:
            sorted_drug_info_list = sorted(drug_info_list, key=lambda x: x[14])  # Sort by meal_id

            # Keep track of displayed meal_ids and the last row and column
            displayed_meal_ids = set()
            last_row, last_col = 0, 0

            for ball_index, current_drug_info in enumerate(sorted_drug_info_list):
                meal_id = current_drug_info[14]

                if meal_id not in displayed_meal_ids:
                    displayed_meal_ids.add(meal_id)
                    meal_time = f"{current_drug_info[15]} {current_drug_info[16]}"

                    meal_id_color_mapping = {
                        1: (255, 102, 102),
                        2: (255, 178, 102),
                        3: (255, 255, 102),
                        4: (178, 255, 102),
                        5: (102, 255, 102),
                        6: (102, 255, 255),
                        7: (0, 180, 255)
                    }

                    color = meal_id_color_mapping.get(meal_id, (200, 200, 200))
                    color_text_mapping = {"text": f"{meal_time}", "enabled": ball_index == self.next_button_press_count - 1}
                    circular_item = CircularColorItem(QtGui.QColor(*color), color_text_mapping)
                    self.tableWidget.setCellWidget(last_row, last_col, circular_item)

                    last_col += 1
                    if last_col >= col_max:
                        last_col = 0
                        last_row += 1

            # Update listWidget with unique medicine names for the selected meal
            if self.next_button_press_count <= len(sorted_drug_info_list):
                current_drug_info = sorted_drug_info_list[self.next_button_press_count - 1]
                selected_meal_id = current_drug_info[14]

                unique_drug_names_for_meal = set()  # Use a set to store unique drug names
                for info in sorted_drug_info_list:
                    if info[14] == selected_meal_id:
                        unique_drug_names_for_meal.add(f"{info[1]} - {info[15]}")

                self.listWidget.clear()
                self.listWidget.addItems(list(unique_drug_names_for_meal))  # Add unique drug names to listWidget






    

    def setup_table_widget(self):
        # สร้างและกำหนด QTableWidget
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(int(260 * width), int(120 * height), int(381 * width), int(251 * height)))                        
        self.tableWidget.setObjectName("tableWidget")

        # Set the background color of the table to white and text color to black
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);")
        shadow = QGraphicsDropShadowEffect(self.tableWidget)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.tableWidget.setGraphicsEffect(shadow)


        # กำหนดหัวข้อคอลัมน์ในตาราง
        self.tableWidget.setColumnCount(col_max)
        # self.tableWidget.setHorizontalHeaderLabels(["Column 1", "Column 2", "Column 3", "Column 4", "Column 5", "Column 6"])
        
        # กำหนดจำนวนแถวในตารางตามจำนวนรายการยาที่ดึงมาจากฐานข้อมูล
        self.tableWidget.setRowCount(row_max)

        cell_size = 62  # You can adjust this value as needed
        for col_idx in range(col_max):
            self.tableWidget.setColumnWidth(col_idx, cell_size)
        for row_idx in range(row_max):
            self.tableWidget.setRowHeight(row_idx, cell_size)
                 
                
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
            drug_id, drug_name, drug_description, drug_remaining, drug_remaining_meal, fraction, external_drug, internal_drug, drug_eat, all_drug_recieve, day_start, drug_log, drug_new, drug_size = updated_drug_info

          
        connection.close()
        
        check_meal = 1
        slot = 1
        
        cursor_row = 0
        cursor_col = 0
        check_all = 1
        while(slot <= row_max * col_max):
            connection = sqlite3.connect("medicine.db")
            cursor = connection.cursor()
            query = '''
                SELECT  h.drug_id, drug_name, drug_description, drug_remaining, drug_remaining_meal, fraction, external_drug, internal_drug, drug_eat, all_drug_recieve, day_start, drug_log, drug_new, drug_size,
                        h.meal_id, meal_name, time
                    FROM Drug_handle AS h
                    LEFT JOIN Drug AS d ON h.drug_id = d.drug_id
                    LEFT JOIN Meal AS m ON h.meal_id = m.meal_id
                WHERE h.meal_id = ?
                '''
            
            # print(check_meal)
            cursor.execute(query, (check_meal,))   
            drug_info_list = cursor.fetchall()
            
            if not drug_info_list:
                pass
                # print(f"check all:{check_all}")
                
                if check_all == 7:
                    QtWidgets.QMessageBox.warning(self.centralwidget, "คำเตือน", "ไม่พบข้อมูลยา")
                    return
                check_all += 1
                

            if drug_info_list:
                check_all = 1
             
                have_drug = False
                
                color_text_mapping = {
                    (255, 102, 102): {"text": "เช้าก่อน", "enabled": True},    # สีแดง
                    (255, 178, 102): {"text": "เช้าหลัง", "enabled": True},   # สีส้ม
                    (255, 255, 102): {"text": "เที่ยงก่อน", "enabled": True},    # สีเหลือง
                    (178, 255, 102): {"text": "เที่ยงหลัง", "enabled": True},   # สีเขียวอ่อน
                    (102, 255, 102): {"text": "เย็นก่อน", "enabled": True},   # สีเขียวเข้ม
                    (102, 255, 255): {"text": "เย็นหลัง", "enabled": True},    # สีฟ้า
                    (0, 180, 255): {"text": "ก่อนนอน", "enabled": True}    # สีน้ำเงิน
                }

                color_index = drug_info_list[0][14] - 1

                if color_index < len(color_text_mapping):
                    color = list(color_text_mapping.keys())[color_index]

                circular_item = CircularColorItem(QtGui.QColor(*color), color_text_mapping[color])
                self.tableWidget.setCellWidget(cursor_col, cursor_row, circular_item)
                
                
                print(drug_info_list[0][15])
                for drug_info in drug_info_list:
                    drug_id, drug_name, drug_description, drug_remaining, drug_remaining_meal, fraction, external_drug, internal_drug, drug_eat, all_drug_recieve, day_start, drug_log, drug_new, drug_size, meal_id, meal_name, time = drug_info
                    
                    if external_drug != 0:
                        print(f"- {drug_name}")
                        
                        # print(f"    มื้อยานอกเครื่อง:{external_drug} (ก่อน update)")
                        # print(f"    มื้อยาในเครื่อง:{internal_drug} (ก่อน update)")
                        # print("-----------------------")
                        
                        external_drug -= 1
                        internal_drug += 1
                        
                        cursor.execute(f"UPDATE Drug SET external_drug = {external_drug}, internal_drug = {internal_drug} WHERE drug_id = {drug_id}")
                        connection.commit()
                        
                        # print(f"    มื้อยานอกเครื่อง:{external_drug} (หลัง update)")
                        # print(f"    มื้อยาในเครื่อง:{internal_drug} (หลัง update)")
                        
                        have_drug = True
                        
                    else:
                        # print("     หมด")
                        pass
                        
                query = '''
                SELECT  h.drug_id, drug_name, drug_description, drug_remaining, drug_remaining_meal, fraction, external_drug, internal_drug, drug_eat, all_drug_recieve, day_start, drug_log, drug_new, drug_size,
                        h.meal_id, meal_name, time
                    FROM Drug_handle AS h
                    LEFT JOIN Drug AS d ON h.drug_id = d.drug_id
                    LEFT JOIN Meal AS m ON h.meal_id = m.meal_id
                '''
                    
                cursor.execute(query)   
                drug_info_list = cursor.fetchall()
                
                
                for drug_info in drug_info_list:
                    drug_info[6] == 0
                    # print(f"\nชื่อยา:{drug_info[1]}\nยานอกเครื่อง:{drug_info[6]}\n")
            
                all_drugs_empty = all(drug_info[6] == 0 for drug_info in drug_info_list)

                if all_drugs_empty:
                    # print("ทุกยามยาหมดแล้ว")
                    slot = (row_max * col_max) + 1
                else:
                    # print("ยังมียาที่ยังไม่หมด")
                    pass
                    
                # print("============================================================================")
                
                if have_drug:                                           # เช็คว่ามียาไหม
                    slot += 1
                    cursor_row += 1

                    # Update listWidget with medicine names and meal times for the current ball
                    current_drug_info = drug_info_list[current_ball_index]

                    drug_name = current_drug_info[1]
                    meal_time = f"{current_drug_info[15]} {current_drug_info[16]}"

                    self.listWidget.clear()
                    self.listWidget.addItem(f"กรุณากดปุ่มถัดไปเพื่อจัดเรียงยา")
                
                row_new = (col_max - row_max) - 1
                col_new = (row_max - col_max) - 1
                
                if cursor_row > row_max + row_new:                      # คำนวณตำแหน่งของ row
                    cursor_row = 0
                    cursor_col += 1
                if cursor_col > col_max + col_new:                      # คำนวณตำแหน่งของ col
                    cursor_col = 0
                check_meal += 1
            
            else:
                check_meal += 1    
                
            if check_meal > 7:
                check_meal = 1
            
        connection.close()

    def retranslateUi(self, prepare):
        _translate = QtCore.QCoreApplication.translate
        prepare.setWindowTitle(_translate("prepare", "เตรียมบอล"))
        self.prepare_label.setText(_translate("prepare", "เตรียมบอล"))
        self.add_back_pushButton.setText(_translate("prepare", "ย้อนกลับ"))
        self.label.setText(_translate("prepare", "รายชื่อยาที่ต้องเตรียม"))
        self.label_2.setText(_translate("prepare", "วางตามช่องที่แสดง"))
        self.next_pushButton.setText(_translate("prepare", "ถัดไป"))
        self.previous_pushButton.setText(_translate("prepare", "ก่อนหน้า"))
import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    prepare = QtWidgets.QMainWindow()
    ui = Ui_prepare()
    ui.setupUi(prepare) 
    prepare.show()
    sys.exit(app.exec_())

# from Utils import Scale_Width_Height, show_widget_fullscreen
# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtWidgets import QGraphicsDropShadowEffect
# import sqlite3

# row_max = 5     # แถวของกล่องยา                                  # กำหนดจำนวน row ของยา
# col_max = 8     # จำนวนลูกบอลที่ใส่ได้ในแต่ละแถว                      # กำหนดจำนวน col ของยา
# current_ball_index = 0
# class CircularColorItem(QtWidgets.QWidget):
#     def __init__(self, color, text, parent=None):
#         super().__init__(parent)
#         self.color = color
#         self.text = text["text"]
#         self.enabled = text["enabled"]

#     def paintEvent(self, event):
#         width, height = Scale_Width_Height()
#         painter = QtGui.QPainter(self)
#         painter.setRenderHint(QtGui.QPainter.Antialiasing, True)
#         if self.enabled:
#             painter.setBrush(QtGui.QBrush(self.color))
#         else:
#             painter.setBrush(QtGui.QBrush(QtGui.QColor(200, 200, 200)))  # You can adjust this color as needed
#         painter.drawEllipse(self.rect())

#         font = painter.font()
#         font.setPointSize(int(8 * height))
#         painter.setFont(font)
#         painter.drawText(self.rect(), QtCore.Qt.AlignCenter, self.text)


# class Ui_prepare(object):
#     def setupUi(self, prepare):
#         width, height = Scale_Width_Height()
#         show_widget_fullscreen(prepare)

#         prepare.setObjectName("prepare")
#         prepare.resize(int(683 * width), int(400 * height))
#         prepare.setStyleSheet("\n"
# "background-color: rgb(23, 73, 110);")
#         self.centralwidget = QtWidgets.QWidget(prepare)
#         self.centralwidget.setObjectName("centralwidget")
#         self.frame = QtWidgets.QFrame(self.centralwidget)
#         self.frame.setGeometry(QtCore.QRect(0, -60 * height, int(683 * width), int(131 * height)))
#         self.frame.setStyleSheet("border-radius: 40px;\n"
# "background-color: rgb(255, 255, 255);")
#          # Add drop shadow effect to the button
#         shadow = QGraphicsDropShadowEffect(self.frame)
#         shadow.setBlurRadius(int(8 * height))
#         shadow.setColor(QtGui.QColor(0, 0, 0, 100))
#         shadow.setOffset(0, int(2 * height))
#         self.frame.setGraphicsEffect(shadow)
#         self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.frame.setObjectName("frame")
#         self.prepare_label = QtWidgets.QLabel(self.frame)
#         self.prepare_label.setGeometry(QtCore.QRect(int(200 * width), int(70 * height), int(281 * width), int(51 * height)))
#         font = QtGui.QFont()
#         font.setPointSize(int(14 * height))
#         font.setBold(True)
#         font.setWeight(75)
#         self.prepare_label.setFont(font)
#         self.prepare_label.setStyleSheet("border-radius: 16px;\n"
# "color: rgb(255, 255, 255);\n"
# "background-color: rgb(23, 73, 110);")
#          # Add drop shadow effect to the button
#         shadow = QGraphicsDropShadowEffect(self.prepare_label)
#         shadow.setBlurRadius(int(8 * height))
#         shadow.setColor(QtGui.QColor(0, 0, 0, 100))
#         shadow.setOffset(0, int(2 * height))
#         self.prepare_label.setGraphicsEffect(shadow)
#         self.prepare_label.setFrameShape(QtWidgets.QFrame.Box)
#         self.prepare_label.setLineWidth(1)
#         self.prepare_label.setTextFormat(QtCore.Qt.AutoText)
#         self.prepare_label.setScaledContents(False)
#         self.prepare_label.setAlignment(QtCore.Qt.AlignCenter)
#         self.prepare_label.setWordWrap(True)
#         self.prepare_label.setObjectName("prepare_label")
#         self.img_label = QtWidgets.QLabel(self.frame)
#         self.img_label.setGeometry(QtCore.QRect(int(230 * width), int(80 * height), int(37 * width), int(31 * height)))
#         self.img_label.setText("")
#         self.img_label.setPixmap(QtGui.QPixmap(":/icons/sort_icon.png"))
#         self.img_label.setScaledContents(True)
#         self.img_label.setAlignment(QtCore.Qt.AlignCenter)
#         self.img_label.setObjectName("img_label")
#         self.add_back_pushButton = QtWidgets.QPushButton(self.frame)
#         self.add_back_pushButton.setGeometry(QtCore.QRect(int(50 * width), int(80 * height), int(81 * width), int(31 * height)))
#         font = QtGui.QFont()
#         font.setPointSize(int(12 * height))
#         self.add_back_pushButton.setFont(font)
#         self.add_back_pushButton.setStyleSheet("border-radius: 9px;\n"
# "color: rgb(0, 0, 0);\n"
# "background-color: rgb(244, 212, 99);")
#          # Add drop shadow effect to the button
#         shadow = QGraphicsDropShadowEffect(self.add_back_pushButton)
#         shadow.setBlurRadius(int(8 * height))
#         shadow.setColor(QtGui.QColor(0, 0, 0, 100))
#         shadow.setOffset(0, int(2 * height))
#         self.add_back_pushButton.setGraphicsEffect(shadow)
#         self.add_back_pushButton.setObjectName("add_back_pushButton")
#         self.frame_2 = QtWidgets.QFrame(self.centralwidget)
#         self.frame_2.setGeometry(QtCore.QRect(int(30 * width), int(80 *height), int(201 * width), int(301 * height)))
#         self.frame_2.setStyleSheet("border-radius: 16px;\n"
# "background-color: rgb(236, 236, 236);")
#          # Add drop shadow effect to the button
#         shadow = QGraphicsDropShadowEffect(self.frame_2)
#         shadow.setBlurRadius(int(8 * height))
#         shadow.setColor(QtGui.QColor(0, 0, 0, 100))
#         shadow.setOffset(0, int(2 * height))
#         self.frame_2.setGraphicsEffect(shadow)
#         self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.frame_2.setObjectName("frame_2")
#         self.frame_3 = QtWidgets.QFrame(self.frame_2)
#         self.frame_3.setGeometry(QtCore.QRect(int(10 * width), int(10 * height), int(181 * width), int(281 * height)))
#         self.frame_3.setStyleSheet("border-radius: 9px;\n"
# "background-color: rgb(170, 203, 223);")
#         self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.frame_3.setObjectName("frame_3")
#         self.label = QtWidgets.QLabel(self.frame_3)
#         self.label.setGeometry(QtCore.QRect(int(20 * width), int(10 * height), int(151 * width), int(21 * height)))
#         font = QtGui.QFont()
#         font.setPointSize(int(12* height))
#         self.label.setFont(font)
#         self.label.setObjectName("label")
#         self.listWidget = QtWidgets.QListWidget(self.frame_3)
#         self.listWidget.setGeometry(QtCore.QRect(int(10 * width), int(40 * height), int(161 * width), int(231 *height)))
#         font = QtGui.QFont()
#         font.setPointSize(int(11 * height))
#         self.listWidget.setFont(font)
#         self.listWidget.setStyleSheet("border-radius: 9px;\n"
# "color: rgb(0, 0, 0);\n"
# "background-color: rgb(255, 255, 255);\n"
# "")
#         self.listWidget.setFrameShape(QtWidgets.QFrame.Box)
#         self.listWidget.setFrameShadow(QtWidgets.QFrame.Plain)
#         self.listWidget.setLineWidth(int(1 * height))
#         self.listWidget.setObjectName("listWidget")
#         self.frame_4 = QtWidgets.QFrame(self.centralwidget)
#         self.frame_4.setGeometry(QtCore.QRect(int(250 * width), int(80 * height), int(401 * width), int(301 * height)))
#         self.frame_4.setStyleSheet("border-radius: 16px;\n"
# "background-color: rgb(236, 236, 236);")
#          # Add drop shadow effect to the button
#         shadow = QGraphicsDropShadowEffect(self.frame_4)
#         shadow.setBlurRadius(int(8 * height))
#         shadow.setColor(QtGui.QColor(0, 0, 0, 100))
#         shadow.setOffset(0, int(2 * height))
#         self.frame_4.setGraphicsEffect(shadow)
#         self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.frame_4.setObjectName("frame_4")
#         self.label_2 = QtWidgets.QLabel(self.frame_4)
#         self.label_2.setGeometry(QtCore.QRect(int(30 * width), int(10 * height), int(191 * width), int(21 * height)))
#         font = QtGui.QFont()
#         font.setPointSize(int(12 * height))
#         self.label_2.setFont(font)
#         self.label_2.setObjectName("label_2")
#         self.previous_pushButton = QtWidgets.QPushButton(self.frame_4)
#         self.previous_pushButton.setGeometry(QtCore.QRect(int(210 * width), int(5 * height), int(71 * width), int(31 * height)))
#         font = QtGui.QFont()
#         font.setPointSize(int(12 * height))
#         self.previous_pushButton.setFont(font)
#         self.previous_pushButton.setStyleSheet("border-radius: 9px;\n"
# "color: rgb(0, 0, 0);\n"
# "background-color: rgb(115, 172, 131);")
#          # Add drop shadow effect to the button
#         shadow = QGraphicsDropShadowEffect(self.previous_pushButton)
#         shadow.setBlurRadius(int(8 *height))
#         shadow.setColor(QtGui.QColor(0, 0, 0, 100))
#         shadow.setOffset(0, int(2 * height))
#         self.previous_pushButton.setGraphicsEffect(shadow)
#         self.previous_pushButton.setObjectName("previous_pushButton")
#         self.next_pushButton = QtWidgets.QPushButton(self.frame_4)
#         self.next_pushButton.setGeometry(QtCore.QRect(int(300 * width), int(5 * height), int(71 * width), int(31 *height)))
#         font = QtGui.QFont()
#         font.setPointSize(int(12 * height))
#         self.next_pushButton.setFont(font)
#         self.next_pushButton.setStyleSheet("border-radius: 9px;\n"
# "color: rgb(0, 0, 0);\n"
# "background-color: rgb(227, 151, 61);")
#          # Add drop shadow effect to the button
#         shadow = QGraphicsDropShadowEffect(self.next_pushButton)
#         shadow.setBlurRadius(int(8 * height))
#         shadow.setColor(QtGui.QColor(0, 0, 0, 100))
#         shadow.setOffset(0, int(2 * height))
#         self.next_pushButton.setGraphicsEffect(shadow)
#         self.next_pushButton.setObjectName("next_pushButton")

#         prepare.setCentralWidget(self.centralwidget)

#         # Set up the table widget
#         self.setup_table_widget()

#         # self.selected_ball_index = -1

#         self.retranslateUi(prepare)
#         QtCore.QMetaObject.connectSlotsByName(prepare)

#         def close_window():
#             prepare.close()
            
#         self.add_back_pushButton.clicked.connect(close_window)

#         # Set up button press and release styling
#         self.add_back_pushButton.pressed.connect(lambda: self.set_button_pressed_style(self.add_back_pushButton))
#         self.add_back_pushButton.released.connect(lambda: self.set_button_released_style(self.add_back_pushButton))

#         self.next_pushButton.pressed.connect(lambda: self.set_button_pressed_style(self.next_pushButton))
#         self.next_pushButton.released.connect(lambda: self.set_button_released_style(self.next_pushButton))

#         self.previous_pushButton.pressed.connect(lambda: self.set_button_pressed_style2(self.previous_pushButton))
#         self.previous_pushButton.released.connect(lambda: self.set_button_released_style2(self.previous_pushButton))

#         # self.next_pushButton.clicked.connect(self.next_pushButton_clicked)                                                           ตรงนี้
#         # self.add_back_pushButton.clicked.connect(self.add_back_pushButton_clicked)

#         # self.previous_pushButton.clicked.connect(self.move_to_previous_ball)
#         self.next_pushButton.clicked.connect(self.move_to_next_ball)

#         self.sort_handle()

#         # self.update_ball_colors()

#     # def next_pushButton_clicked(self):
#     #     global current_ball_index
#     #     current_ball_index = (current_ball_index + 1) % (row_max * col_max)                                                          ตรงนี้
#     #     self.sort_handle()

#     # def add_back_pushButton_clicked(self):
#     #     global current_ball_index
#     #     current_ball_index = (current_ball_index - 1) % (row_max * col_max)
#     #     self.sort_handle()
        
#     def set_button_pressed_style(self, button):
#         button.setStyleSheet(
#             "border-radius: 9px;\n"
#             "color: rgb(0, 0, 0);\n"
#             "background-color: rgb(200, 200, 200);"  # Change color when pressed
#         )

#     def set_button_released_style(self, button):
#         button.setStyleSheet(
#             "border-radius: 9px;\n"
#             "color: rgb(0, 0, 0);\n"
#             "background-color: rgb(227, 151, 61);"
#         )

#     def set_button_pressed_style2(self, button):
#         button.setStyleSheet(
#             "border-radius: 9px;\n"
#             "color: rgb(0, 0, 0);\n"
#             "background-color: rgb(200, 200, 200);"  # Change color when pressed
#         )

#     def set_button_released_style2(self, button):
#         button.setStyleSheet(
#             "border-radius: 9px;\n"
#             "color: rgb(0, 0, 0);\n"
#             "background-color: rgb(115, 172, 131);"
#         )

#     # def move_to_previous_ball(self):
#         # if self.selected_ball_index >= 0:
#         #     self.selected_ball_index -= 1
#         #     print(self.selected_ball_index)
#             # self.update_ball_colors()
#             # if self.selected_ball_index == -1:
#             #     self.sort_handle()

#     def move_to_next_ball(self):
#         # if self.selected_ball_index < (row_max * col_max) - 1:
#         print(self.slot)
#         if self.slot <= (row_max * col_max):
#             # self.selected_ball_index += 1
#             connection = sqlite3.connect("medicine.db")
#             cursor = connection.cursor()
#             query = '''
#                 SELECT  h.drug_id, drug_name, drug_description, drug_remaining, drug_remaining_meal, fraction, external_drug, internal_drug, drug_eat, all_drug_recieve, day_start, drug_log, drug_new, drug_size,
#                         h.meal_id, meal_name, time
#                     FROM Drug_handle AS h
#                     LEFT JOIN Drug AS d ON h.drug_id = d.drug_id
#                     LEFT JOIN Meal AS m ON h.meal_id = m.meal_id
#                 WHERE h.meal_id = ?
#                 '''
            
#             # print(self.check_meal)
#             cursor.execute(query, (self.check_meal,))   
#             drug_info_list = cursor.fetchall()
#             print(drug_info_list)
            
#             if drug_info_list:
#                 self.check_all = 1
             
#                 have_drug = False
                
#                 color_text_mapping = {
#                     (255, 102, 102): {"text": "เช้าก่อน", "enabled": True},    # สีแดง
#                     (255, 178, 102): {"text": "เช้าหลัง", "enabled": True},   # สีส้ม
#                     (255, 255, 102): {"text": "เที่ยงก่อน", "enabled": True},    # สีเหลือง
#                     (178, 255, 102): {"text": "เที่ยงหลัง", "enabled": True},   # สีเขียวอ่อน
#                     (102, 255, 102): {"text": "เย็นก่อน", "enabled": True},   # สีเขียวเข้ม
#                     (102, 255, 255): {"text": "เย็นหลัง", "enabled": True},    # สีฟ้า
#                     (0, 180, 255): {"text": "ก่อนนอน", "enabled": True}    # สีน้ำเงิน
#                 }

#                 color_index = drug_info_list[0][14] - 1

#                 if color_index < len(color_text_mapping):
#                     color = list(color_text_mapping.keys())[color_index]

#                 circular_item = CircularColorItem(QtGui.QColor(*color), color_text_mapping[color])
#                 self.tableWidget.setCellWidget(self.cursor_col, self.cursor_row, circular_item)
                
#                 print(drug_info_list[0][15])
#                 for drug_info in drug_info_list:
#                     drug_id, drug_name, drug_description, drug_remaining, drug_remaining_meal, fraction, external_drug, internal_drug, drug_eat, all_drug_recieve, day_start, drug_log, drug_new, drug_size, meal_id, meal_name, time = drug_info
                    
#                     if external_drug != 0:
#                         print(f"- {drug_name}")
                        
#                         # print(f"    มื้อยานอกเครื่อง:{external_drug} (ก่อน update)")
#                         # print(f"    มื้อยาในเครื่อง:{internal_drug} (ก่อน update)")
#                         # print("-----------------------")
                        
#                         external_drug -= 1
#                         internal_drug += 1
                        
#                         cursor.execute(f"UPDATE Drug SET external_drug = {external_drug}, internal_drug = {internal_drug} WHERE drug_id = {drug_id}")
#                         connection.commit()
                        
#                         # print(f"    มื้อยานอกเครื่อง:{external_drug} (หลัง update)")
#                         # print(f"    มื้อยาในเครื่อง:{internal_drug} (หลัง update)")
                        
#                         have_drug = True
                        
#                     else:
#                         # print("     หมด")
#                         pass
                        
#                 query = '''
#                 SELECT  h.drug_id, drug_name, drug_description, drug_remaining, drug_remaining_meal, fraction, external_drug, internal_drug, drug_eat, all_drug_recieve, day_start, drug_log, drug_new, drug_size,
#                         h.meal_id, meal_name, time
#                     FROM Drug_handle AS h
#                     LEFT JOIN Drug AS d ON h.drug_id = d.drug_id
#                     LEFT JOIN Meal AS m ON h.meal_id = m.meal_id
#                 '''
                    
#                 cursor.execute(query)   
#                 drug_info_list = cursor.fetchall()
                
                
#                 for drug_info in drug_info_list:
#                     drug_info[6] == 0
#                     # print(f"\nชื่อยา:{drug_info[1]}\nยานอกเครื่อง:{drug_info[6]}\n")
            
#                 all_drugs_empty = all(drug_info[6] == 0 for drug_info in drug_info_list)

#                 if all_drugs_empty:
#                     # print("ทุกยามยาหมดแล้ว")
#                     self.slot = (row_max * col_max) + 1
#                 else:
#                     # print("ยังมียาที่ยังไม่หมด")
#                     pass
                    
#                 # print("============================================================================")
                
#                 if have_drug:                                           # เช็คว่ามียาไหม
#                     self.slot += 1
#                     self.cursor_row += 1

#                     # Update listWidget with medicine names and meal times for the current ball
#                     current_drug_info = drug_info_list[current_ball_index]

#                     drug_name = current_drug_info[1]

#                     self.listWidget.clear()
#                     self.listWidget.addItem(f"กรุณากดปุ่มถัดไปเพื่อจัดเรียงยา")
                    
#                 row_new = (col_max - row_max) - 1
#                 col_new = (row_max - col_max) - 1
                
#                 if self.cursor_row > row_max + row_new:                      # คำนวณตำแหน่งของ row
#                     self.cursor_row = 0
#                     self.cursor_col += 1
#                 if self.cursor_col > col_max + col_new:                      # คำนวณตำแหน่งของ col
#                     self.cursor_col = 0
#                 self.check_meal += 1
            
#             else:
#                 # print(f"check all:{self.check_all}")
#                 if self.check_all == 7:
#                     QtWidgets.QMessageBox.warning(self.centralwidget, "คำเตือน", "ไม่พบข้อมูลยา")
#                     return
#                     # เพิ่มกลับไปหน้า main ด้วย
#                 self.check_all += 1
#                 self.check_meal += 1
#                 self.move_to_next_ball()
#                 return
                
#             if self.check_meal > 7:
#                 self.check_meal = 1
            
#             connection.close()

#             drug_names_for_meal = set()  
#             for info in drug_info_list:
#                 if info[14] == self.check_meal:
#                     drug_names_for_meal.add(f"{info[1]} - {info[15]}")

#             self.listWidget.clear()
#             self.listWidget.addItems(list(drug_names_for_meal))  
            
#             # print(self.selected_ball_index)
#             # self.update_ball_colors()

#     def setup_table_widget(self):
#         width, height = Scale_Width_Height()
#         # สร้างและกำหนด QTableWidget
#         self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
#         self.tableWidget.setGeometry(QtCore.QRect(int(260 * width), int(120 * height), int(381 * width), int(251 * height)))                         
#         self.tableWidget.setObjectName("tableWidget")

#         # Set the background color of the table to white and text color to black
#         self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);")
#         shadow = QGraphicsDropShadowEffect(self.tableWidget)
#         shadow.setBlurRadius(int(8 * height))
#         shadow.setColor(QtGui.QColor(0, 0, 0, 100))
#         shadow.setOffset(0, int(2 * height))
#         self.tableWidget.setGraphicsEffect(shadow)


#         # กำหนดหัวข้อคอลัมน์ในตาราง
#         self.tableWidget.setColumnCount(col_max)
#         # self.tableWidget.setHorizontalHeaderLabels(["Column 1", "Column 2", "Column 3", "Column 4", "Column 5", "Column 6"])
        
#         # กำหนดจำนวนแถวในตารางตามจำนวนรายการยาที่ดึงมาจากฐานข้อมูล
#         self.tableWidget.setRowCount(row_max)

#         cell_size = 62  # You can adjust this value as needed
#         for col_idx in range(col_max):
#             self.tableWidget.setColumnWidth(col_idx, cell_size)
#         for row_idx in range(row_max):
#             self.tableWidget.setRowHeight(row_idx, cell_size)
                 
                
#     def sort_handle(self):
#         connection = sqlite3.connect("medicine.db")
#         cursor = connection.cursor()

#         query = '''
#         SELECT  h.drug_id, drug_name, drug_description, drug_remaining, drug_remaining_meal, fraction, external_drug, internal_drug, drug_eat, all_drug_recieve, day_start, drug_log, 
#                 h.meal_id, meal_name, time
#             FROM Drug_handle AS h
#             LEFT JOIN Drug AS d ON h.drug_id = d.drug_id
#             LEFT JOIN Meal AS m ON h.meal_id = m.meal_id
#         '''

#         cursor.execute(query)
#         drug_info_list = cursor.fetchall()
        

#         for drug_info in drug_info_list:
#             drug_id, drug_name, drug_description, drug_remaining, drug_remaining_meal, fraction, external_drug, internal_drug, drug_eat, all_drug_recieve, day_start, drug_log, meal_id, meal_name, time = drug_info

            
#             drug_remaining_meal = drug_remaining / drug_eat                 # คำนวณจำนวนมื้อทั้งหมดที่คงเหลือทั้งหมด
#             drug_remaining_meal = int(drug_remaining_meal)                  # แปลงเป็นจำนวนเต็ม
            
#             fraction = drug_remaining % drug_eat                            # คำนวณจำนวนเศษยาที่ไม่ลงตัวกับจำนวนยาที่กิน
            
#             external_drug = int(drug_remaining_meal)                        # แปลงเป็นจำนวนเต็ม
            
#             # Update external_drug with drug_remaining
#             cursor.execute(f"UPDATE Drug SET drug_remaining_meal = {drug_remaining_meal}, fraction = {fraction}, external_drug = {external_drug}, internal_drug = 0 WHERE drug_id = {drug_id}")
#             connection.commit()

#             # Fetch updated drug information after the update
#             cursor.execute(f"SELECT * FROM Drug WHERE drug_id = {drug_id}")
#             updated_drug_info = cursor.fetchone()
#             drug_id, drug_name, drug_description, drug_remaining, drug_remaining_meal, fraction, external_drug, internal_drug, drug_eat, all_drug_recieve, day_start, drug_log, drug_new, drug_size = updated_drug_info

          
#         connection.close()
        
#         self.check_meal = 1
#         self.slot = 1
        
#         self.cursor_row = 0
#         self.cursor_col = 0
#         self.check_all = 1

#     def retranslateUi(self, prepare):
#         _translate = QtCore.QCoreApplication.translate
#         prepare.setWindowTitle(_translate("prepare", "เตรียมบอล"))
#         self.prepare_label.setText(_translate("prepare", "เตรียมบอล"))
#         self.add_back_pushButton.setText(_translate("prepare", "ย้อนกลับ"))
#         self.label.setText(_translate("prepare", "รายชื่อยาที่ต้องเตรียม"))
#         self.label_2.setText(_translate("prepare", "วางตามช่องที่แสดง"))
#         self.next_pushButton.setText(_translate("prepare", "ถัดไป"))
#         self.previous_pushButton.setText(_translate("prepare", "ก่อนหน้า"))
# import resources_rc

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     prepare = QtWidgets.QMainWindow()
#     ui = Ui_prepare()
#     ui.setupUi(prepare) 
#     prepare.show()
#     sys.exit(app.exec_())
