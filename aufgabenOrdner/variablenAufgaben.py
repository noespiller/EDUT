import streamlit as st
import tools
import layouts

def app():
    global exercises_complete
    exercises_complete = [False, False]
    global progress
    
    st.header("")
    st.title("Praxis - Variablen")
    st.subheader("")
    progress = st.progress(0)
    
    st.header("")
    st.header("Variablen erstellen")
    aufgabe_mein_name(0)
    aufgabe_mein_name_und_alter(1)
    
    st.header("")
    st.header("Arithmetische Operatoren")
    aufgabe_plus(2)
    aufgabe_variablen_addieren(3)


def aufgabe_variablen_addieren(index):
    title = "Variablen addieren"
    aufgabenbeschreibung = "Lege eine Variable mit dem Namen *\"meineZahl1\"* an und weise ihr die Zahl 2039 zu. Lege eine weitere Variable *\"meineZahl2\"* an mit dem Wert 6933,9. Denk an die Besonderheit der floats! Gib die Summe der Variable anschließend in der Konsole aus (rechne es nicht selbst aus, lass Python die Arbeit machen)."
    code = layouts.aufgabe_layout(title, aufgabenbeschreibung)
    
    def evaluate_code(co, out):
        return "meineZahl1" in co and "8972.9" in out and "meineZahl2" in co and not "print(8972.9)" in co.split("\n")[-1]
    
    correct_answer = tools.evaluate_code(title, code, evaluate_code)
    
    if correct_answer:
        exercises_complete[index] = True
        progress.progress(sum(exercises_complete)/len(exercises_complete))
 

def aufgabe_plus(index):
    title = "+"
    aufgabenbeschreibung = "Lege eine Variable mit dem Namen *\"plus\"* an und weise ihr \"5 + 6\" zu. Gib die Variable anschließend in der Konsole aus."
    code = layouts.aufgabe_layout(title, aufgabenbeschreibung)
    
    def evaluate_code(co, out):
        return "plus" in co and "11" in out and "plus" in co.split("\n")[-1]
    
    correct_answer = tools.evaluate_code(title, code, evaluate_code)
    
    if correct_answer:
        exercises_complete[index] = True
        progress.progress(sum(exercises_complete)/len(exercises_complete))
     

def aufgabe_mein_name(index):
    title = "Mein Name"
    aufgabenbeschreibung = "Lege eine Variable mit dem Namen *\"meinName\"* an und speichere darin deinen Namen. Gib dann den Satz *\"Hallo, ich heiße <name>.\"* in der Konsole aus. Benutze die Variable *\"meinName\"*, um die Ausgabe zu machen."
    code = layouts.aufgabe_layout(title, aufgabenbeschreibung)
    
    def evaluate_code(co, out):
        return ("meinName" in co.split("\n")[-1])
    
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
    