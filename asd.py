import speech_recognition as sr

r = sr.Recognizer()

def record():
    with sr.AudioFile("sample.wav") as source:
        audio = r.record(source)
        text = r.recognize_google(audio, language='ja-JP')

    return text
