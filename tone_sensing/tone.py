import pyaudio
import os
import struct
import numpy as np
import matplotlib.pyplot as plt
from PyQt5 import QtWidgets, QtCore
import PyQt5 as pg
import scipy
from scipy.fftpack import fft
import time
from tkinter import TclError
from scipy.io import wavfile as wav
import wave
import soundfile as sf
from pydub import AudioSegment
from pyqtgraph.Qt import QtWidgets, QtCore
import math
from collections import Counter
from pydub.utils import get_array_type
import array
from pydub.silence import split_on_silence

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
c_major_scale_freqs=[]
c_major_scale=['C4', 'D4', 'E4', 'F4', 'G4']
for i in range(len(keys)):
    for j in range(5):
        if c_major_scale[j]==keys[i]:
            c_major_scale_freqs.append(note_freqs[i])

#A function for making sure you can find the closest value in a list
def closest_val(input_list, val):

  arr = np.asarray(input_list)

  i = (np.abs(arr - val)).argmin()

  return arr[i]
class recording()
# constants for recording audio
CHUNK = 1024*2            # samples per frame
FORMAT = pyaudio.paInt16     # audio format 
CHANNELS = 1                 # single channel for microphone
RATE = 44100                 # samples per second
RECORD_SECONDS = 3          # recording time

#record piano sound, remove the silent parts and save the new audio
def piano_sound():
    os.remove('/Users/emmarobinson/Downloads/piano_audio.wav')
    os.remove('/Users/emmarobinson/Downloads/piano_audio_new.wav')        

    p = pyaudio.PyAudio()

    # stream object to get data from microphone
    stream = p.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        input_device_index =3,
        input=True,
        output=True,
        frames_per_buffer=CHUNK
    )
    frames = []
    print("* recording")
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        stream.write(data, CHUNK)
        frames.append(data)

    print("* done")

    stream.stop_stream()
    stream.close()

    p.terminate()
    file_path='/Users/emmarobinson/Downloads/piano_audio.wav'
    file_name = file_path.split('/')[-1]
    wf = wave.open(file_path, "wb")
    # set the channels
    wf.setnchannels(CHANNELS)
    # set the sample format
    wf.setsampwidth(p.get_sample_size(FORMAT))
    # set the sample rate
    wf.setframerate(RATE)
    # write the frames as bytes
    wf.writeframes(b"".join(frames))
    # close the file
    wf.close()
    file_path='/Users/emmarobinson/Downloads/piano_audio.wav'
    file_name = file_path.split('/')[-1]
    sound = AudioSegment.from_file(file_path, format = 'wav') 
    audio_chunks = split_on_silence(sound
                                ,min_silence_len = 100
                                ,silence_thresh = -45
                                ,keep_silence = 50
                            )

    # Putting the file back together
    combined = AudioSegment.empty()
    for chunk in audio_chunks:
        combined += chunk
    combined.export(f'/Users/emmarobinson/Downloads/piano_audio_new.wav', format = 'wav')

piano_sound()

#get information about the audio file
rate, data = wav.read('/Users/emmarobinson/Downloads/piano_audio.wav')
audio_segment = AudioSegment.from_file('/Users/emmarobinson/Downloads/piano_audio.wav')

duration = len(audio_segment)/1000

# calculate the length of our chunk in the np.array using sample rate
chunk = int(rate * duration)

# length of delimiting 1600hz tone
offset = int(rate * 0.005)

# number of bits in the audio data to decode
bits = int(len(data) / chunk)

#get the frequency of the piano note played
def get_freq(bit):
    # start position of the current bit
    strt = (chunk * bit) 
    
    # remove the delimiting 1600hz tone
    end = (strt + chunk) 
   
    
    # slice the array for each bit
    sliced = data[strt:end]

    w = np.fft.fft(sliced)
    w=np.absolute(w)
    freqs = np.fft.fftfreq(len(w))

    

    # Find the peak in the coefficients
    idx = np.argmax(np.abs(w))
    freq = freqs[idx]
    freq_in_hertz = abs(freq * rate)
    return freq_in_hertz

decoded_freqs = [get_freq(bit) for bit in range(bits)]

#check with the closest_val function to see what the frequency of the played note is
for i in range(len(decoded_freqs)):
    note=closest_val(note_freqs,decoded_freqs[i])
    index = note_freqs.index(note)
    played_note=keys[index]
return played_note

x=0
if played_note==c_major_scale[x]:
    print("yay")