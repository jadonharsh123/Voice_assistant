import speech_recognition as sr
import pyttsx3

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said.")
        return None
    except sr.RequestError:
        print("Sorry, there was an error connecting to the Google API.")
        return None

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def main():
    speak("Hello! How can I assist you today?")
    
    while True:
        command = listen()

        if command is not None:
            if "hello" in command.lower():
                speak("Hello! How can I assist you today?")
            elif "goodbye" in command.lower() or "exit" in command.lower():
                speak("Goodbye! Have a great day!")
                break
            else:
                speak("Sorry, I don't understand that command. Could you please repeat?")

if __name__ == "__main__":
    main()

