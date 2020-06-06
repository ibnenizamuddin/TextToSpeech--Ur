from gtts import gTTS
import os

text = "Maine unse kaha ki hum kal baat karenge"
lang = "ur"
speech = gTTS(text=text, lang=lang, slow=False)
speech.save("second.mp3")
