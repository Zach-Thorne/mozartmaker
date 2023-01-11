import numpy as np
import cv2
import tk
from tkinter import *
import constants
import projection
import tone

if __name__ == "__main__":
    #Create empty array 
    keys = np.zeros(constants.total_keys)
    #Initalize Tkinter
    root = Tk()

    #Initialize Canvas
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    canvas = Canvas(width=screen_width, height=screen_height)

    #NOTE SHOULD RUN ON STARTUP 
    #Create inital outline
    inital = projection.create_default(root, canvas, screen_width, screen_height)

    input("Press enter to start practicing")

    #A hard coded c major scale with frequencies
    c_major_scale_freqs = []
    c_major_scale = ['C4', 'D4', 'E4', 'F4', 'G4']
    for i in range(len(constants.keys)):
        for j in range(5):
            if c_major_scale[j] == constants.keys[i]:
                c_major_scale_freqs.append(constants.note_freqs[i])

    


