import streamlit as st
import tools
import layouts
import global_constants
from streamlit_ace import st_ace
import tools

def app():
    aufgabe_erste_schritte()
    

def aufgabe_erste_schritte():
    
    state_key = global_constants.AUFGABE_KEY
    code = st_ace(placeholder="Schreibe hier deinen Code", language="python", key="test")
    
    if code:
        output, error = tools.save_and_run_code(code)
        code_runs = tools.handle_code_output(output, error)
        
    
    
    """if code:
        print("input gegeben")
        output, error = tools.save_and_run_code(code)
        code_runs = tools.handle_code_output(output, error)
        
        if code_runs:
            tools.exper(code, output, evaluate_code_and_output)
            if len(output) > 1:
                st.success("Super!")
                st.balloons()
                tools.update_session_state(global_constants.AUFGABE_KEY + title, code)
            else:
                st.error("Probiere es weiter")
        else:
            st.error("Probiere es weiter")"""