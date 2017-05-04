import simplegui
import random

canvasWidth = 600
canvasHeight = 400
ballpos = [canvasWidth/2, canvasHeight/2]
ballradius = 25
ballvel = [0, 0]
paddlepos1 = canvasHeight/2.5
paddlepos2 = canvasHeight/2.5
paddleHeight = 80
paddlevel = [0, 0]
gudderWidth = 8
scorePlyOne  = 0
scorePlyTwo = 0

def draw(canvas):
    global paddlepos1, paddlepos2, scorePlyOne, scorePlyTwo
    
    canvas.draw_line([8, 0], [8, canvasHeight], 1, "White")
    canvas.draw_line([canvasWidth/2, 0], [canvasWidth/2, canvasHeight], 1, "White")
    canvas.draw_line([canvasWidth - gudderWidth, 0], [canvasWidth - gudderWidth, canvasHeight], 1, "White")    
    
    ballpos[0] += ballvel[0]
    ballpos[1] += ballvel[1]
    
    canvas.draw_circle(ballpos, ballradius, 2, "Red", "White")
        
    if(ballpos[0] <= ballradius + gudderWidth or ballpos[0] >= canvasWidth - ballradius - gudderWidth):         
        ballvel[0] = -ballvel[0]
        if(not(ballpos[1] >= paddlepos1 and ballpos[1] <= paddlepos1 + paddleHeight) and
              ballpos[0] <= ballradius + gudderWidth):
            scorePlyTwo += 1
            newgame()
        if(not(ballpos[1] >= paddlepos2 and ballpos[1] <= paddlepos2 + paddleHeight) and
          ballpos[0] >= canvasWidth - ballradius - gudderWidth):            
            scorePlyOne += 1
            newgame()            
                      
        
    if(ballpos[1] <= ballradius or ballpos[1] >= canvasHeight - ballradius):                     
        ballvel[1] = -ballvel[1]
    
    paddlepos1 += paddlevel[0]
    paddlepos2 += paddlevel[1]
    
    if(paddlepos1 <= 0): paddlepos1 = 0.5
    if(paddlepos1 + paddleHeight >= canvasHeight): paddlepos1 = canvasHeight - paddleHeight - 0.5
    
    if(paddlepos2 <= 0): paddlepos2 = 0.5
    if(paddlepos2 + paddleHeight >= canvasHeight): paddlepos2 = canvasHeight - paddleHeight - 0.5
                            
    canvas.draw_polygon([(0, paddlepos1), (gudderWidth, paddlepos1),
                        (gudderWidth, paddlepos1 + paddleHeight), 
                        (0, paddlepos1 + paddleHeight)], 1, "White", "White" )
    canvas.draw_polygon([(canvasWidth - gudderWidth, paddlepos2), 
                        (canvasWidth, paddlepos2), 
                        (canvasWidth, paddlepos2 + paddleHeight),
                        (canvasWidth - gudderWidth, paddlepos2 + paddleHeight)], 1, "White", "White")    
    #score       
    canvas.draw_text(str(scorePlyOne), [canvasWidth/2 - 80, 70], 38, "White")
    canvas.draw_text(str(scorePlyTwo), [canvasWidth/2 + 70, 70], 38, "White")
    
    if(ballvel[0] >= 0 and not ballpos[0] == canvasWidth/2):
        ballvel[0] += 0.001       
    elif(not ballpos[0] == canvasWidth/2):
        ballvel[0] += 0.001
        
    
             
def keyDown(key):    
    if(key == simplegui.KEY_MAP["w"]): paddlevel[0] -= 2
    if(key == simplegui.KEY_MAP["s"]): paddlevel[0] += 2
    if(key == simplegui.KEY_MAP["up"]): paddlevel[1] -= 2
    if(key == simplegui.KEY_MAP["down"]): paddlevel[1] += 2
        
def keyUp(key):
    if(key == simplegui.KEY_MAP["w"]): paddlevel[0] = 0
    if(key == simplegui.KEY_MAP["s"]): paddlevel[0] = 0
    if(key == simplegui.KEY_MAP["up"]): paddlevel[1] = 0
    if(key == simplegui.KEY_MAP["down"]): paddlevel[1] = 0
        
def newgame():    
    global canvasWidth, canvasHeight, ballpos, ballradius, ballvel, paddlepos1, paddlepos2, paddleHeight, paddleve
    global gudderWidth, scorePlyOne, scorePlyTwo
    canvasWidth = 600
    canvasHeight = 400
    ballpos = [canvasWidth/2, canvasHeight/2]	
    ballradius = 25    
    paddlepos1 = canvasHeight/2.5
    paddlepos2 = canvasHeight/2.5
    paddleHeight = 80
    paddlevel = [0, 0]
    gudderWidth = 8
    
    if(random.randrange(0,2) == 0):
        ballvel[0] = 2.5
        ballvel[1] = -0.9
        print "0"
    else:
        ballvel[0] = -2.5
        ballvel[1] = -0.9
        print "1"
    
def startGame():
    global scorePlyOne, scorePlyTwo
    newgame()    
    scorePlyOne = 0
    scorePlyTwo = 0
        
frame = simplegui.create_frame("Pong", canvasWidth, canvasHeight)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keyDown)
frame.set_keyup_handler(keyUp)
frame.add_button("Start", startGame, 50)


frame.start()