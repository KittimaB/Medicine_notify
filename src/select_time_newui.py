# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'select_time_newui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
# ไม่ใช้แล้ว

class Ui_select_time(object):
    def setupUi(self, select_time):
        select_time.setObjectName("select_time")
        select_time.setFixedSize(1024, 600)
        # select_time.resize(1024, 600)
        select_time.setStyleSheet("background-color: rgb(23, 73, 110);")
        self.centralwidget = QtWidgets.QWidget(select_time)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, -60, 1021, 551))
        self.frame.setStyleSheet("\n"
"border-radius: 30px;\n"
"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(30, 100, 960, 81))
        self.frame_2.setStyleSheet("\n"
"border-radius: 40px;\n"
"background-color: rgb(23, 73, 110);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(320, 20, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(49, 219, 921, 291))
        self.frame_3.setStyleSheet("\n"
"border-radius: 16px;\n"
"background-color: rgb(215, 215, 215);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setGeometry(QtCore.QRect(40, 60, 181, 181))
        self.frame_4.setStyleSheet("border: 2px solid rgb(244, 212, 99);\n"
"border-radius: 16px;\n"
"background-color: rgb(255, 255, 255);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.bb_pushButton = QtWidgets.QPushButton(self.frame_4)
        self.bb_pushButton.setGeometry(QtCore.QRect(30, 50, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.bb_pushButton.setFont(font)
        self.bb_pushButton.setStyleSheet("border: 1px solid rgb(235, 109, 109);\n"
"border-radius: 9px;\n"
"background-color: rgb(235, 109, 109);\n"
"")
        self.bb_pushButton.setObjectName("bb_pushButton")
        self.ab_pushButton = QtWidgets.QPushButton(self.frame_4)
        self.ab_pushButton.setGeometry(QtCore.QRect(30, 110, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.ab_pushButton.setFont(font)
        self.ab_pushButton.setStyleSheet("border: 1px solid rgb(244, 212, 99);\n"
"border-radius: 9px;\n"
"background-color: rgb(244, 212, 99);")
        self.ab_pushButton.setObjectName("ab_pushButton")
        self.frame_5 = QtWidgets.QFrame(self.frame_3)
        self.frame_5.setGeometry(QtCore.QRect(40, 30, 181, 51))
        self.frame_5.setStyleSheet("\n"
"border-radius: 16px;\n"
"background-color: rgb(244, 212, 99);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_2 = QtWidgets.QLabel(self.frame_5)
        self.label_2.setGeometry(QtCore.QRect(60, 10, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.frame_6 = QtWidgets.QFrame(self.frame_3)
        self.frame_6.setGeometry(QtCore.QRect(260, 60, 181, 181))
        self.frame_6.setStyleSheet("border: 2px solid rgb(244, 212, 99);\n"
"border-radius: 16px;\n"
"background-color: rgb(255, 255, 255);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.bl_pushButton = QtWidgets.QPushButton(self.frame_6)
        self.bl_pushButton.setGeometry(QtCore.QRect(30, 50, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.bl_pushButton.setFont(font)
        self.bl_pushButton.setStyleSheet("border: 1px solid rgb(239, 151, 204);\n"
"border-radius: 9px;\n"
"background-color: rgb(239, 151, 204);")
        self.bl_pushButton.setObjectName("bl_pushButton")
        self.al_pushButton = QtWidgets.QPushButton(self.frame_6)
        self.al_pushButton.setGeometry(QtCore.QRect(30, 110, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.al_pushButton.setFont(font)
        self.al_pushButton.setStyleSheet("border: 1px solid rgb(169, 212, 98);\n"
"border-radius: 9px;\n"
"background-color: rgb(169, 212, 98);")
        self.al_pushButton.setObjectName("al_pushButton")
        self.frame_7 = QtWidgets.QFrame(self.frame_3)
        self.frame_7.setGeometry(QtCore.QRect(260, 30, 181, 51))
        self.frame_7.setStyleSheet("\n"
"border-radius: 16px;\n"
"background-color: rgb(244, 212, 99);")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.label_4 = QtWidgets.QLabel(self.frame_7)
        self.label_4.setGeometry(QtCore.QRect(40, 10, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.frame_8 = QtWidgets.QFrame(self.frame_3)
        self.frame_8.setGeometry(QtCore.QRect(480, 60, 181, 181))
        self.frame_8.setStyleSheet("border: 2px solid rgb(244, 212, 99);\n"
"border-radius: 16px;\n"
"background-color: rgb(255, 255, 255);")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.bd_pushButton = QtWidgets.QPushButton(self.frame_8)
        self.bd_pushButton.setGeometry(QtCore.QRect(30, 50, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.bd_pushButton.setFont(font)
        self.bd_pushButton.setStyleSheet("border: 1px solid rgb(235, 143, 76);\n"
"background-color: rgb(235, 143, 76);\n"
"border-radius: 9px;\n"
"\n"
"")
        self.bd_pushButton.setObjectName("bd_pushButton")
        self.ad_pushButton = QtWidgets.QPushButton(self.frame_8)
        self.ad_pushButton.setGeometry(QtCore.QRect(30, 110, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.ad_pushButton.setFont(font)
        self.ad_pushButton.setStyleSheet("border: 1px solid rgb(119, 156, 212);\n"
"background-color: rgb(119, 156, 212);\n"
"border-radius: 9px;\n"
"")
        self.ad_pushButton.setObjectName("ad_pushButton")
        self.frame_9 = QtWidgets.QFrame(self.frame_3)
        self.frame_9.setGeometry(QtCore.QRect(480, 30, 181, 51))
        self.frame_9.setStyleSheet("\n"
"border-radius: 16px;\n"
"background-color: rgb(244, 212, 99);")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.label_5 = QtWidgets.QLabel(self.frame_9)
        self.label_5.setGeometry(QtCore.QRect(60, 10, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.frame_10 = QtWidgets.QFrame(self.frame_3)
        self.frame_10.setGeometry(QtCore.QRect(700, 60, 181, 181))
        self.frame_10.setStyleSheet("border: 2px solid rgb(244, 212, 99);\n"
"border-radius: 16px;\n"
"background-color: rgb(255, 255, 255);")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.bbed_pushButton = QtWidgets.QPushButton(self.frame_10)
        self.bbed_pushButton.setGeometry(QtCore.QRect(30, 50, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.bbed_pushButton.setFont(font)
        self.bbed_pushButton.setStyleSheet("border: 1px solid rgb(176, 107, 193);\n"
"border-radius: 9px;\n"
"background-color: rgb(176, 107, 193);\n"
"")
        self.bbed_pushButton.setObjectName("bbed_pushButton")
        self.frame_11 = QtWidgets.QFrame(self.frame_3)
        self.frame_11.setGeometry(QtCore.QRect(700, 30, 181, 51))
        self.frame_11.setStyleSheet("\n"
"border-radius: 16px;\n"
"background-color: rgb(244, 212, 99);")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.label_6 = QtWidgets.QLabel(self.frame_11)
        self.label_6.setGeometry(QtCore.QRect(40, 10, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.home_label = QtWidgets.QLabel(self.centralwidget)
        self.home_label.setGeometry(QtCore.QRect(140, 550, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.home_label.setFont(font)
        self.home_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.home_label.setObjectName("home_label")
        self.druglist_label = QtWidgets.QLabel(self.centralwidget)
        self.druglist_label.setGeometry(QtCore.QRect(280, 550, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.druglist_label.setFont(font)
        self.druglist_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.druglist_label.setObjectName("druglist_label")
        self.pack_label = QtWidgets.QLabel(self.centralwidget)
        self.pack_label.setGeometry(QtCore.QRect(590, 550, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pack_label.setFont(font)
        self.pack_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.pack_label.setObjectName("pack_label")
        self.sort_label = QtWidgets.QLabel(self.centralwidget)
        self.sort_label.setGeometry(QtCore.QRect(720, 550, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.sort_label.setFont(font)
        self.sort_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.sort_label.setObjectName("sort_label")
        self.frame_12 = QtWidgets.QFrame(self.centralwidget)
        self.frame_12.setGeometry(QtCore.QRect(400, 509, 151, 81))
        self.frame_12.setStyleSheet("\n"
"border-radius: 16px;\n"
"background-color: rgb(255, 255, 255);")
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.time_label = QtWidgets.QLabel(self.frame_12)
        self.time_label.setGeometry(QtCore.QRect(20, 40, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.time_label.setFont(font)
        self.time_label.setStyleSheet("color: rgb(23, 73, 110);")
        self.time_label.setObjectName("time_label")
        select_time.setCentralWidget(self.centralwidget)

        self.retranslateUi(select_time)
        QtCore.QMetaObject.connectSlotsByName(select_time)

    def retranslateUi(self, select_time):
        _translate = QtCore.QCoreApplication.translate
        select_time.setWindowTitle(_translate("select_time", "ตั้งเวลามื้อยา"))
        self.label.setText(_translate("select_time", "ตั้งเวลามื้อยา"))
        self.bb_pushButton.setText(_translate("select_time", "ก่อน อาหาร"))
        self.ab_pushButton.setText(_translate("select_time", "หลัง อาหาร"))
        self.label_2.setText(_translate("select_time", "มื้อเช้า"))
        self.bl_pushButton.setText(_translate("select_time", "ก่อน อาหาร"))
        self.al_pushButton.setText(_translate("select_time", "หลัง อาหาร"))
        self.label_4.setText(_translate("select_time", "มื้อกลางวัน"))
        self.bd_pushButton.setText(_translate("select_time", "ก่อน อาหาร"))
        self.ad_pushButton.setText(_translate("select_time", "หลัง อาหาร"))
        self.label_5.setText(_translate("select_time", "มื้อเย็น"))
        self.bbed_pushButton.setText(_translate("select_time", "ก่อน อาหาร"))
        self.label_6.setText(_translate("select_time", "มื้อก่อนนอน"))
        self.home_label.setText(_translate("select_time", "หน้าหลัก"))
        self.druglist_label.setText(_translate("select_time", "คลังยา"))
        self.pack_label.setText(_translate("select_time", "วิธีใส่ยา"))
        self.sort_label.setText(_translate("select_time", "วิธีเรียงยา"))
        self.time_label.setText(_translate("select_time", "ตั้งเวลามื้อยา"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    select_time = QtWidgets.QMainWindow()
    ui = Ui_select_time()
    ui.setupUi(select_time)
    select_time.show()
    sys.exit(app.exec_())
