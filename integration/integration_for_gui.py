import numpy as np
from tkinter import *
import constants
import projection_luts
import projection
import tone
import time
import midi

def learning_mode(root, canvas, screen_width, screen_height, note_array, scale, keyboard):
    i = 0
    #call function for displaying the first note to play
    projection.project_key(root, canvas, screen_width, screen_height, note_array, i)
    
    while i < len(scale):
        played_note = midi.note_stream(keyboard)
        if played_note == scale[i]:
            print("Played note is: ", played_note)
            print("Note is correct!\n")
            projection.project_white(root, canvas, screen_width, screen_height, note_array, i)
            time.sleep(0.03)
            i += 1
            if (i == len(scale)):
                break
            projection.project_key(root, canvas, screen_width, screen_height, note_array, i)

def testing_mode(scale, keyboard):
    i = 0
    test_notes = []
    while i < len(scale):        
        played_note = midi.note_stream(keyboard)
        if played_note:
            i += 1
            test_notes.append(played_note)
            if (i == len(scale)):
                break
    
    correct_notes = 0
    for n in range(len(scale)):
        if (test_notes[n] == scale[n]):
            correct_notes += 1

    result = float(correct_notes / len(scale)) * 100
    print("Your test score is: ", round(result, 1), "%")

def run_mozart(scale_input, play_mode):
    #Create empty array 
    #Initalize Tkinter
    root = Tk()

    #Initalize midi input
    midi.initialization()

    #Determine what device keyboard is
    #midi.print_devices()

    #set device number once keyboard input is determined
    keyboard = midi.set_device_input(1)
    
    #Initialize Canvas
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    canvas = Canvas(width=screen_width, height=screen_height)

    #NOTE: SHOULD RUN ON STARTUP 
    #Create inital outline
    inital = projection.create_default(root, canvas, screen_width, screen_height)

    #scale_input = input("What Major scale would you like to play?\n")
    #play_mode = input("What mode would you like to play in? learn or test?\n")
    if scale_input == "C":
        scale = constants.c_major
    elif scale_input == "D":
        scale = constants.d_major
    elif scale_input == "E":
        scale = constants.e_major
    elif scale_input == "F":
        scale = constants.f_major
    elif scale_input == "G":
        scale = constants.g_major
    elif scale_input == "ml":
        scale = constants.mary

    projection_index = []
    #print("length of scale: ", len(scale))
    note_array = np.zeros((len(scale), constants.total_keys))
    for i in range(len(scale)):
        projection_index.append(projection_luts.note_lut(scale[i]))

    for n in range(len(scale)):
        note_array[n][projection_index[n]] = 1

    if (play_mode == "learn"):
        learning_mode(root, canvas, screen_width, screen_height, note_array, scale, keyboard)
    elif (play_mode == "test"):
        testing_mode(scale, keyboard)
    

#if __name__ == "__main__":
#    #Create empty array 
#    #Initalize Tkinter
#    root = Tk()
#
#    #Initalize midi input
#    midi.initialization()
#
#    #Determine what device keyboard is
#    #midi.print_devices()
#
#    #set device number once keyboard input is determined
#    keyboard = midi.set_device_input(1)
#    
#    #Initialize Canvas
#    screen_width = root.winfo_screenwidth()
#    screen_height = root.winfo_screenheight()
#    canvas = Canvas(width=screen_width, height=screen_height)
#
#    #NOTE: SHOULD RUN ON STARTUP 
#    #Create inital outline
#    inital = projection.create_default(root, canvas, screen_width, screen_height)
#
#    scale_input = input("What Major scale would you like to play?\n")
#    play_mode = input("What mode would you like to play in? learn or test?\n")
#    if scale_input == "C":
#        scale = constants.c_major
#    elif scale_input == "D":
#        scale = constants.d_major
#    elif scale_input == "E":
#        scale = constants.e_major
#    elif scale_input == "F":
#        scale = constants.f_major
#    elif scale_input == "G":
#        scale = constants.g_major
#    elif scale_input == "ml":
#        scale = constants.mary
#
#    projection_index = []
#    #print("length of scale: ", len(scale))
#    note_array = np.zeros((len(scale), constants.total_keys))
#    for i in range(len(scale)):
#        projection_index.append(projection_luts.note_lut(scale[i]))
#
#    for n in range(len(scale)):
#        note_array[n][projection_index[n]] = 1
#
#    if (play_mode == "learn"):
#        learning_mode(root, canvas, screen_width, screen_height, note_array, scale, keyboard)
#    elif (play_mode == "test"):
#        testing_mode(scale, keyboard)
#    
