import requests
import pyttsx3
import speech_recognition as sr

# Text-to-speech
engine = pyttsx3.init()


def speak(text):
    print("FRIDAY:", text)
    engine.say(text)
    engine.runAndWait()


# Speech-to-text
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print("You:", command)
        return command
    except:
        return "sorry"


# Send to FastAPI backend
def send_to_friday_api(user_input):
    url = "http://127.0.0.1:8000/process"
    data = {"text": user_input}

    try:
        response = requests.post(url, json=data)

        if response.status_code == 200:
            return response.json()["response"]
        else:
            return "Error from server"
    except:
        return "Could not connect to FRIDAY backend"


# Main loop
if __name__ == "__main__":
    speak("FRIDAY is now online")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            speak("Goodbye")
            break

        response = send_to_friday_api(user_input)
        speak(response)
