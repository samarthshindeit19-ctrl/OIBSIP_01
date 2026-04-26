import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except:
        speak("Sorry, Not understand")
        return ""

def run_assistant():
    command = take_command()

    if "hello" in command:
        speak("Hello! How are you?")

    elif "time" in command:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Current time {time}")

    elif "date" in command:
        date = datetime.datetime.now().strftime("%d %B %Y")
        speak(f"todays date {date}")

    elif "search" in command:
        speak("What to search ?")
        query = take_command()
        webbrowser.open(f"https://www.google.com/search?q={query}")
        speak(f"{query} not understand")

    elif "exit" in command:
        speak("Goodbye!")
        exit()

while True:
    run_assistant()
