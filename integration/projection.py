import math
import cv2
import numpy as np
import time
import tk
import wave
import sys
from tkinter import *
from projection_luts import black_lut, white_lut
import constants as c
import tone
#import integration

#NOTE Look into if this would make more sense being a class 
#Sets up default shape for keyboard
def create_default(master, canvas, screen_width, screen_height): 

    #TODO will need update to more match the keys but for now this is fine
    rec_width = math.floor((screen_width-20)/c.num_white_keys)
    
    #Creates blank rectangles for all of the white keys 
    for i in range(c.num_white_keys):
        canvas.create_rectangle(10+rec_width*i,c.top_of_key,10+rec_width+rec_width*i,c.bot_of_key,outline ="black",fill ="white",width = 2)
        #Adds black keys
        #TODO May need to adjust width of black keys
        #if(i == 0,1,3,4,5,7,8,10,11,12,14,15,17,18,19,21,22,24,25,26,28,29,31,32,33):
        if(i == 0 or i == 1 or i == 3 or i == 4 or i == 5 or i == 7 or i ==8 or i ==10 or i ==11 or i ==12 or i ==14 or i ==15 or i ==17 or i ==18 or i ==19 or i ==21 or i ==22 or i ==24 or i ==25 or i ==26 or i ==28 or i ==29 or i ==31 or i ==32 or i ==33):
            #scuffed
            canvas.create_rectangle(10+rec_width*i+math.floor(rec_width/2),c.top_of_key-100,10+rec_width+rec_width*i+math.floor(rec_width/2),c.top_of_key,outline ="black",fill ="white",width = 2)

    canvas.pack()
    canvas.update()
    return canvas

#Place Holder to create basic 3 note song
def create_basic_song():
    #This basic song will just play first left most keys
    basic_song_length = 5
    song = np.zeros((basic_song_length, c.total_keys))
    song[0][24] = 1
    song[0][28] = 1
    song[0][31] = 1
    song[1][26] = 1
    song[2][26] = 1
    song[3][27] = 1
    song[4][28] = 1
    
    print('length song: ', len(song))
    print('length song0: ', len(song[0]))

    #for i in range(basic_song_length): 
    #    song[i,i] = 1 
    return song

#Will light correct keys up gren ideally
def project_song(root, canvas, screen_width, screen_height, song, notes):
    rec_width = math.floor((screen_width-20)/c.num_white_keys)
    #total_elem = song.size
    #notes = math.floor(total_elem/c.num_white_keys)
    #print(notes)
    #for i in range(notes):
    x_index = 0
    for i in range(len(song)): #length of song (5)
        for j in range(len(song[i])): #all notes 61
            #If the element array is one, light up the corresponding Key green
            if(song[i,j] == 1):
                #If j corresponds to a black key
                if(j == 1 or j == 3 or j == 6 or j == 8 or j == 10 or j == 13 or j == 15 or j == 18 or j == 20 or j == 22 or j == 25 or j == 27 or j == 30 or j == 32 or j == 34 or j == 37 or j == 39 or j == 42 or j == 44 or j == 46 or j == 49 or j == 51 or j == 54 or j == 56 or j == 58): 
                    #Feel like there is a better way to do this but we going to do this for now 
                    t = black_lut(j)
                    canvas.create_rectangle(10+rec_width*t+math.floor(rec_width/2),c.top_of_key-100,10+rec_width+rec_width*t+math.floor(rec_width/2),c.top_of_key,outline ="black",fill ="green",width = 2)
                #If j corresponds to a white key
                else:
                    t = white_lut(j)
                    canvas.create_rectangle(10+rec_width*t,c.top_of_key,10+rec_width+rec_width*t,c.bot_of_key,outline ="black",fill ="green",width = 2)
            else:
                #If j corresponds to a black key
                if(j == 1 or j == 3 or j == 6 or j == 8 or j == 10 or j == 13 or j == 15 or j == 18 or j == 20 or j == 22 or j == 25 or j == 27 or j == 30 or j == 32 or j == 34 or j == 37 or j == 39 or j == 42 or j == 44 or j == 46 or j == 49 or j == 51 or j == 54 or j == 56 or j == 58): 
                    #Feel like there is a better way to do this but we going to do this for now 
                    t = black_lut(j)
                    canvas.create_rectangle(10+rec_width*t+math.floor(rec_width/2),c.top_of_key-100,10+rec_width+rec_width*t+math.floor(rec_width/2),c.top_of_key,outline ="black",fill ="white",width = 2)
                #If j corresponds to a white key
                else:
                    t = white_lut(j)
                    canvas.create_rectangle(10+rec_width*t,c.top_of_key,10+rec_width+rec_width*t,c.bot_of_key,outline ="black",fill ="white",width = 2)

            canvas.pack()
        input("Press Enter to start recording window")
        #tone.device_identification()
        tone.piano_sound()
        # start = time.time()
        # spf = wave.open("piano_audio.wav", "r")
        # signal = spf.readframes(-1)
        # signal = np.fromstring(signal, dtype=np.int16)
        # plt.figure(1)
        # plt.title("Signal Wave...")
        # plt.plot(signal)
        # plt.show()

        decoded_freqs = [tone.get_freq(bit) for bit in range(tone.get_bits())]
        
        for i in range(len(decoded_freqs)):
            note = tone.closest_val(c.note_freqs,decoded_freqs[i])
            index = c.note_freqs.index(note)
            played_note = c.keys[index]
        
        # #end = time.time()
        # #print('total time: ', end-start)
        # frequency = tone.det_freq()
        # print("Acquired frequency: ", frequency)
        # # song_notes=[]
        # for i in range(len(frequency)):
        #     note=tone.closest_val(c.note_freqs,frequency[i])
        #     index = c.note_freqs.index(note)
        #     played_note = c.keys[index]
        #     #print(song_notes)

        print("played note is: ", played_note)
        print("correct note is: ", notes[x_index])

        if played_note == notes[x_index]:
            print('Note is correct!\n')
            x_index += 1
            continue
        else:
            print('Note not correct\n')
            # if played_note == notes[x_index]:
            #     print("this is correct") 
            #     x_index += x_index
            #     break
            

def project_key(root, canvas, screen_width, screen_height, song, note_index, colour, finger):
    start_time = time.time()
    rec_width = math.floor((screen_width-20)/c.num_white_keys)
    for j in range(len(song[0])): #all notes 61
        if note_index != 0:
            if(song[note_index - 1,j] == 1):
                #If j corresponds to a black key
                if(j == 1 or j == 3 or j == 6 or j == 8 or j == 10 or j == 13 or j == 15 or j == 18 or j == 20 or j == 22 or j == 25 or j == 27 or j == 30 or j == 32 or j == 34 or j == 37 or j == 39 or j == 42 or j == 44 or j == 46 or j == 49 or j == 51 or j == 54 or j == 56 or j == 58): 
                    #Feel like there is a better way to do this but we going to do this for now 
                    t = black_lut(j)
                    canvas.create_rectangle(10+rec_width*t+math.floor(rec_width/2),c.top_of_key-100,10+rec_width+rec_width*t+math.floor(rec_width/2),c.top_of_key,outline ="black",fill ="white",width = 2)
                #If j corresponds to a white key
                else:
                    t = white_lut(j)
                    canvas.create_rectangle(10+rec_width*t,c.top_of_key,10+rec_width+rec_width*t,c.bot_of_key,outline ="black",fill ="white",width = 2)
        #If the element array is one, light up the corresponding Key green
        if(song[note_index,j] == 1):
            #If j corresponds to a black key
            if(j == 1 or j == 3 or j == 6 or j == 8 or j == 10 or j == 13 or j == 15 or j == 18 or j == 20 or j == 22 or j == 25 or j == 27 or j == 30 or j == 32 or j == 34 or j == 37 or j == 39 or j == 42 or j == 44 or j == 46 or j == 49 or j == 51 or j == 54 or j == 56 or j == 58): 
                #Feel like there is a better way to do this but we going to do this for now 
                t = black_lut(j)
                canvas.create_rectangle(10+rec_width*t+math.floor(rec_width/2),c.top_of_key-100,10+rec_width+rec_width*t+math.floor(rec_width/2),c.top_of_key,outline ="black",fill =colour,width = 2)
                canvas.create_text((10+rec_width+rec_width*t, 100), text = finger, font=("Helvetica", 54))
            #If j corresponds to a white key
            else:
                t = white_lut(j)
                canvas.create_rectangle(10+rec_width*t,c.top_of_key,10+rec_width+rec_width*t,c.bot_of_key,outline ="black",fill =colour,width = 2)
                canvas.create_text((10+rec_width*t+math.floor(rec_width/2) , 200), text = finger, font=("Helvetica", 54))
        canvas.pack()
        canvas.update()
    end_time = time.time()
    #print ("project key time: ", end_time - start_time)
    return (end_time - start_time)

def project_white(root, canvas, screen_width, screen_height, song, note_index):
    start_time = time.time()
    rec_width = math.floor((screen_width-20)/c.num_white_keys)
    for j in range(len(song[0])): #all notes 61
        if(song[note_index,j] == 1):
            #If j corresponds to a black key
            if(j == 1 or j == 3 or j == 6 or j == 8 or j == 10 or j == 13 or j == 15 or j == 18 or j == 20 or j == 22 or j == 25 or j == 27 or j == 30 or j == 32 or j == 34 or j == 37 or j == 39 or j == 42 or j == 44 or j == 46 or j == 49 or j == 51 or j == 54 or j == 56 or j == 58): 
                #Feel like there is a better way to do this but we going to do this for now 
                t = black_lut(j)
                canvas.create_rectangle(10+rec_width*t+math.floor(rec_width/2),c.top_of_key-100,10+rec_width+rec_width*t+math.floor(rec_width/2),c.top_of_key,outline ="black",fill ="white",width = 2)
            #If j corresponds to a white key
            else:
                t = white_lut(j)
                canvas.create_rectangle(10+rec_width*t,c.top_of_key,10+rec_width+rec_width*t,c.bot_of_key,outline ="black",fill ="white",width = 2)
        canvas.pack()
        canvas.update()
    end_time = time.time()
    return (end_time - start_time)

def project_blue(root, canvas, screen_width, screen_height, song):
    start_time = time.time()
    rec_width = math.floor((screen_width-20)/c.num_white_keys)
    octave_len = 12
    for j in range(octave_len): #all notes 61
        #if(song[note_index,j] == 1):
            #If j corresponds to a black key
        if(j == 1 or j == 3 or j == 6 or j == 8 or j == 10): 
            #Feel like there is a better way to do this but we going to do this for now 
            t = black_lut(j + 24)
            canvas.create_rectangle(10+rec_width*t+math.floor(rec_width/2),c.top_of_key-100,10+rec_width+rec_width*t+math.floor(rec_width/2),c.top_of_key,outline ="black",fill ="blue",width = 2)
        #If j corresponds to a white key
        else:
            t = white_lut(j + 24)
            canvas.create_rectangle(10+rec_width*t,c.top_of_key,10+rec_width+rec_width*t,c.bot_of_key,outline ="black",fill ="blue",width = 2)
        canvas.pack()
        canvas.update()
    end_time = time.time()
    return (end_time - start_time)

def project_all_white(root, canvas, screen_width, screen_height, song):
    start_time = time.time()
    rec_width = math.floor((screen_width-20)/c.num_white_keys)
    octave_len = 12
    for j in range(octave_len): #all notes 61
        #if(song[note_index,j] == 1):
            #If j corresponds to a black key
        if(j == 1 or j == 3 or j == 6 or j == 8 or j == 10): 
            #Feel like there is a better way to do this but we going to do this for now 
            t = black_lut(j + 24)
            canvas.create_rectangle(10+rec_width*t+math.floor(rec_width/2),c.top_of_key-100,10+rec_width+rec_width*t+math.floor(rec_width/2),c.top_of_key,outline ="black",fill ="white",width = 2)
        #If j corresponds to a white key
        else:
            t = white_lut(j + 24)
            canvas.create_rectangle(10+rec_width*t,c.top_of_key,10+rec_width+rec_width*t,c.bot_of_key,outline ="black",fill ="white",width = 2)
        canvas.pack()
        canvas.update()
    end_time = time.time()
    return (end_time - start_time)


if __name__ == "__main__":

    #Create empty array 
    keys = np.zeros(c.total_keys)
    #Initalize Tkinter
    root = Tk()

    #Initialize Canvas
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    canvas = Canvas(width=screen_width, height=screen_height)

    #TODO uncomment once we able to make shit fully work
    #root.attributes('-fullscreen', True)

    #NOTE SHOULD RUN ON STARTUP 
    #Create inital outline
    inital = create_default(root, canvas, screen_width, screen_height)

    #TODO replace this with input from user from the interface
    input("Press Enter to continue...")
    #TODO Replace with song that user selects
    song = create_basic_song()

    #Once song selected will project it
    #TODO Add conditional to only do this in training mode
    project_song(root, canvas, screen_width, screen_height, song, song)

    #Return to inital state 
    inital = create_default(root, canvas, screen_width, screen_height)

    #Tells python to run the Tkinter event loop
    #Creates the window
    root.mainloop()

    
