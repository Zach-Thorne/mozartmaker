##########          CONSTANTS FOR ALL SCRIPTS           ##########
##################################################################
##################      MOZARTMAKER         ######################
##################      January 2023        ######################
##################################################################
##################################################################

import pyaudio
import numpy as np

# GLOBAL DEFINES
CHUNK = 1024*2                  # samples per frame
FORMAT = pyaudio.paInt16        # audio format 
CHANNELS = 1                    # single channel for microphone
RATE = 44100                    # samples per second
RECORD_SECONDS = 0.5              # recording time. Minimum time needed to record for integration file is 0.5s
FIRST_NOTE_FOR_KEYBOARD = 21
BEATSPERBAR = 4
BPM = 80
SECONDS = 60
ERROR = 0.6
WHITE_TIME = 0.075
FLASH_TIME = 0.15
PROJECTION_TIME_SHIFT = 0.005

# Timing 
sec_adjusted_bpm = 4 * (SECONDS / BPM)


# Projection constants
num_white_keys = 36             #Since its a mini piano
num_black_keys = 25
total_keys = num_white_keys + num_black_keys
top_of_key = 150
bot_of_key = top_of_key + 100

# Tone Sensing constants
# White keys are in Uppercase and black keys (sharps) are in lowercase
octave = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'] 
base_freq = 440 #Frequency of Note A4
keys = np.array([x+str(y) for y in range(0,9) for x in octave])
# Trim to correct # keys
start = np.where(keys == 'A0')[0][0]
end = np.where(keys == 'C8')[0][0]
keys = keys[start:end+1]        #Notes of a piano

# For keyboard input
midi_num = []
n = FIRST_NOTE_FOR_KEYBOARD
for i in range(len(keys)):    
    midi_num.append(n)
    n += 1


# For live audio recording
note_freqs = list(([2**((n+1-49)/12)*base_freq for n in range(len(keys))]))     #frequency of each key on a piano in order

# Scales
c_major = [['C4', 0.25], ['D4', 0.25], ['E4',0.25], ['F4', 0.25], ['G4', 0.25], ['A4', 0.25], ['B4', 0.25], ['C5', 0.25], ['B4', 0.25], ['A4', 0.25], ['G4', 0.25],
           ['F4', 0.25],  ['E4', 0.25], ['D4', 0.25],  ['C4', 0.25]]
d_major = [['D4', 0.25],  ['E4', 0.25],  ['F#4', 0.25], ['G4', 0.25], ['A4', 0.25], ['B4', 0.25], ['C#5', 0.25], ['D5', 0.25], ['C#5', 0.25], ['B4', 0.25], ['A4', 0.25],
           ['G4', 0.25], ['F#4', 0.25], ['E4', 0.25], ['D4', 0.25]]
e_major = [['E4', 0.25], ['F#4', 0.25],  ['G#4', 0.25], ['A4', 0.25], ['B4', 0.25], ['C#5', 0.25], ['D#5', 0.25], ['E5', 0.25], ['D#5', 0.25], ['C#5', 0.25], ['B4', 0.25],
           ['A4', 0.25], ['G#4', 0.25], ['F#4', 0.25], ['E4', 0.25]]
f_major = [['F4', 0.25], ['G4', 0.25], ['A4', 0.25], ['A#4', 0.25], ['C5', 0.25], ['D5', 0.25], ['E5', 0.25], ['F5', 0.25], ['E5', 0.25], ['D5', 0.25], ['C5', 0.25], 
           ['A#4', 0.25], ['A4', 0.25], ['G4', 0.25], ['F4', 0.25]]
g_major = [['G4',  0.25], ['A4', 0.25], ['B4', 0.25], ['C5', 0.25], ['D5', 0.25], ['E5', 0.25], ['F#5', 0.25], ['G5', 0.25], ['F#5', 0.25], ['E5', 0.25], ['D5', 0.25],
           ['C5', 0.25], ['B4', 0.25], ['A4', 0.25], ['G4', 0.25]]
mhall = [['E4', 0.25], ['D4', 0.25], ['C4', 0.25], ['D4', 0.25], ['E4', 0.25], ['E4', 0.25], ['E4', 0.5], ['D4', 0.25], ['D4', 0.25], ['D4', 0.5], ['E4', 0.25],['G4', 0.25],
         ['G4', 0.5], ['E4', 0.25], ['D4', 0.25], ['C4', 0.25], ['D4', 0.25], ['E4', 0.25], ['E4', 0.25], ['E4', 0.25], ['E4', 0.25], ['D4', 0.25], ['D4', 0.25], ['E4', 0.25], 
         ['D4', 0.25], ['C4', 1]]