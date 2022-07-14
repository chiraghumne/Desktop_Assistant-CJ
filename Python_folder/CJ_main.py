import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import winsound
import wolframalpha
import requests
import cv2

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am CJ sir. please tell me how may i help you?")

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

def  Alarm(query):
    TimeHere = open("C:\\Python\\Project\\Database\\alarm.txt","a")
    TimeHere.write(query)
    TimeHere.close()
    os.startfile("C:\\Python\\Project\\MyAlarm.py")

def wolfRam(query):
    api_key = "V5WATW-QX5R94R94P"

    requester = wolframalpha.Client(api_key)

    requested = requester.query(query)

    try:

         Answer = next(requested.results).text
         return Answer

    except:

        speak("No Data Found")

def Calculator(query):
    Term = str(query)
    Term.replace("CJ","")
    Term.replace("multiply ","*")
    Term.replace("into ","*")
    Term.replace("plus ","+")
    Term.replace("minus ","-")
    Term.replace("divide ","/")

    Final = str(Term)

    try:
        result = wolfRam(Final)
        speak(f"Your answer is{result}")
    except:
        speak("No Data Found")

def Temp(query):
    Term = str(query)
    Term.replace("CJ ","")
    Term.replace("in ","")
    Term.replace("temperature ","")
    Term.replace("What is the ","")

    temp_query = str(Term)
    
    if "outside" in temp_query:
        var1 = "temperature in Nagpur"
        answer = wolfRam(var1)
        speak(f"{var1} Is {answer} .")

    else:
        var2 = "Temperature In" + temp_query
        answ = wolfRam(var2)
        speak(f"{var2} is {answ}")

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        #logic for executing task based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results) 

        elif 'how are you' in query:
            speak("I'm great Sir, afterall you made me")

        elif 'great' in query:
            speak("Thankyou Sir!")

        elif 'who are you' in query:
            speak("I'm CJ sir, I'm a Desktop Assistant you can call me your helping hand")

        elif 'who made you' in query:
            speak("Mr. Chirag created me using Python")

        elif 'youtube' in query:
            webbrowser.open("youtube.com")

        elif 'google' in query:
            webbrowser.open("google .com")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'vs code' in query:
            vsPath = "C:\\Users\\chira\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vsPath)

        elif 'remind me that' in query:
            rememberMsg = query.replace("remind me that","")
            rememberMsg = rememberMsg.replace("CJ","")
            speak(f"You Have told me to remind that :{rememberMsg}")
            remember = open("reminder.txt","w")
            remember.write(rememberMsg)
            remember.close()

        elif 'reminder' in query:
            remember = open("reminder.txt")
            speak(f"Hello Chirag I remind you that:{remember.read()}")

        elif 'alarm' in query:
            speak("Sir please enter the time to set alarm")
            print("")
            t = input("Enter Time Example : 10 and 10 :- ")
            Alarm(t)
            speak("Done Sir")

        elif 'play music' in query:
            music_dir = 'C:\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'temperature' in query:
            Temp(query)  

        elif 'calculate' in query:
            speak("What do you want to calculate?")
            math = takeCommand()
            Calculator(math)

        elif 'chrome' in query:
            from Automation import autoChrome
            autoChrome(query)

        elif 'camera' in query:
            cam = cv2.VideoCapture(0)
            while True:
                ret, img = cam.read()
                cv2.imshow('webcam',img)
                k = cv2.waitKey(50)
                if k==27:
                    break
            cam.release()
            cv2.destroyAllWindows()

        elif 'make a note' in query:
            from Automation import notePad
            notePad()

        elif 'screenshot' in query:
            import pyautogui
            im = pyautogui.screenshot()
            im.save("ss.jpg")

        elif 'translate' in query:
            from translator import translategl
            query = query.replace("metapy ","")
            query = query.replace("translate ","")
            translategl(query)
