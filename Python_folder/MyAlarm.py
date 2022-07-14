import os
import datetime
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

extracted_time = open("C:\\Python\\Project\\Database\\alarm.txt","rt")
time = extracted_time.read()
Time = str(time)
extracted_time.close()

delete_time = open("C:\\Python\\Project\\Database\\alarm.txt","r+")
delete_time.truncate(0)
delete_time.close()

def RingerNow(time):
    time_to_set = str(time)
    time_now = time_to_set.replace("CJ","")
    time_now = time_now.replace("set alarm for ","")
    time_now = time_now.replace("set ","")
    time_now = time_now.replace("alarm ","")
    time_now = time_now.replace("for ","") 
    time_now = time_now.replace(" and ",":")

    Alarm_Time = str(time_now)
    print(Alarm_Time)
    while True:

        current_time = datetime.datetime.now().strftime("%H:%M")

        if current_time == Alarm_Time:
            print("Time is Over Sir, Let's get back to work")
            ring_dir = 'C:\\Python\\Project\\Audio\\alarm.mp3'
            os.startfile(ring_dir)

        elif current_time>Alarm_Time:
            exit()
        
RingerNow(time)