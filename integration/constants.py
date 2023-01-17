##########          CONSTANTS FOR ALL SCRIPTS           ##########
##################################################################
##################      MOZARTMAKER         ######################
##################      January 2023        ######################
##################################################################
##################################################################

import pyaudio
import numpy as np

# Projection constants
num_white_keys = 36 #Since its a mini piano
num_black_keys = 25
total_keys = num_white_keys + num_black_keys
top_of_key = 150
bot_of_key = top_of_key+100

# Tone Sensing constants
# White keys are in Uppercase and black keys (sharps) are in lowercase
octave = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'] 
base_freq = 440 #Frequency of Note A4
keys = np.array([x+str(y) for y in range(0,9) for x in octave])
# Trim to correct # keys
start = np.where(keys == 'A0')[0][0]
end = np.where(keys == 'C8')[0][0]
keys = keys[start:end+1]        #Notes of a piano

note_freqs = list(([2**((n+1-49)/12)*base_freq for n in range(len(keys))]))     #frequency of each key on a piano in order

# FOR RECORDING
CHUNK = 1024*2                  # samples per frame
FORMAT = pyaudio.paInt16        # audio format 
CHANNELS = 1                    # single channel for microphone
RATE = 44100                    # samples per second
RECORD_SECONDS = 0.5              # recording time. Minimum time needed to record for integration file is 0.5s