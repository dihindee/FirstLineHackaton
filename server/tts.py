# запускать так python3 ./tts.py input output

from gtts import gTTS
from pathlib import Path
import sys

print("src file: " + sys.argv[1])
print("dest file: "+ sys.argv[2])
txt = Path(sys.argv[1]).read_text()
tts = gTTS(text=txt,lang='ru')
tts.save(sys.argv[2])
