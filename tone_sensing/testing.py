import numpy as np
import statistics

def note_to_freq(note_freqs, keys, note):
    ind = np.argwhere(keys==note)
    #print(ind[0][0])
    song_freq=note_freqs[ind[0][0]]
    return song_freq
def detect_outlier(data_set):
    thresh = 1
    mean = statistics.mean(data_set)
    std = statistics.stdev(data_set)
    result = [y  for y in data_set if abs((y - mean)/std)<=thresh ]
    return result
octave = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'] 
base_freq = 440 #Frequency of Note A4
keys = np.array([x+str(y) for y in range(0,9) for x in octave])
# Trim to correct # keys
start = np.where(keys == 'A0')[0][0]
end = np.where(keys == 'C8')[0][0]
keys = keys[start:end+1]        #Notes of a piano

note_freqs = list(([2**((n+1-49)/12)*base_freq for n in range(len(keys))]))

notes=['F6', 'F6', 'F6', 'F5', 'F4', 'G5', 'G6', 'G6', 'G4', 'A4', 'A4', 'A#4', 'A#4', 'A#4', 'A#4', 'A#4', 'C5', 'C5', 'C5', 'C5', 'C6', 'D5', 'D5', 'D5', 'D5', 'D5', 'D5', 'E5', 'E5', 'E5', 'E5', 'E5', 'E5', 'E5', 'F5', 'F5', 'F5', 'F5', 'F5', 'F5', 'F5', 'E5', 'E5', 'E5', 'E5', 'E5', 'E5', 'E5', 'E5', 'D5', 'D5', 'D5', 'D5', 'D5', 'D5', 'D5', 'D5', 'C5', 'C5', 'C5', 'C5', 'C5', 'C5', 'C5', 'A#4', 'A#4', 'A#4', 'A#4', 'A#4', 'A#4', 'A5', 'A6', 'A4', 'A4', 'A4', 'A4', 'A4', 'F2', 'G6', 'G6', 'G4', 'G4', 'G4', 'G4', 'F2', 'F6', 'F6', 'F6', 'F5', 'F5']
#A function for making sure you can find the closest value in a list
def closest_val(input_list, val):
  arr = np.asarray(input_list)
  i = (np.abs(arr - val)).argmin()
  return arr[i]
def freq_to_note(played_freq, note_freqs, keys):
    freq=closest_val(note_freqs,played_freq)
    ind = note_freqs.index(freq)
    song_note=keys[ind]
    return song_note

for i in range(len(notes)):
    notes[i]=note_to_freq(note_freqs, keys, notes[i])
notes=detect_outlier(notes)
for i in range(len(notes)):
    notes[i]=freq_to_note(notes[i], note_freqs, keys)

print(notes[1::2])