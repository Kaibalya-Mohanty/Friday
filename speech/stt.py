import assemblyai as aai
from config.settings import ASSEMBLYAI_KEY

aai.settings.api_key = ASSEMBLYAI_KEY


def listen_and_transcribe() -> str:
    transcriber = aai.Transcriber()
    print("🎙️ Listening...")
    transcript = transcriber.transcribe_from_microphone()
    if transcript.status == aai.TranscriptStatus.error:
        print(f"❌ STT error: {transcript.error}")
        return ""
    print(f"📝 You said: {transcript.text}")
    return transcript.text or ""
