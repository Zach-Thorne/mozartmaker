import pygame.midi
import constants
import time

# find out which is the midi device index (it must have the 1 at the beginning of the tuple)
def initialization():
    pygame.midi.init()
    for n in range(pygame.midi.get_count()):
        midi_input = pygame.midi.get_device_info(n)
        #print (n,pygame.midi.get_device_info(n))
        model = "CASIO USB-MIDI"
        model = model.encode('utf-8')
        if ((model in midi_input[1]) and midi_input[2]):
            keyboard_detect = n
            print("Keyboard is: ", midi_input, keyboard_detect)
            return pygame.midi.Input(keyboard_detect)
            break

def number_to_note(number):
    index = constants.midi_num.index(number)
    note_played = (constants.keys[index])
    return note_played

def readInput(input_device):
    while True:
        if input_device.poll():
            event = input_device.read(1)[0]
            # start = time.clock()
            data = event[0]
            timestamp = event[1]
            note_number = data[1]
            
            # stop = time.clock()
            
            if data[2] == 100:
                print(time.time())
                print(data)
                print (number_to_note(note_number))
def similar(x,y):
    si = 0
    for a,b in zip(x, y):
        if a == b:
            si += 1
    return (si/len(x)) * 100

def note_stream(input_device):
    if input_device.poll():
        event = input_device.read(1)[0]
        data = event[0]
        timestamp = event[1]
        note_number = data[1]
        velocity = data[2]
        print("event: ", event)
        #print("data: ", data)
        return [number_to_note(note_number), velocity, timestamp]
        # if (velocity == 100):
        #     return number_to_note(note_number)

if __name__ == '__main__':
    keyboard = initialization()
    readInput(keyboard)


    
