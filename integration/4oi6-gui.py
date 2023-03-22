#
# EE 4OI6 CAPSTONE 2023
# Sophie Ciardullo
# March 19, 2023
#

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

        self.FRAME_inProgress.setVisible(False)
        self.FRAME_play.setVisible(False)
        self.FRAME_feedback.setVisible(False)

        self.tempo_flag = "0" #default

        #
        #
        # CONNECT BUTTON FUNCTIONALITY

        self.current_task = self.PB_play.clicked.connect(self.play_button_clicked)
        self.PB_song_gallery.clicked.connect(self.song_gallery_button_clicked)
        self.PB_user_guide.clicked.connect(self.user_guide_button_clicked)
        self.PB_play_2.clicked.connect(self.final_play_button_clicked)
        self.PB_feedback.clicked.connect(self.reset_play_screen)

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
        
        # "play setup" frame
        self.FRAME_play.setGeometry(QtCore.QRect(self.width_menu, 0, self.width_play_screen, self.height_play_screen))
        self.FRAME_play.setStyleSheet("QFrame#FRAME_play { background-color: #343843; }")

        # "in progress" frame
        self.FRAME_inProgress.setGeometry(QtCore.QRect(self.width_menu, 0, self.width_play_screen, self.height_play_screen))
        self.FRAME_inProgress.setStyleSheet("QFrame#FRAME_inProgress { background-color: #343843; }")

        # "feedback" frame
        self.FRAME_feedback.setGeometry(QtCore.QRect(self.width_menu, 0, self.width_play_screen, self.height_play_screen))
        self.FRAME_feedback.setStyleSheet("QFrame#FRAME_feedback { background-color: #343843; }")

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

        # "in progress" label
        self.LABEL_inProgress.setGeometry(QtCore.QRect(0, 0, self.width_play_screen, self.height_play_screen))
        self.LABEL_inProgress.setStyleSheet("QLabel#LABEL_inProgress { color: white; font-style: bold; font-size: 50pt; }")

        # "feedback" labels
        self.LABEL_feedback1.setGeometry(QtCore.QRect(0, 200, self.width_play_screen, self.label_height))
        self.LABEL_feedback1.setStyleSheet("QLabel#LABEL_feedback1 { color: white; font-style: bold; font-size: 20pt; }")
        self.LABEL_feedback2.setGeometry(QtCore.QRect(0, 300, self.width_play_screen, self.label_height))
        self.LABEL_feedback2.setStyleSheet("QLabel#LABEL_feedback2 { color: white; font-style: bold; font-size: 20pt; }")
        self.LABEL_feedback3.setGeometry(QtCore.QRect(0, 400, self.width_play_screen, self.label_height))
        self.LABEL_feedback3.setStyleSheet("QLabel#LABEL_feedback3 { color: white; font-style: bold; font-size: 20pt; }")

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

        # feedback button
        self.PB_feedback.setFlat(True)
        self.PB_feedback.setStyleSheet("QPushButton#PB_feedback { color: #343843; background-color: #A5A5A5; font-style: bold; font-size: 12pt; border-radius: 8px; }")
        self.PB_feedback.setGeometry (QtCore.QRect(int(0.38*self.width_play_screen), int(0.7*self.height_window), self.button_width, self.frame_height))
        #self.PB_feedback.clicked.connect(self.mode_1_button_clicked)

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
        #if(self.current_task != "play"):
        if(self.FRAME_play.isVisible() == False):

            # change appearance of menu buttons to indicate the play button is selected
            self.PB_play.setStyleSheet("QPushButton#PB_play { font-style: bold; font-size: 18pt; color: #343843; background-color: #7DCB79; border: none; vertical-align: middle; }")
            self.PB_song_gallery.setStyleSheet("QPushButton#PB_song_gallery { font-style: bold; font-size: 18pt; color: white; background-color: #696969; border: none; vertical-align: middle; }")
            self.PB_user_guide.setStyleSheet("QPushButton#PB_user_guide { font-style: bold; font-size: 18pt; color: white; background-color: #696969; border: none; vertical-align: middle; }")

            # show play screen and hide other screens
            self.setup_play_screen()
            self.FRAME_inProgress.setVisible(False)
            self.FRAME_feedback.setVisible(False)
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
    # FUNCTION FOR MODE 1 BUTTON
    def mode_1_button_clicked(self):
        self.mode = "learn"

        # change appearance of training mode button to appear selected
        self.PB_mode_1.setStyleSheet("QPushButton#PB_mode_1 { color: #343843; background-color: #7DCB79; font-style: bold; font-size: 12pt; border-radius: 8px; }")

        # reset testing mode button
        self.PB_mode_2.setStyleSheet("QPushButton#PB_mode_2 { color: #343843; background-color: #A5A5A5; font-style: bold; font-size: 12pt; border-radius: 8px; }")

    #
    #
    # FUNCTION FOR MODE 2 BUTTON
    def mode_2_button_clicked(self):
        self.mode = "test"

        # change appearance of testing mode button to appear selected
        self.PB_mode_2.setStyleSheet("QPushButton#PB_mode_2 { color: #343843; background-color: #7DCB79; font-style: bold; font-size: 12pt; border-radius: 8px; }")

        # reset training mode button
        self.PB_mode_1.setStyleSheet("QPushButton#PB_mode_1 { color: #343843; background-color: #A5A5A5; font-style: bold; font-size: 12pt; border-radius: 8px; }")

    def tempo_button_1_clicked(self):
        self.tempo_flag = FALSE

        # reset training mode button
        self.PB_tempo_2.setStyleSheet("QPushButton#PB_tempo_2 { color: #343843; background-color: #A5A5A5; font-style: bold; font-size: 12pt; border-radius: 8px; }")
        self.PB_tempo_1.setStyleSheet("QPushButton#PB_tempo_1 { color: #343843; background-color: #7DCB79; font-style: bold; font-size: 12pt; border-radius: 8px; }")

    def tempo_button_2_clicked(self):
        self.tempo_flag = TRUE

        # reset training mode button
        self.PB_tempo_1.setStyleSheet("QPushButton#PB_tempo_1 { color: #343843; background-color: #A5A5A5; font-style: bold; font-size: 12pt; border-radius: 8px; }")
        self.PB_tempo_2.setStyleSheet("QPushButton#PB_tempo_2 { color: #343843; background-color: #7DCB79; font-style: bold; font-size: 12pt; border-radius: 8px; }")

    def feedback_screen(self, note_score, timing_score, total_score):
        
        # if the user was playing WITHOUT timing, only output "Score: %"
        if((note_score == None) & (timing_score== None) & (total_score != None)):
            self.LABEL_feedback2.setText("SCORE: " + str(total_score) + "%")
            self.LABEL_feedback1.setVisible(False)
            self.LABEL_feedback2.setVisible(True)
            self.LABEL_feedback3.setVisible(False)

        # if the user was playing WITH timing, output all three scores
        elif ((note_score != None) & (timing_score!= None) & (total_score != None)):
            self.LABEL_feedback1.setText("NOTE ACCURACY: " + str(note_score) + "%")
            self.LABEL_feedback2.setText("TIMING ACCURACY: " + str(timing_score) + "%")
            self.LABEL_feedback3.setText("OVERALL SCORE: " + str(total_score) + "%")
            self.LABEL_feedback1.setVisible(True)
            self.LABEL_feedback2.setVisible(True)
            self.LABEL_feedback3.setVisible(True)
        
        else:
            self.LABEL_feedback1.setVisible(False)
            self.LABEL_feedback2.setVisible(False)
            self.LABEL_feedback3.setVisible(False)
        
        # update which main screen frame is showing
        self.FRAME_play.setVisible(False)
        self.FRAME_inProgress.setVisible(False)
        self.FRAME_feedback.setVisible(True)

    def reset_play_screen(self):
        # reset buttons
        self.PB_mode_1.setStyleSheet("QPushButton#PB_mode_1 { color: #343843; background-color: #A5A5A5; font-style: bold; font-size: 12pt; border-radius: 8px; }")
        self.PB_mode_2.setStyleSheet("QPushButton#PB_mode_2 { color: #343843; background-color: #A5A5A5; font-style: bold; font-size: 12pt; border-radius: 8px; }")
        self.PB_tempo_1.setStyleSheet("QPushButton#PB_tempo_1 { color: #343843; background-color: #A5A5A5; font-style: bold; font-size: 12pt; border-radius: 8px; }")
        self.PB_tempo_2.setStyleSheet("QPushButton#PB_tempo_2 { color: #343843; background-color: #A5A5A5; font-style: bold; font-size: 12pt; border-radius: 8px; }")
        self.PB_play_2.setStyleSheet("QPushButton#PB_play_2 { color: #343843; background-color: #A5A5A5; font-style: bold; font-size: 12pt; border-radius: 8px; }")

        self.FRAME_feedback.setVisible(False)
        self.FRAME_play.setVisible(True)

    #
    #
    # FUNCTION FOR FINAL PLAY BUTTON
    def final_play_button_clicked(self):
        self.PB_play_2.setStyleSheet("QPushButton#PB_play_2 { color: #343843; background-color: #7DCB79; font-style: bold; font-size: 12pt; border-radius: 8px; }")
        print('hello world')
        
        tempo = 0
        # tempo selection
        if(self.tempo_flag):
            tempo = self.SPIN_tempo.value()
        
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

        # update GUI
        self.FRAME_play.setVisible(False)
        self.FRAME_inProgress.setVisible(True)
        result = run_mozart(self.song_selection, self.mode, self.tempo_flag, tempo)
        if result == None:
            self.feedback_screen(None, None, None)    
        else:
            self.feedback_screen(result[0], result[1], result[2])
        
app = QtWidgets.QApplication(sys.argv)
dialog = QtWidgets.QDialog()
prog = MainWindow(dialog)
dialog.show()
app.exec()