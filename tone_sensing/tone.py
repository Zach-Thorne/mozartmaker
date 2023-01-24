import pyaudio
import pylab
import os
from struct import pack
from sys import byteorder
import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.signal import find_peaks
from scipy.fftpack import fft
import time
from tkinter import TclError
from scipy.io import wavfile as wav
import wave
from pydub import AudioSegment
from collections import Counter
from array import array
from pydub.silence import split_on_silence
import crepe

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
#class recording()
# constants for recording audio
CHUNK = 1024*4          # samples per frame
FORMAT = pyaudio.paInt16     # audio format (bytes per sample?)
CHANNELS = 1                 # single channel for microphone
RATE = 48000                 # samples per second
RECORD_SECONDS = 1

#record piano sound, remove the silent parts and save the new audio
def piano_sound():
    os.remove('/Users/emmarobinson/Downloads/piano_audio.wav') #change this according to your computer file
    os.remove('/Users/emmarobinson/Downloads/piano_audio_new.wav')   #change this according to your computer file      

    p = pyaudio.PyAudio()
    #p.get_device_info_by_index(3)['defaultSampleRate']

    # stream object to get data from microphone
    stream = p.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        #input_device_index =3, #change this according to the mic port on your computer
        input=True,output=True,
        frames_per_buffer=CHUNK
    )
    frames = []
    print("* listening")

    while 1:
        
        data = stream.read(CHUNK, exception_on_overflow = False)
        data_chunk=array('h',data)
        vol=max(data_chunk)
        if vol >= 400:
            print("* recording")
            for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
                stream.write(data, CHUNK)
                frames.append(data)
            break

        else:
            print("* waiting")

    print("* done")

    stream.stop_stream()
    stream.close()

    p.terminate()
    file_path='/Users/emmarobinson/Downloads/piano_audio.wav' #change this according to your computer file
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
    combined.export(f'/Users/emmarobinson/Downloads/piano_audio_new.wav', format = 'wav') #change this according to your computer file

piano_sound()

#get information about the audio file
sr, audio = wav.read('/Users/emmarobinson/Downloads/piano_audio.wav') #change this according to your computer file
time, frequency, confidence, activation = crepe.predict(audio, sr, viterbi=True, model_capacity="small")
freq1=np.array([np.mean(frequency)])

#check with the closest_val function to see what the frequency of the played note is
song_notes=[]
for i in range(len(freq1)):
    note=closest_val(note_freqs,freq1[i])
    index = note_freqs.index(note)
    song_notes.append(keys[index])
    print(song_notes)

x=0
if song_notes[0]==c_major_scale[x]:
    print("yay")