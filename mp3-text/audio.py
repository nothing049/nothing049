import os
import speech_recognition as sr
from pydub import AudioSegment

def convert_to_wav(input_audio_file, output_wav_file):
    audio = AudioSegment.from_mp3(input_audio_file)
    audio.export(output_wav_file, format="wav")

def recognize_language(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
    
    try:
        recognized_text = recognizer.recognize_google(audio, language="vi-VN")  # Change to your desired language code
        return recognized_text
    except sr.UnknownValueError:
        print("Could not understand the audio.")
        return None
    except sr.RequestError as e:
        print(f"Error making the request: {e}")
        return None

def main():
    input_audio_file = "D:/voice/mp3-text/ngoloi.mp3"
    output_wav_file = "D:/voice/mp3-text/ngoloi.wav"
    output_text_file = "D:/voice/mp3-text/ngoloi.txt"
    
    # Convert mp3 to wav
    convert_to_wav(input_audio_file, output_wav_file)
    
    # Recognize the language and get the recognized text
    recognized_text = recognize_language(output_wav_file)
    if recognized_text:
        print("Recognized Text:")
        print(recognized_text)
        
        # Export recognized text to a text file
        with open(output_text_file, "w", encoding="utf-8") as file:
            file.write(recognized_text)
        print(f"Text exported to '{output_text_file}'.")

    # Remove the temporary WAV file
    os.remove(output_wav_file)

if __name__ == "__main__":
    main()
