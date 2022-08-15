from gtts import gTTS
from playsound import playsound

with open("data.txt", "r")  as f:
    data = f.read().replace("\n", " ")

text = gTTS(text =data,tld='co.in', lang = 'en', slow = False)
text.save("voice.mp3")
playsound("voice.mp3")
