# backend/services/graph_store.py

import json
import os
from datetime import datetime
import time

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
STORE_PATH = os.path.join(DATA_DIR, "agent_memory.json")

# Ensure directory exists
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

def _load_store():
    if not os.path.exists(STORE_PATH):
        return []
    try:
        with open(STORE_PATH, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def _save_store(events):
    with open(STORE_PATH, "w") as f:
        json.dump(events, f, indent=2)

def save_event(agent_name: str, event_type: str, payload: dict, success=True, chain:list=None, duration:float=None):
    """
    Saves execution context of AI agent decisions.
    Includes: success flag, chain, execution time
    """
    events = _load_store()
    
    events.append({
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "agent": agent_name,
        "event": event_type,
        "chain": chain if chain else [],
        "success": success,
        "execution_time_ms": round(duration * 1000, 2) if duration else None,
        "payload": payload
    })

    _save_store(events)

def get_recent_events(limit: int = 10):
    events = _load_store()
    return events[-limit:]

def get_events_by_agent(agent_name: str):
    events = _load_store()
    return [e for e in events if e["agent"] == agent_name]

def clear_memory():
    """
    Reset the AI agent memory store
    """
    _save_store([])
    return {"status": "CLEARED", "message": "Agent memory wiped successfully"}
