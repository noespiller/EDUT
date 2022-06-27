import os
import layouts
import streamlit as st


def app():
    st.title('Theorie - Variablen')
    video_path = os.path.join(".", "media", "videos", "Variablen_erstellen.mp4")
    cheat_sheet_path = os.path.join(".", "media", "cheatsheets", "Variablen_erstellen.png")
    layouts.theorie_layout("Variablen erstellen", video_path, cheat_sheet_path)