import simplegui
import random


secret_guess = 0
attempts = 0

def range100():
    global secret_guess, attempts
    secret_guess = random.randrange(0, 100)
    attempts = 7
    print "Number of guesses:", attempts
    print ""    

def range1000():
    global secret_guess, attempts
    secret_guess = random.randrange(0, 1000)
    attempts = 10
    print "New Game"
    print "Number of guesses:", attempts
    print ""    
    
def newGame():
    print "New Game"    
    range100()
    
def mainLogic(num):
    global attempts
    num = int(num)
    print num
    attempts -= 1;   
    if(attempts >= 1):   
        if (num == secret_guess):
            print "Correct"
            return newGame()
        elif (num > secret_guess):
            print "Lower"
        elif (num < secret_guess):
            print "Higher"            
    else:
        print "You Lost"
        return newGame()
     
    print "Number of remaining attempts", attempts
    print ""
    
    
    
frame = simplegui.create_frame("Guess the number", 200, 200)
frame.add_button("Range(0-100)", range100, 150)
frame.add_button("Range(0-1000)", range1000, 150)
inp = frame.add_input("Care for a guess", mainLogic, 150)

frame.start()
newGame()
   
