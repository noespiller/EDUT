import streamlit as st
import layouts
import os

def app():
    st.title('Theorie - print()')
    video_path = os.path.join(".", "media", "videos", "print().mp4")
    cheat_sheet_path = None
    layouts.theorie_layout("print()", video_path, cheat_sheet_path)