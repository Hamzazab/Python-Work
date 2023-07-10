from email.mime import audio
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5') #builtin voices
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning sir!.How are you?')
    elif hour>=12 and hour<18:
        speak('Good Afternoon sir!.How are you?')
    else:
        speak('Good Evening sir!.How are you?')
        
    speak('I am your assistant Sir! How may i help you?') 
    
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening......')
        r.pause_threshold = 1             # seconds of non-speaking audio before a phrase is considered complete
        audio = r.listen(source)
        
    try:
        print('Recognizing......')
        query = r.recognize_google(audio , language='en-in')
        print(f'User said: {query}\n')
    
    except Exception as e:
        print('Say that again please......')
        return 'None'
    return query

if __name__ == '__main__':
    wishme()
    while True:
        query = takecommand().lower()
        
        if 'wikipedia' in query:
            speak('Searching Wikipedia......')
            query = query.replace('wikipedia', '')
            result = wikipedia.summary(query, sentences=2)
            speak('According to wikipedia')
            print(result)
            speak(result)
        
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
            
        elif 'open news' in query:
            webbrowser.open('https://www.youtube.com/watch?v=38IEolI8f-w')
            
        elif 'open google' in query:
            webbrowser.open('google.com')
        
        elif 'open stack overflow' in query:
            webbrowser.open('stackoverflow.com')
        
        elif 'open wikipedia' in query:
            webbrowser.open('wikipedia.com')
            
        elif 'play music' in query:
            music_dir = 'F:\\Music'
            songs = os.listdir(music_dir)
            #print(songs)
            os.startfile(os.path.join(music_dir,songs[3]))
        
        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'Sir, the time is {strtime}')
            
        elif 'open code' in query:
            codepath = '"C:\\Users\\Hamza\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"'
            os.startfile(codepath)
        
        elif 'ok close' in query:
            speak('exit,Thank You!!!')
            break