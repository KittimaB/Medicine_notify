self.drugLeft_pushButton.pressed.connect(lambda: self.set_button_pressed_style(self.drugLeft_pushButton))
        self.drugLeft_pushButton.released.connect(lambda: self.set_button_released_style(self.drugLeft_pushButton))

        
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
            "background-color: rgb(255, 255, 255);"
        )