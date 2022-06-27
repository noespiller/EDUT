import streamlit as st
import tools
import layouts

def app():
    global exercises_complete
    exercises_complete = [False, False, False]
    global progress
    st.title('Praxis - print()')
    st.subheader("")
    progress = st.progress(0)
    
    aufgabe_erste_schritte(0)
    aufgabe_text(1)
    aufgabe_eine_zahl(2)
    

def aufgabe_erste_schritte(index):
    title = "Erste Schritte"
    code = layouts.aufgabe_layout(title, "Gib irgendetwas mit der print Funktion in der Konsole aus.")
    
    def evaluate(co, out):
        return len(out) > 2
    
    correct_answer = tools.evaluate_code(title, code, evaluate)
    
    if correct_answer:
        exercises_complete[index] = True
        progress.progress(sum(exercises_complete)/len(exercises_complete))
    
    
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

def aufgabe_eine_zahl(index):
    title = "100"
    code = layouts.aufgabe_layout(title, "Gib die Zahl 100 in der Konsole aus. Benutze keine Anführungszeichen!")
    
    def evaluate(co, out):
        no_single_quotes =  co.count("\'") == 0
        no_double_quotes = co.count("\"") == 0
        return len(out) > 2 and no_single_quotes and no_double_quotes  and "print(100)" in co
    
    correct_answer = tools.evaluate_code(title, code, evaluate)
    
    if correct_answer:
        exercises_complete[index] = True
        progress.progress(sum(exercises_complete)/len(exercises_complete))

def aufgabe_text(index):
    title = "Text"
    code = layouts.aufgabe_layout(title, "Gib den Satz \"Herzlich Willkommen zum Kurs!\" in der Konsole aus.")
    
    def evaluate(co, out):
        return "Herzlich Willkommen zum Kurs!" in co
    
    correct_answer = tools.evaluate_code(title, code, evaluate)
    
    if correct_answer:
        exercises_complete[index] = True
        progress.progress(sum(exercises_complete)/len(exercises_complete))