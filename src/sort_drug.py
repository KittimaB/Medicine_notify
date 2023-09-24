import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QLabel, QSpinBox

class TableExample(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("ระบบจัดการตารางยา")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()

        # ส่วนเลือกขนาดของตาราง (row และ column)
        size_label = QLabel("เลือกขนาดของตาราง")
        layout.addWidget(size_label)

        self.row_spinbox = QSpinBox()
        row_label = QLabel("Row (แนวนอน)")
        self.row_spinbox.setMaximum(20)  # กำหนดค่าสูงสุดของ row
        layout.addWidget(row_label)
        layout.addWidget(self.row_spinbox)

        self.col_spinbox = QSpinBox()
        col_label = QLabel("Column (แนวตั้ง)")
        self.col_spinbox.setMaximum(20)  # กำหนดค่าสูงสุดของ column
        layout.addWidget(col_label)
        layout.addWidget(self.col_spinbox)

        create_table_button = QPushButton("สร้างตาราง")
        create_table_button.clicked.connect(self.create_table)
        layout.addWidget(create_table_button)

        self.table_widget = QTableWidget()
        layout.addWidget(self.table_widget)

        self.central_widget.setLayout(layout)

    def create_table(self):
        rows = self.row_spinbox.value()
        cols = self.col_spinbox.value()

        self.table_widget.setRowCount(rows)
        self.table_widget.setColumnCount(cols)

        # ตั้งชื่อ column ในตาราง
        for col in range(cols):
            header_item = QTableWidgetItem(f"Column {col + 1}")
            self.table_widget.setHorizontalHeaderItem(col, header_item)

        # คำนวณและแสดงช่องในตาราง
        for row in range(rows):
            for col in range(cols):
                item = QTableWidgetItem(f"มื้อเช้าก่อนอาหาร ช่อง {chr(65 + col)}{rows - row}")
                self.table_widget.setItem(row, col, item)

        self.table_widget.setHorizontalHeaderLabels([f"Column {col + 1}" for col in range(cols)])

def main():
    app = QApplication(sys.argv)
    ex = TableExample()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()