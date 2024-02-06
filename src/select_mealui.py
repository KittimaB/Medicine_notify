# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'select_mealui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_select_meal(object):
    def setupUi(self, select_meal):
        select_meal.setObjectName("select_meal")
        select_meal.resize(531, 401)
        select_meal.setStyleSheet("\n"
"background-color: rgb(23, 73, 110);")
        self.centralwidget = QtWidgets.QWidget(select_meal)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, -60, 531, 131))
        self.frame.setStyleSheet("border-radius: 40px;\n"
"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.meal_label = QtWidgets.QLabel(self.frame)
        self.meal_label.setGeometry(QtCore.QRect(180, 70, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.meal_label.setFont(font)
        self.meal_label.setStyleSheet("border-radius: 16px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(23, 73, 110);")
        self.meal_label.setFrameShape(QtWidgets.QFrame.Box)
        self.meal_label.setLineWidth(1)
        self.meal_label.setTextFormat(QtCore.Qt.AutoText)
        self.meal_label.setScaledContents(False)
        self.meal_label.setAlignment(QtCore.Qt.AlignCenter)
        self.meal_label.setWordWrap(True)
        self.meal_label.setObjectName("meal_label")
        self.back_pushButton = QtWidgets.QPushButton(self.frame)
        self.back_pushButton.setGeometry(QtCore.QRect(50, 80, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.back_pushButton.setFont(font)
        self.back_pushButton.setStyleSheet("border-radius: 9px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(244, 212, 99);")
        self.back_pushButton.setObjectName("back_pushButton")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(30, 120, 141, 61))
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
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(30, 260, 141, 41))
        self.frame_4.setStyleSheet("border-radius: 16px;\n"
"background-color: rgb(255, 255, 255);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(30, 160, 141, 121))
        self.frame_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.bb_label = QtWidgets.QLabel(self.frame_5)
        self.bb_label.setGeometry(QtCore.QRect(30, 20, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.bb_label.setFont(font)
        self.bb_label.setStyleSheet("border-radius: 9px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(235, 109, 109);")
        self.bb_label.setFrameShape(QtWidgets.QFrame.Box)
        self.bb_label.setLineWidth(1)
        self.bb_label.setTextFormat(QtCore.Qt.AutoText)
        self.bb_label.setScaledContents(False)
        self.bb_label.setAlignment(QtCore.Qt.AlignCenter)
        self.bb_label.setWordWrap(True)
        self.bb_label.setObjectName("bb_label")
        self.bb_checkBox = QtWidgets.QCheckBox(self.frame_5)
        self.bb_checkBox.setGeometry(QtCore.QRect(10, 0, 16, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bb_checkBox.sizePolicy().hasHeightForWidth())
        self.bb_checkBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bb_checkBox.setFont(font)
        self.bb_checkBox.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.bb_checkBox.setText("")
        self.bb_checkBox.setTristate(False)
        self.bb_checkBox.setObjectName("bb_checkBox")
        self.ab_checkBox = QtWidgets.QCheckBox(self.frame_5)
        self.ab_checkBox.setGeometry(QtCore.QRect(10, 60, 16, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ab_checkBox.sizePolicy().hasHeightForWidth())
        self.ab_checkBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ab_checkBox.setFont(font)
        self.ab_checkBox.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.ab_checkBox.setText("")
        self.ab_checkBox.setTristate(False)
        self.ab_checkBox.setObjectName("ab_checkBox")
        self.ab_label = QtWidgets.QLabel(self.frame_5)
        self.ab_label.setGeometry(QtCore.QRect(30, 80, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.ab_label.setFont(font)
        self.ab_label.setStyleSheet("border-radius: 9px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(244, 212, 99);")
        self.ab_label.setFrameShape(QtWidgets.QFrame.Box)
        self.ab_label.setLineWidth(1)
        self.ab_label.setTextFormat(QtCore.Qt.AutoText)
        self.ab_label.setScaledContents(False)
        self.ab_label.setAlignment(QtCore.Qt.AlignCenter)
        self.ab_label.setWordWrap(True)
        self.ab_label.setObjectName("ab_label")
        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        self.frame_6.setGeometry(QtCore.QRect(190, 160, 141, 121))
        self.frame_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(190, 120, 141, 61))
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
        self.frame_7 = QtWidgets.QFrame(self.centralwidget)
        self.frame_7.setGeometry(QtCore.QRect(190, 260, 141, 41))
        self.frame_7.setStyleSheet("border-radius: 16px;\n"
"background-color: rgb(255, 255, 255);")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.bl_label = QtWidgets.QLabel(self.centralwidget)
        self.bl_label.setGeometry(QtCore.QRect(220, 180, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.bl_label.setFont(font)
        self.bl_label.setStyleSheet("border-radius: 9px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(239, 151, 204);\n"
"")
        self.bl_label.setFrameShape(QtWidgets.QFrame.Box)
        self.bl_label.setLineWidth(1)
        self.bl_label.setTextFormat(QtCore.Qt.AutoText)
        self.bl_label.setScaledContents(False)
        self.bl_label.setAlignment(QtCore.Qt.AlignCenter)
        self.bl_label.setWordWrap(True)
        self.bl_label.setObjectName("bl_label")
        self.bl_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.bl_checkBox.setGeometry(QtCore.QRect(200, 160, 16, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bl_checkBox.sizePolicy().hasHeightForWidth())
        self.bl_checkBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bl_checkBox.setFont(font)
        self.bl_checkBox.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.bl_checkBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bl_checkBox.setText("")
        self.bl_checkBox.setTristate(False)
        self.bl_checkBox.setObjectName("bl_checkBox")
        self.al_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.al_checkBox.setGeometry(QtCore.QRect(200, 220, 16, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.al_checkBox.sizePolicy().hasHeightForWidth())
        self.al_checkBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.al_checkBox.setFont(font)
        self.al_checkBox.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.al_checkBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.al_checkBox.setText("")
        self.al_checkBox.setTristate(False)
        self.al_checkBox.setObjectName("al_checkBox")
        self.al_label = QtWidgets.QLabel(self.centralwidget)
        self.al_label.setGeometry(QtCore.QRect(220, 240, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.al_label.setFont(font)
        self.al_label.setStyleSheet("border-radius: 9px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(169, 212, 98);")
        self.al_label.setFrameShape(QtWidgets.QFrame.Box)
        self.al_label.setLineWidth(1)
        self.al_label.setTextFormat(QtCore.Qt.AutoText)
        self.al_label.setScaledContents(False)
        self.al_label.setAlignment(QtCore.Qt.AlignCenter)
        self.al_label.setWordWrap(True)
        self.al_label.setObjectName("al_label")
        self.frame_8 = QtWidgets.QFrame(self.centralwidget)
        self.frame_8.setGeometry(QtCore.QRect(350, 260, 141, 41))
        self.frame_8.setStyleSheet("border-radius: 16px;\n"
"background-color: rgb(255, 255, 255);")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.frame_9 = QtWidgets.QFrame(self.centralwidget)
        self.frame_9.setGeometry(QtCore.QRect(350, 160, 141, 121))
        self.frame_9.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.ad_label = QtWidgets.QLabel(self.frame_9)
        self.ad_label.setGeometry(QtCore.QRect(30, 80, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.ad_label.setFont(font)
        self.ad_label.setStyleSheet("border-radius: 9px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(119, 156, 212);\n"
"")
        self.ad_label.setFrameShape(QtWidgets.QFrame.Box)
        self.ad_label.setLineWidth(1)
        self.ad_label.setTextFormat(QtCore.Qt.AutoText)
        self.ad_label.setScaledContents(False)
        self.ad_label.setAlignment(QtCore.Qt.AlignCenter)
        self.ad_label.setWordWrap(True)
        self.ad_label.setObjectName("ad_label")
        self.ad_checkBox = QtWidgets.QCheckBox(self.frame_9)
        self.ad_checkBox.setGeometry(QtCore.QRect(10, 60, 16, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ad_checkBox.sizePolicy().hasHeightForWidth())
        self.ad_checkBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ad_checkBox.setFont(font)
        self.ad_checkBox.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.ad_checkBox.setText("")
        self.ad_checkBox.setTristate(False)
        self.ad_checkBox.setObjectName("ad_checkBox")
        self.bd_label = QtWidgets.QLabel(self.frame_9)
        self.bd_label.setGeometry(QtCore.QRect(30, 20, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.bd_label.setFont(font)
        self.bd_label.setStyleSheet("border-radius: 9px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(235, 143, 76);\n"
"")
        self.bd_label.setFrameShape(QtWidgets.QFrame.Box)
        self.bd_label.setLineWidth(1)
        self.bd_label.setTextFormat(QtCore.Qt.AutoText)
        self.bd_label.setScaledContents(False)
        self.bd_label.setAlignment(QtCore.Qt.AlignCenter)
        self.bd_label.setWordWrap(True)
        self.bd_label.setObjectName("bd_label")
        self.bd_checkBox = QtWidgets.QCheckBox(self.frame_9)
        self.bd_checkBox.setGeometry(QtCore.QRect(10, 0, 16, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bd_checkBox.sizePolicy().hasHeightForWidth())
        self.bd_checkBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bd_checkBox.setFont(font)
        self.bd_checkBox.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.bd_checkBox.setText("")
        self.bd_checkBox.setTristate(False)
        self.bd_checkBox.setObjectName("bd_checkBox")
        self.frame_10 = QtWidgets.QFrame(self.centralwidget)
        self.frame_10.setGeometry(QtCore.QRect(350, 120, 141, 61))
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
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 80, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.frame_11 = QtWidgets.QFrame(self.centralwidget)
        self.frame_11.setGeometry(QtCore.QRect(130, 320, 121, 51))
        self.frame_11.setStyleSheet("border-radius: 16px;\n"
"background-color: rgb(244, 212, 99);")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.bed_label = QtWidgets.QLabel(self.frame_11)
        self.bed_label.setGeometry(QtCore.QRect(10, 10, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bed_label.setFont(font)
        self.bed_label.setAlignment(QtCore.Qt.AlignCenter)
        self.bed_label.setObjectName("bed_label")
        self.frame_12 = QtWidgets.QFrame(self.centralwidget)
        self.frame_12.setGeometry(QtCore.QRect(230, 320, 131, 51))
        self.frame_12.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.bbed_checkBox = QtWidgets.QCheckBox(self.frame_12)
        self.bbed_checkBox.setGeometry(QtCore.QRect(20, -10, 21, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bbed_checkBox.sizePolicy().hasHeightForWidth())
        self.bbed_checkBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bbed_checkBox.setFont(font)
        self.bbed_checkBox.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.bbed_checkBox.setText("")
        self.bbed_checkBox.setTristate(False)
        self.bbed_checkBox.setObjectName("bbed_checkBox")
        self.bbed_label = QtWidgets.QLabel(self.frame_12)
        self.bbed_label.setGeometry(QtCore.QRect(40, 10, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.bbed_label.setFont(font)
        self.bbed_label.setStyleSheet("border-radius: 9px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(176, 107, 193);\n"
"")
        self.bbed_label.setFrameShape(QtWidgets.QFrame.Box)
        self.bbed_label.setLineWidth(1)
        self.bbed_label.setTextFormat(QtCore.Qt.AutoText)
        self.bbed_label.setScaledContents(False)
        self.bbed_label.setAlignment(QtCore.Qt.AlignCenter)
        self.bbed_label.setWordWrap(True)
        self.bbed_label.setObjectName("bbed_label")
        self.frame_13 = QtWidgets.QFrame(self.centralwidget)
        self.frame_13.setGeometry(QtCore.QRect(330, 320, 51, 51))
        self.frame_13.setStyleSheet("border-radius: 16px;\n"
"background-color: rgb(255, 255, 255);")
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.next_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.next_pushButton.setGeometry(QtCore.QRect(430, 340, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.next_pushButton.setFont(font)
        self.next_pushButton.setStyleSheet("border-radius: 9px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(227, 151, 61);")
        self.next_pushButton.setObjectName("next_pushButton")
        self.frame_13.raise_()
        self.frame_10.raise_()
        self.frame.raise_()
        self.frame_2.raise_()
        self.frame_4.raise_()
        self.frame_5.raise_()
        self.frame_3.raise_()
        self.frame_7.raise_()
        self.frame_6.raise_()
        self.bl_label.raise_()
        self.bl_checkBox.raise_()
        self.al_checkBox.raise_()
        self.al_label.raise_()
        self.frame_8.raise_()
        self.frame_9.raise_()
        self.label_2.raise_()
        self.frame_11.raise_()
        self.frame_12.raise_()
        self.next_pushButton.raise_()
        select_meal.setCentralWidget(self.centralwidget)

        self.retranslateUi(select_meal)
        QtCore.QMetaObject.connectSlotsByName(select_meal)

    def retranslateUi(self, select_meal):
        _translate = QtCore.QCoreApplication.translate
        select_meal.setWindowTitle(_translate("select_meal", "เลือกมื้อ"))
        self.meal_label.setText(_translate("select_meal", "ชื่อยา"))
        self.back_pushButton.setText(_translate("select_meal", "ย้อนกลับ"))
        self.b_label.setText(_translate("select_meal", "มื้อเช้า"))
        self.bb_label.setText(_translate("select_meal", "ก่อน อาหาร"))
        self.ab_label.setText(_translate("select_meal", "หลัง อาหาร"))
        self.l_label.setText(_translate("select_meal", "มื้อเที่ยง"))
        self.bl_label.setText(_translate("select_meal", "ก่อน อาหาร"))
        self.al_label.setText(_translate("select_meal", "หลัง อาหาร"))
        self.ad_label.setText(_translate("select_meal", "หลัง อาหาร"))
        self.bd_label.setText(_translate("select_meal", "ก่อน อาหาร"))
        self.d_label.setText(_translate("select_meal", "มื้อเย็น"))
        self.label_2.setText(_translate("select_meal", "เลือกมื้อต้องการรับประทานยา"))
        self.bed_label.setText(_translate("select_meal", "มื้อก่อนนอน"))
        self.bbed_label.setText(_translate("select_meal", "ก่อนนอน"))
        self.next_pushButton.setText(_translate("select_meal", "ถัดไป"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    select_meal = QtWidgets.QMainWindow()
    ui = Ui_select_meal()
    ui.setupUi(select_meal)
    select_meal.show()
    sys.exit(app.exec_())
