#Look up table for black keys to convert array index to projection index
def black_lut(j):
    if(j==1):
        return 0 
    if(j==3):
        return 1 
    if(j==6):
        return 3 
    if(j==8):
        return 4 
    if(j==10):
        return 5 
    if(j==13):
        return 7 
    if(j==15):
        return 8 
    if(j==18):
        return 10 
    if(j==20):
        return 11 
    if(j==22):
        return 12 
    if(j==25):
        return 14 
    if(j==27):
        return 15 
    if(j==30):
        return 17
    if(j==32):
        return 18
    if(j==34):
        return 19
    if(j==37):
        return 21
    if(j==39):
        return 22
    if(j==42):
        return 24
    if(j==44):
        return 25
    if(j==46):
        return 26
    if(j==49):
        return 28
    if(j==51):
        return 29
    if(j==54):
        return 31
    if(j==56):
        return 32
    if(j==58):
        return 33 

#Look up table for white keys to convert array index to projection index
def white_lut(j):
    if(j==0):
        return 0 
    if(j==2):
        return 1 
    if(j==4):
        return 2 
    if(j==5):
        return 3 
    if(j==7):
        return 4 
    if(j==9):
        return 5 
    if(j==11):
        return 6 
    if(j==12):
        return 7 
    if(j==14):
        return 8 
    if(j==16):
        return 9 
    if(j==17):
        return 10 
    if(j==19):
        return 11 
    if(j==21):
        return 12
    if(j==23):
        return 13
    if(j==24):
        return 14
    if(j==26):
        return 15
    if(j==28):
        return 16
    if(j==29):
        return 17
    if(j==31):
        return 18
    if(j==33):
        return 19
    if(j==35):
        return 20
    if(j==36):
        return 21
    if(j==38):
        return 22
    if(j==40):
        return 23
    if(j==41):
        return 24
    if(j==43):
        return 25
    if(j==45):
        return 26
    if(j==47):
        return 27
    if(j==48):
        return 28
    if(j==50):
        return 29
    if(j==52):
        return 30
    if(j==53):
        return 31
    if(j==55):
        return 32
    if(j==57):
        return 33
    if(j==59):
        return 34
    if(j==60):
        return 35
