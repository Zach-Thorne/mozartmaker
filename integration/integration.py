import numpy as np
from tkinter import *
import constants
import projection_luts
import projection
import tone
import time
import midi
import Timing
import finger_placement

def learning_mode(root, canvas, screen_width, screen_height, note_array, scale, keyboard):
    i = 0
    chord_check = 0
    previous_note = 0
    note_time = 0
    played_note = [0,0]
    #call function for displaying the first note to play
    projection.project_key(root, canvas, screen_width, screen_height, note_array, i)
    
    while i < len(scale):
        played_note = midi.note_stream(keyboard)
        if (played_note):
            if played_note[0] == scale[i]:
                note_time = played_note[2]
                print("played note: ", played_note)
                # if (note_time - previous_note < 0.05):
                #     chord_check = TRUE
                #     print("CHORD DETECTED")
                print("Played note is: ", played_note)
                print("Note is correct!\n")
                projection.project_white(root, canvas, screen_width, screen_height, note_array, i)
                i += 1
                if (i == len(scale)):
                    break
                projection.project_key(root, canvas, screen_width, screen_height, note_array, i)
            #previous_note = note_time

def timing_refactor(scale):
    timed_song = constants.mhall        #needs to be changed to song that is imported with timing, not mhall
    for i in range (0, len(scale)):
        timed_song[i][1] = timed_song[i][1] * constants.sec_adjusted_bpm
    return timed_song

def timing_refactor_finger(scale, note_array):
    timed_song_fingers = constants.mhall        #needs to be changed to song that is imported with timing, not mhall
    fingers = finger_placement.fingers(scale, note_array)
    for i in range (0, len(scale)):
        timed_song_fingers[i][1] = timed_song_fingers[i][1] * constants.sec_adjusted_bpm
        timed_song_fingers[i].append(fingers[i])
    return timed_song_fingers

def learning_mode_timing(root, canvas, screen_width, screen_height, note_array, scale, keyboard):
    i = 0
    chord_check = 0
    previous_note = NONE
    note_time = 0
    song_bpm_adjust = timing_refactor(scale)
    note_status = "green"
    make_times=[]

    
    for i in range (0,len(scale)):
        
        #call function for displaying the first note to play
        project_time = projection.project_key(root, canvas, screen_width, screen_height, note_array, i, note_status)
        note_status = "orange"
        note_start = time.time()
        #print ('dog')
        while (note_start + song_bpm_adjust[i][1] - constants.WHITE_TIME - project_time) > time.time():
            played_note = midi.note_stream(keyboard)
            if (played_note):
                if played_note[1] == 100:
                    if played_note[0] == scale[i][0]:
                        make_times.append(played_note[2])
                        #print(make_times)

                elif (played_note[0] == scale[i][0] or played_note[0] == scale[i-1][0]):
                    break_time = played_note[2]
                    #print("break_time",break_time)
                    try:
                        make_time = make_times[0]
                    except IndexError:
                        # note_status = "orange"
                        make_time = break_time
                    #print("make time",make_time)                        
                    time_on_note = abs(break_time - make_time)
                    #print("time on note (ms): ", time_on_note)
                    time_on_note /= 1000
                    print("played time", time_on_note)
                    if (time_on_note > (constants.ERROR * song_bpm_adjust[i][1])) and (time_on_note < ((2 - constants.ERROR) * song_bpm_adjust[i-1][1])):
                        note_status = "green"
                    # else:
                    #     note_status = "orange"
                    #print("note status: ", note_status)
                    try:    
                        make_times.pop(0)   
                    except Exception:
                        pass

                    #print("Played note is: ", played_note)
                    #print("Note is correct!\n")
                    #i += 1
                    #previous_note=played_note
        white_time = projection.project_white(root, canvas, screen_width, screen_height, note_array, i)    
        time.sleep(constants.WHITE_TIME - white_time)

<<<<<<< Updated upstream
=======

>>>>>>> Stashed changes
def testing_mode_timing(scale, keyboard):
    i = 0
    chord_check = 0
    song_bpm_adjust = timing_refactor(scale)
    make_times=[]
    correct_notes=0
    correct_times=0
    for i in range (0,len(scale)):
        played_note = midi.note_stream(keyboard)
        if (played_note):
            print(played_note)
            if played_note[1] == 100:
                #print("1")
                if played_note[0] == scale[i][0]:
                    correct_notes += 1
                    #print("2")
                    make_times.append(played_note[2])
                    #print(make_times)
                i += 1

            elif (played_note[0] == scale[i][0] or played_note[0] == scale[i-1][0]):
                break_time = played_note[2]
                print("3")
                #print("break_time",break_time)
                try:
                    make_time = make_times[0]
                except IndexError:
                    make_time = break_time
                    #print("5")
                print("make time",make_time)
                time_on_note = abs(break_time - make_time)
                print("time on note (ms): ", time_on_note)
                time_on_note /= 1000
                print("played time", time_on_note)
                if (time_on_note > (constants.ERROR * song_bpm_adjust[i][1])) and (time_on_note < ((2 - constants.ERROR) * song_bpm_adjust[i-1][1])):
                    print("time is correct")
                    correct_times+=1

                #print("note status: ", note_status)
                try:
                    make_times.pop(0) 
                except Exception:
                    pass  
            
    result_note = float(correct_notes / len(scale)) * 100
    result_time=float(correct_times / len(scale)) * 100
    print("Your correct note score is: ", round(result_note, 1), "%")
    print("Your time note score is: ", round(result_time, 1), "%")

def testing_mode(scale, keyboard):
    i = 0
    chord_check = 0
    previous_note = 0
    note_time = 0
    test_notes = []
    while i < len(scale):        
        played_note = midi.note_stream(keyboard)
        if played_note:
            note_time = time.time()
            if (note_time - previous_note < 0.05):
                chord_check = TRUE
                print("CHORD DETECTED")
            i += 1
            test_notes.append(played_note)
            if (i == len(scale)):
                break
        previous_note = note_time
    
    correct_notes = 0
    for n in range(len(scale)):
        if (test_notes[n] == scale[n]):
            correct_notes += 1

    result = float(correct_notes / len(scale)) * 100
    print("Your test score is: ", round(result, 1), "%")

def count_in():
    first_note = 0
    for i in range(2*constants.BEATSPERBAR):
        blue_time = projection.project_key(root, canvas, screen_width, screen_height, note_array, first_note, "blue")
        time.sleep(constants.FLASH_TIME - blue_time)
        white_time = projection.project_white(root, canvas, screen_width, screen_height, note_array, first_note)    
        time.sleep((constants.sec_adjusted_bpm / constants.BEATSPERBAR) - constants.FLASH_TIME - white_time)

    
if __name__ == "__main__":
    #Create empty array 
    #Initalize Tkinter
    root = Tk()

    #Initalize midi input. Searches for keyboard and sets as a midi output
    keyboard = midi.initialization()

    #Initialize Canvas
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    canvas = Canvas(width=screen_width, height=screen_height)
    root.state('zoomed')

    #NOTE: SHOULD RUN ON STARTUP 
    #Create inital outline
    inital = projection.create_default(root, canvas, screen_width, screen_height)

    scale_input = input("What Major scale would you like to play?\n")
    if (scale_input == "C") or (scale_input == "c"):
        scale = constants.c_major
    elif (scale_input == "D") or (scale_input == "d"):
        scale = constants.d_major
    elif (scale_input == "E") or (scale_input == "e"):
        scale = constants.e_major
    elif (scale_input == "F") or (scale_input == "f"):
        scale = constants.f_major
    elif (scale_input == "G") or (scale_input == "g"):
        scale = constants.g_major
    elif scale_input == "ml":
        scale = constants.mary
    elif scale_input == "mhall":
        scale = constants.mhall
    else:
        raise Exception("Scale is not valid. Try again\n")
    
    play_mode = input("What mode would you like to play in? learn or test?\n")
    #if not((play_mode == "test") or (play_mode == "learn")):
    #    raise Exception("Not a valid mode. Please try again\n")

    projection_index = []
    #print("length of scale: ", len(scale))
    note_array = np.zeros((len(scale), constants.total_keys))
    for i in range(len(scale)):
        if (play_mode == 'learntime') or (play_mode == 'testtime'):
            projection_index.append(projection_luts.note_lut(scale[i][0]))
        else:
            projection_index.append(projection_luts.note_lut(scale[i]))
        
        

    for n in range(len(scale)):
        note_array[n][projection_index[n]] = 1

    #values = timing_refactor_finger(scale, note_array)
    #print("values: ", values)
    count_in()    
    if (play_mode == "learn"):
        learning_mode(root, canvas, screen_width, screen_height, note_array, scale, keyboard)
    elif (play_mode == "test"):
        testing_mode(scale, keyboard)
    elif (play_mode == "testtime"):
        testing_mode_timing(scale, keyboard)
    elif (play_mode == "learntime"):
        learning_mode_timing(root, canvas, screen_width, screen_height, note_array, scale, keyboard)
    