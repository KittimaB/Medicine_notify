from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsDropShadowEffect
from timeEdit import Ui_time_Edit

class Ui_select_time(object):
    def open_time_edit(self, meal_label_text):
        time_edit_window = QtWidgets.QMainWindow()
        time_edit_ui = Ui_time_Edit()
        time_edit_ui.meal_label_text = meal_label_text  # Set meal label text
        time_edit_ui.setupUi(time_edit_window)
        time_edit_window.show()

    def setupUi(self, select_time):
        select_time.setObjectName("select_time")
        select_time.resize(683, 400)
        select_time.setStyleSheet("\n"
"background-color: rgb(23, 73, 110);")
        self.centralwidget = QtWidgets.QWidget(select_time)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, -60, 683, 131))
        self.frame.setStyleSheet("border-radius: 40px;\n"
"background-color: rgb(255, 255, 255);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.frame)
        shadow.setBlurRadius(8)
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(0,2)
        self.frame.setGraphicsEffect(shadow)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(200, 70, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("border-radius: 16px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(23, 73, 110);")
         # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.label)
        shadow.setBlurRadius(8)
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(0,2)
        self.label.setGraphicsEffect(shadow)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setLineWidth(1)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.add_back_pushButton = QtWidgets.QPushButton(self.frame)
        self.add_back_pushButton.setGeometry(QtCore.QRect(50, 80, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add_back_pushButton.setFont(font)
        self.add_back_pushButton.setStyleSheet("border-radius: 9px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(244, 212, 99);")
         # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.add_back_pushButton)
        shadow.setBlurRadius(8)
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(0,2)
        self.add_back_pushButton.setGraphicsEffect(shadow)
        self.add_back_pushButton.setObjectName("add_back_pushButton")
        self.frame_9 = QtWidgets.QFrame(self.centralwidget)
        self.frame_9.setGeometry(QtCore.QRect(350, 150, 141, 121))
        self.frame_9.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.frame_12 = QtWidgets.QFrame(self.centralwidget)
        self.frame_12.setGeometry(QtCore.QRect(510, 150, 141, 121))
        self.frame_12.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(30, 150, 141, 121))
        self.frame_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.frame_8 = QtWidgets.QFrame(self.centralwidget)
        self.frame_8.setGeometry(QtCore.QRect(350, 250, 141, 41))
        self.frame_8.setStyleSheet("border-radius: 16px;\n"
"background-color: rgb(255, 255, 255);")
         # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.frame_8)
        shadow.setBlurRadius(8)
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(0,2)
        self.frame_8.setGraphicsEffect(shadow)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.frame_10 = QtWidgets.QFrame(self.centralwidget)
        self.frame_10.setGeometry(QtCore.QRect(350, 110, 141, 61))
        self.frame_10.setStyleSheet("border-radius: 16px;\n"
"background-color: rgb(244, 212, 99);")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.d_label = QtWidgets.QLabel(self.frame_10)
        self.d_label.setGeometry(QtCore.QRect(10, 0, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.d_label.setFont(font)
        self.d_label.setAlignment(QtCore.Qt.AlignCenter)
        self.d_label.setObjectName("d_label")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(30, 110, 141, 61))
        self.frame_2.setStyleSheet("border-radius: 16px;\n"
"background-color: rgb(244, 212, 99);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.b_label = QtWidgets.QLabel(self.frame_2)
        self.b_label.setGeometry(QtCore.QRect(10, 0, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.b_label.setFont(font)
        self.b_label.setAlignment(QtCore.Qt.AlignCenter)
        self.b_label.setObjectName("b_label")
        self.frame_13 = QtWidgets.QFrame(self.centralwidget)
        self.frame_13.setGeometry(QtCore.QRect(510, 250, 141, 41))
        self.frame_13.setStyleSheet("border-radius: 16px;\n"
"background-color: rgb(255, 255, 255);")
         # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.frame_13)
        shadow.setBlurRadius(8)
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(0,2)
        self.frame_13.setGraphicsEffect(shadow)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        self.frame_6.setGeometry(QtCore.QRect(190, 150, 141, 121))
        self.frame_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.frame_7 = QtWidgets.QFrame(self.centralwidget)
        self.frame_7.setGeometry(QtCore.QRect(190, 250, 141, 41))
        self.frame_7.setStyleSheet("border-radius: 16px;\n"
"background-color: rgb(255, 255, 255);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.frame_7)
        shadow.setBlurRadius(8)
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(0,2)
        self.frame_7.setGraphicsEffect(shadow)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(30, 250, 141, 41))
        self.frame_4.setStyleSheet("border-radius: 16px;\n"
"background-color: rgb(255, 255, 255);")
         # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.frame_4)
        shadow.setBlurRadius(8)
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(0,2)
        self.frame_4.setGraphicsEffect(shadow)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.frame_11 = QtWidgets.QFrame(self.centralwidget)
        self.frame_11.setGeometry(QtCore.QRect(510, 110, 141, 61))
        self.frame_11.setStyleSheet("border-radius: 16px;\n"
"background-color: rgb(244, 212, 99);")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.bed_label = QtWidgets.QLabel(self.frame_11)
        self.bed_label.setGeometry(QtCore.QRect(20, 0, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bed_label.setFont(font)
        self.bed_label.setAlignment(QtCore.Qt.AlignCenter)
        self.bed_label.setObjectName("bed_label")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(190, 110, 141, 61))
        self.frame_3.setStyleSheet("border-radius: 16px;\n"
"background-color: rgb(244, 212, 99);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.l_label = QtWidgets.QLabel(self.frame_3)
        self.l_label.setGeometry(QtCore.QRect(10, 0, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.l_label.setFont(font)
        self.l_label.setAlignment(QtCore.Qt.AlignCenter)
        self.l_label.setObjectName("l_label")
        self.bb_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.bb_pushButton.setGeometry(QtCore.QRect(50, 170, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bb_pushButton.setFont(font)
        self.bb_pushButton.setStyleSheet("border-radius: 9px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(235, 109, 109);")
         # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.bb_pushButton)
        shadow.setBlurRadius(8)
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(0,2)
        self.bb_pushButton.setGraphicsEffect(shadow)
        self.bb_pushButton.setObjectName("bb_pushButton")
        self.ab_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.ab_pushButton.setGeometry(QtCore.QRect(50, 230, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ab_pushButton.setFont(font)
        self.ab_pushButton.setStyleSheet("border-radius: 9px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(244, 212, 99);")
         # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.ab_pushButton)
        shadow.setBlurRadius(8)
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(0,2)
        self.ab_pushButton.setGraphicsEffect(shadow)
        self.ab_pushButton.setObjectName("ab_pushButton")
        self.bl_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.bl_pushButton.setGeometry(QtCore.QRect(210, 170, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bl_pushButton.setFont(font)
        self.bl_pushButton.setStyleSheet("border-radius: 9px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(239, 151, 204);\n"
"")
         # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.bl_pushButton)
        shadow.setBlurRadius(8)
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(0,2)
        self.bl_pushButton.setGraphicsEffect(shadow)
        self.bl_pushButton.setObjectName("bl_pushButton")
        self.al_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.al_pushButton.setGeometry(QtCore.QRect(210, 230, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.al_pushButton.setFont(font)
        self.al_pushButton.setStyleSheet("border-radius: 9px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(169, 212, 98);")
         # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.al_pushButton)
        shadow.setBlurRadius(8)
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(0,2)
        self.al_pushButton.setGraphicsEffect(shadow)
        self.al_pushButton.setObjectName("al_pushButton")
        self.bd_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.bd_pushButton.setGeometry(QtCore.QRect(370, 170, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bd_pushButton.setFont(font)
        self.bd_pushButton.setStyleSheet("border-radius: 9px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(235, 143, 76);\n"
"")
         # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.bd_pushButton)
        shadow.setBlurRadius(8)
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(0,2)
        self.bd_pushButton.setGraphicsEffect(shadow)
        self.bd_pushButton.setObjectName("bd_pushButton")
        self.ad_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.ad_pushButton.setGeometry(QtCore.QRect(370, 230, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ad_pushButton.setFont(font)
        self.ad_pushButton.setStyleSheet("border-radius: 9px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(119, 156, 212);\n"
"")
         # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.ad_pushButton)
        shadow.setBlurRadius(8)
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(0,2)
        self.ad_pushButton.setGraphicsEffect(shadow)
        self.ad_pushButton.setObjectName("ad_pushButton")
        self.bbed_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.bbed_pushButton.setGeometry(QtCore.QRect(530, 170, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bbed_pushButton.setFont(font)
        self.bbed_pushButton.setStyleSheet("border-radius: 9px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(176, 107, 193);\n"
"")
         # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.bbed_pushButton)
        shadow.setBlurRadius(8)
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(0,2)
        self.bbed_pushButton.setGraphicsEffect(shadow)
        self.bbed_pushButton.setObjectName("bbed_pushButton")
        self.frame_3.raise_()
        self.frame_11.raise_()
        self.frame_10.raise_()
        self.frame_8.raise_()
        self.frame_7.raise_()
        self.frame_4.raise_()
        self.frame_2.raise_()
        self.frame.raise_()
        self.frame_9.raise_()
        self.frame_12.raise_()
        self.frame_5.raise_()
        self.frame_13.raise_()
        self.frame_6.raise_()
        self.bb_pushButton.raise_()
        self.ab_pushButton.raise_()
        self.bl_pushButton.raise_()
        self.al_pushButton.raise_()
        self.bd_pushButton.raise_()
        self.ad_pushButton.raise_()
        self.bbed_pushButton.raise_()
        select_time.setCentralWidget(self.centralwidget)

        self.retranslateUi(select_time)
        QtCore.QMetaObject.connectSlotsByName(select_time)

        self.bb_pushButton.clicked.connect(lambda: self.open_time_edit("มื้อเช้า ก่อนอาหาร"))
        self.ab_pushButton.clicked.connect(lambda: self.open_time_edit("มื้อเช้า หลังอาหาร"))
        self.bl_pushButton.clicked.connect(lambda: self.open_time_edit("มื้อเที่ยง ก่อนอาหาร"))
        self.al_pushButton.clicked.connect(lambda: self.open_time_edit("มื้อเที่ยง หลังอาหาร"))
        self.bd_pushButton.clicked.connect(lambda: self.open_time_edit("มื้อเย็น ก่อนอาหาร"))
        self.ad_pushButton.clicked.connect(lambda: self.open_time_edit("มื้อเย็น หลังอาหาร"))
        self.bbed_pushButton.clicked.connect(lambda: self.open_time_edit("มื้อก่อนนอน"))

        def close_window():
            select_time.close()

        self.add_back_pushButton.clicked.connect(close_window)

        self.add_back_pushButton.pressed.connect(lambda: self.set_button_pressed_style(self.add_back_pushButton))
        self.bb_pushButton.pressed.connect(lambda: self.set_button_pressed_style(self.bb_pushButton))
        self.ab_pushButton.pressed.connect(lambda: self.set_button_pressed_style(self.ab_pushButton))
        self.bl_pushButton.pressed.connect(lambda: self.set_button_pressed_style(self.bl_pushButton))
        self.al_pushButton.pressed.connect(lambda: self.set_button_pressed_style(self.al_pushButton))
        self.bd_pushButton.pressed.connect(lambda: self.set_button_pressed_style(self.bd_pushButton))
        self.ad_pushButton.pressed.connect(lambda: self.set_button_pressed_style(self.ad_pushButton))
        self.bbed_pushButton.pressed.connect(lambda: self.set_button_pressed_style(self.bbed_pushButton))
        

        
    def set_button_pressed_style(self, button):
        button.setStyleSheet(
            "border-radius: 9px;\n"
            "color: rgb(0, 0, 0);\n"
            "background-color: rgb(200, 200, 200);"  # Change color when pressed
        )

    def retranslateUi(self, select_time):
        _translate = QtCore.QCoreApplication.translate
        select_time.setWindowTitle(_translate("select_time", "ตั้งเวลามื้อยา"))
        self.b_label.setText(_translate("select_time", "มื้อเช้า"))
        self.add_back_pushButton.setText(_translate("select_time", "ย้อนกลับ"))
        self.d_label.setText(_translate("select_time", "มื้อเย็น"))
        self.l_label.setText(_translate("select_time", "มื้อเที่ยง"))
        self.label.setText(_translate("select_time", "ตั้งเวลามื้อยา"))
        self.bed_label.setText(_translate("select_time", "มื้อก่อนนอน"))
        self.bb_pushButton.setText(_translate("select_time", "ก่อน อาหาร"))
        self.ab_pushButton.setText(_translate("select_time", "หลัง อาหาร"))
        self.bl_pushButton.setText(_translate("select_time", "ก่อน อาหาร"))
        self.al_pushButton.setText(_translate("select_time", "หลัง อาหาร"))
        self.bd_pushButton.setText(_translate("select_time", "ก่อน อาหาร"))
        self.ad_pushButton.setText(_translate("select_time", "หลัง อาหาร"))
        self.bbed_pushButton.setText(_translate("select_time", "ก่อนนอน"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    select_time = QtWidgets.QMainWindow()
    ui = Ui_select_time()
    ui.setupUi(select_time)
    select_time.show()
    sys.exit(app.exec_())
