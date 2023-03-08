import sys
import os

# import QApplication and all the required widgets
from PyQt6 import uic, QtGui, QtCore, QtWidgets
from PyQt6.QtWidgets import *

# import main UI
from app.main_ui import Ui_MainWindow

class main_window(Ui_MainWindow):

    def __init__(self, dialog):
        Ui_MainWindow.__init__(self)
        self.setupUi(dialog)

        self.title = "Mozart Maker"
        self.left = 10
        self.top = 10
        self.width = 400
        self.height = 150

        self.button1.clicked.connect(self.test1)
        self.button2.clicked.connect(self.test2)

    def test1(self):
        self.button1.setStyleSheet("background-color: rgb(200,200,200);")
    
    def test2(self):
        self.button2.setStyleSheet("background-color: rgb(200,200,200);")

if __name__ == "__main__":
    app = QApplication([])
    window = main_window()
    window.show()
    app.exec()
    sys.exit(app.exec())