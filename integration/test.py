import csv
import os
import time
import datetime

CURRENT_DIR = os.path.dirname(__file__)
file_path = os.path.join(CURRENT_DIR, 'song_gallery.csv')
#print("file_path ", file_path)
scale_input = input("What Major scale would you like to play?\n")
def csv_retrieval(scale_input,file_path):
    with open(file_path) as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            name, data = row
            if name == scale_input:
                scale = data
                return scale
            #else:
               # raise Exception("Scale is not valid. Try again\n")
            
                #print(scale)
#print(csv_retrieval(scale_input, file_path))
print(datetime.time()+time(0.2))


    #print(rows[22])