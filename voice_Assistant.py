import pyttsx3 as py  #text to speech
import speech_recognition as sr #speech recognization
import webbrowser as wb #this is useful for searching on web
import datetime as dt #it gives time or date
import pyjokes #it gives jokes
import os 

#speech to text
def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        recognizer.adjust_for_ambient_noise(source) #recognizer inputs to microphone
        audio = recognizer.listen(source) #recording the audio 
        try:
            print("recognizing...")
            data = (recognizer.recognize_google(audio)).lower() #recognizing the audio by google in lowercase and convert to text
            # print(data)
            return data
        except sr.UnknownValueError:
            print("Not Understand ")

#text to speech
def txtspeech(x):
    engine = py.init() #output unit speaker
    voices = engine.getProperty('voices') # two voices
    engine.setProperty('voice',voices[1].id)     #put only voice because we have two default voices male for 0 and female for 1,choose the female voice
    rate = engine.getProperty('rate') #speech voice speed 
    engine.setProperty('rate',150) #set the speech voice speech
    engine.say(x)   #to get voice speech
    engine.runAndWait()


if __name__ == '__main__': 
    data1 = sptext()
while True:
    if "your name" in data1:
        name = "my name is siri" 
        txtspeech(name)
    elif "old are you" in data1:
        age = "I am two year old"
        txtspeech(age)
    elif "now time" in data1:
        time = dt.datetime.now().strftime("%I%M%p")
        txtspeech(time)
    elif "youtube" in data1:
        wb.open("https://www.youtube.com/")
    elif "joke" in data1:
        joke_1 = pyjokes.get_joke(language="en",category="neutral")
        txtspeech(joke_1)
    elif "play song" in data1:
        add = "D:/Downloads/utube"
        listsong = os.listdir(add)
        print(listsong)
        os.startfile(os.path.join(add,listsong[0]))

    elif "exit" in data1:
        txtspeech("thank you")
        break


