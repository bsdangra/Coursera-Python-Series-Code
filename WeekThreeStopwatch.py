import simplegui

val = "0.00.0"
minute = 0
second = 0
milisec = 0
flag = 0
tempSec = "00"
attempts = 0
score = 0

def draw(canvas):
    canvas.draw_text(val, [130, 150], 30, "White")
    canvas.draw_text(str(score)+ "/" + str(attempts), [240, 30], 30, "Red")
def convert():
    global val, minute, second, milisec, flag, tempSec
    
    if(flag == 1):
        milisec += 1
        if(milisec > 9):
            second += 1
            milisec = 0
        if(second > 59):
            second = 0
            minute += 1
        if(second <= 9):
            tempSec = "0" + str(second)
        else:
            tempSec = str(second)
        if(val == "59.59.9"):
            minute = 0     
        
    
    val = str(minute) + "." + tempSec + "." + str(milisec)    
       
        
def start():
    global flag
    flag = 1

def stop():
    global flag, attempts, score
    flag = 0
    if(second % 5 == 0):
        attempts += 1
        score += 1
    else:
        attempts += 1

def reset():
    global flag, val, minute, second, tempSec, milisec
    val = "0.00.0"
    flag = 0
    minute = second = milisec = 0
    tempSec = "00"
        
        
frame = simplegui.create_frame("StopWatch", 300, 300)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, convert)
frame.add_button("Start", start, 50)
frame.add_button("Stop", stop, 50)
frame.add_button("Reset", reset, 50)




frame.start()
timer.start()
