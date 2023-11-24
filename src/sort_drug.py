from PyQt5 import QtCore, QtGui, QtWidgets

#version old ไม่ใช้แล้ว

class Ui_sortDrug(object):
    def setupUi(self, sortDrug):
        sortDrug.setObjectName("sortDrug")
        sortDrug.setEnabled(True)
        sortDrug.resize(531, 401)
        sortDrug.setStyleSheet("background-color: rgb(217, 244, 255)")
        self.centralwidget = QtWidgets.QWidget(sortDrug)
        self.centralwidget.setObjectName("centralwidget")
        self.add_back_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.add_back_pushButton.setGeometry(QtCore.QRect(30, 40, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add_back_pushButton.setFont(font)
        self.add_back_pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(166, 0, 0)")
        self.add_back_pushButton.setObjectName("add_back_pushButton")
        self.sort_label = QtWidgets.QLabel(self.centralwidget)
        self.sort_label.setGeometry(QtCore.QRect(130, 20, 291, 51))
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
        self.line.setGeometry(QtCore.QRect(-10, 90, 551, 20))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        sortDrug.setCentralWidget(self.centralwidget)

        self.retranslateUi(sortDrug)
        QtCore.QMetaObject.connectSlotsByName(sortDrug)

        def close_window():
            sortDrug.close()
            
        self.add_back_pushButton.clicked.connect(close_window)



       # Create a QTableWidget with 5 rows and 8 columns
        self.tableWidget = QtWidgets.QTableWidget(5, 8)
        self.tableWidget.setObjectName("tableWidget")

        # Set the column labels (optional)
        column_labels = ["Column 1", "Column 2", "Column 3", "Column 4", "Column 5", "Column 6", "Column 7", "Column 8"]
        self.tableWidget.setHorizontalHeaderLabels(column_labels)

        # Set the size of each cell to be a square (4x4)
        cell_size = 60  # You can adjust this value as needed
        for col_idx in range(8):
            self.tableWidget.setColumnWidth(col_idx, cell_size)
        for row_idx in range(5):
            self.tableWidget.setRowHeight(row_idx, cell_size)

    #     meal_data = [
    #         ["Breakfast Before"] * 5,    # 5 Breakfast Before
    #         ["Lunch Before"] * 5,        # 5 Lunch Before
    #         ["Dinner Before"] * 5,       # 5 Dinner Before
    #     ]

    #     # Define colors for each meal type
    #     meal_colors = {
    #         "Breakfast Before": QtGui.QColor(255, 0, 0),  # Red
    #         "Lunch Before": QtGui.QColor(255, 165, 0),    # Orange
    #         "Dinner Before": QtGui.QColor(0, 0, 255),    # Blue
    #     }

    #     for meal_row in meal_data:
    #         row_idx = self.tableWidget.rowCount()  # Get the current row index
    #         print(row_idx)
    #         for meal_type in meal_row:
    #             # Set cell background color based on meal type
    #             print("=====")
    #             print(meal_type)
    #             print("=====")
    #             if meal_type in meal_colors:
    #                 color = meal_colors[meal_type]
    #                 for i in range(5):
    #                     item = QtWidgets.QTableWidgetItem()
    #                     #item.setFlags(QtCore.Qt.ItemIsEnabled)  # Disable editing
    #                     self.tableWidget.setItem(row_idx + i, 0, item)  # Set to the first column
    #                     item.setBackground(color)  # Set cell background color
    #                     print(color)
    #                 row_idx += 5  # Increment row index by 5 for the next group

        # Populate the table with meal data and set cell background color
        meal_data = [
            ["Breakfast Before", "Lunch Before", "Dinner Before"],
        ]

        # Define colors for each meal type
        meal_colors = {
            "Breakfast Before": QtGui.QColor(255, 0, 0),  # Red
            "Lunch Before": QtGui.QColor(255, 165, 0),    # Orange
            "Dinner Before": QtGui.QColor(0, 0, 255),    # Blue
        }

        row_idx = 0  # Initialize row index
        meal_count = 5  # Number of meals before changing color

        for meal_row in meal_data:
            for meal_type in meal_row:
                # Set cell background color based on meal type
                if meal_type in meal_colors:
                    color = meal_colors[meal_type]
                    for i in range(meal_count):
                        item = QtWidgets.QTableWidgetItem()
                        item.setFlags(QtCore.Qt.ItemIsEnabled)  # Disable editing
                        self.tableWidget.setItem(row_idx, i, item)
                        item.setBackground(color)
                    row_idx += 1  # Increment row index

                    # Check if we need to reset meal count and change color
                    print(meal_count)
                    meal_count -= 1

                    if meal_count == 0:
                        # Change color to the next meal type (cycling)
                        next_meal_type = meal_colors.popitem()[0]
                        meal_colors[next_meal_type] = meal_colors.popitem()[1]

                        print("===========")


        # Create a layout for self.centralwidget and add the table to it
        layout = QtWidgets.QVBoxLayout(self.centralwidget)
        layout.addWidget(self.tableWidget)



    def retranslateUi(self, sortDrug):
        _translate = QtCore.QCoreApplication.translate
        sortDrug.setWindowTitle(_translate("sortDrug", "วิธีเรียงกล่องบรรจุยา"))
        self.add_back_pushButton.setText(_translate("sortDrug", "ย้อนกลับ"))
        self.sort_label.setText(_translate("sortDrug", "วิธีเรียงกล่องบรรจุยา"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    sortDrug = QtWidgets.QMainWindow()
    ui = Ui_sortDrug()
    ui.setupUi(sortDrug)
    sortDrug.show()
    sys.exit(app.exec_())
