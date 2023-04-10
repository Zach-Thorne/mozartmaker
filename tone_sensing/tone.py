import pyaudio

from struct import pack
from sys import byteorder
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from scipy.fftpack import fft, fftfreq
import time
from tkinter import *
from scipy.io import wavfile as wav
from collections import Counter
from array import array
import projection_luts
from tkinter import *
import constants
import projection
import tone
import timing
import threading




# White keys are in Uppercase and black keys (sharps) are in lowercase
octave = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'] 
base_freq = 440 #Frequency of Note A4
keys = np.array([x+str(y) for y in range(0,9) for x in octave])
# Trim to correct # keys
start = np.where(keys == 'A0')[0][0]
end = np.where(keys == 'C8')[0][0]
keys = keys[start:end+1]        #Notes of a piano

note_freqs = list(([2**((n+1-49)/12)*base_freq for n in range(len(keys))]))     #frequency of each key on a piano in order


#A hard coded c major scale with frequencies
e_major_scale=['E4','F#4', 'G#4', 'A4','B4', 'C#5', 'D#5', 'E5']

#A function for making sure you can find the closest value in a list
def closest_val(input_list, val):
  arr = np.asarray(input_list)
  i = (np.abs(arr - val)).argmin()
  return arr[i]

def freq_to_note(played_freq, note_freqs, keys):
    note=closest_val(note_freqs,played_freq)
    index = note_freqs.index(note)
    song_note=keys[index]
    return song_note

#record piano sound, remove the silent parts and save the new audio
def piano_sound():   
    # constants for audio
    CHUNK = 1024*2          # samples per frame
    FORMAT = pyaudio.paInt16     # audio format (bytes per sample?)
    CHANNELS = 1                 # single channel for microphone
    RATE = 48000                 # samples per second  
    p = pyaudio.PyAudio()

    # stream object to get data from microphone
    stream = p.open(
        format = FORMAT,
        channels = CHANNELS,
        rate = RATE,
        #input_device_index  = 3, #change this according to the mic port on your computer
        input = True,
        frames_per_buffer = CHUNK)

    print("* listening")

    while True:   
        #print("while")   
        data = stream.read(CHUNK)
        data_sample = np.frombuffer(data, dtype=np.int16)
        data_sample = data_sample * np.blackman(len(data_sample))
        data_chunk=array('h',data)
        vol=max(data_chunk)
        if vol >= 500:
            
            fft = np.fft.fft(data_sample)
            fft=np.absolute(fft)
            freqs = np.fft.fftfreq(len(fft))

    

            # Find the peak in the coefficients
            idx = np.argmax(np.abs(fft))
            freq = freqs[idx]
            freq_hz = abs(freq * RATE)
            #print(freq_hz)
            note_played=[]
            
            #get average of played note to make sure its right (cuz when notes taper off it produces diff freq)
            for i in range(4):
                note_played.append(freq_to_note(freq_hz, note_freqs, keys))
            most_common_note= [note for note, note_count in Counter(note_played).most_common(1)]
            note_play=most_common_note[0]
            note_play=freq_to_note(freq_hz, note_freqs, keys)
            print("the note played is : ", note_play)
            #time.sleep(0.5)


            #stream.stop_stream()

            #stream.close()
            #p.terminate() 
            return note_play


def learning_mode_audio(root, canvas, screen_width, screen_height, note_array,scale):
    note_status = "green"
    #call function for displaying the first note to play
    song_fingerings = timing.finger_refactor(scale, note_array)
    j=0
    projection.project_key(root, canvas, screen_width, screen_height, note_array, j, note_status, str(song_fingerings[j][2]))
    #check if note is right based on scale
    while j<(len(scale)):
        played_note=piano_sound()
        #print("supposed note: ",song[j])
        if played_note==scale[j][0]:
            projection.project_white(root, canvas, screen_width, screen_height, note_array, j)
            #print(played_note)
            #print(j)
            j=j+1
        
            projection.project_key(root, canvas, screen_width, screen_height, note_array, j, note_status,str(song_fingerings[j][2]))



#def testing_mode_audio(song)

if __name__ == "__main__":
    #Create empty array 
    #Initalize Tkinter
    root = Tk()

    #Initalize midi input. Searches for keyboard and sets as a midi output
    #keyboard = midi.initialization()

    #Initialize Canvas
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    canvas = Canvas(width=screen_width, height=screen_height)
    root.state('zoomed')
    inital = projection.create_default(root, canvas, screen_width, screen_height)
    projection_index = []
    #print("length of scale: ", len(scale))
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
    note_array = np.zeros((len(scale), constants.total_keys))
    for i in range(len(scale)):
        # print(i)
        if (scale[i][0] == None):
            print("none executed at ", i)
            continue
        else:
            note_array[i][projection_luts.note_lut(scale[i][0])] = 1

    learning_mode_audio(root, canvas, screen_width, screen_height, note_array,scale)
    #piano_sound()

#t1=threading.Thread(target=piano_sound)