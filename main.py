from agents.gemini import GeminiAgent
from datetime import datetime
from elevenlabs.client import ElevenLabs
from elevenlabs import play
from config.settings import ELEVENLABS_KEY

# Initialize client
client = ElevenLabs(api_key=ELEVENLABS_KEY)


def speak(text):
    try:
        print("🔊 Speaking...")

        audio = client.text_to_speech.convert(
            text=text,
            voice_id="21m00Tcm4TlvDq8ikWAM",  # Rachel voice
            model_id="eleven_monolingual_v1",
        )

        play(audio)

    except Exception as e:
        print("TTS Error:", e)


def main():
    agent = GeminiAgent()

    print("FRIDAY: FRIDAY is now online")
    speak("Friday is now online")

    while True:
        query = input("You: ")

        if query.lower() in ["exit", "quit", "bye", "shutdown"]:
            response = "Shutting down. Goodbye."
            print("FRIDAY:", response)
            speak(response)
            break

        # 🕒 Handle time locally
        if "time" in query.lower():
            now = datetime.now().strftime("%I:%M %p")
            response = f"The current time is {now}"
        else:
            response = agent.respond(query)

        print("FRIDAY:", response)
        speak(response)


if __name__ == "__main__":
    main()
