import speech_recognition as sr
import os
r=sr.Recognizer()
with sr.Microphone() as source:
    print("start saying")
    audio=r.listen(source)
    print("speech done")
inp=r.recognize_google(audio)
print(inp)

if ("chrome" in inp) or ("Chrome" in inp):
    print("yes")
    os.system("start chrome")
elif ("notepad" in inp) or ("Notepad" in inp):
    os.system("notepad")
elif ("opera" in inp)or ("Opera" or "Oprah" in inp):
    os.system("start opera")
elif ("firefox" in inp) or ("Firefox" in inp):
    os.system("firefox")
else:
    print("No such operation available at the moment")
