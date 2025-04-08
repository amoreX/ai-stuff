import json
import os

def save_history(chat_history, file="history.json"):
    if not os.path.exists(file):
        with open(file, "w") as f:
            json.dump([], f) 
    with open(file, "w") as f:
        json.dump(chat_history, f)

def load_history(file="history.json"):
    try:
        with open(file, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []