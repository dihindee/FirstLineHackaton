# запускать так python3 ./tts.py input output

from gtts import gTTS
from pathlib import Path
import sys

#print("src file: " + sys.argv[1])
#print("dest file: "+ sys.argv[2])
print("asdasdfasf");
txt = ''
for i in range(1, len(sys.argv)-1):
    txt+=sys.argv[i]+' '
tts = gTTS(text=txt,lang='ru')
tts.save(sys.argv[len(sys.argv)-1])
