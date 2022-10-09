img = None

def setup():
    global img1, img2
    size(1000,1000)
    #Bilder aus Data laden
    img1 = loadImage("industrie.png")
    img2 = loadImage("house.png")
        
    
def draw():
    background(0, 153, 204)
    #Position der Bilder setzen
    image(img1, 50,300)
    image(img2, 650, 250)
    drawArrow(420,420,420,420)

# Pfeilform
def drawArrow(x, y, length, width):
    beginShape()
    vertex(180,82)
    vertex(207,36)
    vertex(214,63)
    vertex(407,11)
    vertex(412,30)
    vertex(219,82)
    vertex(226,109)
    endShape(CLOSE)
    #Farbe Pfeil
    fill(238,157,13)
    
    
