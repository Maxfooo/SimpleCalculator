'''
Created on Sep 14, 2014

@author: Max Ruiz
'''


from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from SimpleCalculator import *
import re
from math import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.currentFunction = ''
        self.currentVal = ''
        self.pastFunctions = []
        self.ans = 0
        self.parseState = 0
        self.prevInd = 0
        #self.safe_list = ['math','acos', 'asin', 'atan', 'atan2', 'ceil', 'cos', 'cosh', 'degrees', 'e', 'exp', 'fabs', 'floor', 'fmod', 'frexp', 'hypot', 'ldexp', 'log', 'log10', 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'abs']
        #self.safe_dict = dict([ (k, locals().get(k, None)) for k in self.safe_list ])
        self.configDisplay(0)
        self.keyPress()


    def parseFunction(self):
        opError = False
        errorOp = []
        ops = ['+', '/', '*', '^', '.', '-']
        split = re.findall(r'[\W\d]', self.currentFunction)

        a = split.count('(')
        b = split.count(')')
        c = a-b
        d = False
        if c != 0:
            d = True
            opError = True

        errorInd = []
        for x in range(len(split)):
            if x < len(split)-1:
                for z in ops:
                    if split[x] == z:
                        for y in ops:
                            if split[x+1] == y:
                                opError = True
                                errorOp.append(y)
                                errorInd.append(str(x+1))

        if not opError:
            try:
                self.ans = eval(self.currentFunction)
                self.displayAnswer()
                self.configDisplay(1)
                self.currentFunction = ''
            except:
                opError = True
                errorOp.append('?')


        if opError:
            self.currentFunction = ''
            if d:
                self.currentFunction = ('Unbalanced Parenthesis {0} (\'s and {1} )\'s'.format(a, b))
            else:
                try:
                    for x in errorOp:
                        self.currentFunction = self.currentFunction + str(x)
                    self.currentFunction = self.currentFunction + ' At place: '

                    for x in range(len(errorOp)):
                        if len(errorOp) > 0:
                            if len(errorOp) > 1 and x < len(errorOp)-1:
                                self.currentFunction = self.currentFunction + str(errorInd[x]) + ', '
                            else:
                                self.currentFunction = self.currentFunction + str(errorInd[x])
                except: pass

            self.ui.Display_textBrowser.insertPlainText('Error: ')
            self.displayFunction()
            self.configDisplay(1)



    def takeInput(self, value):
        if value is 'C':
            self.currentFunction = ''
            self.clearPrevious()
            self.configDisplay(-1)
        elif value is 'P':
            self.fetchPrevious()
            self.configDisplay(1)
            self.displayFunction()
        elif value is '=':
            self.storePrevious()
            self.configDisplay(1)
            self.parseFunction()
        elif value is 'N':
            self.currentFunction = self.currentFunction + '-'
            self.currentVal = '-'
            self.displayVal()
        elif value is '^':
            self.currentFunction = self.currentFunction + 'pow('
            self.currentVal = 'pow('
            self.displayVal()
        elif value is 'sqrt(':
            self.currentFunction = self.currentFunction + 'sqrt('
            self.currentVal = 'sqrt('
            self.displayVal()
        elif value is ',':
            self.currentFunction = self.currentFunction + ','
            self.currentVal = ','
            self.displayVal()
        elif value is 'sin(':
            self.currentFunction = self.currentFunction + 'sin('
            self.currentVal = 'sin('
            self.displayVal()
        elif value is 'cos(':
            self.currentFunction = self.currentFunction + 'cos('
            self.currentVal = 'cos('
            self.displayVal()
        elif value is 'exp(':
            self.currentFunction = self.currentFunction + 'exp('
            self.currentVal = 'exp('
            self.displayVal()
        elif value is 'PI':
            self.currentFunction = self.currentFunction + 'pi'
            self.currentVal = 'PI'
            self.displayVal()
        else:
            self.currentFunction = self.currentFunction + value
            self.currentVal = value
            self.displayVal()

    def storePrevious(self):
        self.pastFunctions.append(self.currentFunction)
        if len(self.pastFunctions) > 1:
            self.prevInd = self.prevInd + 1

    def fetchPrevious(self):
        if len(self.pastFunctions) > 0:
            self.currentFunction = self.pastFunctions[self.prevInd]
            if self.prevInd >= 1:
                self.prevInd = self.prevInd - 1
        else:
            pass

    def clearPrevious(self):
        self.prevInd = 0
        self.pastFunctions = []

    def displayVal(self):
        self.ui.Display_textBrowser.insertPlainText(self.currentVal)

    def displayFunction(self):
        self.ui.Display_textBrowser.insertPlainText(self.currentFunction)



    def displayAnswer(self):
        self.ui.Display_textBrowser.insertPlainText(str(self.ans))
        self.ans = 0
        self.currentFunction = ''

    def configDisplay(self, c):
        if c == 0:
            self.ui.Display_textBrowser.insertPlainText('>> ')
        elif c == 1:
            self.ui.Display_textBrowser.append('')
            self.configDisplay(0)
        elif c == -1:
            self.ui.Display_textBrowser.clear()
            self.configDisplay(0)
        else: pass



    def keyPress(self):
        self.ui.Clear.pressed.connect(lambda: self.takeInput('C'))
        self.ui.Previous.pressed.connect(lambda: self.takeInput('P'))
        self.ui.Zero.pressed.connect(lambda: self.takeInput('0'))
        self.ui.One.pressed.connect(lambda: self.takeInput('1'))
        self.ui.Two.pressed.connect(lambda: self.takeInput('2'))
        self.ui.Three.pressed.connect(lambda: self.takeInput('3'))
        self.ui.Four.pressed.connect(lambda: self.takeInput('4'))
        self.ui.Five.pressed.connect(lambda: self.takeInput('5'))
        self.ui.Six.pressed.connect(lambda: self.takeInput('6'))
        self.ui.Seven.pressed.connect(lambda: self.takeInput('7'))
        self.ui.Eight.pressed.connect(lambda: self.takeInput('8'))
        self.ui.Nine.pressed.connect(lambda: self.takeInput('9'))
        self.ui.Point.pressed.connect(lambda: self.takeInput('.'))
        self.ui.Negative.pressed.connect(lambda: self.takeInput('N'))
        self.ui.Equals.pressed.connect(lambda: self.takeInput('='))
        self.ui.LeftParen.pressed.connect(lambda: self.takeInput('('))
        self.ui.RightParen.pressed.connect(lambda: self.takeInput(')'))
        self.ui.Plus.pressed.connect(lambda: self.takeInput('+'))
        self.ui.Minus.pressed.connect(lambda: self.takeInput('-'))
        self.ui.Multiply.pressed.connect(lambda: self.takeInput('*'))
        self.ui.Divide.pressed.connect(lambda: self.takeInput('/'))
        self.ui.Exponent.pressed.connect(lambda: self.takeInput('^'))
        self.ui.Sqrt.pressed.connect(lambda: self.takeInput('sqrt('))
        self.ui.comma.pressed.connect(lambda: self.takeInput(','))
        self.ui.sine.pressed.connect(lambda: self.takeInput('sin('))
        self.ui.cosine.pressed.connect(lambda: self.takeInput('cos('))
        self.ui.eToThe.pressed.connect(lambda: self.takeInput('exp('))
        self.ui.Pi.pressed.connect(lambda: self.takeInput('PI'))


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    wind = MainWindow()
    wind.show()
    app.exec()
