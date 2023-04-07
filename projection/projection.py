import math
import cv2
import matplotlib.pyplot as plt
import numpy as np
import time
import tk
from tkinter import *
from projection_luts import black_lut, white_lut

#TODO move global variables into own file so we can change them in one file and it wont impact anything else
num_white_keys = 36 #Since its a mini piano
num_black_keys = 25
total_keys = num_white_keys + num_black_keys
top_of_key = 550
bot_of_key = top_of_key+100
const_to_change_width = 7

#NOTE Look into if this would make more sense being a class 
#Sets up default shape for keyboard
def create_default(master, canvas, screen_width, screen_height): 

    #TODO will need update to more match the keys but for now this is fine
    rec_width = math.floor((screen_width-20)/num_white_keys) - const_to_change_width
    
    #Creates blank rectangles for all of the white keys 
    for i in range(num_white_keys):
        canvas.create_rectangle(10+rec_width*i,top_of_key,10+rec_width+rec_width*i,bot_of_key,outline ="black",fill ="white",width = 2)
        #Adds black keys
        #TODO May need to adjust width of black keys
        #if(i == 0,1,3,4,5,7,8,10,11,12,14,15,17,18,19,21,22,24,25,26,28,29,31,32,33):
        if(i == 0 or i == 1 or i == 3 or i == 4 or i == 5 or i == 7 or i ==8 or i ==10 or i ==11 or i ==12 or i ==14 or i ==15 or i ==17 or i ==18 or i ==19 or i ==21 or i ==22 or i ==24 or i ==25 or i ==26 or i ==28 or i ==29 or i ==31 or i ==32 or i ==33):
            #scuffed
            canvas.create_rectangle(10+rec_width*i+math.floor(rec_width/2),top_of_key-100,10+rec_width+rec_width*i+math.floor(rec_width/2),top_of_key,outline ="black",fill ="white",width = 2)

    canvas.pack()
    return canvas

#Place Holder to create basic 3 note song
def create_basic_song():
    #This basic song will just play first left most keys
    song = np.zeros((total_keys,3))
    for i in range(3): 
        song[i,i] = 1 
    return song

#Will light correct keys up gren ideally
def project_song(root, canvas, screen_width, screen_height, song):
    rec_width = math.floor((screen_width-20)/num_white_keys) - const_to_change_width
    total_elem = song.size
    notes = math.floor(total_elem/num_white_keys)
    for i in range(notes):
        for j in range(len(song[i])):
            #If the element array is one, light up the corresponding Key green
            if(song[i,j] == 1):
                #If j corresponds to a black key
                if(j == 1 or j == 3 or j == 6 or j == 8 or j == 10 or j == 13 or j == 15 or j == 18 or j == 20 or j == 22 or j == 25 or j == 27 or j == 30 or j == 32 or j == 34 or j == 37 or j == 39 or j == 42 or j == 44 or j == 46 or j == 49 or j == 51 or j == 54 or j == 56 or j == 58): 
                    #Feel like there is a better way to do this but we going to do this for now 
                    t = black_lut(j)
                    canvas.create_rectangle(10+rec_width*t+math.floor(rec_width/2),top_of_key-100,10+rec_width+rec_width*t+math.floor(rec_width/2),top_of_key,outline ="black",fill ="green",width = 2)
                #If j corresponds to a white key
                else:
                    t = white_lut(j)
                    canvas.create_rectangle(10+rec_width*t,top_of_key,10+rec_width+rec_width*t,bot_of_key,outline ="black",fill ="green",width = 2)
            else:
                #If j corresponds to a black key
                if(j == 1 or j == 3 or j == 6 or j == 8 or j == 10 or j == 13 or j == 15 or j == 18 or j == 20 or j == 22 or j == 25 or j == 27 or j == 30 or j == 32 or j == 34 or j == 37 or j == 39 or j == 42 or j == 44 or j == 46 or j == 49 or j == 51 or j == 54 or j == 56 or j == 58): 
                    #Feel like there is a better way to do this but we going to do this for now 
                    t = black_lut(j)
                    canvas.create_rectangle(10+rec_width*t+math.floor(rec_width/2),top_of_key-100,10+rec_width+rec_width*t+math.floor(rec_width/2),top_of_key,outline ="black",fill ="white",width = 2)
                #If j corresponds to a white key
                else:
                    t = white_lut(j)
                    canvas.create_rectangle(10+rec_width*t,top_of_key,10+rec_width+rec_width*t,bot_of_key,outline ="black",fill ="white",width = 2)

            canvas.pack()
        input("Press Enter to continue...")
            
if __name__ == "__main__":

    #Create empty array 
    keys = np.zeros(total_keys)
    #Initalize Tkinter
    root = Tk()

    #Function to open tkinter window on another display
    d    

    #Initialize Canvas
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    canvas = Canvas(width =screen_width, height=screen_height)


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
    project_song(root, canvas, screen_width, screen_height, song)

    #Return to inital state 
    inital = create_default(root, canvas, screen_width, screen_height)

    #Tells python to run the Tkinter event loop
    #Creates the window
    root.mainloop()

    
