# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SimpleCalculator.ui'
#
# Created: Sun Sep 14 02:35:50 2014
#      by: PyQt5 UI code generator 5.3.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(434, 316)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 401, 257))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Previous = QtWidgets.QPushButton(self.widget)
        self.Previous.setObjectName("Previous")
        self.gridLayout.addWidget(self.Previous, 1, 4, 1, 1)
        self.One = QtWidgets.QPushButton(self.widget)
        self.One.setObjectName("One")
        self.gridLayout.addWidget(self.One, 3, 0, 1, 1)
        self.Display_textBrowser = QtWidgets.QTextBrowser(self.widget)
        self.Display_textBrowser.setObjectName("Display_textBrowser")
        self.gridLayout.addWidget(self.Display_textBrowser, 0, 0, 3, 4)
        self.Plus = QtWidgets.QPushButton(self.widget)
        self.Plus.setObjectName("Plus")
        self.gridLayout.addWidget(self.Plus, 3, 3, 1, 1)
        self.Clear = QtWidgets.QPushButton(self.widget)
        self.Clear.setObjectName("Clear")
        self.gridLayout.addWidget(self.Clear, 0, 4, 1, 1)
        self.Two = QtWidgets.QPushButton(self.widget)
        self.Two.setObjectName("Two")
        self.gridLayout.addWidget(self.Two, 3, 1, 1, 1)
        self.Five = QtWidgets.QPushButton(self.widget)
        self.Five.setObjectName("Five")
        self.gridLayout.addWidget(self.Five, 4, 1, 1, 1)
        self.Three = QtWidgets.QPushButton(self.widget)
        self.Three.setObjectName("Three")
        self.gridLayout.addWidget(self.Three, 3, 2, 1, 1)
        self.Pi = QtWidgets.QPushButton(self.widget)
        self.Pi.setObjectName("Pi")
        self.gridLayout.addWidget(self.Pi, 3, 4, 1, 1)
        self.Four = QtWidgets.QPushButton(self.widget)
        self.Four.setObjectName("Four")
        self.gridLayout.addWidget(self.Four, 4, 0, 1, 1)
        self.Minus = QtWidgets.QPushButton(self.widget)
        self.Minus.setObjectName("Minus")
        self.gridLayout.addWidget(self.Minus, 4, 3, 1, 1)
        self.Equals = QtWidgets.QPushButton(self.widget)
        self.Equals.setObjectName("Equals")
        self.gridLayout.addWidget(self.Equals, 2, 4, 1, 1)
        self.Six = QtWidgets.QPushButton(self.widget)
        self.Six.setObjectName("Six")
        self.gridLayout.addWidget(self.Six, 4, 2, 1, 1)
        self.eToThe = QtWidgets.QPushButton(self.widget)
        self.eToThe.setObjectName("eToThe")
        self.gridLayout.addWidget(self.eToThe, 4, 4, 1, 1)
        self.Seven = QtWidgets.QPushButton(self.widget)
        self.Seven.setObjectName("Seven")
        self.gridLayout.addWidget(self.Seven, 5, 0, 1, 1)
        self.LeftParen = QtWidgets.QPushButton(self.widget)
        self.LeftParen.setObjectName("LeftParen")
        self.gridLayout.addWidget(self.LeftParen, 7, 0, 1, 1)
        self.Divide = QtWidgets.QPushButton(self.widget)
        self.Divide.setObjectName("Divide")
        self.gridLayout.addWidget(self.Divide, 6, 3, 1, 1)
        self.sine = QtWidgets.QPushButton(self.widget)
        self.sine.setObjectName("sine")
        self.gridLayout.addWidget(self.sine, 6, 4, 1, 1)
        self.Eight = QtWidgets.QPushButton(self.widget)
        self.Eight.setObjectName("Eight")
        self.gridLayout.addWidget(self.Eight, 5, 1, 1, 1)
        self.comma = QtWidgets.QPushButton(self.widget)
        self.comma.setObjectName("comma")
        self.gridLayout.addWidget(self.comma, 7, 4, 1, 1)
        self.cosine = QtWidgets.QPushButton(self.widget)
        self.cosine.setObjectName("cosine")
        self.gridLayout.addWidget(self.cosine, 5, 4, 1, 1)
        self.Point = QtWidgets.QPushButton(self.widget)
        self.Point.setObjectName("Point")
        self.gridLayout.addWidget(self.Point, 6, 0, 1, 1)
        self.Zero = QtWidgets.QPushButton(self.widget)
        self.Zero.setObjectName("Zero")
        self.gridLayout.addWidget(self.Zero, 6, 1, 1, 1)
        self.Negative = QtWidgets.QPushButton(self.widget)
        self.Negative.setObjectName("Negative")
        self.gridLayout.addWidget(self.Negative, 6, 2, 1, 1)
        self.RightParen = QtWidgets.QPushButton(self.widget)
        self.RightParen.setObjectName("RightParen")
        self.gridLayout.addWidget(self.RightParen, 7, 1, 1, 1)
        self.Multiply = QtWidgets.QPushButton(self.widget)
        self.Multiply.setObjectName("Multiply")
        self.gridLayout.addWidget(self.Multiply, 5, 3, 1, 1)
        self.Sqrt = QtWidgets.QPushButton(self.widget)
        self.Sqrt.setObjectName("Sqrt")
        self.gridLayout.addWidget(self.Sqrt, 7, 3, 1, 1)
        self.Exponent = QtWidgets.QPushButton(self.widget)
        self.Exponent.setObjectName("Exponent")
        self.gridLayout.addWidget(self.Exponent, 7, 2, 1, 1)
        self.Nine = QtWidgets.QPushButton(self.widget)
        self.Nine.setObjectName("Nine")
        self.gridLayout.addWidget(self.Nine, 5, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 434, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuMade_By = QtWidgets.QMenu(self.menuFile)
        self.menuMade_By.setObjectName("menuMade_By")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionMax_A_Ruiz = QtWidgets.QAction(MainWindow)
        self.actionMax_A_Ruiz.setObjectName("actionMax_A_Ruiz")
        self.menuMade_By.addAction(self.actionMax_A_Ruiz)
        self.menuFile.addAction(self.menuMade_By.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Previous.setText(_translate("MainWindow", "Previous"))
        self.One.setText(_translate("MainWindow", "1"))
        self.Plus.setText(_translate("MainWindow", "+"))
        self.Clear.setText(_translate("MainWindow", "Clear"))
        self.Two.setText(_translate("MainWindow", "2"))
        self.Five.setText(_translate("MainWindow", "5"))
        self.Three.setText(_translate("MainWindow", "3"))
        self.Pi.setText(_translate("MainWindow", "PI"))
        self.Four.setText(_translate("MainWindow", "4"))
        self.Minus.setText(_translate("MainWindow", "-"))
        self.Equals.setText(_translate("MainWindow", "="))
        self.Six.setText(_translate("MainWindow", "6"))
        self.eToThe.setText(_translate("MainWindow", "e^"))
        self.Seven.setText(_translate("MainWindow", "7"))
        self.LeftParen.setText(_translate("MainWindow", "("))
        self.Divide.setText(_translate("MainWindow", "/"))
        self.sine.setText(_translate("MainWindow", "sin"))
        self.Eight.setText(_translate("MainWindow", "8"))
        self.comma.setText(_translate("MainWindow", ","))
        self.cosine.setText(_translate("MainWindow", "cos"))
        self.Point.setText(_translate("MainWindow", "."))
        self.Zero.setText(_translate("MainWindow", "0"))
        self.Negative.setText(_translate("MainWindow", "(-)"))
        self.RightParen.setText(_translate("MainWindow", ")"))
        self.Multiply.setText(_translate("MainWindow", "*"))
        self.Sqrt.setText(_translate("MainWindow", "sqrt"))
        self.Exponent.setText(_translate("MainWindow", "^"))
        self.Nine.setText(_translate("MainWindow", "9"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuMade_By.setTitle(_translate("MainWindow", "Made By . . ."))
        self.actionMax_A_Ruiz.setText(_translate("MainWindow", "Max A. Ruiz"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

