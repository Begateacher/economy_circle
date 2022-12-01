# importieren der pfeile
from mehrere_pfeile import *

#globale Vereinbarungen 
img = None
#Variable ohne Zuweisung
font = None
#Vaiable mit Zuweisung
tt ="Der Wirtschaftkreislauf"
# Variable zu den Texten
lines = ""
#Variable zur Klickfunktion
value = 0


def setup():
    global img1, img2
    size(1000,1000)
    #Bilder aus Data laden
    img1 = loadImage("industrie2.png")
    img2 = loadImage("house.png")
    font = createFont("Century Gothic",50)
    textFont(font)
    
# --------------------    
def draw():
    background(150, 155, 155)
    
    #tt Variable, Titel Wirtschaftskreislauf wird geladen und gesetzt
    xPos = 500
    yPos = 70
    textSize(60)
    fill(0,26,100)
    textAlign(CENTER)
    text(tt, xPos,yPos)


    #Legende Wirtschaftskreislauf
    xPos = 40
    yPos = 700
    textSize(30)
    textAlign(LEFT) 
    
    fill(255,250,8)
    text(u"Güterstrom", xPos, yPos)
    
    fill(0,255,10)
    text("Geldstrom", xPos+250,yPos)    
    
    fill(0,102,204)
    text("Produzenten", xPos+480,yPos)    
    
    fill(255,0,0)
    text("Konsumenten", xPos+740,yPos)
    
    fill(0,0,0)
    textSize(20)
    text("Klicke auf einen der Begriffe!",xPos,yPos-40)
 
    #Position der Bilder und Grösse der Bilder 
    image(img1, 60, 250, 240, 220)
    image(img2, 700, 270, 240, 220)   
# --------------------
    
    #Interaktionsmöglichkeiten
    
    #Maustaste drücken, Pfeile und Definitionstext Güterstrom erscheinen  
    if value == 1:
        #Farbe
        fill(255, 250, 8)
        
        #Pfeile
        arrow_right(90, 540)    
        arrow_left(140, 170)  
        
        #Definitionstextgrösse, Textposition, Text laden
        textSize(20)
              
        u = 700
        lines = loadStrings("gueter.txt")

        for line in lines:
            text(line, xPos, u+20, 950,950)
            u += 700*10
    
    #Maustaste drücken, Pfeile und Definitionstext Geldstrom erscheinen
    if value == 2:
        #Farbe
        fill(0, 255, 10)
        
        #Pfeile
        arrow_right(90, 120)    
        arrow_left(140, 590)
        
        #Definitionstext
        textSize(20)
              
        u = 700
        lines = loadStrings("geldstrom.txt")

        for line in lines:
            text(line, xPos, u+20, 950,950)
            u += 700*10
                    
    # Maustaste drücken, Rahmen und Definitionstext Produzent erscheinen
    if value == 3:
        #Rahmen
        stroke(0,102,204)
        strokeWeight(3)
        rahmen(50,230)
        
        #Definitionstext
        fill(0,102,204)
        textSize(20)
              
        u = 700
        lines = loadStrings("produzenten.txt")

        for line in lines:
            text(line, xPos, u+20, 950,950)
            u += 700*10
    
    # Maustaste drücken, Definitionstext Konsument erscheint 
    if value == 4:
        #Rahmen
        stroke(255,0,0)
        strokeWeight(3)
        rahmen(690,230)
        
        #Definitionstext
        fill(255,0,0)
        textSize(20)
              
        u = 700
        lines = loadStrings("konsumenten.txt")

        for line in lines:
            text(line, xPos, u+20, 950,950)
            u += 700*10
    
#Klickfunktion
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
        
    else:
        value = 0

        



    
