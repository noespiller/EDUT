from streamlit_player import st_player
import streamlit as st
import os
import layouts


def app():
    video_path = os.path.join(".", "..", "Datentypen_test_video.mp4")
    layouts.theorie_layout("Datentypen", video_path, "https://images.pexels.com/photos/276452/pexels-photo-276452.jpeg?cs=srgb&dl=pexels-pixabay-276452.jpg&fm=jpg")