from elevenlabs.client import ElevenLabs
from elevenlabs import play
from config.settings import ELEVENLABS_KEY

client = ElevenLabs(api_key=ELEVENLABS_KEY)


def speak(text: str):
    print(f"🔊 FRIDAY: {text}")
    audio = client.generate(text=text, voice="Rachel", model="eleven_monolingual_v1")
    play(audio)
