import pyttsx3
import speech_recognition as sr   # PyAudio

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 120)


def say(s):
    engine.say(s)
    engine.runAndWait()  # blocks


recognizer = sr.Recognizer()


def recognize(d):
    print("Listening")
    with sr.Microphone() as m:
        audio = recognizer.record(m, duration=d)  # seconds
        print("PROCESSING : Converting audio to text....")
        user_response = recognizer.recognize_google(audio, language="en-IN")
        return user_response


say('What is your name')
name = recognize(5)
say('What is your name')
age = recognize(4)
say('What is your name')
gender = recognize(20)
print(name, age, gender)