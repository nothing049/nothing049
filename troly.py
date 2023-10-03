import pyttsx3
import datetime
from datetime import date
import speech_recognition as sr
import webbrowser as wb
import openai
import os
support = pyttsx3.init()
voice = support.getProperty('voices')
support.setProperty('voice', voice[1].id)

def speak(audio):
    print('support :' + audio)
    support.say(audio)
    support.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I: %M : %p")
    speak(Time)

def welcome():
    hour = datetime.datetime.now().hour
    if 6 <= hour < 12:
        speak("Good morning sir")
    elif 12 <= hour < 18:
        speak("Good Afternoon sir")
    elif 18 <= hour < 24:
        speak("Good Night sir")
    speak("How can I help you?")

def command():
    c = sr.Recognizer()
    with sr.Microphone() as source:
        c.pause_threshold = 2
        audio = c.listen(source)
    try:
        query = c.recognize_google(audio, language='en')
        print("Huy: " + query)
        return query.lower()
    except sr.UnknownValueError:
        print("Please repeat or type")
        query = str(input('Your order is: '))
        return query.lower()

if __name__ == "__main__":
    welcome()
    while True:
        query = command()
        if "google" in query:
            speak("What should I search for on Google?")
            search = command()
            url = f"https://www.google.com/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on Google.')
        elif "youtube" in query:
            speak("What should I search for on YouTube?")
            search = command()
            url = f"https://www.youtube.com/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on YouTube.')
        elif "facebook" in query:
            speak("Opening Facebook")
            url = f"https://www.facebook.com/"
            wb.get().open(url)
        elif "instagram" in query:
            speak("Opening Instagram")
            url = f"https://www.instagram.com/"
            wb.get().open(url)
        elif "zalo" in query:
            speak("Opening Zalo")
            url = f"https://chat.zalo.me/"
            wb.get().open(url)
        elif "time" in query:
            time()
        elif "quit" in query:
            speak("Support is quitting, sir. Goodbye")
            quit()
        elif "hello" in query:
            speak("Hello!")
        elif "weather" in query:
            speak("It's good")
        elif "thank" in query:
            speak("You're welcome")
        elif "how are you" in query:
            speak("I'm just a computer program, but I'm doing well. How can I assist you?")
        elif "what's your name" in query:
            speak("I don't have a name, but you can call me Support.")
        else:
            speak("I'm sorry, I didn't catch that. Please say it again.")
