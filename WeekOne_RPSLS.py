#Rock-Paper-Scissors-Lizard-Spock
import random

def name_to_number(name):
    if(name == "rock"):
        return 0
    elif(name == "spock"):
        return 1
    elif(name == "paper"):
        return 2
    elif(name == "lizard"):
        return 3
    elif(name == "scissors"):
        return 4
    else:
        return "Invalid input"

def number_to_name(number):
    if(number == 0):
        return "rock"
    elif(number == 1):
        return "spock"
    elif(number == 2):
        return "paper"
    elif(number == 3):
        return "lizard"
    elif(number == 4):
        return "scissors"
    else:
        return "Invalid input"
    
    
def rpsls(guess):
    num1 = name_to_number(guess)
    num2  = random.randrange(0, 5)
    print "Computer chooses", number_to_name(num2)
    print "Player chooses", guess
    num2 = (num1 - num2) % 5
    if num2 >= 3:
        print "Computer wins"
    elif num2 == 0:
        print "Game draw"
    else:
        print "Player wins"
    
    print ""
    

rpsls("rock")
rpsls("paper")
rpsls("scissors")
rpsls("lizard")
rpsls("spock")


