import speech_recognition as sr

r= sr.Recognizer()
harvard=sr.AudioFile('/home/sangeetha/Downloads/out1-[AudioTrimmer.com].wav')
with harvard as source:
    audio=r.record(source)
print(r.recognize_google(audio))