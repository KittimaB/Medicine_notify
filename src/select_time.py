# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'select_time.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_select_time(object):
    def setupUi(self, select_time):
        select_time.setObjectName("select_time")
        select_time.resize(531, 401)
        select_time.setStyleSheet("background-color: rgb(217, 244, 255)")
        self.centralwidget = QtWidgets.QWidget(select_time)
        self.centralwidget.setObjectName("centralwidget")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 280, 1201, 20))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(350, 100, 20, 181))
        self.line_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_4.setLineWidth(3)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setObjectName("line_4")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(170, 100, 20, 181))
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setLineWidth(3)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setObjectName("line_3")
        self.b_label = QtWidgets.QLabel(self.centralwidget)
        self.b_label.setGeometry(QtCore.QRect(20, 110, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.b_label.setFont(font)
        self.b_label.setAlignment(QtCore.Qt.AlignCenter)
        self.b_label.setObjectName("b_label")
        self.back_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.back_pushButton.setGeometry(QtCore.QRect(30, 40, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.back_pushButton.setFont(font)
        self.back_pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(166, 0, 0)")
        self.back_pushButton.setObjectName("back_pushButton")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-10, 90, 1201, 16))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.d_label = QtWidgets.QLabel(self.centralwidget)
        self.d_label.setGeometry(QtCore.QRect(380, 110, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.d_label.setFont(font)
        self.d_label.setAlignment(QtCore.Qt.AlignCenter)
        self.d_label.setObjectName("d_label")
        self.l_label = QtWidgets.QLabel(self.centralwidget)
        self.l_label.setGeometry(QtCore.QRect(200, 110, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.l_label.setFont(font)
        self.l_label.setAlignment(QtCore.Qt.AlignCenter)
        self.l_label.setObjectName("l_label")
        self.time_label = QtWidgets.QLabel(self.centralwidget)
        self.time_label.setGeometry(QtCore.QRect(160, 20, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.time_label.setFont(font)
        self.time_label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.time_label.setFrameShape(QtWidgets.QFrame.Box)
        self.time_label.setLineWidth(1)
        self.time_label.setTextFormat(QtCore.Qt.AutoText)
        self.time_label.setScaledContents(False)
        self.time_label.setAlignment(QtCore.Qt.AlignCenter)
        self.time_label.setWordWrap(True)
        self.time_label.setObjectName("time_label")
        self.bed_label = QtWidgets.QLabel(self.centralwidget)
        self.bed_label.setGeometry(QtCore.QRect(120, 300, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bed_label.setFont(font)
        self.bed_label.setAlignment(QtCore.Qt.AlignCenter)
        self.bed_label.setObjectName("bed_label")
        self.bb_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.bb_pushButton.setGeometry(QtCore.QRect(40, 160, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bb_pushButton.setFont(font)
        self.bb_pushButton.setStyleSheet("background-color: rgb(255, 198, 199);")
        self.bb_pushButton.setObjectName("bb_pushButton")
        self.ab_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.ab_pushButton.setGeometry(QtCore.QRect(40, 220, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ab_pushButton.setFont(font)
        self.ab_pushButton.setStyleSheet("background-color: rgb(255, 232, 194);")
        self.ab_pushButton.setObjectName("ab_pushButton")
        self.bl_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.bl_pushButton.setGeometry(QtCore.QRect(220, 160, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bl_pushButton.setFont(font)
        self.bl_pushButton.setStyleSheet("background-color: rgb(255, 254, 202);")
        self.bl_pushButton.setObjectName("bl_pushButton")
        self.al_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.al_pushButton.setGeometry(QtCore.QRect(220, 220, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.al_pushButton.setFont(font)
        self.al_pushButton.setStyleSheet("background-color: rgb(219, 255, 199);")
        self.al_pushButton.setObjectName("al_pushButton")
        self.bd_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.bd_pushButton.setGeometry(QtCore.QRect(400, 160, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bd_pushButton.setFont(font)
        self.bd_pushButton.setStyleSheet("background-color: rgb(185, 227, 255);")
        self.bd_pushButton.setObjectName("bd_pushButton")
        self.ad_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.ad_pushButton.setGeometry(QtCore.QRect(400, 220, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ad_pushButton.setFont(font)
        self.ad_pushButton.setStyleSheet("background-color: rgb(201, 205, 255);")
        self.ad_pushButton.setObjectName("ad_pushButton")
        self.bbed_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.bbed_pushButton.setGeometry(QtCore.QRect(220, 330, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bbed_pushButton.setFont(font)
        self.bbed_pushButton.setStyleSheet("background-color: rgb(250, 211, 255);")
        self.bbed_pushButton.setObjectName("bbed_pushButton")
        select_time.setCentralWidget(self.centralwidget)

        self.retranslateUi(select_time)
        QtCore.QMetaObject.connectSlotsByName(select_time)

        def close_window():
            select_time.close()

        self.back_pushButton.clicked.connect(close_window)

    def retranslateUi(self, select_time):
        _translate = QtCore.QCoreApplication.translate
        select_time.setWindowTitle(_translate("select_time", "ตั้งเวลามื้อยา"))
        self.b_label.setText(_translate("select_time", "มื้อเช้า"))
        self.back_pushButton.setText(_translate("select_time", "ย้อนกลับ"))
        self.d_label.setText(_translate("select_time", "มื้อเย็น"))
        self.l_label.setText(_translate("select_time", "มื้อเที่ยง"))
        self.time_label.setText(_translate("select_time", "ตั้งเวลามื้อยา"))
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