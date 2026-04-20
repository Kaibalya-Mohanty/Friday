from google import genai
from agents.base import BaseAgent
from config.settings import GEMINI_API_KEY, GEMINI_MODEL


class GeminiAgent(BaseAgent):
    """
    Handles: web search, news, real-time information, current events.
    Model: Gemini 2.0 Flash via Google AI Studio (free tier)
    """

    SYSTEM_PROMPT = """
    You are F.R.I.D.A.Y., Tony Stark's AI assistant.
    You specialize in finding current information, news, and real-time data.
    Keep responses concise and spoken-friendly. No markdown, no bullet points.
    Respond as if speaking out loud. Be informative and direct.
    """

    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)

    def respond(self, query: str, context: list = []) -> str:
        try:
            # Build conversation history as a single string for context
            context_text = ""
            if context:
                for msg in context:
                    role = "User" if msg["role"] == "user" else "FRIDAY"
                    context_text += f"{role}: {msg['content']}\n"

            # Combine system prompt + context + query
            full_prompt = f"{self.SYSTEM_PROMPT}\n\n{context_text}User: {query}"

            response = self.client.models.generate_content(
                model=GEMINI_MODEL, contents=full_prompt
            )
            return response.text

        except Exception as e:
            return f"Gemini agent error: {str(e)}"
