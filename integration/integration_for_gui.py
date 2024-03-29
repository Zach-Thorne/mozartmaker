import numpy as np
from tkinter import *
import constants
import projection_luts
import projection
import tone
import time
import midi
import timing
import threading
from screeninfo import get_monitors
from song_gallery_file import *

#***************************************************************************************#
#*************** NEED TO BE GLOBAL IN ORDER TO BE UPDATED MULTIPLE TIMES ***************#
#***************************************************************************************#

root = Tk()
monitors = 0 
for m in get_monitors(): 
    monitors = monitors + 1  
    
#Initialize Canvas if there is only one monitor
#If only one monitor create shit the same way 
if(monitors <= 1): 
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    canvas = Canvas(width=screen_width, height=screen_height)
    root.state('zoomed')
#Indicates there is a second monitor to write canvas to.
else: 
    #Primary screen 
    m1 = (str(get_monitors()[0])).split() 
    #Secondary Screen 
    m2 = (str(get_monitors()[1])).split()

    #Gets width and height of the displays 
    w0, h0 = int(m1[2][6:-1]), int(m1[3][7:-1])
    w1, h1 = int(m2[2][6:-1]), int(m2[3][7:-1])
    screen_width = w1
    screen_height = h1
    canvas = Canvas(width=screen_width, height=screen_height)
    
    #Shift to other monitor
    root.geometry(f"{w1}x{h1}-{w0}+0")
    root.state('zoomed')

#***************************************************************************************#
#***************************************************************************************#
#***************************************************************************************#


def learning_mode(root, canvas, screen_width, screen_height, note_array, scale, keyboard):
    i = 0
    played_note = [0,0]
    note_status = "green"
    #call function for displaying the first note to play
    song_fingerings = timing.finger_refactor(scale, note_array)

    projection.project_key(root, canvas, screen_width, screen_height, note_array, i, note_status, str(song_fingerings[i][2]))
    
    while i < len(scale):
        played_note = midi.note_stream(keyboard)
        if (played_note):
            if played_note[1] == 100:
                if played_note[0] == scale[i][0]:
                    projection.project_white(root, canvas, screen_width, screen_height, note_array, i)
                    i += 1
                    if (i == len(scale)):
                        break
                    projection.project_key(root, canvas, screen_width, screen_height, note_array, i, note_status, str(song_fingerings[i][2]))
    #root.destroy()
    midi.destroy()

def learning_mode_timing(root, canvas, screen_width, screen_height, note_array, scale, keyboard):
    i = 0
    make_times=[]
    note_status = "green"
    
    song_bpm_adjust = timing.timing_refactor_finger(scale, note_array)

    song_length = 0
    for i in range (0,len(song_bpm_adjust)):
        song_length += song_bpm_adjust[i][1]
    song_length += 8 * (0.25 * constants.sec_adjusted_bpm)
    print("song length", song_length)

    x = threading.Thread(target = timing.metronome, args=(constants.sec_adjusted_bpm, song_length))
    x.start()
    count_in(root, canvas, screen_width, screen_height, note_array) 
           
    for i in range (0,len(scale)):
        
        #call function for displaying the first note to play
        project_time = projection.project_key(root, canvas, screen_width, screen_height, note_array, i, note_status, str(song_bpm_adjust[i][2]))
        note_start = time.time()
        note_status = "orange"
        while (note_start + song_bpm_adjust[i][1] - constants.WHITE_TIME - project_time) > time.time():
            played_note = midi.note_stream(keyboard)
            if (played_note):
                if played_note[1] == 100:
                    if played_note[0] == scale[i][0]:
                        make_times.append(played_note[2])

                elif (played_note[0] == scale[i][0] or played_note[0] == scale[i-1][0]):
                    break_time = played_note[2]
                    try:
                        make_time = make_times[0]
                    except IndexError:
                        note_status = "orange"
                        make_time = break_time           
                    time_on_note = abs(break_time - make_time)
                    time_on_note /= 1000
                    print("played time", time_on_note)
                    if (time_on_note > (constants.ERROR * song_bpm_adjust[i][1])) and (time_on_note < ((2 - constants.ERROR) * song_bpm_adjust[i-1][1])):
                        note_status = "green"
                    else:
                        note_status = "orange"
                    try:    
                        make_times.pop(0)   
                    except Exception:
                        pass
        white_time = projection.project_white(root, canvas, screen_width, screen_height, note_array, i)    
        time.sleep(constants.WHITE_TIME - white_time)
    midi.destroy()
    #root.destroy()

def testing_mode(scale, keyboard):
    i = 0
    correct_notes = 0
    while i < len(scale):        
        played_note = midi.note_stream(keyboard)
        if played_note:
            if played_note[1] == 100:
                print("played note is ", played_note[0])
                if (played_note[0] == scale[i][0]):
                    correct_notes += 1
                i += 1
        if (i == len(scale)):
            break    

    result = float(correct_notes / len(scale)) * 100
    midi.destroy()
    return [None, None, result]
    #print("Your test score is: ", round(result, 1), "%")


def testing_mode_timing(root, canvas, screen_width, screen_height, note_array, scale, keyboard):
    i = 0
    song_bpm_adjust = timing.timing_refactor(scale)
    make_times=[]
    correct_notes=0
    correct_times=0

    song_length = 0
    for i in range (0,len(song_bpm_adjust)):
        song_length += song_bpm_adjust[i][1]
    song_length += 8 * (0.25 * constants.sec_adjusted_bpm)
    print("song length", song_length)
    

    x = threading.Thread(target = timing.metronome, args=(constants.sec_adjusted_bpm, song_length))
    x.start()
    count_in(root, canvas, screen_width, screen_height, note_array) 

    for i in range (0,len(scale)):
        
        #call function for displaying the first note to play
        note_start = time.time()
        while (note_start + song_bpm_adjust[i][1]) > time.time():
            played_note = midi.note_stream(keyboard)
            if (played_note):
                if played_note[1] == 100:
                    if played_note[0] == scale[i][0]:
                        correct_notes += 1
                        make_times.append(played_note[2])

                elif (played_note[0] == scale[i][0] or played_note[0] == scale[i-1][0]):
                    break_time = played_note[2]
                    try:
                        make_time = make_times[0]
                    except IndexError:
                        make_time=break_time
                    time_on_note = abs(break_time - make_time)
                    time_on_note /= 1000
                    if (time_on_note > (constants.ERROR * song_bpm_adjust[i][1])) and (time_on_note < ((2 - constants.ERROR) * song_bpm_adjust[i-1][1])):
                        correct_times+=1

                    try:
                        make_times.pop(0) 
                    except Exception:
                        pass  
    result_note = float(correct_notes / len(scale)) * 100
    result_time=float(correct_times / len(scale)) * 100
    #root.destroy()
    midi.destroy()
    return [round(result_note, 1), round(result_time, 1), round((result_note+result_time)/2, 1)]


def count_in(root, canvas, screen_width, screen_height, note_array):
    first_note = 0
    for i in range(2*constants.BEATSPERBAR):
        blue_time = projection.project_key(root, canvas, screen_width, screen_height, note_array, first_note, "blue", "")
        time.sleep(constants.FLASH_TIME - blue_time)
        white_time = projection.project_white(root, canvas, screen_width, screen_height, note_array, first_note)    
        time.sleep((constants.sec_adjusted_bpm / constants.BEATSPERBAR) - constants.FLASH_TIME - white_time)
           

def run_mozart(scale_input, play_mode, timing_state, tempo, no_play_just_disp, input_type):
    
    #Create inital outline
    inital = projection.create_default(root, canvas, screen_width, screen_height)
    #canvas.pack()
    #canvas.update()

    if(no_play_just_disp != 0):
        constants.BPM = tempo
        print("tempo = ", tempo)
        if tempo != 0:
            constants.sec_adjusted_bpm = constants.calculate_bpm_adj()
        print("adjust bpm: ", constants.sec_adjusted_bpm)
        
        #Initalize midi input. Searches for keyboard and sets as a midi output
        if not(input_type):
            keyboard = midi.initialization()

        scale = song_gallery(scale_input, None, 'read')

        projection_index = []
        #print("length of scale: ", len(scale))
        note_array = np.zeros((len(scale), constants.total_keys))
        for i in range(len(scale)):
            # if (play_mode == 'learntime') or (play_mode == 'testtime'):
            projection_index.append(projection_luts.note_lut(scale[i][0]))
            # else:
            #     projection_index.append(projection_luts.note_lut(scale[i]))
        
        for n in range(len(scale)):
            note_array[n][projection_index[n]] = 1

        if (play_mode == "learn"):
            if (input_type):
                tone.learning_mode_audio(root, canvas, screen_width, screen_height, note_array,scale)
            elif(timing_state):
                learning_mode_timing(root, canvas, screen_width, screen_height, note_array, scale, keyboard)
            else:
                learning_mode(root, canvas, screen_width, screen_height, note_array, scale, keyboard)
        elif (play_mode == "test"):
            if (input_type):
                return tone.testing_mode_audio(root, canvas, screen_width, screen_height, note_array,scale)
            elif(timing_state):
                return testing_mode_timing(root, canvas, screen_width, screen_height, note_array, scale, keyboard)
            else:
                projection.project_all_white(root, canvas, screen_width, screen_height, scale)
                return testing_mode(scale, keyboard)

