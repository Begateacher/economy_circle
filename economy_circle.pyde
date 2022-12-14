#importieren der Pfeile und Rahmen
from mehrere_pfeile import *

#Variable ohne Zuweisung
font = None
#Vaiable mit Zuweisung
tt ="Der Wirtschaftkreislauf"
#Variable zu den Texten
lines = ""
#Variable zur Klickfunktion
value = 0
#Variable für die Pfeilrichtung
richtung = None
#Variable für Textfeld
u = 720

def setup():
    global img1, img2
    size(1000,1000)
    #Bilder aus data laden
    img1 = loadImage("industrie2.png")
    img2 = loadImage("house.png")
     
def draw():
    background(255, 255, 255)
    
    # --- Titel
    #tt Variable, Titel Wirtschaftskreislauf wird geladen und gesetzt
    xPostt = 500
    yPostt = 70
    font1 = createFont("Century Gothic",60)
    textFont(font1)
    fill(0,26,100)
    textAlign(CENTER)
    text(tt, xPostt,yPostt)
    
    # --- Anweisung zum Nutzen des Programms
    fill(0,0,0)
    textSize(20)
    text(u"Klicke auf einen der fettgedruckten Begriffe!",xPostt,yPostt+40)
    
    # --- Bilder des Wirtschaftskreislaufs
    # Position der Bilder und Grösse der Bilder 
    image(img1, 60, 250, 240, 220)
    image(img2, 700, 270, 240, 220)  
    
    # --- Legende 
    # gesamter Wirtschaftskreislauf
    fill(0,26,100)
    font2 = createFont("Century Gothic Bold",25)
    textFont(font2)
    
    text("Gesamter Wirtschaftskreislauf", xPostt, yPostt+ 330)
    
    # einzelne Begriffe zum Wirtschaftskreislauf
    xPos = 40
    yPos = 700
    
    textAlign(LEFT) 
    fill(84,139,84)
    text(u"Güterstrom", xPos, yPos)
    
    fill(238,201,0)
    text("Geldstrom", xPos+250,yPos)    
    
    fill(0,102,204)
    text("Produzenten", xPos+480,yPos)    
    
    fill(139,0,0)
    text("Konsumenten", xPos+740,yPos)
    
     
# --------------------
    
    # --- Interaktionsmöglichkeiten
    
    #Mausklick auf den Begriff Güterstrom: Pfeile und Definitionstext erscheinen und bleiben bis zum nächsten Klick
    if value == 1:
        #Farbe für Pfeile und Text
        fill(84,139,84)
        
        #Pfeile
        arrow(140, 540, 1)    
        arrow(190, 170, 0)  
        
        #Definitionstext: Grösse, Textposition, Text in einem definierten Textfeld laden
        textSize(17)
              
        lines = loadStrings("gueter.txt")

        for line in lines:
            text(line, xPos, u, xPos+910, u+20)

            
    #Mausklick auf den Begriff Geldstrom: Pfeile und Definitionstext erscheinen und bleiben bis zum nächsten Klick
    if value == 2:
        #Farbe für Pfeile und Text
        fill(238,201,0)
        
        #Pfeile
        arrow(190, 120, 0)    
        arrow(140, 590, 1)
        
        #Definitionstext: Grösse, Textposition, Text in einem definierten Textfeld laden
        textSize(17)

        lines = loadStrings("geldstrom.txt")
        
        for line in lines:
            text(line, xPos, u, xPos+910, u+20)
            
                    
    # Mausklick auf den Begriff Produzent:  Rahmen und Definitionstext erscheinen und bleiben bis zum nächsten Klick
    if value == 3:
        #Rahmen für das Produzentenbild 
        stroke(0,102,204)
        rahmen(50,230)
        
        #Definitionstext: Farbe, Grösse, Textposition, Text in einem definierten Textfeld laden
        fill(0,102,204)
        textSize(17)
              
        lines = loadStrings("produzenten.txt")

        for line in lines:
            text(line, xPos, u, xPos+910, u+20)
           
    
    # Mausklick auf den Begriff Konsument: Rahmen und Definitionstext erscheinen und bleiben bis zum nächsten Klick
    if value == 4:
        #Rahmen für das Konsumentenbild
        stroke(139,0,0)
        rahmen(690,230)
        
        #Definitionstext: Grösse, Textposition, Text in einem definierten Textfeld laden
        fill(139,0,0)
        textSize(17)

        lines = loadStrings("konsumenten.txt")

        for line in lines:
            text(line, xPos, u, xPos+910, u+20)
         
     # Mausklick auf den Begriff gesamter Wirtschaftskreislauf: alle Pfeile und Rahmen werden angezeigt
    if value == 99:
        #Pfeile für den Güterstrom
        fill(84,139,84)
        arrow(140, 540, 1)    
        arrow(190, 170, 0) 
        
        #Pfeile für den Geldstrom
        fill(238,201,0)
        arrow(140, 120, 1)    
        arrow(190, 590, 0)
        
        #Rahmen für das Produzentenbild
        stroke(0,102,204)
        rahmen(50,230)
        
        #Rahmen für das Konsumentenbild
        stroke(139,0,0)
        rahmen(690,230)
    
    print(value)   #Zustandskontrolle
    
# --- Klickfunktion
# Wird in einem bestimmten Bereich (auf einen Begriff) geklickt, stellt sich das value entsprechend um und löst das Erscheinen der Texte und Bilder aus. (Zeilen 76 bis 171).
# Beim nächsten Klick (beliebiger Ort) verschwindet der Text wieder, da value nicht auf 0 ist und somit der else-Bereich der Definition aufgerufen wird, wodurch value wieder 0 ist.
# Wird zu Beginn an einen beliebigen Ort geklickt, passiert nichts, da value 0 ist und bleibt. 
def mouseClicked():
    global value
    if value == 0 and mouseX > 40 and mouseX < 200 and mouseY > 675 and mouseY < 700:
        value = 1

    elif value == 0 and mouseX > 290 and mouseX < 445 and mouseY > 675 and mouseY < 700:
        value = 2
         
    elif value == 0 and mouseX > 520 and mouseX < 705 and mouseY > 675 and mouseY < 700:
        value = 3
        
    elif value == 0 and mouseX > 780 and mouseX < 980 and mouseY > 675 and mouseY < 700:
        value = 4

    elif value == 0 and mouseX > 300 and mouseX < 700 and mouseY > 375 and mouseY < 400:
        value = 99
        
    else:
        value = 0

        



    
