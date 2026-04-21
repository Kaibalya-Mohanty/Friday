from groq import Groq
from agents.base import BaseAgent
from config.settings import GROQ_API_KEY, LLAMA_MODEL


class GeminiAgent(BaseAgent):
    SYSTEM_PROMPT = """
    You are F.R.I.D.A.Y, Tony Stark's AI assistant.
    You are smart, fast, and helpful.
    Answer clearly and naturally.
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
