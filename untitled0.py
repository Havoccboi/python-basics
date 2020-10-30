# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 14:39:41 2020

@author: Havoc
"""

import pyttsx3
engine = pyttsx3.init()
string = input()
engine.say(string)
engine.runAndWait()