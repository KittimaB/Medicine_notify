def open_day_start(self):
        self.day_start_window = QtWidgets.QMainWindow()
        self.day_start_ui = Ui_day_start()

        self.day_start_ui.setupUi(self.day_start_window)
        self.day_start_window.show()