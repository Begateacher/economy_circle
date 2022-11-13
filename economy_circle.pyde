 #mehrere Pfeile werden aus dem Zusatz geladen
from mehrere_pfeile import arrow

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
    #Position der Bilder und Grösse der Bilder 
    image(img1, 50,300,240,220)
    image(img2, 650, 320,240,220)
    
    arrow(180,150)
  
    
    #Titel Wirtschaftskreislauf
    xPos = 40
    yPos = 70
    textSize(60)
    fill(0,26,100)
    text("Wirtschaftskreislauf", xPos,yPos)
    textAlign(LEFT)
    
    
    #Legende Wirtschaftskreislauf
    yPos = 700
    textSize(30)
    fill(255,250,8)
    text("Gueterstrom", xPos,yPos)
    textAlign(LEFT)

    fill(0,255,10)
    text("Geldstrom", xPos+250,yPos)    
    
    fill(0,102,204)
    text("Produzenten", xPos+480,yPos)    
    
    fill(255,0,0)
    text("Konsumenten", xPos+740,yPos)
    
    fill(0,0,0)
    text("klicke auf einen der Begriffe!",xPos+20,yPos+100)

      
    



    
