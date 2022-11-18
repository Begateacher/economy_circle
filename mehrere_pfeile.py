#benoetigte Formen zeichnen

#zeichnet Pfeile von links nach rechts
def arrow_right(xPos, yPos): 
    noStroke()
    rect(xPos,yPos,780,20)
    triangle(xPos+780, yPos-20, xPos+780,yPos+40, xPos+830,yPos+10) 

#zeichnet Pfeile von rechts nach links
def arrow_left(xPos, yPos):
    noStroke()
    rect(xPos,yPos,780,20)
    triangle(xPos, yPos-20, xPos, yPos+40, xPos-50,yPos+10) 

#Rahmen für die beiden Bilder
def rahmen(xPos, yPos):
    noFill()
    rect(xPos, yPos, 260, 260)
    
    
