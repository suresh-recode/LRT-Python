import speech_recognition as sr   # PyAudio
recognizer = sr.Recognizer()

print("Listening")
with sr.Microphone() as m:
    audio = recognizer.record(m, duration=4)  # seconds
    print("PROCESSING : Converting audio to text....")
    user_response = recognizer.recognize_google(audio, language="en-IN")
    print(user_response)