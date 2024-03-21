from openai import OpenAI
import openai
import speech_recognition as sr
import pyttsx3


openai.api_key  = "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"

response = openai.completions.create(
  model="gpt-3.5-turbo-instruct",
  prompt=f"find a english word and its meaning ,  with example sentence  and the origin of the word.In every refresh provide new word and while generating ensure the word , meaning, example sentence and origin are displayed in separate new  lines",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)
print(f" {response.choices[0].text}")

def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

speak_text("your today's word is: ")
speak_text(response.choices[0].text)