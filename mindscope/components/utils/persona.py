import json
import os


def from_json(path: str):
    if os.path.exists(path):
        with open(path, "r") as f:
            persona = json.load(f)
        return persona
    else:
        raise FileNotFoundError("No file found at given path")
