# song gallery - back-end to store pre-loaded songs and songs uploaded by user

import pandas
import os.path

#
#
# FUNCTIONS FOR CREATING / EDITING CSV FILE

# create csv file for the first time - ALL GOOD
def create_csv():
    print('create')
    
    # create .csv headers
    headerList = ['name','data']
    
    # create the dataFrame for pre-loaded songs
    songData_C = pandas.DataFrame({ 'name': ['C'], 
                                    'data': [['C4','0.25','1',  'D4','0.25','2',  'E4','0.25','3',  'F4','0.25','1',  'G4','0.25','2',  'A4','0.25','3',  'B4','0.25','4',  'C5','0.25','5',
                                            'B4','0.25','4',  'A4','0.25','3',  'G4','0.25','2',  'F4','0.25','1',  'E4','0.25','3',  'D4','0.25','2',  'C4','0.25','1']]} )
    songData_D = pandas.DataFrame({ 'name': ['D'], 
                                    'data': [['C4','0.25','1',  'D4','0.25','2',  'E4','0.25','3',  'F4','0.25','1',  'G4','0.25','2',  'A4','0.25','3',  'B4','0.25','4',  'C5','0.25','5',
                                            'B4','0.25','4',  'A4','0.25','3',  'G4','0.25','2',  'F4','0.25','1',  'E4','0.25','3',  'D4','0.25','2',  'C4','0.25','1']]} )
    
    allData = pandas.concat([songData_C, songData_D])
    allData.to_csv('song_gallery.csv',mode='w',index=False,header=headerList)

# add new song to the csv file
def append_csv(name, data):
    print('append')
    
    copyData = pandas.read_csv('song_gallery.csv', usecols=['name','data'])

    # create new data for desired song
    newData = pandas.DataFrame({'name': [name], 'data': [data]})

    allData = pandas.concat([copyData,newData])

    clear_csv()
    # append new data to csv
    allData.to_csv('song_gallery.csv',mode='a',index=False,header=['name','data'])

# reset the csv
def clear_csv():
    print('clear')
    dataframe_clear = pandas.DataFrame(list())
    dataframe_clear.to_csv('song_gallery.csv', mode='w')

#
#
# FUNCTIONS FOR READING DATA FROM CSV FILE

# read data from csv for desired song
def read_csv(song):
    songData = pandas.read_csv('song_gallery.csv')
    songIndex = songData[songData['name']=='C'].index.values
    print(songIndex)

# read data from csv for desired song
def get_index(song):
    print("get index")
    songData = pandas.read_csv('song_gallery.csv')
    print(songData)
    songIndex = songData[songData['name']=='D'].index
    print(songIndex)
    
    return songIndex[0]

#
#
# MAIN SONG GALLERY FUNCTION

def song_gallery(name, data, action):
    
    # TODO: convert data array to the way it needs to be stored in the csv
    # if action is read, just send a 0 for data

    # remove this when we actually start calling this function and sending in this data
    
    # action = 'add'
    # name = "E"
    # data = ['C4','0.25','1']

    #

    # check if the csv file already exists (if not - create it)
    path = './song_gallery.csv'
    file_exists_flag = os.path.isfile(path)

    # if the song_gallery file exists, just append new song
    if file_exists_flag == False:
        create_csv()
    else:
        if action == 'read':
            name = "D" # remove this later

            # read data for song
            print('read')

            songData = pandas.read_csv('song_gallery.csv')
            print(songData)
            songData_dict = songData.to_dict()
            print(songData_dict)

            csv_dict = {}
            csv_header_map = {
            "name" : 0,
            "data" : 1 }
            inverse_csv_map = dict((x, y) for y, x in csv_header_map.items())

            get_index(name)
            csv = open('song_gallery.csv', 'r')
            print("csv data")
            firstline = 1
            csv_list =[]
            i=0
            for line in csv.readlines():
                if firstline:
                    for header in line.split(','):
                        csv_dict[header.strip()] = []
                else:
                    print(line)
                    print(type(line))
                    
                    for entry in enumerate(line.split(',')):
                        csv_list.append(entry)
                firstline = 0

            print(csv_list)
            

            # create dict with only data for desired song
            
            # read data for desired song
            #songData = pandas.read_csv('song_gallery.csv', skiprows=skiprows_list, usecols=['data'])
            #songData_dict = songData.to_dict()
            #print(songData_dict.items())
            # TODO: convert songData to the array type that's actually used for projection
            
            

        elif action == 'add':
            # append song
            append_csv(name, data)

# data for pre-loaded songs
c_major = [['C4', 0.25, 1], ['D4', 0.25, 2], ['E4',0.25, 3], ['F4', 0.25], ['G4', 0.25], ['A4', 0.25], ['B4', 0.25], ['C5', 0.25], ['B4', 0.25], ['A4', 0.25], ['G4', 0.25],
           ['F4', 0.25],  ['E4', 0.25], ['D4', 0.25],  ['C4', 0.25]]
d_major = [['D4', 0.25],  ['E4', 0.25],  ['F#4', 0.25], ['G4', 0.25], ['A4', 0.25], ['B4', 0.25], ['C#5', 0.25], ['D5', 0.25], ['C#5', 0.25], ['B4', 0.25], ['A4', 0.25],
           ['G4', 0.25], ['F#4', 0.25], ['E4', 0.25], ['D4', 0.25]]
e_major = [['E4', 0.25], ['F#4', 0.25],  ['G#4', 0.25], ['A4', 0.25], ['B4', 0.25], ['C#5', 0.25], ['D#5', 0.25], ['E5', 0.25], ['D#5', 0.25], ['C#5', 0.25], ['B4', 0.25],
           ['A4', 0.25], ['G#4', 0.25], ['F#4', 0.25], ['E4', 0.25]]
f_major = [['F4', 0.25], ['G4', 0.25], ['A4', 0.25], ['A#4', 0.25], ['C5', 0.25], ['D5', 0.25], ['E5', 0.25], ['F5', 0.25], ['E5', 0.25], ['D5', 0.25], ['C5', 0.25], 
           ['A#4', 0.25], ['A4', 0.25], ['G4', 0.25], ['F4', 0.25]]
g_major = [['G4',  0.25], ['A4', 0.25], ['B4', 0.25], ['C5', 0.25], ['D5', 0.25], ['E5', 0.25], ['F#5', 0.25], ['G5', 0.25], ['F#5', 0.25], ['E5', 0.25], ['D5', 0.25],
           ['C5', 0.25], ['B4', 0.25], ['A4', 0.25], ['G4', 0.25]]
mhall = ['E4', 0.25, 'D4', 0.25]
name = "mhall"




song_gallery(name,mhall,'read')