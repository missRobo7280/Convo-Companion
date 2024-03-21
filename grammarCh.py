#from  config import *
import openai
import speech_recognition as sr
import pyttsx3

def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Example usage:
speak_text("Hello, I am convo companion;your virtual communication pal ")


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

# Example usage:
user_input = listen_for_speech()
if user_input:
    print(f"User said: {user_input}")


openai.api_key = "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"

def solve(text):
    response = openai.completions.create(
    model="gpt-3.5-turbo-instruct",
    prompt=f"improve grammer for the text and show the mistakes and Give me only the final result in  the output\n{text}",
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    return response.choices[0].text

def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

speak_text(response.choices[0].text)

openai.api_key = "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"

result = openai.completions.create(
  model="gpt-3.5-turbo-instruct",
  prompt=f"find spelling mistakes, accuracy in percentage from the given text as json format with fields mistakes_count, mistakes_array, corrected_mistakes and accuracy of this text:\n{text}",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(result)
print(f"The grammatically correct sentence is: {result.choices[0].text}")