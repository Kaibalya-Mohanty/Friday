import speech_recognition as sr

recognizer = sr.Recognizer()


def listen_and_transcribe() -> str:
    print("🎙️ Listening... (speak now)")
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            print("⚙️ Transcribing...")
            text = recognizer.recognize_google(audio)
            print(f"📝 You said: {text}")
            return text
        except sr.WaitTimeoutError:
            print("⏱️ No speech detected.")
            return ""
        except sr.UnknownValueError:
            print("❓ Could not understand.")
            return ""
        except Exception as e:
            print(f"❌ STT error: {e}")
            return ""
