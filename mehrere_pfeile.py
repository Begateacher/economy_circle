#Pfeil zeichnen
def arrow(xPos, yPos): 
    
    noStroke()
    fill(0,50,150)
    
    #zeichnet pfeile von links nach rechts
    rect(xPos-100,yPos,700,20);
    triangle(xPos+600,125, yPos+700,164, xPos+600,200) 
    
    fill(0,0,0)
    #zeichnet Pfeile von rechts nach links
    rect(0+167,600,700,20);
    triangle(0+167,575, -70+167, 610, 0+167,640) 
    
  
    
