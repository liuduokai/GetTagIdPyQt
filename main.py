# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(537, 538)
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(10, 10, 351, 511))
        self.listWidget.setObjectName("listWidget")
        self.lcdNumber = QtWidgets.QLCDNumber(Form)
        self.lcdNumber.setGeometry(QtCore.QRect(380, 90, 101, 71))
        self.lcdNumber.setObjectName("lcdNumber")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(370, 10, 161, 81))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.ResetButton = QtWidgets.QPushButton(Form)
        self.ResetButton.setGeometry(QtCore.QRect(380, 340, 93, 28))
        self.ResetButton.setObjectName("ResetButton")
        self.CloseButton = QtWidgets.QPushButton(Form)
        self.CloseButton.setGeometry(QtCore.QRect(380, 410, 93, 28))
        self.CloseButton.setObjectName("CloseButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "检测到标签数量"))
        self.ResetButton.setText(_translate("Form", "重新检测"))
        self.CloseButton.setText(_translate("Form", "退出"))
