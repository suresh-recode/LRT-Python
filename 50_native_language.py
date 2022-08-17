import speech_recognition as sr
r = sr.Recognizer()
print("Listening....")
with sr.Microphone() as source:
    audio_text = r.listen(source)
    try:
        print("Text: " + r.recognize_google(audio_text, language="ta-IN"))
    except:
        print("Sorry, I did not get that")