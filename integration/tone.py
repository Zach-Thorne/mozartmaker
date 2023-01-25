import pyaudio
import numpy as np
import scipy
from scipy.fftpack import fft
from scipy.io import wavfile as wav
import wave
import matplotlib.pyplot as plt
from pydub import AudioSegment
from pydub.utils import get_array_type
from pydub.silence import split_on_silence
import constants as c
from array import array

#A function for making sure you can find the closest value in a list
def closest_val(input_list, val):

  arr = np.asarray(input_list)

  i = (np.abs(arr - val)).argmin()

  return arr[i]

def device_identification():
    p = pyaudio.PyAudio()
    info = p.get_host_api_info_by_index(0)
    numdevices = info.get('deviceCount')

    for i in range(0, numdevices):
        if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
            print("Input Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0, i).get('name'))

#record piano sound, remove the silent parts and save the new audio
def piano_sound():
    #os.remove('/Users/emmarobinson/Downloads/piano_audio.wav') #change this according to your computer file
    #os.remove('/Users/emmarobinson/Downloads/piano_audio_new.wav')   #change this according to your computer file      

    p = pyaudio.PyAudio()

    # stream object to get data from microphone
    stream = p.open(
        format = c.FORMAT,
        channels = c.CHANNELS,
        rate = c.RATE,
        input_device_index = 1, #change this according to your mic port
        input=True,
        output=True,
        frames_per_buffer = c.CHUNK
    )
    frames = []
    print("* recording")


    while True:
        
        data = stream.read(c.CHUNK, exception_on_overflow = False)
        data_chunk = array('h',data)
        vol = max(data_chunk)
        if vol >= 400:
            print("* recording")
            for i in range(0, int(c.RATE / c.CHUNK * c.RECORD_SECONDS)):
                stream.write(data, c.CHUNK)
                frames.append(data)
            break

        else:
            print("* waiting")

    print("* done")

    stream.stop_stream()
    stream.close()

    p.terminate()
    file_path='D:\\Users\\Documents\\Connor\\piano_audio.wav' #change this according to your computer file
    file_name = file_path.split('\\')[-1]
    wf = wave.open(file_path, "wb")
    # set the channels
    wf.setnchannels(c.CHANNELS)
    # set the sample format
    wf.setsampwidth(p.get_sample_size(c.FORMAT))
    # set the sample rate
    wf.setframerate(c.RATE)
    # write the frames as bytes
    wf.writeframes(b"".join(frames))
    # close the file
    wf.close()

    sound = AudioSegment.from_file(file_path, format = 'wav') 
    audio_chunks = split_on_silence(sound
                                ,min_silence_len = 100
                                ,silence_thresh = -45
                                ,keep_silence = 50
                            )

    # Putting the file back together
    combined = AudioSegment.empty()
    for chunk in audio_chunks:
        combined += chunk
    combined.export(f'D:\\Users\\Documents\\Connor\\piano_audio_new.wav', format = 'wav') #change this according to your computer file

def get_bits():
    rate, data = wav.read('D:\\Users\\Documents\\Connor\\piano_audio.wav') #change this according to your computer file
    audio_segment = AudioSegment.from_file('D:\\Users\\Documents\\Connor\\piano_audio.wav') #change this according to your computer file

    duration = len(audio_segment)/1000

    # calculate the length of our chunk in the np.array using sample rate       samples/s * s = samples
    chunk = int(rate * duration)

    # number of bits in the audio data to decode
    bits = int(len(data) / chunk)
    return bits

#get the frequency of the piano note played
def get_freq(bit):

    #get information about the audio file
    rate, data = wav.read('D:\\Users\\Documents\\Connor\\piano_audio.wav') #change this according to your computer file
    audio_segment = AudioSegment.from_file('D:\\Users\\Documents\\Connor\\piano_audio.wav') #change this according to your computer file

    duration = len(audio_segment)/1000

    # calculate the length of our chunk in the np.array using sample rate       samples/s * s = samples
    chunk = int(rate * duration)
    
    # start position of the current bit
    strt = (chunk * bit) 
    
    # remove the delimiting 1600hz tone
    end = (strt + chunk) 
   
    # slice the array for each bit
    sliced = data[strt:end]

    w = np.fft.fft(sliced)
    plt.figure(1)
    plt.title("Signal Wave...")
    plt.plot(w)
    plt.show(block=False)
    w = np.absolute(w)
    plt.figure(2)
    plt.title("Signal Wave...")
    plt.plot(w)
    plt.show(block=False)
    freqs = np.fft.fftfreq(len(w))

    plt.figure(3)
    plt.title("Signal Wave...")
    plt.plot(freqs)
    plt.show(block=False)

    # Find the peak in the coefficients
    #Change w to be half of the index that it usually is to only get the left half of the freq spectrum
    idx = np.argmax(np.abs(w))
    print("idx: ", idx)
    freq = freqs[idx]
    print("freq: ", freq)
    freq_in_hertz = abs(freq * rate)
    print("freq in hertz: ", freq_in_hertz)
    return freq_in_hertz

#decoded_freqs = [get_freq(bit) for bit in range(bits)]

#check with the closest_val function to see what the frequency of the played note is
# for i in range(len(decoded_freqs)):
#     note=closest_val(note_freqs,decoded_freqs[i])
#     index = note_freqs.index(note)
#     played_note=keys[index]

# x=0
# if played_note==c_major_scale[x]:
#     print("yay")