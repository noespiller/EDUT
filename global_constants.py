import os

THEMEN = {
    1: ""
    }

AUFGABE_KEY = "Aufgabe: "

UNCHANGEABLE_SESSION_STATE_KEYS = ["init", "authentication_status", "username", "name", "logout", "output", "errors"]



file_path = os.path.join(".", "temp")
os.makedirs(file_path, exist_ok=True)
file_path = os.path.join(file_path, "Code_Buffer.py")