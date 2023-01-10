# form implementation generated from reading ui file

from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        # change all this stuff later when it's working
        MainWindow.setObjectName("Main Window")
        MainWindow.resize(500,300)
        MainWindow.setStyleSheet("background-color: rgb(255,255,255);")
        
        self.button1 = QtWidgets.QPushButton(MainWindow)
        self.button1.setGeometry(QtCore.QRect,0,0,100,50)
        self.button1.setStyleSheet("background-color: rgb(0,0,0);")
        self.button1.setObjectName("Play_Button")
        
        self.button2 = QtWidgets.QPushButton(MainWindow)
        self.button2.setGeometry(QtCore.QRect(100,50,100,50))
        self.button2.setStyleSheet("background-color: rgb(100,100,100);")
        self.button2.setObjectName("Button2")
