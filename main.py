import asyncio
import edge_tts
import tempfile
import os
import time
from datetime import datetime
from agents.groq_llama import GroqLlamaAgent
from agents.groq_mixtral import GroqMixtralAgent
from core.router import route
from tools.system import get_system_info, get_current_time
from tools.web import search_google, open_youtube, handle_open_command


# --- TTS ---
async def _generate_speech(text: str, path: str):
    communicate = edge_tts.Communicate(text, "en-GB-SoniaNeural")
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


# --- Agents ---
llama = GroqLlamaAgent()
mixtral = GroqMixtralAgent()


def get_response(query: str) -> str:
    agent_name = route(query)

    if agent_name == "system_tool":
        info = get_system_info()
        q = query.lower()
        if "time" in q or "date" in q:
            return f"The current time is {get_current_time()}"
        if "battery" in q:
            status = "charging" if info["charging"] else "not charging"
            return f"Battery is at {info['battery']} and {status}."
        if "ram" in q or "memory" in q:
            return f"RAM usage is at {info['ram_used']} out of {info['ram_total']}."
        if "cpu" in q:
            return f"CPU at {info['cpu_usage']} across {info['cpu_cores']} cores."
        return f"CPU: {info['cpu_usage']}, RAM: {info['ram_used']}, Battery: {info['battery']}."

    if agent_name == "tool":
        q = query.lower()
        if "youtube" in q:
            term = (
                q.replace("play", "")
                .replace("on youtube", "")
                .replace("youtube", "")
                .strip()
            )
            return open_youtube(term)
        if "search" in q or "google" in q:
            term = (
                q.replace("search for", "")
                .replace("search", "")
                .replace("google", "")
                .strip()
            )
            return search_google(term)
        return handle_open_command(query)

    if agent_name == "groq_llama":
        return llama.respond(query)
    else:
        return mixtral.respond(query)


# --- Main Loop ---
def main():
    print("🤖 F.R.I.D.A.Y. is online")
    speak("F.R.I.D.A.Y. is online. How can I help you?")

    while True:
        try:
            query = input("\nYou: ").strip()
        except KeyboardInterrupt:
            speak("Shutting down. Goodbye.")
            break

        if not query:
            continue

        if query.lower() in ["exit", "quit", "bye", "shutdown"]:
            speak("Shutting down. Goodbye.")
            break

        response = get_response(query)
        print(f"FRIDAY: {response}")
        speak(response)


if __name__ == "__main__":
    main()
