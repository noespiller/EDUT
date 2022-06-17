import streamlit as st
import tools
import layouts

def app():
    global exercises_complete
    exercises_complete = [False, False]
    global progress
    st.title("Aufgaben")
    st.subheader("")
    progress = st.progress(0)
    
    aufgabe_mein_name(0)
    aufgabe_mein_name_und_alter(1)
    

def aufgabe_mein_name(index):
    title = "Mein Name"
    aufgabenbeschreibung = "Lege eine Variable mit dem Namen *\"meinName\"* an und speichere darin deinen Namen. Gib dann den Satz *\"Hallo, ich heiße <name>.\"* in der Konsole aus. Benutze die Variable *\"meinName\"*, um die Ausgabe zu machen."
    code = layouts.aufgabe_layout(title, aufgabenbeschreibung)
    
    def evaluate_code(co, out):
        return ("meinName" in code.split("\n")[-1])
    
    correct_answer = tools.evaluate_code(title, code, evaluate_code)
    
    if correct_answer:
        exercises_complete[index] = True
        progress.progress(sum(exercises_complete)/len(exercises_complete))
                
def aufgabe_mein_name_und_alter(index):
    title = "Mein Name und Alter"
    aufgabenbeschreibung = "Erweitere die Aufgabe von oben und lege noch eine Variable *\"meinAlter\"* an. Gib dann den Satz *\"Hallo, ich heiße <name> und bin <alter> Jahre alt.\"* in der Konsole aus. Benutze die Variablen *\"meinName\"* und *\"meinAlter\"*, um die Ausgabe zu machen."
    code = layouts.aufgabe_layout("Mein Name und Alter", aufgabenbeschreibung)
    
    def evaluate_code(co, out):
        return "meinName" in code.split("\n")[-1] and "meinAlter" in code.split("\n")[-1]
    
    correct_answer = tools.evaluate_code(title, code, evaluate_code)
    
    if correct_answer:
        exercises_complete[index] = True
        progress.progress(sum(exercises_complete)/len(exercises_complete))
    