from elevenlabs import ElevenLabs
from config.settings import ELEVENLABS_KEY
import tempfile
import os
import time
import pygame

client = ElevenLabs(api_key=ELEVENLABS_KEY)


def speak(text: str):
    print(f"🔊 FRIDAY: {text}")
    try:
        audio = client.text_to_speech.convert(
            text=text, voice_id="JBFqnCBsd6RMkjVDRZzb", model_id="eleven_turbo_v2_5"
        )

        # Save to temp file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
            for chunk in audio:
                f.write(chunk)
            temp_path = f.name

        # Play with pygame
        pygame.mixer.init()
        pygame.mixer.music.load(temp_path)
        pygame.mixer.music.play()

        # Wait for audio to finish
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)

        pygame.mixer.quit()
        os.remove(temp_path)

    except Exception as e:
        print(f"❌ TTS error: {e}")
