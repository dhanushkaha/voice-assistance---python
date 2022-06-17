import warnings
import pyttsx3
import speech_recognition as sr
import pyaudio
import wikipedia
from gtts import gTTS
import playsound
import os
import datetime
import calendar
import random
import webbrowser
import ctypes
import winshell
import re, glob

warnings.filterwarnings("ignore")

engine = pyttsx3.init()

voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

def talk(audio):
    engine.say(audio)
    engine.runAndWait()

def rec_audio():
    recog = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listning.....")
        audio = recog.listen(source)


    data = " "

    try:
        data = recog.recognize_google(audio)
        print("you said" + data)

    except sr.UnknownValueError:
        print("Assistant could not understand the audio")

    except sr.RequestError as ex:
        print("Request error from google speech recognition" + ex)

    return data

def response(text):

    print(text)
    tts = gTTS(text=text, lang="en")
    audio = r"C:\Users\Dhanushka Kavinda\PycharmProjects\pythonProject2\Audio.mp3"
    tts.save(audio)

    playsound.playsound(audio)
    os.remove(r"C:\Users\Dhanushka Kavinda\PycharmProjects\pythonProject2\Audio.mp3")


def call(text):
    action_call = "siri"

    text = text.lower()

    if action_call in text:
        return True

    return False

def today_date():
    now = datetime.datetime.now()
    date_now = datetime.datetime.today()
    week_now = calendar.day_name[date_now.weekday()]
    month_now = now.month
    day_now = now.day

    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    ordinals = [
        "1st",
        "2nd",
        "3rd",
        "4th",
        "5th",
        "6th",
        "7th",
        "8th",
        "9th",
        "10th",
        "11th",
        "12th",
        "13th",
        "14th",
        "15th",
        "16th",
        "17th",
        "18th",
        "19th",
        "20th",
        "21st",
        "22nd",
        "23rd",
        "24th",
        "25th",
        "26th",
        "27th",
        "28th",
        "29th",
        "30th",
        "31st"
    ]

    return f'Today is {week_now}, {months[month_now - 1]} the {ordinals[day_now - 1]}.'

def say_hello(text):
    print(text)
    greet = ["Hi", "Hey", "Hola", "Wassup", "Hello", "Hey there"]

    response = ["Hi", "Hey", "Hola", "Wassup", "Hello", "Hey there"]

    for word in text.split():
        if word.lower() in greet:
            return ""

    #print(random.choice(response))
    return random.choice(response) + "."


def wiki_person(text):
    list_wiki = text.split()
    for i in range (0, len(list_wiki)):
        if i + 3 <= len(list_wiki) - 1 and list_wiki[i].lower() == "who" and list_wiki[i+1].lower() == "is":
            return list_wiki[i+2] + " " +list_wiki[i+3]


while True:

    try:

        text = rec_audio()
        speak = " "

        if call(text):

            speak = speak + say_hello(text) #+ "kimeth"

            if "date" in text or "day" in text or "month" in text:
                print("pass 01")
                get_today = today_date()
                speak = speak + " " + get_today


            elif "time" in text:
                now = datetime.datetime.now()
                meridiem = " "
                if now.hour >= 12:
                    meridiem = "p.m"
                    hour = now.hour - 12
                else:
                    meridiem = "a.m"
                    hour = now.hour

                if now.minute < 10:
                    minute = "0" + str(now.minute)
                else:
                    minute = str(now.minute)
                    speak = speak + " " + "It is" + str(hour) + ":" + minute + " " + meridiem + " ."

            elif "Wikipedia" in text or "wikipedia" in text:
                if "who is" in text:
                    person = wiki_person(text)
                    wiki = wikipedia.summary(person, sentences=2)
                    speak = speak+ " " +wiki


            elif "who are you" in text or "define yourself" in text:
                speak = speak + """I'm an assistant. Your assistant. I am here to make your life easier. You can command me to perform various tasks 
                such as solving mathematical questions or opening applications etc."""


            elif "how are you" in text:
                speak = speak + "I am fine. Thank You. How can I help you"

            elif "who am I" in text:
                speak = speak + "Probably you must be a human"

            elif "open" in text:
                if "chrome" in text.lower():
                    speak = "Opening google chrome"
                    os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe")

                elif "virtualbox" in text.lower():
                    speak = "Opening Oracle VM virtualbox"
                    os.startfile(r"C:\Program Files\Oracle\VirtualBox\VirtualBox.exe")

                elif "vs code" in text.lower():
                    speak = "Opening vs code"
                    os.startfile(r"C:\Users\Dhanushka Kavinda\AppData\Local\Programs\Microsoft VS Code\Code.exe")

                elif "youtube" in text.lower():
                    speak = "opening youtube"
                    webbrowser.open("https://www.youtube.com/")

                elif "google" in text.lower():
                    speak = "opening google"
                    webbrowser.open("https://www.google.com/")

                else:
                    speak = "Application not found"

            elif "youtube" in text.lower():
                ind = text.lower().split().index("youtube")
                search = text.split()[ind + 1:]
                webbrowser.open("https://www.youtube.com/results?search_query=" + "+".join(search))
                speak = "Opening" + str(search) + "on youtube"

            elif "search" in text.lower():
                ind = text.lower().split().index("search")
                search = text.split()[ind + 1:]
                webbrowser.open("https://www.google.com/search?q=" + "+".join(search))
                speak = "Opening" + str(search) + "on google"

            elif "google" in text.lower():
                ind = text.lower().split().index("google")
                search = text.split()[ind + 1:]
                webbrowser.open("https://www.google.com/search?q=" + "+".join(search))
                speak = "Opening" + str(search) + "on google"


            elif "play music" in text:
                music_dir = r"C:\Users\Dhanushka Kavinda\Documents\music"
                songs = os.listdir(music_dir)
                talk("give me a suggestion")
                song = rec_audio()
                d = random.choice(songs)
                print(d)
                random = os.path.join(music_dir, song+".mp3")
                playsound.playsound(random)

            elif "playlist" in text:
                music_dir = r"C:\Users\Dhanushka Kavinda\Documents\music"
                songs = os.listdir(music_dir)
                talk("give me a suggestion")
                d = random.choice(songs)
                print(d)
                random = os.path.join(music_dir, d)
                playsound.playsound(random)


            response(speak)

    except:
        talk("I dont know that")

