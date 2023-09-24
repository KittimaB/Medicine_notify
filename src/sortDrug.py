
from PyQt5 import QtCore, QtGui, QtWidgets



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

        # Populate the table with colored circles based on meal data
        meal_data = [
            # Replace this with data from your Meal table
            ["Breakfast Before", "Breakfast After", "Lunch Before", "Lunch After", "Dinner Before", "Dinner After", "Bedtime"],
            # Add more rows as needed
        ]

        for row_idx, meal_row in enumerate(meal_data):
            for col_idx, meal_type in enumerate(meal_row):
                item = QtWidgets.QTableWidgetItem()
                item.setFlags(QtCore.Qt.ItemIsEnabled)  # Disable editing
                self.tableWidget.setItem(row_idx, col_idx, item)

                # Set cell background color based on meal type
                if "Breakfast Before" in meal_type:
                    item.setBackground(QtGui.QColor(255, 0, 0))  # Red
                elif "Breakfast After" in meal_type:
                    item.setBackground(QtGui.QColor(255, 165, 0))  # Orange
                elif "Lunch Before" in meal_type:
                    item.setBackground(QtGui.QColor(255, 255, 0))  # Yellow
                elif "Lunch After" in meal_type:
                    item.setBackground(QtGui.QColor(0, 128, 0))  # Green
                elif "Dinner Before" in meal_type:
                    item.setBackground(QtGui.QColor(0, 0, 255))  # Blue
                elif "Dinner After" in meal_type:
                    item.setBackground(QtGui.QColor(128, 0, 128))  # Purple
                elif "Bedtime" in meal_type:
                    item.setBackground(QtGui.QColor(0, 0, 0))  # Black

        # ...

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
