import os
import speech_recognition as sr
from pydub import AudioSegment
from pydub.utils import make_chunks
import warnings
from langdetect import detect


warnings.filterwarnings("ignore")
def process_audio(filename):
    myaudio = AudioSegment.from_wav(filename)
    chunks_length_ms = 8000
    chunks = make_chunks(myaudio, chunks_length_ms)
    
    for i, chunk in enumerate(chunks):
        chunkName = './chunked/' + filename + "_{0}.wav".format(i)
        print('Đang xuất file: ', chunkName)
        chunk.export(chunkName, format="wav")
        file = chunkName
        r = sr.Recognizer()

        with sr.AudioFile(file) as source:
            audio_listened = r.listen(source)
            recognized_text = r.recognize_google(audio_listened, show_all=True)
        
        try:
            if recognized_text:
                recognized_text = recognized_text['alternative'][0]['transcript']
                detected_lang = detect(recognized_text)
                if detected_lang == 'vi':
                    language = 'vi'
                else:
                    language = 'en-US'
                rec = recognized_text

                # Lưu tệp văn bản với tên chứa mã ngôn ngữ
                text_file_name = f"./output_{language}.txt"
                with open(text_file_name, "a", encoding="utf-8") as txtf:
                    txtf.write(rec + ".\n")
                    
            else:
                print("Không thể nhận dạng âm thanh")
        except sr.UnknownValueError:
            print("Không thể nhận dạng âm thanh")
        except sr.RequestError as e:
            print("Không thể kết nối đến API, hãy kiểm tra kết nối internet")

try:
    os.makedirs("chunked")
except:
    pass
process_audio("english.wav")
