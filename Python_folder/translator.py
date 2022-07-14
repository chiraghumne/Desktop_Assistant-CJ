from time import sleep
from googletrans import Translator
from gtts import gTTS
import googletrans
import pyttsx3
import speech_recognition as sr
from playsound import playsound
import time
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    #it takes microphon input from the user and returns string output
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

def translategl(query):
    speak("Sure Sir")
    print(googletrans.LANGUAGES)
    translator = Translator()
    speak("Choose the language in which you want to translate")
    lan = input("Language: ")
    text_to_translate = translator.translate(query,src="auto",dest= lan,)
    text = text_to_translate.text

    try:
        speakgl = gTTS(text=text,lang=lan,slow=False)
        speakgl.save("voice.mp3")
        playsound("voice.mp3")

        time.sleep(5)
        os.remove("voice.mp3")
    except:
        print("Unable to translate")