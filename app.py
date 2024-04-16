# flask code 
from flask import *
from openai import OpenAI
import openai
import speech_recognition as sr
import pyttsx3

def fun():
    openai.api_key = "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"
    response = openai.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=f"find a english word and its meaning ,only the word and its meaning ,in every refresh provide new word with example sentance and the origin of the word and maintain saperate lines for word,origin,example and meaning",
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text

def listen_for_speech():
    r = sr.Recognizer()
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

def grammer_corrected(text):

    openai.api_key = "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"

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

def grammer_better(text):
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

    return result.choices[0].text




def language_selected(language, text):
    openai.api_key = "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"
    language  = user_input
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
 
 
    # Extract the translated text from the response
    translated_text = response.choices[0].text.strip()  # Add this line for debugging
    return translated_text


def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dailyhunt')
def dailyhunt():
    k=fun()
    return render_template('dailyhunt.html',ans=k)

@app.route('/grammer')
def grammer():
    return render_template('grammer.html')

@app.route('/translate')
def translate():
    return render_template('translate.html')

@app.route('/grammer_correct', methods=['POST'])
def grammer_correct():
    user_input = listen_for_speech()
    if user_input:
        a=grammer_corrected(user_input)
        b=grammer_better(user_input)
        return render_template('grammer.html',a=a,b=b)
    return "Mic Not Working"

@app.route('/translator', methods=['POST'])
def translator():
    speak_text('Speak which language you need')
    language_select = listen_for_speech()
    speak_text('Speak what you need to translate')
    
    if language_select:
        speak_text('Please speak the text you want to translate')
        user_input_text = listen_for_speech()


        translated_text = language_selected(language_select, user_input_text)
        return render_template('translate.html', x=translated_text)
    else:
        return "Please select a language."



if __name__ == '__main__':
    app.run(debug=True)
    
