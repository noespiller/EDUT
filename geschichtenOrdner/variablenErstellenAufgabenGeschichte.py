import streamlit as st
import tools
import layouts
import global_constants

def app():
    st.title('Geschichte - Chapter 2')
    aufgabe_erste_schritte()
    

def aufgabe_erste_schritte():
    
    title = "Chapter 2"
    
    body = '''"Hmmm, ", deinenNamen," werdet ihr Zweibeiner immer so seltsam benannt?"
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
    \n"Ich nehme an ihr könnte schreiben?"
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
    