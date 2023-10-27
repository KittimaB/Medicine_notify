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