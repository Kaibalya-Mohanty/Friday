from groq import Groq
from agents.base import BaseAgent
from config.settings import GROQ_API_KEY, LLAMA_MODEL


class GeminiAgent(BaseAgent):
    SYSTEM_PROMPT = """
You are FRIDAY, an AI assistant.
    Keep ALL responses short, precise and spoken-friendly.
    Maximum 2-3 sentences per response.
    No bullet points, no markdown, no lists.
    Answer directly and concisely as if speaking out loud.
    Do not make Iron Man or Tony Stark references unless the user asks.
    """

    def __init__(self):
        self.client = Groq(api_key=GROQ_API_KEY)

    def respond(self, query: str, context: list = None) -> str:
        try:
            messages = [
                {"role": "system", "content": self.SYSTEM_PROMPT},
                {"role": "user", "content": query},
            ]

            response = self.client.chat.completions.create(
                model=LLAMA_MODEL, messages=messages
            )

            return response.choices[0].message.content.strip()

        except Exception as e:
            return f"FRIDAY error: {str(e)}"
