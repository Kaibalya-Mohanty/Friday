import asyncio
import time
from speech.wake_word import wait_for_wake_word
from speech.stt import listen_and_transcribe
from speech.tts import speak
from core.router import route
from core.memory import save_conversation, get_recent_context
from agents.groq_llama import GroqLlamaAgent
from agents.gemini import GeminiAgent
from agents.groq_mixtral import GroqMixtralAgent
from tools.system import get_system_info, get_current_time
from tools.web import search_web, search_google, open_youtube, handle_open_command


class Pipeline:
    def __init__(self):
        self.agents = {
            "groq_llama": GroqLlamaAgent(),
            "gemini": GeminiAgent(),
            "groq_mixtral": GroqMixtralAgent(),
        }
        print("✅ All agents initialized")

    async def run(self):
        speak("F.R.I.D.A.Y. is online. Say Hey Jarvis to activate.")

        while True:
            wait_for_wake_word()
            speak("Yes?")

            query = listen_and_transcribe()
            if not query:
                speak("I didn't catch that. Try again.")
                continue

            agent_name = route(query)
            print(f"🔀 Routing to: {agent_name}")
            start_time = time.time()

            if agent_name == "system_tool":
                response = self._handle_system(query)
            elif agent_name == "tool":
                response = self._handle_tool(query)
            else:
                context = get_recent_context()
                agent = self.agents[agent_name]
                response = agent.respond(query, context)

            latency = int((time.time() - start_time) * 1000)
            speak(response)
            save_conversation(query, response, agent_name, latency)

    def _handle_system(self, query: str) -> str:
        query_lower = query.lower()
        if "time" in query_lower or "date" in query_lower:
            return f"The current time is {get_current_time()}"
        info = get_system_info()
        if "battery" in query_lower:
            status = "charging" if info["charging"] else "not charging"
            return f"Battery is at {info['battery']} and {status}."
        if "ram" in query_lower or "memory" in query_lower:
            return f"RAM usage is at {info['ram_used']} out of {info['ram_total']}."
        if "cpu" in query_lower:
            return (
                f"CPU usage is at {info['cpu_usage']} across {info['cpu_cores']} cores."
            )
        if "disk" in query_lower or "storage" in query_lower:
            return f"Disk usage is at {info['disk_used']} out of {info['disk_total']}."
        return f"CPU at {info['cpu_usage']}, RAM at {info['ram_used']}, Battery at {info['battery']}."

    def _handle_tool(self, query: str) -> str:
        query_lower = query.lower()
        if "youtube" in query_lower:
            term = (
                query_lower.replace("play", "")
                .replace("on youtube", "")
                .replace("youtube", "")
                .strip()
            )
            return open_youtube(term)
        if "search" in query_lower or "google" in query_lower:
            term = (
                query_lower.replace("search for", "")
                .replace("search", "")
                .replace("google", "")
                .strip()
            )
            return search_google(term)
        if "open" in query_lower or "launch" in query_lower:
            return handle_open_command(query)
        return "I'm not sure how to handle that action."
