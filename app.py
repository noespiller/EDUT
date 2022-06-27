import aufgaben
import aufgabenOrdner.printAufgaben
import aufgabenOrdner.variablenAufgaben
import aufgabenOrdner.ifAufgaben
import aufgabenOrdner.listenAufgaben
import aufgabenOrdner.schleifenAufgaben
import aufgabenOrdner.funktionenAufgaben
import theorie
import theorieOrdner.printTheorie
import theorieOrdner.datentypenTheorie
import theorieOrdner.variablenTheorie
import theorieOrdner.ifTheorie
import theorieOrdner.listenTheorie
import theorieOrdner.schleifenTheorie
import theorieOrdner.funktionenTheorie
import geschichte
import geschichtenOrdner.printAufgabenGeschichte
import geschichtenOrdner.variablenErstellenAufgabenGeschichte
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
    "Geschichte - Chapter 1": geschichtenOrdner.printAufgabenGeschichte,
    "Geschichte - Chapter 2": geschichtenOrdner.variablenErstellenAufgabenGeschichte,
    "Aufgaben": aufgaben,
    "Aufgaben - print()": aufgabenOrdner.printAufgaben,
    "Aufgaben - Variablen": aufgabenOrdner.variablenAufgaben,
    "Aufgaben - If Statement": aufgabenOrdner.ifAufgaben,
    "Aufgaben - Listen": aufgabenOrdner.listenAufgaben,
    "Aufgaben - Schleifen": aufgabenOrdner.schleifenAufgaben,
    "Aufgaben - Funktionen": aufgabenOrdner.funktionenAufgaben,
    "Theorie": theorie,
    "Theorie - print()": theorieOrdner.printTheorie,
    "Theorie - Datentypen": theorieOrdner.datentypenTheorie,
    "Theorie - Variablen": theorieOrdner.variablenTheorie,
    "Theorie - If Statement": theorieOrdner.ifTheorie,
    "Theorie - Listen": theorieOrdner.listenTheorie,
    "Theorie - Schleifen": theorieOrdner.schleifenTheorie,
    "Theorie - Funktionen": theorieOrdner.funktionenTheorie
}
selected = "Geschichte"



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
            icons=['book-fill', 'file-code-fill', 'file-code', 'file-code', 'file-code', 'file-code', 'file-code', 'file-code', 'camera-video-fill', 'camera-video', 'camera-video', 'camera-video', 'camera-video', 'camera-video', 'camera-video', 'camera-video'], menu_icon="compass", default_index=0)
    authenticator.logout('Logout', 'sidebar')
        
    
    page = PAGES[selected]
    page.app()
elif authentication_status == False:
    st.error('Benutzername/Passwort ist falsch')
elif authentication_status == None:
    st.warning('Bitte gebe dein Benutzername und Passwort ein.')





