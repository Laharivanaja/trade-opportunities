from datetime import datetime

# In-memory session store
sessions = {}


def track_session(user_id: str):
    """
    Tracks API usage per user/session in memory.
    """
    sessions[user_id] = {
        "last_access": datetime.utcnow().isoformat()
    }
