# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'piano_ui.ui'
#
# Created by: PyQt5 UI code generator 5.11
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(586, 143)
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setGeometry(QtCore.QRect(20, 40, 541, 71))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.C = QtWidgets.QPushButton(self.splitter)
        self.C.setObjectName("C")
        self.D = QtWidgets.QPushButton(self.splitter)
        self.D.setObjectName("D")
        self.E = QtWidgets.QPushButton(self.splitter)
        self.E.setObjectName("E")
        self.F = QtWidgets.QPushButton(self.splitter)
        self.F.setObjectName("F")
        self.G = QtWidgets.QPushButton(self.splitter)
        self.G.setObjectName("G")
        self.A = QtWidgets.QPushButton(self.splitter)
        self.A.setObjectName("A")
        self.B = QtWidgets.QPushButton(self.splitter)
        self.B.setObjectName("B")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Пианино"))
        self.C.setText(_translate("Form", "До"))
        self.D.setText(_translate("Form", "Ре"))
        self.E.setText(_translate("Form", "Ми"))
        self.F.setText(_translate("Form", "Фа"))
        self.G.setText(_translate("Form", "Соль"))
        self.A.setText(_translate("Form", "Ля"))
        self.B.setText(_translate("Form", "Си"))

