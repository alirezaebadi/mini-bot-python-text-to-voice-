import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate',150)
engine.setProperty('volume',1)
text = 'Hello, I am a text-to-speech bot'
engine.say(text)
engine.runAndWait()
