from playsound import playsound
import time
import constants
import finger_placement
import os

def metronome(adjust,length):
    loop_length = int(length/((1/4) * adjust))  ## integer value of loop length is how many quarter notes there are
    #Gets path of current directory
    path_to_ding = os.getcmd()
    path_to_ding = path_to_ding + "\ding.mp3" 
    
    for i in range(0,int(loop_length)):
        start_time = time.time()
        #Hardcoded values
        #playsound('C:\\Users\\Garret\\Desktop\\Capstone\\mozartmaker\\integration\\ding.mp3',FALSE)        #garrets desktop
        playsound('D:\\Users\\Documents\\Connor\\Connors Schoolwork\\ELEC ENG 4OI6\\mozartmaker\\integration\\ding.mp3', False)         #connors desktop  
        #playsound('C:\\Users\\royal\\Documents\\Connor\\Connors Schoolwork\\ELEC ENG 4OI6\\mozartmaker\\integration\\ding.mp3', False)         #connors laptop  

        #TODO uncomment to do Without hardcoding        
        #playsound(path_to_ding, False)   

        time.sleep((0.25 * adjust) - (time.time() - start_time)) 


def timing_refactor(scale):
    timed_song = scale        #needs to be changed to song that is imported with timing, not mhall
    for i in range (0, len(scale)):
        timed_song[i][1] = timed_song[i][1] * constants.sec_adjusted_bpm
    return timed_song

def timing_refactor_finger(scale, note_array):
    timed_song_fingers = scale        #needs to be changed to song that is imported with timing, not mhall
    fingers = finger_placement.fingers(scale, note_array)
    for i in range (0, len(scale)):
        timed_song_fingers[i][1] = timed_song_fingers[i][1] * constants.sec_adjusted_bpm
        timed_song_fingers[i].append(fingers[i])
    return timed_song_fingers

def finger_refactor(scale, note_array):
    song_fingers = scale        #needs to be changed to song that is imported with timing, not mhall
    fingers = finger_placement.fingers(scale, note_array)
    # print(fingers)
    for i in range (0, len(scale)):
        song_fingers[i].append(fingers[i])
    return song_fingers
