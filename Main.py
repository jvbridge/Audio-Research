#!/usr/bin/python
import os
import play
import Tkinter

filename = os.getcwd() + "/piano2.wav"

play.play_file(filename)
