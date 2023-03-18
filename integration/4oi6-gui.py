# updated: 6:46 pm dec. 7
# TO DO
# upload different versions with timestamps to show progress lol
# create global variable to track which tab is open
# change font size according to size of window
# combobox: change selection highlight color, change appearance of dropdown arrow
# once user has selected their preferences, change "play" button to green
# clear combo box items
# combo box set default value

import sys
from integration_for_gui import *
from PyQt6 import QtWidgets, uic, QtCore, QtGui
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QDialog, QFrame

from app.MainWindow import Ui_Dialog

class MainWindow(Ui_Dialog):

    def __init__(self, dialog):
        self.song_selection = ""
        self.mode = ""
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
        x_window, y_window = 750, 500 # initial dimensions of main application window
        
        # calculate scale factor of initial dimensions : user screen size
        self.x_scale, self.y_scale = x_screen/x_window, y_screen/y_window

        self.FRAME_play.setVisible(False)
        self.tempo_flag = "0" #default

        #
        #
        # CONNECT BUTTON FUNCTIONALITY

        self.current_task = self.PB_play.clicked.connect(self.play_button_clicked)
        self.PB_song_gallery.clicked.connect(self.song_gallery_button_clicked)
        self.PB_user_guide.clicked.connect(self.user_guide_button_clicked)
        self.PB_play_2.clicked.connect(self.final_play_button_clicked)

        self.setup_window(dialog)

    def setup_window(self, dialog):

        #
        #
        # SET DIMENSIONS

        # set dimensions & position for window
        self.width_window = int(750*self.x_scale) # width of window is initially set to 750
        self.height_window = int(500*self.y_scale) # height of window frame is initially set to 500
        dialog.resize(int(750*self.x_scale), int(500*self.y_scale)) # set width & height of dialog object
        self.FRAME_main_window.setGeometry(QtCore.QRect(0, 0, self.width_window, self.height_window)) # set dimensions for frame which contains all content

        # set dimensions for menu frame
        self.width_menu = int(150*self.x_scale) # width of all menu elements is initially set to 150
        self.height_menu = int(500*self.y_scale) # height of menu frame is initially set to 500
        self.FRAME_menu.setGeometry(QtCore.QRect(0,0, self.width_menu, self.height_menu))
        self.FRAME_menu.setStyleSheet("QFrame#FRAME_menu { background-color: #696969; }")

        # set dimensions for menu label
        height_label = int(100*self.y_scale)
        self.LABEL_logo.setGeometry(QtCore.QRect(0, 0, self.width_menu, height_label))

        # set dimensions for menu buttons
        height_menu_buttons = int(50*self.y_scale) # height of menu buttons is initially set to 50
        self.PB_play.setGeometry(QtCore.QRect(0, height_label, self.width_menu, height_menu_buttons))
        self.PB_song_gallery.setGeometry(QtCore.QRect(0, (height_label+height_menu_buttons), self.width_menu, height_menu_buttons))
        self.PB_user_guide.setGeometry(QtCore.QRect(0, (height_label+2*height_menu_buttons), self.width_menu, height_menu_buttons))

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
    
    def setup_play_screen(self):

        #
        #
        # SET UP SCREEN FRAME

        # screen frame: dimensions
        self.width_play_screen = self.width_window - self.width_menu
        self.height_play_screen = self.height_window
        self.FRAME_play.setGeometry(QtCore.QRect(self.width_menu, 0, self.width_play_screen, self.height_play_screen))
        
        # screen frame: formatting
        self.FRAME_play.setStyleSheet("QFrame#FRAME_play { background-color: #343843; }")

        #
        #
        # FRAMES

        # frames: dimensions
        self.frame_width = int(0.8*self.width_play_screen)
        self.frame_height = int(0.1*self.height_play_screen)

        # frames: set geometry
        self.FRAME_mode.setGeometry (QtCore.QRect(int(0.1*self.width_play_screen), int(0.1*self.height_play_screen),  self.frame_width, self.frame_height))
        self.FRAME_song.setGeometry (QtCore.QRect(int(0.1*self.width_play_screen), int(0.25*self.height_play_screen), self.frame_width, self.frame_height))
        self.FRAME_tempo.setGeometry(QtCore.QRect(int(0.1*self.width_play_screen), int(0.4*self.height_play_screen),  self.frame_width, self.frame_height))

        # frames: styling
        self.FRAME_mode.setStyleSheet("QFrame#FRAME_mode { border-radius: 15px; background-color: #696969; } ")
        self.FRAME_song.setStyleSheet("QFrame#FRAME_song { border-radius: 15px; background-color: #696969; } ")
        self.FRAME_tempo.setStyleSheet("QFrame#FRAME_tempo { border-radius: 15px; background-color: #696969; } ")
        
        #
        #
        # LABELS

        # labels: dimensions
        self.label_width = int(0.2*self.frame_width)
        self.label_height = int(0.5*self.frame_height)
        
        # labels: set geometry
        self.LABEL_mode.setGeometry(QtCore.QRect(int(0.05*self.frame_width), int(0.25*self.frame_height), self.label_width, self.label_height))
        self.LABEL_song.setGeometry(QtCore.QRect(int(0.05*self.frame_width), int(0.25*self.frame_height), self.label_width, self.label_height))

        # labels: styling
        self.LABEL_mode.setStyleSheet("QLabel#LABEL_mode { color: white; font-style: bold; font-size: 14pt; }")
        self.LABEL_song.setStyleSheet("QLabel#LABEL_song { color: white; font-style: bold; font-size: 14pt; }")

        #
        #
        # PUSH BUTTONS

        # buttons: dimensions
        self.button_width = int(0.3*self.frame_width)
        self.button_height = int(0.5*self.frame_height)

        # buttons: set geometry
        self.PB_mode_1.setGeometry (QtCore.QRect(int(0.3*self.frame_width),  int(0.25*self.frame_height), self.button_width, self.button_height))
        self.PB_mode_2.setGeometry (QtCore.QRect(int(0.65*self.frame_width), int(0.25*self.frame_height), self.button_width, self.button_height))
        self.PB_tempo_1.setGeometry(QtCore.QRect(int(0.03*self.frame_width), int(0.25*self.frame_height), self.button_width, self.button_height))
        self.PB_tempo_2.setGeometry(QtCore.QRect(int(0.35*self.frame_width),  int(0.25*self.frame_height), self.button_width, self.button_height))
        self.PB_play_2.setGeometry (QtCore.QRect(int(0.38*self.width_play_screen), int(0.7*self.height_window), self.button_width, self.frame_height))

        # buttons: styling
        self.PB_mode_1.setFlat(True)
        self.PB_mode_1.setStyleSheet("QPushButton#PB_mode_1 { color: #343843; background-color: #A5A5A5; font-style: bold; font-size: 12pt; border-radius: 8px; }")
        self.PB_mode_2.setFlat(True)
        self.PB_mode_2.setStyleSheet("QPushButton#PB_mode_2 { color: #343843; background-color: #A5A5A5; font-style: bold; font-size: 12pt; border-radius: 8px; }")

        self.PB_tempo_1.setFlat(True)
        self.PB_tempo_1.setStyleSheet("QPushButton#PB_tempo_1 { color: #343843; background-color: #A5A5A5; font-style: bold; font-size: 12pt; border-radius: 8px; }")
        self.PB_tempo_2.setFlat(True)
        self.PB_tempo_2.setStyleSheet("QPushButton#PB_tempo_2 { color: #343843; background-color: #A5A5A5; font-style: bold; font-size: 12pt; border-radius: 8px; }")

        self.PB_play_2.setStyleSheet("QPushButton#PB_play_2 { color: #343843; background-color: #A5A5A5; font-style: bold; font-size: 12pt; border-radius: 8px; } ")

        # buttons: functionality
        self.PB_mode_1.clicked.connect(self.mode_1_button_clicked)
        self.PB_mode_2.clicked.connect(self.mode_2_button_clicked)

        self.PB_tempo_1.clicked.connect(self.tempo_button_1_clicked)
        self.PB_tempo_2.clicked.connect(self.tempo_button_2_clicked)

        #
        #
        # COMBO BOX

        # combo box: dimensions
        self.combo_width = int(0.65*self.frame_width)
        self.combo_height = self.button_height

        # combo box: set geometry
        self.COMBO_song.setGeometry(QtCore.QRect(int(0.3*self.frame_width), int(0.25*self.frame_height), self.combo_width, self.combo_height))

        # combo box: set styling
        self.COMBO_song.setStyleSheet("QComboBox#COMBO_song { color: #343843; background-color: #A5A5A5; border-radius: 10px; font-style: bold; font-size: 12pt; selection-background-color: #7DCB79; } ")

        # combo box: set items
        self.COMBO_song.setEditable(True)
        self.COMBO_song.addItem("C Scale")
        self.COMBO_song.addItem("D Scale")
        self.COMBO_song.addItem("E Scale")
        self.COMBO_song.addItem("F Scale")
        self.COMBO_song.addItem("G Scale")
        self.COMBO_song.addItem("Mary Had a Little Lamb")
        
        #
        #
        # SPIN BOX

        # spin box: dimensions
        self.spin_width = self.button_width
        self.spin_height = self.button_height

        # spin box: set geometry
        self.SPIN_tempo.setGeometry(QtCore.QRect(int(0.67*self.frame_width), int(0.25*self.frame_height), self.spin_width, self.spin_height))

        # spin box: set styling
        self.SPIN_tempo.setStyleSheet("QSpinBox#SPIN_tempo { color: #343843; background-color: #A5A5A5; font-style: bold; font-size: 14pt; border-radius: 10px; } ")

        # spin box: set values
        self.SPIN_tempo.setMinimum(0)
        self.SPIN_tempo.setMaximum(200)
        self.SPIN_tempo.singleStep()

        #
        #
        # DISPLAY PLAY SCREEN
        self.FRAME_play.setVisible(True)

    #
    #
    # FUNCTION FOR PLAY BUTTON
    def play_button_clicked(self):

        # if the user is currently operating in another tab of the application
        if(self.current_task != "play"):

            # change appearance of menu buttons to indicate the play button is selected
            self.PB_play.setStyleSheet("QPushButton#PB_play { font-style: bold; font-size: 18pt; color: #343843; background-color: #7DCB79; border: none; vertical-align: middle; }")
            self.PB_song_gallery.setStyleSheet("QPushButton#PB_song_gallery { font-style: bold; font-size: 18pt; color: white; background-color: #696969; border: none; vertical-align: middle; }")
            self.PB_user_guide.setStyleSheet("QPushButton#PB_user_guide { font-style: bold; font-size: 18pt; color: white; background-color: #696969; border: none; vertical-align: middle; }")

            # show play screen and hide other screens
            self.setup_play_screen()
            self.FRAME_play.setVisible(True)
            
            # change current task indicator
            self.current_task = "play"
            
            # reset mode selection indicator variable for play screen
            self.mode = ""

        # if the user is already operating in the "play" tab, do nothing

    #
    #
    # FUNCTION FOR SONG GALLERY BUTTON
    def song_gallery_button_clicked(self):
        if(self.current_task != "song_gallery"):

            # change appearance of menu buttons to indicate the song gallery button is selected
            self.PB_song_gallery.setStyleSheet("QPushButton#PB_song_gallery { font-style: bold; font-size: 18pt; color: #343843; background-color: #7DCB79; border: none; vertical-align: middle; }")
            self.PB_play.setStyleSheet("QPushButton#PB_play { font-style: bold; font-size: 18pt; color: white; background-color: #696969; border: none; vertical-align: middle; }")
            self.PB_user_guide.setStyleSheet("QPushButton#PB_user_guide { font-style: bold; font-size: 18pt; color: white; background-color: #696969; border: none; vertical-align: middle; }")

            # show song gallery screen and hide other screens
            self.FRAME_play.setVisible(False)

            # change current task indicator
            self.current_task = "song_gallery"

    #
    #
    # FUNCTION FOR USER GUIDE BUTTON
    def user_guide_button_clicked(self):
        if(self.current_task != "user_guide"):

            # change appearance of menu buttons to indicate the user guide button is selected
            self.PB_play.setStyleSheet("QPushButton#PB_play { font-style: bold; font-size: 18pt; color: white; background-color: #696969; border: none; vertical-align: middle; }")
            self.PB_song_gallery.setStyleSheet("QPushButton#PB_song_gallery { font-style: bold; font-size: 18pt; color: white; background-color: #696969; border: none; vertical-align: middle; }")
            self.PB_user_guide.setStyleSheet("QPushButton#PB_user_guide { font-style: bold; font-size: 18pt; color: 343843; background-color: #7DCB79; border: none; vertical-align: middle; }")

            # show user guide screen and hide other screens
            self.FRAME_play.setVisible(False)

            # change current task indicator
            self.current_task = "user_guide"

    #
    #
    # FUNCTION FOR MODE 1 (LEARNING MODE) BUTTON
    def mode_1_button_clicked(self):
        self.mode = "learn"

        # change appearance of training mode button to appear selected
        self.PB_mode_1.setStyleSheet("QPushButton#PB_mode_1 { color: #343843; background-color: #7DCB79; font-style: bold; font-size: 12pt; border-radius: 8px; }")

        # reset testing mode button
        self.PB_mode_2.setStyleSheet("QPushButton#PB_mode_2 { color: #343843; background-color: #A5A5A5; font-style: bold; font-size: 12pt; border-radius: 8px; }")

    #
    #
    # FUNCTION FOR MODE 2 (TESTING MODE) BUTTON
    def mode_2_button_clicked(self):
        self.mode = "test"

        # change appearance of testing mode button to appear selected
        self.PB_mode_2.setStyleSheet("QPushButton#PB_mode_2 { color: #343843; background-color: #7DCB79; font-style: bold; font-size: 12pt; border-radius: 8px; }")

        # reset training mode button
        self.PB_mode_1.setStyleSheet("QPushButton#PB_mode_1 { color: #343843; background-color: #A5A5A5; font-style: bold; font-size: 12pt; border-radius: 8px; }")

    #
    #
    # FUNCTION FOR TEMPO 1 (NO TIMING) BUTTON
    def tempo_button_1_clicked(self):
        self.tempo_flag = FALSE

        # reset training mode button
        self.PB_tempo_2.setStyleSheet("QPushButton#PB_tempo_2 { color: #343843; background-color: #A5A5A5; font-style: bold; font-size: 12pt; border-radius: 8px; }")
        self.PB_tempo_1.setStyleSheet("QPushButton#PB_tempo_1 { color: #343843; background-color: #7DCB79; font-style: bold; font-size: 12pt; border-radius: 8px; }")

    #
    #
    # FUNCTION FOR TEMPO 2 (TIMING) BUTTON
    def tempo_button_2_clicked(self):
        self.tempo_flag = TRUE

        # reset training mode button
        self.PB_tempo_1.setStyleSheet("QPushButton#PB_tempo_1 { color: #343843; background-color: #A5A5A5; font-style: bold; font-size: 12pt; border-radius: 8px; }")
        self.PB_tempo_2.setStyleSheet("QPushButton#PB_tempo_2 { color: #343843; background-color: #7DCB79; font-style: bold; font-size: 12pt; border-radius: 8px; }")

    #
    #
    # FUNCTION FOR FINAL PLAY (START PLAYING) BUTTON
    def final_play_button_clicked(self):
        # change styling for play button
        self.PB_play_2.setStyleSheet("QPushButton#PB_play_2 { color: #343843; background-color: #7DCB79; font-style: bold; font-size: 12pt; border-radius: 8px; }")
        
        # tempo selection
        if(self.tempo_flag == TRUE):
            tempo = self.SPIN_tempo.value()
        else:
            tempo = 0
        
        # song selection
        if(self.COMBO_song.currentText() == "Mary Had a Little Lamb"):
            self.song_selection = "mhall"
        elif(self.COMBO_song.currentText() == "C Scale"):
            self.song_selection = "C"
        elif(self.COMBO_song.currentText() == "D Scale"):
            self.song_selection = "D"
        elif(self.COMBO_song.currentText() == "E Scale"):
            self.song_selection = "E"
        elif(self.COMBO_song.currentText() == "F Scale"):
            self.song_selection = "F"
        elif(self.COMBO_song.currentText() == "G Scale"):
            self.song_selection = "G"

        # call integration function with parameters from user input
        result = run_mozart(self.song_selection, self.mode, self.tempo_flag, tempo)

app = QtWidgets.QApplication(sys.argv)
dialog = QtWidgets.QDialog()
prog = MainWindow(dialog)
dialog.show()
app.exec()