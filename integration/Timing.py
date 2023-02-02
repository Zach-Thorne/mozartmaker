import array
def create_song(song,bpm): 

    
    bpm = 80
    spb = 1/(bpm/60)

    new_song=[ [0]*2 for i in range(len(song))]
    for i in range(0,len(song)):
        new_song[i][0]= song[i]
        if song[i] == 1:#wholenote
            new_song[i][1]= spb*4
        elif song[i] == 2:#halfnote
            new_song[i][1]= spb*2
        elif song[i] == 4:#quarternote
            new_song[i][1]= spb
        elif song[i] == 8:#eighthnote
            new_song[i][1]= spb/2
        else: #sixteenthnote
            new_song[i][1]= spb/4

    #print (new_song)
    return new_song
    

 

    
#new_song = create_song(song,beatsperbar,bpm) # put this in import song function


    
    #print (new_song)





# def create_bar(song,skip):
#     check=0
#     bar = []
#     i=1
#     while (check < 16):
#         if i+skip >= len(song):
#             break
#         elif song[i+skip] == 1: #wholenote
#             for j in range(0,16):
#                 bar.append(1)
#             check += 16
#         elif song[i+skip] == 2: #halfnote
#             for j in range(0,8):
#                 bar.append(2)
#             check += 8
#         elif song[i+skip] == 4:#quarternote
#             for j in range(0,4):
#                 bar.append(4)
#             check += 4
#         elif song[i+skip] == 8:#eighthnote
#             for j in range(0,2):
#                 bar.append(8)
#             check += 2
#         else: #sixteenthnote           
#             bar.append(16)
#             check +=1
#         i+=1
#     print (bar, '\n \n')
#     return bar
            