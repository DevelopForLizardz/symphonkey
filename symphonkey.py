#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
symphonkey.py: Turn keyboard strokes into a random symphony. Goes 
really well with hackertyper.com

When script is run (with sudo), keyboard events will be hooked to a f
unction that will pick a random Hz in the range of NOTE_RANGE and play 
it for NOTE_LENGTH seconds. The length of time set for playing notes 
will influence howfast one can type without experiencing notes being 
played after one is done typing. For instance a NOTE_LENGTH of 0.5 
second will allow for a maximum of 120 notes to be played per minute 
((1 / 0.5) * 60), therefore supporting a max speed of 120 key strokes 
per minute. 

Only dependencies are the modules pysine and keyboard, which can be 
installed via pip (see https://github.com/libpd/libpd/issues/106 if 
installing on OSX). Future goal would be to make this script entirely
stand alone, to prevent bulk and also to prevent need of admin 
privileges to run keyboard.on_press
"""

import random
import pysine
import keyboard


NOTE_RANGE = range(100, 7000, 100)  # hz
NOTE_LENGTH = 0.05  # seconds


def play_note(*args, **kwargs):
    """
    Selects a random frequency out of NOTE_RANGE and plays it
    for NOTE_LENGTH seconds. Uses the module pysine.
    """

    pysine.sine(frequency=random.choice(NOTE_RANGE), duration=NOTE_LENGTH)


def main():
    """
    When executed, will bind `play_note` to all keystroke events and 
    then block forever so the binding will persist until exit. 
    Requires admin privleges for keyboard.on_press.
    """

    # add the function bind, to execute play_note whenver a key is 
    # pressed
    keyboard.on_press(play_note)

    # block until exited
    keyboard.wait()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
