import streamlit as st
import tools
import layouts
import global_constants

def app():
    st.title('Geschichte')
    erstes_kapitel()
    

def erstes_kapitel():
    
    st.header('Chapter 1')
    
    title = "Aufgabe - Chapter 1"
    
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
    
    correct_answer = tools.evaluate_code(title, code, evaluate)
    output = tools.get_output(title, code, evaluate)
    
    if correct_answer:
        name = str(output).replace('\\n\'', '').replace('\\r', '').replace('b\'', '')
        #name = str(output)
        zweites_kapitel(name)
        
    

def zweites_kapitel(name):
    
    st.title('')
    
    st.header('Chapter 2')
    
    title = "Aufgabe - Chapter 2"
    
    body = '''"Hmmm, ''' + str(name) + ''', werdet ihr Zweibeiner immer so seltsam benannt?"
    \n"Ich trage im übrigen den schönsten Namen westlich der grünen Lande, Pythonia."
    \nAls du gerade einen Kommentar über den Namen der geflügelten Schlange machen willst, hörst du sich nähernde Schritte.
    \nDein Kopf dreht sich zur Seite, doch ein nervöses zischen lässt dich wieder zu Pythonia sehen.
    \n"Oh nein, eine Wache. Schnell heb dein Gewand an, damit ich mich verstecken kann!"
    \nBevor du überhaupt reagieren kannst, huscht Pythonia über dein Hosenbein unter dein Hemd und windet sich elegant um deinen Arm. 
    \nNur ihre zwei roten Augen lugen noch verstohlen hervor.
    \n"Wenn die mich finden, werden sie garantiert versuchen die Lage meiner Schätze aus mir herauszukitzeln."
    \nDie Schritte kommen näher. 
    \nEin kleiner Lichtpunkt am Ende des Tunnels ist nun zu sehen.
    \nDu scheinst dich in einer Art Höhle zu befinden.
    \nDie Gitter, welche dir den Weg zu dem Tunnel versperren sind aus Metall und werden von einem Schloss im Riegel gehalten.
    \nDie Schritte werden lauter und langsam erkennt man eine Figur die eine Lampe trägt.
    \nSie sieht aus, wie ein normaler, hochgewachsener Mensch, doch ihre Ohren sind etwas länger und spitzer.
    \n"Ah, ist das Dornröschen endlich erwacht?", hörst du es ironisch durch den Gang hallen.
    \n"Wir haben dich dabei erwischt wie du in unser Teritorium eingedrungen bist."
    \nDer Wächter läuft vor die Gitter und bleibt nur eine handlänge vor dir stehen.
    \nEr wirft dir durch die Eisenstäbe ein Blatt und ein paar Kohlestifte zu.
    \n"Ich nehme an, Ihr könnt schreiben?"
    \nDu nickst.
    \n"Schreibt auf dieses Blatt euren Namen, Berufung und Alter.
    \nIch werde dann sehen ob wir euch direkt hinrichten oder ihr noch gebraucht werden könnt."'''
    
    st.markdown(body)

    audio_file = open('media/audio/chapter2.WAV', 'rb')
    audio_bytes = audio_file.read()

    st.audio(audio_bytes, format='audio/WAV')
        
    code = layouts.aufgabe_layout(title, 'Übergebe deinen Namen der Variablen "Blatt".')
    
    def evaluate(co, out):
        return len(out) > 1
    
    tools.evaluate_code(title, code, evaluate)