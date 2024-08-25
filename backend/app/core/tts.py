# app/core/tts.py

from gtts import gTTS

def text_to_speech(text, lang="en"):
    tts = gTTS(text=text, lang=lang)
    output_file = "output.mp3"
    tts.save(output_file)
    return output_file