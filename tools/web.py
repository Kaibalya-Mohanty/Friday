from tavily import TavilyClient
from config.settings import TAVILY_KEY
import webbrowser
import urllib.parse
import subprocess

tavily = TavilyClient(api_key=TAVILY_KEY)


def search_web(query: str) -> str:
    """Actually searches the web and returns results — no browser needed."""
    try:
        results = tavily.search(query=query, max_results=3)
        summaries = [r["content"] for r in results["results"]]
        return " ".join(summaries[:2])  # return top 2 results
    except Exception as e:
        return f"Search failed: {e}"


def search_google(query: str) -> str:
    """Opens Google in browser as fallback."""
    encoded = urllib.parse.quote(query)
    webbrowser.open(f"https://www.google.com/search?q={encoded}")
    return f"Searching Google for: {query}"


def open_youtube(query: str) -> str:
    encoded = urllib.parse.quote(query)
    webbrowser.open(f"https://www.youtube.com/results?search_query={encoded}")
    return f"Opening YouTube for: {query}"


def handle_open_command(query: str) -> str:
    query_lower = query.lower()
    app_map = {
        "notepad": "notepad",
        "calculator": "calc",
        "file explorer": "explorer",
        "task manager": "taskmgr",
        "github": lambda: webbrowser.open("https://github.com"),
        "youtube": lambda: webbrowser.open("https://youtube.com"),
        "google": lambda: webbrowser.open("https://google.com"),
        "spotify": lambda: webbrowser.open("https://open.spotify.com"),
        "gmail": lambda: webbrowser.open("https://mail.google.com"),
        "linkedin": lambda: webbrowser.open("https://linkedin.com"),
    }
    for keyword, action in app_map.items():
        if keyword in query_lower:
            if callable(action):
                action()
            else:
                subprocess.Popen(action)
            return f"Opening {keyword}."
    return "I couldn't find that app."
