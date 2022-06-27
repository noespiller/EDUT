import streamlit as st
import tools
import layouts
import global_constants

def app():
    st.title('Geschichte - Chapter 1')
    aufgabe_erste_schritte()
    

def aufgabe_erste_schritte():
    
    title = "Chapter 1"
    
    body = '''Du spürst ein ziehen an deiner Schulter.
    \nAm Anfang versuchst du es noch zu ignorieren.
    \nVielleicht geht es ja weg und lässt dich weiterschlafen.
    \nDas schütteln wird stärker.
    \nDu gibst ein müdes und genervtes "hmmm" von dir 
    \nund versuchst zu erspähen wer oder was so dringent nach deiner Aufmerksamkeit verlangt.
    \nDeine Augen lassen sich nur langsam Öffnen. 
    \n'Haben die sich schon immer so schwer angefühlt?' 
    \ndenkst du dir, während du dich langsam aufrichtest und in die Richtung des Übeltäters schaust.
    \nObwohl deine Augen klare Struturen erkennen, kannst du niemand entdecken.
    \njedoch fällt dir jetzt auf wie dunkel es hier ist.
    \n'Hatte ich nicht auf einer Waldlichtung geschlafen?'
    \nDu spürst einen kurzen aber doch sehr schmerzahften Tritt gegen deinen Fuß.
    \n"He!", Krakelt es von unten.
    \nErschrocken schaust du in die Richtung der Stimme und kannst deinen Augen kaum trauen.
    \n"Was fällt dir ein in meinen Hort einzudringen!?!?", wütet das kleine, fremdartige Wesen. 
    \nDu schaust dich verlegen um.
    \nDabei fällt dir auf, dass der "Hort" von dem gerade noch gesrpochen wurde, sehr stark einer Zelle ähnelt.
    \nDu fängst an das Wesen, welches dich immernoch mit seinen kleinen roten Augen anfunkelt näher zu betrachten.
    \nEs scheint eine Art Schlange zu sein. 
    \nDer einzige Unterschied, es besitzt zwei kleine Flügel.
    \n"Hat man dir keine Manieren beigebracht?", knurrt es mit hochgezogener Augenbraue.
    \n"Wie lange willst du mich denn noch anstarren ohne dich vorzustellen?"'''
    
    st.markdown(body)

    audio_file = open('media/audio/chapter1.WAV', 'rb')
    audio_bytes = audio_file.read()

    st.audio(audio_bytes, format='audio/WAV')
        
    code = layouts.aufgabe_layout(title, 'Gib einen Namen zwischen die Klammern einer "print()" Funktion ein.')
    
    def evaluate(co, out):
        return len(out) > 1
    
    tools.evaluate_code(title, code, evaluate)
    
    
