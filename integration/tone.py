import pyaudio
import numpy as np
from scipy.fftpack import fft, fftfreq
#from pydub.utils import get_array_type
#from pydub.silence import split_on_silence
import constants
from array import array
from collections import Counter
import projection
import timing
import time
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

def device_identification():
    p = pyaudio.PyAudio()
    info = p.get_host_api_info_by_index(0)
    numdevices = info.get('deviceCount')

    for i in range(0, numdevices):
        if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
            print("Input Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0, i).get('name'))

#record piano sound, remove the silent parts and save the new audio
def piano_sound():   
    # constants for audio
    CHUNK = 1024         # samples per frame
    FORMAT = pyaudio.paInt16     # audio format (bytes per sample?)
    CHANNELS = 1                 # single channel for microphone
    RATE = 44100                 # samples per second  
    p = pyaudio.PyAudio()

    # stream object to get data from microphone
    stream = p.open(
        format = FORMAT,
        channels = CHANNELS,
        rate = RATE,
        #input_device_index  = 2, #change this according to the mic port on your computer
        input = True,
        frames_per_buffer = CHUNK)

    print("* listening")
    noise_time=time.time()
    while True:   
        #print("while")   
        data = stream.read(CHUNK)
        data_sample = np.frombuffer(data, dtype=np.int16)
        data_sample = data_sample * np.blackman(len(data_sample))
        data_chunk=array('h',data)
        vol=max(data_chunk)
        #print(vol)
        if vol >= 500:
            noise_time=time.time()
            f = fft(data_sample)
            f=np.absolute(f)
            freqs = fftfreq(len(f))

    

            # Find the peak in the coefficients
            idx = np.argmax(np.abs(f))
            freq = freqs[idx]
            freq_hz = abs(freq * RATE)
            #print(freq_hz)
            note_played=[]
            #notes=[]
            
            #get average of played note to make sure its right (cuz when notes taper off it produces diff freq)
            for i in range(4):
                note_played.append(freq_to_note(freq_hz, constants.note_freqs, constants.keys))
            most_common_note= [note for note, note_count in Counter(note_played).most_common(1)]
            note_play=most_common_note[0]
            #note_play=freq_to_note(freq_hz, note_freqs, keys)
            print("the note played is : ", note_play)
            #notes.append(note_play)
            return note_play

        elif vol<500 and time.time()-noise_time>2:
            print("Stoping Listening")
            stream.stop_stream()
            stream.close()
            p.terminate()
            return False

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
            j=j+1
            if (j == len(scale)):
                break
            projection.project_key(root, canvas, screen_width, screen_height, note_array, j, note_status,str(song_fingerings[j][2]))

def testing_mode_audio(scale):
    notes=[]
    correct_notes=0
    while piano_sound():
        played_note=piano_sound()
        notes.append(played_note)
    notes.pop()
    notes=notes[1::2]
    notes=notes[1::2]
    print(notes)
    for i in range(len(scale)):
        if notes[i]==scale[i][0]:
            correct_notes=correct_notes+1
    result = float(correct_notes / len(scale)) * 100
    # print("Your test score is: ", round(result, 1), "%")
    return [None, None, round(result, 1)]