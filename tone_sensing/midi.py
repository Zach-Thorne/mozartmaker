import pygame.midi
import numpy as np
# find out which is the midi device index (it must have the 1 at the beginning of the tuple)
def print_devices():
    for n in range(pygame.midi.get_count()):
        print (n,pygame.midi.get_device_info(n))

#if __name__ == '__main__':
    #pygame.midi.init()
    #print_devices()

notes = ['c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#', 'a', 'a#', 'b']
keys = np.array([x+str(y) for y in range(0,9) for x in notes])
# Trim to correct # keys
start = np.where(keys == 'a0')[0][0]
end = np.where(keys == 'c8')[0][0]
keys = keys[start:end+1]
midi_num=[]
n=21
for i in range(len(keys)):    
    midi_num.append(n)
    n=n+1

c_major_scale_freqs=[]
c_major_scale=['c4', 'd4', 'e4', 'f4', 'g4', 'a4', 'b4', 'c5']
for i in range(len(keys)):
    for j in range(8):
        if c_major_scale[j]==keys[i]:
            c_major_scale_freqs.append(midi_num[i])

def number_to_note(number):
    index = midi_num.index(number)
    note_played=(keys[index])
    return note_played

def readInput(input_device):
    while True:
        if input_device.poll():
            event = input_device.read(1)[0]
            
            data = event[0]
            timestamp = event[1]
            note_number = data[1]
            velocity = data[2]
            print (number_to_note(note_number), velocity)

def testInput(input_device):
    test=[]
    while len(test)<16:
        if input_device.poll():
            event = input_device.read(1)[0]
            
            data = event[0]
            #timestamp = event[1]
            note_number = data[1]
            #velocity = data[2]
            test.append(number_to_note(note_number))
    test=test[::2]
    print(test)
    #turns the items into set and compares the similar individual elemtns using 'and' and 'or' statements
    percent_correct = len(set(c_major_scale) & set(test)) / float(len(set(c_major_scale) | set(test))) * 100
    print(str(percent_correct))


  
if __name__ == '__main__':
    pygame.midi.init()
    my_input = pygame.midi.Input(0) #only in my case the id is 0
    testInput(my_input)
