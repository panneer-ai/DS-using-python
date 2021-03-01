# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 12:07:48 2020

@author: SANGAR LOCAL
"""

import speech_recognition as sr

listener = sr.Recognizer()

try:
    with sr.Microphone as source:
        print("listenining....")
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if "alexa" in command:
            print(command)


except:
  with sr.Microphone as source:
        print("listenining....")
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if "alexa" in command:
            print(command)