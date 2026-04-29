**Voice Assistant (Python)** 


A simple voice-activated assistant built with Python that can respond to spoken commands in English. It recognizes speech, speaks back responses, tells the time/date, and performs Google searches.

**Features**


Speech Recognition — Listens to your voice using the microphone
Text-to-Speech — Responds out loud using `pyttsx3`
 Current Time & Date — Tells you the current time or date on command
 Google Search — Opens a browser and searches Google for your query
 English Responses — Replies in a English

**Requirements :-**

 
Python 3.7+
A working microphone

**Install all required packages with:-**


```bash
pip install SpeechRecognition pyttsx3
```

You may also need `PyAudio` for microphone access:
```bash
pip install pyaudio


**Project Structure:-**

voice-assistant/
│
├── voice.py       # Main assistant script
└── README.md      # Project documentation

**How to Run:-**


bash
python voice.py

**Supported Commands:-**

`hello` :-	Greets you in English
`time` :-	Tells the current time
`date` :-	Tells today's date
`search` :-	Asks what to search, then opens Google
`exit`:-	Exits the assistant

**Example Interaction:-**

Listening...
You said: hello
Assistant: Hello! How are you?

Listening...
You said: what is the time
Assistant: Current time  14:35:22

Listening...
You said: search
Assistant: What to Search?
Listening...
You said: python tutorials
[Opens browser: google.com/search?q=python+tutorials]

**Known Limitations :-**

Requires an active internet connection for Google Speech Recognition
Speech recognition accuracy may vary with background noise
Currently supports a fixed set of commands (no NLP/AI integration)

**Future Improvements :-**


Add more commands (weather, jokes, Wikipedia lookup, etc.)
Integrate an AI/LLM for open-ended conversations
Support offline speech recognition (e.g., Vosk or Whisper)
Add a GUI interface

License :-
This project is open-source and free to use for personal and educational purposes.
