# song gallery - back-end to store pre-loaded songs and songs uploaded by user

import pandas
import os.path

#
#
# FUNCTIONS FOR CREATING / EDITING CSV FILE

# create csv file for the first time with pre-loaded songs
def create_csv(): # ALL GOOD
    
    # create .csv headers
    headerList = ['name','data']
    
    # create the dataFrame for pre-loaded songs
    songData_C = pandas.DataFrame({ 'name': ['C'], 
                                    'data': [['C4',0.25,1,  'D4',0.25,2,  'E4',0.25,3,  'F4',0.25,1,  'G4',0.25,2,  'A4',0.25,3,  'B4',0.25,4,  'C5',0.25,5,
                                              'B4',0.25,4,  'A4',0.25,3,  'G4',0.25,2,  'F4',0.25,1,  'E4',0.25,3,  'D4',0.25,2,  'C4',0.25,1]]} )
    songData_D = pandas.DataFrame({ 'name': ['D'], 
                                    'data': [['C4',0.25,1,  'D4',0.25,2,  'E4',0.25,3,  'F4',0.25,1,  'G4',0.25,2,  'A4',0.25,3,  'B4',0.25,4,  'C5',0.25,5,
                                              'B4',0.25,4,  'A4',0.25,3,  'G4',0.25,2,  'F4',0.25,1,  'E4',0.25,3,  'D4',0.25,2,  'C4',0.25,1]]} )
    
    # ADD ANY MORE PRE-LOADED SONGS HERE

    allData = pandas.concat([songData_C, songData_D],ignore_index=True)
    allData.to_csv('song_gallery.csv',mode='w',index=True,header=headerList)

# add new song to the csv file
def append_csv(name, data): # good (i think)

    newData = pandas.DataFrame({'name': [name], 'data': [data]}) # create new dataframe    
    newData.to_csv('song_gallery.csv',mode='a',index=True, header=False) # append new data to csv

    # these are all lines that aren't being used but i'm scared to delete them lol

    # note:
    # the indices will appear fucked in the .csv but that's not the actual index file
    # these two lines will print the contents into the terminal and show the real indices
    #songData = pandas.read_csv('song_gallery.csv')
    #print(songData)

    #allData = pandas.concat([copyData,newData])
    #print("allData created")

    #allData.to_csv('song_gallery.csv',mode='a',index=True,columns=headerList) #append
    
    # headerList = ['name','data']

    #copyData = pandas.read_csv('song_gallery.csv', usecols=['name','data'], header=1)
    #copyData = pandas.read_csv('song_gallery.csv')
    #print("copyData created")

    # try resetting indices?
    #copyData = pandas.read_csv('song_gallery.csv')
    #copyData = copyData.reset_index(drop=True) # mess around with inplace and drop
    #clear_csv()
    #copyData.to_csv('song_gallery.csv', mode='w')


# reset the csv
def clear_csv(): # ALL GOOD
    dataframe_clear = pandas.DataFrame(list())
    dataframe_clear.to_csv('song_gallery.csv', mode='w')

#
#
# FUNCTIONS FOR READING DATA FROM CSV FILE

# read data from csv for desired song
def get_index(name): # ALL GOOD

    # create dataframe of current contents
    songData = pandas.read_csv('song_gallery.csv')

    # get index from song name
    name = str(name)
    songIndex = songData[songData['name']==name].index.to_list()
    
    return songIndex[0]

# create list of rows to skip when reading data from the csv (since we only want to read the desired song)
def create_skip_rows(length, songIndex): # ALL GOOD
    
    skip_rows_list = []
    
    for i in range(length):
        if (i != songIndex):
            skip_rows_list.append(i+1)
    
    return skip_rows_list

#
#
# MAIN SONG GALLERY FUNCTION

# if action is "read" -> return song data
# if action is "add" -> returns 0

def song_gallery(name, data, action): # ALL GOOD
    
    # check if the csv file already exists (if not - create it)
    path = './song_gallery.csv'
    file_exists_flag = os.path.isfile(path)

    # if the song gallery .csv doesn't exist yet, create one with the pre-loaded songs
    if file_exists_flag == False:
        create_csv()

    #
    #
    # READ SONG DATA
    if (action == "read"):
        print("reading data for", name)

        #
        # READ FROM .CSV -> ALL GOOD

        # create dataframe of all data in .csv
        allData = pandas.read_csv('song_gallery.csv',usecols=['data']) # copy dataframe from csv
        length = allData.shape[0] # get length of dataframe (how many songs there are)

        # create list of data for only desired song
        songIndex = get_index(name) # get index of song in csv    
        skip_rows_list = create_skip_rows(length, songIndex) # create list of indices to skip (any indices that are not the desired song)
        songData = pandas.read_csv('song_gallery.csv',usecols=['data'],skiprows=skip_rows_list) # create dataframe for desired song
        songData_List = songData.values.tolist() # convert dataframe to list

        # 
        # CONVERT DATA TO NEEDED FORMAT -> TODO: hmm. it's not including the last data element?

        # create temp variables and an array to store final data
        songData_split = []
        tempString = ""
        tempArray = []

        # iterate through song list, create tempArray for each triplet of data: ['note', duration, finger] -> [string, float, int]
        for i in range(len(songData_List[0][0])):
            if (songData_List[0][0][i] == ",") | (i == len(songData_List[0][0])-1): # if it's a comma or if it's the last element?
                tempArray.append(tempString)
                tempString = "" 
                
                if(len(tempArray)==3): # if the tempArray has all needed data for the note
                    tempArray[1] = float(tempArray[1]) # type cast duration (1) to float
                    tempArray[2] = int(tempArray[2]) # type cast finger (2) to int
                    songData_split.append(tempArray) # append the triplet of data to the array of all data
                    tempArray = []

            # this conditional is here because we don't want to add any of the weird ,'[] characters to our array
            elif ((songData_List[0][0][i] != ",") & (songData_List[0][0][i] != "'") & (songData_List[0][0][i] != "[") & (songData_List[0][0][i] != "]")):
                    tempString = tempString + songData_List[0][0][i] # fill the tempString

        return songData_split

    #
    #
    # ADD SONG TO .CSV
    elif (action=="add"):
        print("adding", name, "to the database")
        append_csv(name, data)
        return 0
    
# song gallery parameters:
# 1. name: name of song to read/write
# 2. data: data of song to write. if reading, just pass NULL
# 3. action: "read" or "add"

# name = "E"
# data = C_major
# action = 'read'

# songData = song_gallery(name,data,action)
# print(name, "=", songData)