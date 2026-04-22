import asyncio
import edge_tts
import tempfile
import os
import time

VOICE = "en-GB-SoniaNeural"


async def _generate_speech(text: str, path: str):
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(path)


def speak(text: str):
    print(f"🔊 FRIDAY: {text}")
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
            temp_path = f.name
        asyncio.run(_generate_speech(text, temp_path))
        os.startfile(temp_path)
        time.sleep(4)
    except Exception as e:
        print(f"❌ TTS error: {e}")
