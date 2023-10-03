input_audio_file = "D:/tool/ngoloi.mp3"

import os

file_path = "D:/tool/ngoloi.mp3"
if os.path.exists(file_path):
    print("File exists.")
else:
    print("File not found.")
