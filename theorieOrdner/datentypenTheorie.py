import os
import layouts
import streamlit as st


def app():
    st.title('Theorie - Datentypen')
    video_path = os.path.join(".", "media", "videos", "Datentypen.mp4")
    cheat_sheet_path = os.path.join(".", "media", "cheatsheets", "Datentypen.png")
    layouts.theorie_layout("Datentypen", video_path, cheat_sheet_path)