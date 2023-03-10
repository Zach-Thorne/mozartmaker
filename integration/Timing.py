from playsound import playsound
import time
import constants
import finger_placement

def metronome(adjust,length):
    loop_length = int(length/((1/4) * adjust))  ## integer value of loop length is how many quarter notes there are
    
    for i in range(0,int(loop_length)):
        start_time = time.time()
        #playsound('C:\\Users\\Garret\\Desktop\\Capstone\\mozartmaker\\integration\\ding.mp3',FALSE)        #garrets desktop
        playsound('D:\\Users\\Documents\\Connor\\Connors Schoolwork\\ELEC ENG 4OI6\\mozartmaker\\integration\\ding.mp3', False)         #connors desktop  
        time.sleep((0.25 * adjust) - (time.time() - start_time)) 


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

def finger_refactor(scale, note_array):
    song_fingers = scale        #needs to be changed to song that is imported with timing, not mhall
    fingers = finger_placement.fingers(scale, note_array)
    for i in range (0, len(scale)):
        song_fingers[i].append(fingers[i])
    return song_fingers