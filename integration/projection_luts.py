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

def note_lut(j):
    if(j=='C2'):
        return 0 
    if(j=='C#2' or 'Db2'):
        return 1 
    if(j=='D2'):
        return 2 
    if(j=='D#2' or 'Eb2'):
        return 3 
    if(j=='E2'):
        return 4 
    if(j=='F2'):
        return 5 
    if(j=='F#2' or 'Gb2'):
        return 6 
    if(j=='G2'):
        return 7 
    if(j=='G#2' or 'Ab2'):
        return 8 
    if(j=='A2'):
        return 9 
    if(j=='A#2' or 'Bb2'):
        return 10 
    if(j=='B2'):
        return 11 
    if(j=='C3'):
        return 12 
    if(j=='C#3' or 'Db3'):
        return 13 
    if(j=='D3'):
        return 14 
    if(j=='D#3' or 'Eb3'):
        return 15 
    if(j=='E3'):
        return 16 
    if(j=='F3'):
        return 17 
    if(j=='F#3' or 'Gb3'):
        return 18 
    if(j=='G3'):
        return 19 
    if(j=='G#3' or 'Ab3'):
        return 20 
    if(j=='A3'):
        return 21 
    if(j=='A#3' or 'Bb2'):
        return 22 
    if(j=='B3'):
        return 23 
    if(j=='C4'):
        return 24 
    if(j=='C#4' or 'Db4'):
        return 25 
    if(j=='D4'):
        return 26 
    if(j=='D#4' or 'Eb4'):
        return 27 
    if(j=='E4'):
        return 28 
    if(j=='F4'):
        return 29 
    if(j=='F#4' or 'Gb4'):
        return 30 
    if(j=='G4'):
        return 31 
    if(j=='G#4' or 'Ab4'):
        return 32 
    if(j=='A4'):
        return 33 
    if(j=='A#4' or 'Bb4'):
        return 34 
    if(j=='B4'):
        return 35
    if(j=='C5'):
        return 36 
    if(j=='C#5' or 'Db5'):
        return 37 
    if(j=='D5'):
        return 38 
    if(j=='D#5' or 'Eb5'):
        return 39 
    if(j=='E5'):
        return 40 
    if(j=='F5'):
        return 41 
    if(j=='F#5' or 'Gb5'):
        return 42 
    if(j=='G5'):
        return 43 
    if(j=='G#5' or 'Ab5'):
        return 44 
    if(j=='A5'):
        return 45 
    if(j=='A#5' or 'Bb5'):
        return 46 
    if(j=='B5'):
        return 47
    if(j=='C6'):
        return 48 
    if(j=='C#6' or 'Db6'):
        return 49 
    if(j=='D6'):
        return 50 
    if(j=='D#6' or 'Eb6'):
        return 51 
    if(j=='E6'):
        return 52 
    if(j=='F6'):
        return 53 
    if(j=='F#6' or 'Gb6'):
        return 54 
    if(j=='G6'):
        return 55 
    if(j=='G#6' or 'Ab6'):
        return 56 
    if(j=='A6'):
        return 57 
    if(j=='A#6' or 'Bb6'):
        return 58 
    if(j=='B6'):
        return 59   
    if(j=='C7'):
        return 60   
