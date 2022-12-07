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
     
def draw():
    background(155, 150, 150)
    
    #tt Variable, Titel Wirtschaftskreislauf wird geladen und gesetzt
    xPos = 500
    yPos = 70
    textSize(60)
    fill(0,0,0)
    textAlign(CENTER)
    text(tt, xPos,yPos)
    
    fill(0,26,100)
    textSize(25)
    text("Gesamter Wirtschaftskreislauf", xPos, yPos+ 330)
    
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
    text("Klicke auf einen der Begriffe!",xPos+50,yPos-590)
 
    #Position der Bilder und Grösse der Bilder 
    image(img1, 60, 250, 240, 220)
    image(img2, 700, 270, 240, 220)   
# --------------------
    
    #Interaktionsmöglichkeiten
    
    #Maustaste drücken, Pfeile und Definitionstext Güterstrom erscheinen und bleiben bis zum nächsten Klick
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
            
    #Maustaste drücken, Pfeile und Definitionstext Geldstrom erscheinen und bleiben bis zum nächsten Klick
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
            
                    
    # Maustaste drücken, Rahmen und Definitionstext Produzent erscheinen und bleiben bis zum nächsten Klick
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
           
    
    # Maustaste drücken, Definitionstext Konsument erscheint und bleiben bis zum nächsten Klick
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
         
        
    if value == 5:
        #Farbe
        fill(255, 250, 8)
        
        #Pfeile
        arrow_right(90, 540)    
        arrow_left(140, 170)
        
        #Farbe
        fill(0, 255, 10)
        
        #Pfeile
        arrow_right(90, 120)    
        arrow_left(140, 590)
        
        #Rahmen
        stroke(0,102,204)
        strokeWeight(3)
        rahmen(50,230)
        
        #Rahmen
        stroke(255,0,0)
        strokeWeight(3)
        rahmen(690,230)
    
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

    elif value == 0 and mouseX > 300 and mouseX < 700 and mouseY > 375 and mouseY < 400:
        value = 5
        
    else:
        value = 0

        



    
