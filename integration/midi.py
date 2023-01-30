import pygame.midi
import constants

# find out which is the midi device index (it must have the 1 at the beginning of the tuple)
def print_devices():
    for n in range(pygame.midi.get_count()):
        print (n,pygame.midi.get_device_info(n))

def number_to_note(number):
    index = constants.midi_num.index(number)
    note_played = (constants.keys[index])
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
def similar(x,y):
    si = 0
    for a,b in zip(x, y):
        if a == b:
            si += 1
    return (si/len(x)) * 100

# def testInput(input_device):
#     test=[]
#     while len(test)<16:
#         if input_device.poll():
#             event = input_device.read(1)[0]
            
#             data = event[0]
#             #timestamp = event[1]
#             note_number = data[1]
#             #velocity = data[2]
#             test.append(number_to_note(note_number))
#     test=test[::2]
#     print(test)
#     res = len(set(c_major_scale) & set(test)) / float(len(set(c_major_scale) | set(test))) * 100
#     print(str(res))

def note_stream(input_device):
    if input_device.poll():
        event = input_device.read(1)[0]
        data = event[0]
        note_number = data[1]
        velocity = data[2]
        if (velocity == 100):
            return number_to_note(note_number)

def initialization():
    pygame.midi.init()

def set_device_input(device_number):
    return pygame.midi.Input(device_number)

# if __name__ == '__main__':
#     pygame.midi.init()
#     my_input = pygame.midi.Input(0) #only in my case the id is 0
#     testInput(my_input)
