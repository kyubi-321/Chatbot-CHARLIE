import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import sys
from PIL import Image


engine = pyttsx3.init(driverName='sapi5',debug=False)
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


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

    speak("I am Aakash badhaani  Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-IN')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")  
        return "None"
    return query



if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

         #Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        
        elif  'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'please stop' in query:
            speak("I will stop now O K , Bye Bye see you next time.")
            sys.exit()  

        elif 'fool' in query:
            speak("you are fool also.")

        elif 'are you' in query:
            speak("I am Ankit Badhani Chatbot  And my name is Aakash Badhaani. And Ankit Badhani created me.")

        elif 'car' in query:
            speak("my   favourite  car  is  the Volks wagen ,B M W")
           # img=Image.open("C:\\Users\\ACER\Downloads\\ABT Amps Up Volkswagen's Touareg TDI SUV _ Man of Many.jpg")
           # img.show()  

        elif 'favourite song' in query:
            speak('My favourite song is Blue eyes by Honey singh')      

        else:
            speak("Can you say that again please.")    

        

        
            