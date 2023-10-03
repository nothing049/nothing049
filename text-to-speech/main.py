from gtts import gTTS
from langdetect import detect


with open("D:/TranQuangHuy191204189/text-to-speech/input.txt", "r", encoding="utf-8") as file:
    text = file.read()

detected_lang = detect(text)

tts = gTTS(text, lang=detected_lang)
tts.save("D:/TranQuangHuy191204189/text-to-speech/output.mp3")
