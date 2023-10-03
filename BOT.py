import pyttsx3
import datetime
from datetime import date
import speech_recognition as sr
import webbrowser as wb
import openai
import os
support= pyttsx3.init()
voice = support.getProperty('voices')
support.setProperty('voice',voice[1].id)
def speak(audio):
    print('support :' + audio)
    support.say(audio)
    support.runAndWait()
def time():
    Time=datetime.datetime.now().strftime("%I: %M : %p")
    speak(Time)
def welcome():
    hour = datetime.datetime.now().hour
    if hour>=6 and hour<12 :
        speak("Good morning sir")
    elif hour>=12 and hour<18 :
        speak("Good Afternoon sir")
    elif hour>=18 and hour<24:
        speak("Good Night sir")
    speak("How can i help you?")
def command():
    c = sr.Recognizer()
    with sr.Microphone() as source:
        c.pause_threshold= 2
        audio=c.listen(source)
    try:
        query = c.recognize_google(audio,language='en')
        print("Huy: "+ query)
    except sr.UnknownValueError:
        print("please repeat or typing")
        query =str(input('Your order is :'))
    return query
if __name__ == "__main__":
    welcome()
    while True:
        query = command().lower()
        if "google" in query:
            speak("What should I search ?")
            search=command().lower()
            url=f"https://www.google.com/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your{search} on google ')
        if "youtube" in query:
            speak("What should I search ?")
            search=command().lower()
            url=f"https://www.youtube.com/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your{search} on youtube ')
        if "facebook" in query:
            speak("opening Facebook")
            url=f"https://www.facebook.com/"
            wb.get().open(url)
        if "instagram" in query:
            speak("opening instagram")
            url=f"https://www.instagram.com/"
            wb.get().open(url)
        if "zalo" in query:
            speak("opening zalo")
            url=f"https://chat.zalo.me/"
            wb.get().open(url)
            
           
        elif "time " in query:
            time()
        elif "quit" in query:
            speak("support is quitting sir. Goodbye")
            quit()
        