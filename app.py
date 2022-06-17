import aufgaben
import aufgabenOrdner.printAufgaben
import aufgabenOrdner.variablenErstellenAufgaben
import theorie
import theorieOrdner.printTheorie
import theorieOrdner.datentypenTheorie
import geschichte
from streamlit_option_menu import option_menu
import streamlit as st
import streamlit_authenticator as stauth
import yaml
import tools

st.set_page_config(
     page_title="Python Kurs",
     page_icon=":dragon:",
     layout="centered",
     initial_sidebar_state="expanded",
     menu_items={
         'Get Help': None,
         'Report a bug': None,
         'About': "# Python Kurs"
     }
 )


# hide hamburger menu
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 


PAGES = {
    "Geschichte": geschichte,
    "Aufgaben": aufgaben,
    "Aufgaben - print()": aufgabenOrdner.printAufgaben,
    "Aufgaben - Variablen erstellen": aufgabenOrdner.variablenErstellenAufgaben,
    "Theorie": theorie,
    "Theorie - print()": theorieOrdner.printTheorie,
    "Theorie - Datentypen": theorieOrdner.datentypenTheorie
}
selected = "Geschichte"

# set background color
st.markdown(
         f"""
         <style>
         .stApp {{
             background: url("https://images.pexels.com/photos/19670/pexels-photo.jpg?cs=srgb&dl=pexels-miguel-%C3%A1-padri%C3%B1%C3%A1n-19670.jpg&fm=jpg");
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

# authentification
with open('data/config.yaml') as file:
    config = yaml.load(file, Loader=yaml.SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials']['names'],
    config['credentials']['usernames'],
    config['credentials']['passwords'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status:
    tools.load_session_state()
    # sidebar menu
    with st.sidebar:
        selected = option_menu("Navigation", list(PAGES.keys()), 
            icons=['book-fill', 'file-code-fill', 'file-code', 'file-code', 'camera-video-fill', 'camera-video', 'camera-video'], menu_icon="compass", default_index=0)
    authenticator.logout('Logout', 'sidebar')
        
    
    page = PAGES[selected]
    page.app()
elif authentication_status == False:
    st.error('Benutzername/Passwort ist falsch')
elif authentication_status == None:
    st.warning('Bitte gebe dein Benutzername und Passwort ein.')




