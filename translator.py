#from  config import *
import openai
import speech_recognition as sr
import pyttsx3

def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Example usage:

speak_text("which language you want to translate?")

r = sr.Recognizer()

def listen_for_speech():
    with sr.Microphone() as source:
        print("Listening for speech...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        return text.lower()
    except sr.UnknownValueError:
        print("Could not understand audio")
        return None

language_select = listen_for_speech()
if language_select:
    print(f"User said: {language_select}")

    
speak_text("so you want to translate")

speak_text(language_select)

speak_text("say what you want to translate:")




user_input = listen_for_speech()
if user_input:
    print(f"User said: {user_input}")
    
    
openai.api_key = "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"


language  = language_select
text = user_input
response = openai.completions.create(
  model="gpt-3.5-turbo-instruct",
  prompt=f"translate {language} in english and Give me only the final result in  the output\n{text}",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)
print(f"The grammatically correct sentence is: {response.choices[0].text}")

def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

speak_text(response.choices[0].text)