


import json
import os
from config import DATA_FILE

def load_habits():
    if not os.path.exists(DATA_FILE):
        return {}
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}

def save_habits(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


