#!/usr/bin/python
'''
Created on May 6, 2014

@author: jonathan
'''
import wave
import pyaudio

class Play(object):
    '''
    this is a class with functions to play audio files both in real time as well
    as sound is input
    '''

    def __init__(self):
        '''
        Constructor
        '''
    
def play_file(path_to_file):
    '''
    plays a file at the path given
    '''
    CHUNK = 1024
    p = pyaudio.PyAudio()
    wf = wave.open(path_to_file, 'rb')
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)
    data = wf.readframes(CHUNK)
    while data != '':
        stream.write(data)
        data = wf.readframes(CHUNK)
    stream.stop_stream()
    stream.close()
    p.terminate
    
def listen(path_to_file, time):
    '''
    listens to the mic for a specified time
    '''
    CHUNK = 1024
    p = pyaudio.PyAudio()
    wf = wave.open(path_to_file, 'w')
    #stream = 
    #data =
    p.terminate