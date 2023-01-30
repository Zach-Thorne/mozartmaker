# updated: 6:46 pm dec. 7
# TO DO
# upload different versions with timestamps to show progress lol
# create global variable to track which tab is open

import sys
from PyQt6 import QtWidgets, uic, QtCore, QtGui
from PyQt6.QtWidgets import QDialog

from app.MainWindow import Ui_Dialog

class MainWindow(Ui_Dialog):

    def __init__(self, dialog):

        self.current_task = ""
        dialog.title = "Mozart Maker"

        # Initialize dialogue window
        Ui_Dialog.__init__(self)
        self.setupUi(dialog)
        self.title = "Mozart Maker"

        # RESIZE WINDOW
        screen = app.primaryScreen()
        rect = screen.availableGeometry()
        x_screen, y_screen = rect.width(), rect.height()

        # calculate scale factor of initial dimensions : user screen size
        x_window, y_window = 750, 500 # initial dimensions of main application window
        x_scale, y_scale = x_screen/x_window, y_screen/y_window

        #
        #
        # SET DIMENSIONS

        # set dimensions & position for window
        width_window = int(750*x_scale) # width of window is initially set to 750
        height_window = int(500*y_scale) # height of window frame is initially set to 500
        dialog.resize(int(750*x_scale), int(500*y_scale)) # set width & height of dialog object
        self.FRAME_main_window.setGeometry(QtCore.QRect(0, 0, width_window, height_window)) # set dimensions for frame which contains all content

        # set dimensions for menu frame
        width_menu = int(150*x_scale) # width of all menu elements is initially set to 150
        height_menu = int(500*y_scale) # height of menu frame is initially set to 500
        self.FRAME_menu.setGeometry(QtCore.QRect(0,0, width_menu, height_menu))
        self.FRAME_menu.setStyleSheet("QFrame#FRAME_menu { background-color: #696969; }")

        # set dimensions for menu label
        height_label = int(100*y_scale)
        self.LABEL_logo.setGeometry(QtCore.QRect(0, 0, width_menu, height_label))

        # set dimensions for menu buttons
        height_menu_buttons = int(50*y_scale) # height of menu buttons is initially set to 50
        self.PB_play.setGeometry(QtCore.QRect(0, height_label, width_menu, height_menu_buttons))
        self.PB_song_gallery.setGeometry(QtCore.QRect(0, (height_label+height_menu_buttons), width_menu, height_menu_buttons))
        self.PB_user_guide.setGeometry(QtCore.QRect(0, (height_label+2*height_menu_buttons), width_menu, height_menu_buttons))

        #
        #
        # SET FORMATTING
        
        # set color of window frame
        self.FRAME_main_window.setStyleSheet("QFrame#FRAME_main_window { background-color: #343843; }")
        
        # set icon for menu label
        self.LABEL_logo.setPixmap(QtGui.QPixmap("logo_wide.png"))
        self.LABEL_logo.setScaledContents(True) # scale image to the size of the label
        
        # set formatting for menu buttons
        self.PB_play.setStyleSheet("background-color: rgb(200,200,200);")

        self.PB_play.setText("PLAY") # set text to be displayed on button
        self.PB_play.setFlat(True) # set appearance of button to be flat
        self.PB_play.setStyleSheet("QPushButton { font-style: bold; font-size: 18pt; color: white; background-color: #696969; border: none; vertical-align: middle; }")

        self.PB_song_gallery.setText("VIEW + EDIT\nSONG GALLERY")
        self.PB_song_gallery.setFlat(True)
        self.PB_song_gallery.setStyleSheet("QPushButton { font-style: bold; font-size: 18pt; color: white; background-color: #696969; border: none; vertical-align: middle; }")

        self.PB_user_guide.setText("USER GUIDE")
        self.PB_user_guide.setFlat(True)
        self.PB_user_guide.setStyleSheet("QPushButton { font-style: bold; font-size: 18pt; color: white; background-color: #696969; border: none; vertical-align: middle; }")
        
        #
        #
        # CONNECT BUTTON FUNCTIONALITY

        current_task = self.PB_play.clicked.connect(self.play_button_clicked)
        self.PB_song_gallery.clicked.connect(self.song_gallery_button_clicked)
        self.PB_user_guide.clicked.connect(self.user_guide_button_clicked)

        #
        #
        # SET UP "PLAY" FRAME

    #
    #
    # FUNCTION FOR PLAY BUTTON
    def play_button_clicked(self):

        # if the user is currently operating in another tab of the application
        if(self.current_task != "play"):
            self.PB_play.setStyleSheet("QPushButton#PB_play { font-style: bold; font-size: 18pt; color: 343843; background-color: #7DCB79; border: none; vertical-align: middle; }")
            self.current_task = "play"

        # if the user is already operating in the "play" tab, do nothing

    #
    #
    # FUNCTION FOR SONG GALLERY BUTTON
    def song_gallery_button_clicked(self):
        self.PB_song_gallery.setStyleSheet("QPushButton#PB_song_gallery { font-style: bold; font-size: 18pt; color: 343843; background-color: #7DCB79; border: none; vertical-align: middle; }")
    
    #
    #
    # FUNCTION FOR USER GUIDE BUTTON
    def user_guide_button_clicked(self):
        self.PB_user_guide.setStyleSheet("QPushButton#PB_user_guide { font-style: bold; font-size: 18pt; color: 343843; background-color: #7DCB79; border: none; vertical-align: middle; }")

app = QtWidgets.QApplication(sys.argv)
dialog = QtWidgets.QDialog()
prog = MainWindow(dialog)
dialog.show()
app.exec()

# Back up method of initializing UI in case something gets fucked
""" 
class MainWindow(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()                
"""