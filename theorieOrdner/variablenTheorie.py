import os
import layouts


def app():
    video_path = os.path.join(".", "media", "videos", "Datentypen.mp4")
    cheat_sheet_path = os.path.join(".", "media", "cheatsheets", "Datentypen.png")
    layouts.theorie_layout("Theorie - Datentypen", video_path, cheat_sheet_path)