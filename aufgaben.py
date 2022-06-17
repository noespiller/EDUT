import streamlit as st
import subprocess
import tools
import os
from streamlit_ace import st_ace
import global_constants





def set_file_path(path):
    global file_path
    file_path = path

def run():
    command = f'python {file_path}'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    return output, error

def app():
    print("aufgaben.app()")
    st.title('Aufgaben')
    st.write('In diesem Bereich kannst du Aufgaben zu den verschiedenen Themengebieten lösen, die in den Theorievideos behandelt werden.')
    #st.write('Willkommen zu den Aufgaben')
    #st.write("Themenfelder")
    
    # Navigation zu den bestimmten Themenfeldern
    #st.button("print()", on_click=set_exercise, disabled=False)
    #placeholder.empty()


def aufgabe_TODO():    
    #code = st.text_area('Text to analyze',"print()")
    #st.code("print('hi')", language="python")
    st.write("Lege eine Variable mit dem Namen *\"meinName\"* an und speichere darin deinen Namen. Gib dann den Satz *\"Hallo, ich heiße <name>.\"* in der Konsole aus. Benutze die Variable *\"meinName\"*, um die Ausgabe zu machen.")
    code = st_ace(placeholder="Schreibe hier deinen Code", language="python")
    

    output = ""
    error = ""
    
    if code:
        with open(global_constants.file_path, 'w') as file:
            #code = code + '\nprint("Alder Ja!!!!!!!!!!111!!1!111!!1elf!!1")'
            file.write(code)
            print(code)
            set_file_path(global_constants.file_path)
            
        output,error = run()

        runs = tools.handle_code_output(output, error)
        
        if runs:
            if("meinName" in code.split("\n")[-1]):
                st.success("Richtig!")
                st.balloons()
            else:
                st.error("Falsch")
                
    
    
    
    
    