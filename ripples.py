import simplegui

canvasWidth = 300
canvasHeight = 300
circleposOne = [0,0] 

radiusCircleOne = 15
radiusCircleTwo = 20
radiusCircleThree = 25
radiusCircleFour = 30

def draw(canvas):
    if(circleposOne[0] > 0):
        canvas.draw_circle(circleposOne, radiusCircleOne, 1, "Red")
        canvas.draw_circle(circleposOne, radiusCircleTwo, 1, "Red")
        canvas.draw_circle(circleposOne, radiusCircleThree, 1, "Red")
        canvas.draw_circle(circleposOne, radiusCircleFour, 1, "Red")
    if(radiusCircleOne > canvasWidth/2):
        circleposOne[0] = 0
        
    
    
def tick():
    global radiusCircleOne, radiusCircleTwo, radiusCircleThree, radiusCircleFour
    radiusCircleOne += 10
    radiusCircleTwo += 10
    radiusCircleThree += 10
    radiusCircleFour += 10
    
def mouseClk(pos):
    global circleposOne, radiusCircleOne, radiusCircleTwo, radiusCircleThree, radiusCircleFour
    radiusCircleOne = 15
    radiusCircleTwo = 20
    radiusCircleThree = 25
    radiusCircleFour = 30
    
    circleposOne = list(pos)
    timer.start()
    
    
frame = simplegui.create_frame("Ripples", 300, 300)
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(mouseClk)

timer = simplegui.create_timer(200, tick)

frame.start()
