from os import path
from pydub import AudioSegment
src = "input.mp3"
dst = "output.mp3"
#convert
sound= AudioSegment.from_mp3(src)
sound=export(dst, format="wav")
