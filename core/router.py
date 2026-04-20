CODE_KEYWORDS = [
    "code",
    "program",
    "debug",
    "error",
    "function",
    "class",
    "algorithm",
    "explain",
    "how does",
    "why does",
    "difference between",
    "what is",
    "fix",
    "bug",
    "syntax",
    "python",
    "java",
    "javascript",
]

WEB_KEYWORDS = [
    "search",
    "news",
    "latest",
    "what's happening",
    "today",
    "current",
    "recent",
    "find",
    "look up",
    "google",
    "weather",
    "price",
    "score",
    "result",
    "trending",
    "update",
]

SYSTEM_KEYWORDS = [
    "battery",
    "ram",
    "memory",
    "cpu",
    "disk",
    "storage",
    "time",
    "date",
    "system",
    "charging",
    "how's my",
    "performance",
    "how much",
    "what time",
    "what's the time",
]

TOOL_KEYWORDS = [
    "open",
    "launch",
    "start",
    "play",
    "show me",
    "go to",
    "youtube",
    "spotify",
    "browser",
    "folder",
    "file",
]


def route(query: str) -> str:
    query_lower = query.lower()

    if any(word in query_lower for word in SYSTEM_KEYWORDS):
        return "system_tool"

    if any(word in query_lower for word in TOOL_KEYWORDS):
        return "tool"

    if any(word in query_lower for word in WEB_KEYWORDS):
        return "gemini"

    if any(word in query_lower for word in CODE_KEYWORDS):
        return "groq_llama"

    return "groq_mixtral"
