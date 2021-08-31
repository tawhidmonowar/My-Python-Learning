import speech_recognition as sr
import pyttsx3 as ts

listener = sr.Recognizer()
engine = ts.init()

try:
    with sr.Microphone() as source:
        print('I am Listening...')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()



except:
    engine.say('Error')
    engine.runAndWait()
