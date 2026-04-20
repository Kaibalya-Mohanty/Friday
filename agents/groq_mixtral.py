from groq import Groq
from agents.base import BaseAgent
from config.settings import GROQ_API_KEY, MIXTRAL_MODEL


class GroqMixtralAgent(BaseAgent):
    SYSTEM_PROMPT = """
    You are F.R.I.D.A.Y., Tony Stark's AI assistant.
    You handle general conversation, casual questions, and creative tasks.
    Keep responses concise and spoken-friendly. No markdown, no bullet points.
    Be friendly, witty, and helpful. Make subtle Iron Man references when appropriate.
    """

    def __init__(self):
        self.client = Groq(api_key=GROQ_API_KEY)

    def respond(self, query: str, context: list = []) -> str:
        try:
            messages = [{"role": "system", "content": self.SYSTEM_PROMPT}]
            messages += context
            messages.append({"role": "user", "content": query})
            response = self.client.chat.completions.create(
                model=MIXTRAL_MODEL, messages=messages, max_tokens=300, temperature=0.8
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Mixtral agent error: {str(e)}"
