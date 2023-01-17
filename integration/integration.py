import numpy as np
from tkinter import *
import constants
import projection_luts
import projection
#import tone

if __name__ == "__main__":
    #Create empty array 
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
    projection_index = []
    c_major_scale = ['F4', 'G4', 'A4', 'A#4', 'C5']
    scale_test = np.zeros((len(c_major_scale), constants.total_keys))
    for i in range(len(c_major_scale)):
        projection_index.append(projection_luts.note_lut(c_major_scale[i]))
        for j in range(len(constants.keys)):
            if c_major_scale[i] == constants.keys[j]:
                c_major_scale_freqs.append(constants.note_freqs[j])

    for n in range(len(c_major_scale)):
        scale_test[n][projection_index[n]] = 1

    #print("C major scale: ", c_major_scale)
    #print("projection index: ", projection_index)
    #print("C major scale frequencies: ", c_major_scale_freqs)
    #print("scale test: ", scale_test)
    
    projection.project_song(root, canvas, screen_width, screen_height, scale_test, c_major_scale)
    inital = projection.create_default(root, canvas, screen_width, screen_height)
    #root.mainloop()
