import streamlit as st
import tools
import layouts
import global_constants

def app():
    st.title('Praxis - print()')
    aufgabe_erste_schritte()
    

def aufgabe_erste_schritte():
    title = "Erste Schritte"
    code = layouts.aufgabe_layout(title, "Gib irgendetwas mit der print Funktion in der Konsole aus.")
    
    def evaluate(co, out):
        return len(out) > 1
    
    tools.evaluate_code(title, code, evaluate)
    
    
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