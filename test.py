from gtts import gTTS

def speak_text(text):
    try:
        tts = gTTS(text)
        tts.save('output.mp3')
        print("Audio saved successfully.")
    except Exception as e:
        print("Error:", e)

# Example usage:
text_to_speak = "Hello, world!"
speak_text(text_to_speak)
