#File to help convert a picture of sheet music into the array type that we need to input into system
import numpy as np
import oemer
import os.path
import subprocess
from music21 import *
from mido import MidiFile

TEMP = 'bells.musicxml'
test_mode = 0
            
#Gets input and makes sure it exists
def get_file_input():
  while(1):
    print("Please input file you want to scan")
    file_name = input() 
    if os.path.exists(file_name):
      break
    else: 
      print("File does not exist try again")
  return file_name

def convert_to_notes(sheet_music):
  #Take picture of sheet music and convert to musicXML Format
  #TODO use Oemer call her to convert to XML 
  if(test_mode == 1):
    print("RUN WITH OEMER")
    #Run mode to get to XML
    #NOTE Slow as shit 
    subprocess.run(["oemer", sheet_music])
    
    #Gets Name of musicxml file
    sheet_xml = sheet_music.split('.')[0]+".musicxml"

  #Take musicXML and use music21 library to convert it
  if(test_mode == 1):
    c = converter.parse(sheet_xml)
  else:
    c = converter.parse(sheet_music)

  #Convert to midi file
  fp = c.write('midi', fp='midi.mid')
  
  #Now to read in midi file and get data in usable format do this using mido
  mid = MidiFile('midi.mid', clip=True) 
  print(mid)
  
  #Prints different tracks
  for track in mid.tracks:
    print(track)
    
  print("*******************TRACK 1***********************")
  for msg in mid.tracks[0]:
    print(msg)

  #Need to append notes, velocity and time to scale
  track2_data = []
  track2_notes = []
  track3_data = []
  track3_notes = []

  #Pretty sure track 2 corresponds to treble staff
  print("*******************TRACK 2***********************")
  for msg in mid.tracks[1]:
    print(msg)
    if msg.type == 'note_on':
      print(msg.note)
      tuple_1 = [msg.note, msg.velocity, msg.time]
      track2_data.append(tuple_1) 
      track2_notes.append([msg.note]) 

  #Pretty sure track 3 corresponds to bass staff
  print("*******************TRACK 3***********************")
  for msg in mid.tracks[2]:
    print(msg)
    if msg.type == 'note_on':
      print(msg.note)
      tuple_2 = [msg.note, msg.velocity, msg.time]
      track3_data.append(tuple_2) 
      track3_notes.append([msg.note]) 


if __name__ == "__main__":
  #TEST_MODE ASK 
  print("Run with Oemer? 1 = yes, 0 = no") 
  test_mode = int(input())
  #Function to get file name
  if(test_mode == 1):
    sheet_music = get_file_input()
  else:
    sheet_music = TEMP 
  return_string = convert_to_notes(sheet_music)
  
  print("Make sure file setup correct") 


