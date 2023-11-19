import speech_recognition as sr


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something! or 'STOP'")
        audio = r.listen(source)
        print("..")

    try:
        # Recognize speech using Google Web Speech API
        text = r.recognize_google(audio)
        print("\nYou: {}".format(text))
        return text
    except sr.UnknownValueError:
        print("Couldn't understand")
        return listen()
    except sr.RequestError as e:
        print("RequestError: {0}".format(e))
        return "stop"

