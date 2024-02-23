from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_loading(object):
    def setupUi(self, loading):
        loading.setObjectName("loading")
        loading.resize(683, 400)
        loading.setStyleSheet("\n"
                              "background-color: rgb(23, 73, 110);")
        self.centralwidget = QtWidgets.QWidget(loading)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 60, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")

        self.img_label = QtWidgets.QLabel(self.centralwidget)
        self.img_label.setGeometry(QtCore.QRect(280, 150, 110, 100))
        self.img_label.setText("")
        self.img_label.setPixmap(QtGui.QPixmap(":/image/load.png"))
        self.img_label.setScaledContents(True)
        self.img_label.setAlignment(QtCore.Qt.AlignCenter)
        self.img_label.setObjectName("img_label")

        loading.setCentralWidget(self.centralwidget)

        self.retranslateUi(loading)
        QtCore.QMetaObject.connectSlotsByName(loading)

    def retranslateUi(self, loading):
        _translate = QtCore.QCoreApplication.translate
        loading.setWindowTitle(_translate("loading", "loading"))
        self.label.setText(_translate("loading", "กรุณารอสักครู่..."))

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    loading = QtWidgets.QMainWindow()
    ui = Ui_loading()
    ui.setupUi(loading)
    loading.show()
    sys.exit(app.exec_())
