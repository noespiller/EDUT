import streamlit as st
import global_constants
import subprocess
import json
import os

def session_state_to_json():
    dictionary = {}
    for key in st.session_state.keys():
        dictionary[key] = st.session_state[key]
    return dictionary

def handle_errors(error):
    #TODO height weg = 200
    st.text_area('Konsole:', error.decode("utf-8"), key='errors')
    error_code = error.decode("utf-8")
    error_line = error_code.split(" ")
    
    if('IndentationError' in error.decode("utf-8")):
        error_text = '''Ein IndentationError taucht immer dann auf, wenn Code in Python falsch eingerückt ist.
        Das heißt, dass dir in deinem Code irgendwo Leerzeichen fehlen, oder zu viele vorhanden sind.
        \nDer Fehler liegt in Zeile Nummer {} vor.'''.format(error_line[6])
        #st.write("<font color='red'>{}</font>".format(error_text), unsafe_allow_html=True)
        st.info(error_text)
        #st.warning(error_text)
        
    if('SyntaxError' in error.decode("utf-8")):
        error_text = '''Ein SyntaxError taucht meistens auf, wenn du eine Klammer vergessen hast zu öffnen oder zu schließen. Es kann aber auch sein, dass du vergessen hast, Anführungszeichen zu setzen.
        \nDer Fehler liegt in Zeile Nummer {} vor.'''.format(error_line[6])
        #st.write("<font color='red'>{}</font>".format(error_text), unsafe_allow_html=True)
        st.info(error_text)
        #st.warning(error_text)
        
    if('TypeError' in error.decode("utf-8")):
        error_text = '''Ein TypeError taucht immer dann auf, wenn ein Fehler mit Datentypen vorliegt. 
        Schaue am besten nochmal unser Video zu Datentypen an wenn du Probleme hast den Error zu finden.
        \nDer Fehler liegt in Zeile Nummer {} vor.'''.format(error_line[6])
        #st.write("<font color='red'>{}</font>".format(error_text), unsafe_allow_html=True)
        st.info(error_text)
        #st.warning(error_text)
        
    if('NameError' in error.decode("utf-8")):
        error_text = '''Ein NameError taucht immer dann auf, wenn ein eine Variable noch nicht existiert aber benutzt werden soll. 
        Schau, ob du deine Variable richtig geschrieben, und Groß- und Kleinschreibung beachtet hast.
        Wenn du das gemacht hast, kann es sein, dass du statt einer globalen Variable eine lokale Variable verwenden willst, diese aber nicht mehr existiert.
        \nDer Fehler liegt in Zeile Nummer {} vor.'''.format(error_line[10])
        #st.write("<font color='red'>{}</font>".format(error_text), unsafe_allow_html=True)
        st.info(error_text)
        #st.warning(error_text)
        
def handle_code_output(output, error):
    if(len(error) == 0):
        # TODO height weg
        st.text_area('Konsole:', output.decode('utf-8'), key='output')
        print(output.decode('utf-8'))
        return True
    else:
        handle_errors(error)
        return False

"""def set_file_path(path):
    global file_path
    file_path = path"""
    
def run():
    file_path = global_constants.file_path
    print(global_constants.file_path)
    command = f'python {file_path}'
    print(command)
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    return output, error

def save_and_run_code(code):
    with open(global_constants.file_path, 'w') as file:
        #code = code + '\nprint("Alder Ja!!!!!!!!!!111!!1!111!!1elf!!1")'
        file.write(code)
        print(code)
        
        #set_file_path(global_constants.file_path)
    output, error = run()
    print("output:", output)
    print("error:", error)
    return output, error

def load_session_state():
    file_path = "./data/" + st.session_state["username"] + ".json"
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            dictionary = json.load(f)
            for key in dictionary:
                if key not in global_constants.UNCHANGEABLE_SESSION_STATE_KEYS:
                    st.session_state[key] = dictionary[key]

def save_session_state():
    file_path = "./data/" + st.session_state["username"] + ".json"
    with open(file_path, 'w', encoding='utf-8') as f:
        dictionary = session_state_to_json()
        if len(dictionary) != 0:
            json.dump(dictionary, f)
        
def update_session_state(key, value):
    st.session_state[key] = value
    save_session_state()

def evaluate_code(title, code, eval_func):
    if code:
        print("input gegeben")
        output, error = save_and_run_code(code)
        code_runs = handle_code_output(output, error)
        
        if code_runs:
            if eval_func(code, output):
                st.success("Super!")
                #st.balloons()
                update_session_state(global_constants.AUFGABE_KEY + title, code)
                return True
            else:
                st.error("Probiere es weiter")
                return False
        else:
            st.error("Probiere es weiter")
            return False

def get_output(title, code, eval_func):
    if code:
        output, error = save_and_run_code(code)
        code_runs = False
        if(len(error) == 0):
            code_runs = True
        
        if code_runs:
            if eval_func(code, output):
                update_session_state(global_constants.AUFGABE_KEY + title, code)
                return output
            else:
                return None
        else:
            return None