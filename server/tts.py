# запускать так python3 ./tts.py input output

from gtts import gTTS
from pathlib import Path
import sys

#print("src file: " + sys.argv[1])
#print("dest file: "+ sys.argv[2])
tts = gTTS(text=sys.argv[1],lang='ru')
tts.save(sys.argv[2])
