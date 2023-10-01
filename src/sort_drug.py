
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem 


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

        # สร้างและกำหนด QTableWidget
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 120, 491, 241))
        self.tableWidget.setObjectName("tableWidget")

        # กำหนดหัวข้อคอลัมน์ในตาราง
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setHorizontalHeaderLabels(["Column 1", "Column 2", "Column 3", "Column 4", "Column 5", "Column 6", "Column 7", "Column 8"])
        
        # กำหนดจำนวนแถวในตารางตามจำนวนรายการยาที่ดึงมาจากฐานข้อมูล
        self.tableWidget.setRowCount(5)

        # Set the size of each cell to be a square (4x4)
        cell_size = 58  # You can adjust this value as needed
        for col_idx in range(8):
            self.tableWidget.setColumnWidth(col_idx, cell_size)
        for row_idx in range(5):
            self.tableWidget.setRowHeight(row_idx, cell_size)

        # กำหนดสีพื้นหลังของแต่ละเซลล์
        colors = [QtGui.QColor(255, 0, 0), QtGui.QColor(255, 165, 0), QtGui.QColor(0, 0, 255)]  # สีแดง, ส้ม, ฟ้า
        color_index = 0

        for row in range(5):
            for col in range(8):
                item = QTableWidgetItem()
                item.setBackground(colors[color_index])
                ui.tableWidget.setItem(row, col, item)
                color_index = (color_index + 1) % len(colors)  # สลับสี
    



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

