 #Pfeile werden aus dem Zusatz geladen
from mehrere_pfeile import arrow_right
from mehrere_pfeile import arrow_left
from mehrere_pfeile import rahmen

img = None

def setup():
    global img1, img2
    global font
    size(1000,1000)
    #Bilder aus Data laden
    img1 = loadImage("industrie2.png")
    img2 = loadImage("house.png")
    font = createFont("Century Gothic",50)
    textFont(font)
    
        
def draw():
    background(155, 155, 155)
    
    #Titel Wirtschaftskreislauf
    xPos = 500
    yPos = 70
    textSize(60)
    fill(0,26,100)
    textAlign(CENTER)
    text("Wirtschaftskreislauf", xPos,yPos)


    #Legende Wirtschaftskreislauf
    xPos = 40
    yPos = 700
    textSize(30)
    textAlign(LEFT) 
    
    fill(255,250,8)
    text("Gueterstrom", xPos, yPos)
    
    fill(0,255,10)
    text("Geldstrom", xPos+250,yPos)    
    
    fill(0,102,204)
    text("Produzenten", xPos+480,yPos)    
    
    fill(255,0,0)
    text("Konsumenten", xPos+740,yPos)
    
    fill(0,0,0)
    text("klicke auf einen der Begriffe!",xPos+20,yPos+100)
        
    
    #Position der Bilder und Grösse der Bilder 
    image(img1, 60, 250, 240, 220)
    image(img2, 700, 270, 240, 220)
    
    #Rahmen für die Bilder
    stroke(0,102,204)
    rahmen(50,230)
    
    stroke(255,0,0)
    rahmen(690,230)
    
    
    #Pfeile für den Güterstrom in gelb
    fill(255, 250, 8)
    arrow_right(90, 540)    
    arrow_left(140, 170)
    
    #Pfeile für den Geldstrom in grün
    fill(0, 255, 10)
    arrow_right(90, 120)    
    arrow_left(140, 590)
    
    
   

      
    



    
