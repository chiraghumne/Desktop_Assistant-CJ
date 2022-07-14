from datetime import datetime
from fileinput import filename
from os import startfile
from pyautogui import click
from keyboard import press
from keyboard import press_and_release
from keyboard import write
from time import sleep
import pyttsx3
import speech_recognition as sr
import webbrowser as web
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again Please...")
        return "None"
    return query

def autoChrome(command):
    
    query = str(command)
    query = query.replace("chrome ","")

    if 'new tab' in query:
        press_and_release('ctrl + t')

    elif 'close tab' in query:
        press_and_release('ctrl + w')

    elif 'new window' in query:
        press_and_release('ctrl + n')

    elif 'history' in query:
        press_and_release('ctrl + h')

    elif 'download' in query:
        press_and_release('ctrl + j')

    elif 'bookmark' in query:
        press_and_release('ctrl + d')
        press('enter')

    elif 'incognito mode' in query:
        press_and_release('ctrl + Shift + n')

    elif 'switch tab' in query:
        speak("To which Tab Sir?")
        tab = takeCommand()
        Tab = int(tab)

        if '1' in Tab:
            press_and_release('ctrl + 1')

        if '2' in Tab:
            press_and_release('ctrl + 2')

        if '3' in Tab:
            press_and_release('ctrl + 3')

        if '4' in Tab:
            press_and_release('ctrl + 4')

        if '5' in Tab:
            press_and_release('ctrl + 5')

def notePad():
    speak("What should I note, Sir. I am ready to make a note of it.")

    writes = takeCommand()

    time = datetime.now().strftime("%H:%M")

    filename = str(time).replace(":","-") + "-note.txt" 

    with open(filename,"w") as file:
        file.write(writes)

    path1 = "C:\\Python\\Project\\Python_folder\\" + str(filename)

    path2 = "C:\\Python\\Project\\Database\\Notepad" + str(filename)

    os.rename(path1,path2)
    os.startfile(path2)
