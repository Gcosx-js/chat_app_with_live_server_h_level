# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'connection.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class first_ui(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(490, 325)
        font = QtGui.QFont()
        font.setFamily("NSimSun")
        Form.setFont(font)
        Form.setStyleSheet("#Form{\n"
"    \n"
"    background-color: rgb(2, 141, 200);\n"
"}")
        self.baglan_button = QtWidgets.QPushButton(Form)
        self.baglan_button.setGeometry(QtCore.QRect(190, 150, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(16)
        self.baglan_button.setFont(font)
        self.baglan_button.setObjectName("baglan_button")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(60, 230, 411, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.username_input = QtWidgets.QLineEdit(Form)
        self.username_input.setGeometry(QtCore.QRect(110, 50, 271, 61))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(37)
        self.username_input.setFont(font)
        self.username_input.setText("")
        self.username_input.setObjectName("username_input")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", " Join your friend now!"))
        self.baglan_button.setText(_translate("Form", "Bağlan"))
        self.label_4.setText(_translate("Form", "Qeyd : Cihazın Wi-Fi bağlantısı vacibdir!"))
        self.username_input.setPlaceholderText(_translate("Form", "Username"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = first_ui()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
