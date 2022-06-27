import streamlit as st
from streamlit_ace import st_ace
import tools
import global_constants

def theorie_layout(title, video_path, cheat_sheet_path):
    st.header(title)
    st.subheader("")
    st.subheader("Video")
    st.video(video_path)
    st.subheader("")
    if cheat_sheet_path != None:
        st.subheader("Cheat Sheet")
        st.image(cheat_sheet_path)


def aufgabe_layout(title, aufgabe):
    st.subheader("")
    st.subheader(title)
    st.markdown(aufgabe)
    state_key = global_constants.AUFGABE_KEY + title
    value=""
    if state_key in st.session_state:
        value = st.session_state[state_key]
    code = st_ace(placeholder="Schreibe hier deinen Code", language="python", key=title, value=value)
    global_constants.UNCHANGEABLE_SESSION_STATE_KEYS.append(title)
    
    print(state_key)
    print("vorm Speichern des states")
    if state_key not in st.session_state:
        tools.update_session_state(state_key, "")
    print("nach dem Speichern des states")
    print(code)
    return code
