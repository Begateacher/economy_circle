#benoetigte Formen zeichnen

#Pfeile
def arrow(xPos, yPos, richtung):
    noStroke()
    rect(xPos,yPos,680,20)
    if richtung == 0 : 
        triangle(xPos, yPos-20, xPos, yPos+40, xPos-50,yPos+10)
    elif richtung == 1 :
        triangle(xPos+680, yPos-20, xPos+680,yPos+40, xPos+730,yPos+10) 

#Rahmen fuer die beiden Bilder
def rahmen(xPos, yPos):
    strokeWeight(3)
    noFill()
    rect(xPos, yPos, 260, 260)
