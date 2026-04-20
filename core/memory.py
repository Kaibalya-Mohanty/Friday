from supabase import create_client
from config.settings import SUPABASE_URL, SUPABASE_KEY, MEMORY_CONTEXT_LIMIT

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


def save_conversation(query: str, response: str, agent: str, latency_ms: int):
    try:
        supabase.table("conversations").insert(
            {
                "user_query": query,
                "response": response,
                "agent_used": agent,
                "latency_ms": latency_ms,
            }
        ).execute()
    except Exception as e:
        print(f"⚠️ Could not save to Supabase: {e}")


def get_recent_context() -> list:
    try:
        result = (
            supabase.table("conversations")
            .select("user_query, response")
            .order("created_at", desc=True)
            .limit(MEMORY_CONTEXT_LIMIT)
            .execute()
        )

        messages = []
        for row in reversed(result.data):
            messages.append({"role": "user", "content": row["user_query"]})
            messages.append({"role": "assistant", "content": row["response"]})
        return messages
    except Exception as e:
        print(f"⚠️ Could not fetch context: {e}")
        return []


def get_all_conversations() -> list:
    try:
        result = (
            supabase.table("conversations")
            .select("*")
            .order("created_at", desc=True)
            .limit(50)
            .execute()
        )
        return result.data
    except Exception as e:
        print(f"⚠️ Could not fetch conversations: {e}")
        return []
