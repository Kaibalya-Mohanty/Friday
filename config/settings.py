import os
from dotenv import load_dotenv

load_dotenv()

# LLM
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Speech
ASSEMBLYAI_KEY = os.getenv("ASSEMBLYAI_API_KEY")
ELEVENLABS_KEY = os.getenv("ELEVENLABS_API_KEY")

# Database
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Web search
TAVILY_KEY = os.getenv("TAVILY_API_KEY")

# Models
LLAMA_MODEL = "llama-3.3-70b-versatile"
MIXTRAL_MODEL = "mixtral-8x7b-32768"
GEMINI_MODEL = "gemini-2.0-flash"

# Wake word
WAKE_WORD_MODEL = "hey_jarvis"
WAKE_WORD_THRESHOLD = 0.5

# TTS voice (ElevenLabs)
TTS_VOICE = "Rachel"

# Dashboard
DASHBOARD_PORT = 5000

# Memory
MEMORY_CONTEXT_LIMIT = 5
