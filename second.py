# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'second.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class second_ui(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(844, 582)
        Form.setStyleSheet("#Form{\n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.user2_mesaj = QtWidgets.QLineEdit(Form)
        self.user2_mesaj.setGeometry(QtCore.QRect(180, 450, 461, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.user2_mesaj.setFont(font)
        self.user2_mesaj.setObjectName("user2_mesaj")
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setGeometry(QtCore.QRect(80, 30, 691, 401))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 689, 399))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gonder = QtWidgets.QPushButton(Form)
        self.gonder.setGeometry(QtCore.QRect(340, 510, 151, 51))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(17)
        self.gonder.setFont(font)
        self.gonder.setObjectName("gonder")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.user2_mesaj.setPlaceholderText(_translate("Form", "Mesajı daxil edin.."))
        self.gonder.setText(_translate("Form", "Göndər"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = second_ui()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())