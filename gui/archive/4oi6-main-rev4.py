""" TO DO:
# INCREASE EVERYTHING BY THIS SCALE FACTOR
# set dimensions to be fractions of the screen size
# see if there's a way to read the dimensions of widgets from qtdesigner rather than hard coding them
# dynamically adjust font size
# opening welcome screen
"""

import sys

#1 Import QApplication and all the required widgets
from PyQt6 import uic, QtGui, QtCore
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QMainWindow, QPushButton
from PyQt6.QtGui import QScreen # I think this can be removed

class UI_Login(object):

    def setupUI(self, Login):
        Login.setObjectName("Login")
        Login.resize(581,294)
        self.PB_Confirm = QPushButton(Login)

    # Initialize app
    app = QApplication([])

    # import Qt Designer file
    Form, Window = uic.loadUiType("designer.ui")
    form = Form()
    window = Window()
    form.setupUi(window)

    def button1_clicked(form):
        print("clicked")
        form.button1.setText("CLICKED")

    #
    # FORMAT WINDOW

    # Set title the user sees in the taskbar
    window.setObjectName("Mozart Maker") # this isn't right lol

    # style window
    window.setStyleSheet("background-color: #343843;")

    #
    #
    # Calculate dimensions of main window and child elements

    # get dimensions of user screen
    screen = app.primaryScreen()
    rect = screen.availableGeometry()
    x_screen, y_screen = rect.width(), rect.height()

    # calculate scale factor of initial dimensions : user screen size
    x_window, y_window = 750, 500 # initial dimensions of main application window
    x_scale, y_scale = x_screen/x_window, y_screen/y_window

    # calculate dimensions of child elements
    width_menu = int(150*x_scale) # width of all menu elements is initially set to 150

    height_menu_frame = int(750*y_scale) # height of menu frame is initially set to 750
    height_menu_buttons = int(50*y_scale) # height of menu buttons is initially set to 50
    height_menu_logo = int(100*y_scale) # height of menu logo is initially set to 80

    #
    #
    # FRAME 1
    form.frame1.setStyleSheet("QFrame { background-color: #696969; }") # set background colour of menu frame
    form.frame1.setGeometry(QtCore.QRect(0, 0, width_menu, height_menu_frame)) # set dimensions of menu frame

    #
    #
    # LABEL 1 - logo

    form.label1.setPixmap(QtGui.QPixmap("logo_wide.png")) # set image to be displayed
    form.label1.setGeometry(QtCore.QRect(0, 0, width_menu, height_menu_logo)) # set dimensions of the label
    form.label1.setScaledContents(True) # scale image to the size of the label

    #
    #
    # BUTTON 1 - "play" button
    form.button1.setText("PLAY") # set text to be displayed on button
    form.button1.setGeometry(QtCore.QRect(0, height_menu_logo, width_menu, height_menu_buttons)) # set dimensions + position of the button
    form.button1.setFlat(True) # set appearance of button to be flat
    form.button1.clicked.connect(button1_clicked(form)) # set function call when button is clicked

    form.button1.setStyleSheet("QPushButton { font-style: bold; font-size: 18pt; color: white; background-color: #696969; border: none; vertical-align: middle; }\n"
    "QPushButton:pressed { color: #343843; background-color: #7DCB79; }\n")

    #
    # BUTTON 2 - "song gallery" button

    # coordinates of button2
    form.button2.setText("VIEW + EDIT\nSONG GALLERY") # set text to be displayed on button
    form.button2.setGeometry(QtCore.QRect(0, (height_menu_logo + height_menu_buttons),width_menu, height_menu_buttons)) # set dimensions + position of the button
    form.button2.setFlat(True) # set appearance of button to be flat

    form.button2.setStyleSheet("QPushButton { font-style: bold; font-size: 18pt; color: white; background-color: #696969; border: none; }\n"
    "QPushButton:pressed { color: #343843; background-color: #7DCB79; }\n")

    #
    # BUTTON 3 - "user guide" button

    form.button3.setText("USER GUIDE") # set text to be displayed on button
    form.button3.setGeometry(QtCore.QRect(0, (height_menu_logo + 2*height_menu_buttons), width_menu, height_menu_buttons)) # set dimensions + position of the button
    form.button3.setFlat(True) # set appearance of button to be flat

    form.button3.setStyleSheet("QPushButton { font-style: bold; font-size: 18pt; color: white; background-color: #696969; border: none; }\n"
    "QPushButton:pressed { color: #343843; background-color: #7DCB79; }\n")

    #
    #
    #

    # resize UI dynamic to screen size
    window.resize(x_screen,y_screen)
    window.move(0,0) # move to center

    window.show()
    app.exec()

    #5 Run your application's event loop
    sys.exit(app.exec())