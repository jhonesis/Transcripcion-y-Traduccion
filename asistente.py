# install first -- pip install SpeechRecognition -- pip install googletrans==3.1.0a0

import speech_recognition as sr
from googletrans import Translator

# Create an instance of the Recognizer class
recognizer = sr.Recognizer()

# Read the audio file
with sr.AudioFile('audio.flac') as source:
    audio = recognizer.record(source)

# Use the Google Speech Recognition model to recognize the audio
texto = recognizer.recognize_google(audio, language='en-US')

translator = Translator()

texto_traducido = translator.translate(texto, src='en', dest='es').text

print(texto_traducido)

with open('texto_traducido.txt', 'w') as f:
  f.write(texto_traducido)
