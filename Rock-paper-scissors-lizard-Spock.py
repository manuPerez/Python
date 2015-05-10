# Rock-paper-scissors-lizard-Spock template

import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    
    if (name == "rock"):
        return 0
    elif (name == "Spock"):
        return 1
    elif (name == "paper"):
        return 2
    elif (name == "lizard"):
        return 3
    elif (name == "scissors"):
        return 4
    else:
        return 5


def number_to_name(number):
    
    if (number == 0):
        return "rock"
    elif (number == 1):
        return "Spock"
    elif (number == 2):
        return "paper"
    elif (number == 3):
        return "lizard"
    elif (number == 4):
        return "scissors"
    else:
        print "no valid number: " + number


def rpsls(player_choice):     
    
    print " "
    
    print "Player chooses", player_choice
    
    player_number = name_to_number(player_choice)
    
    if (player_number != 5):
        
        comp_number = random.randrange(0, 5)
        
        player_random = number_to_name(comp_number)
        
        print "Computer chooses", player_random

        difference = (comp_number - player_number) % 5

        if (difference == 0):
            winner = "Player and computer tie!"
        elif (difference == 1 or difference == 2):
            winner = "Computer wins!"
        elif (difference == 3 or difference == 4):
            winner = "Player wins!"
        print winner
    else:
        print "no valid name: " + player_choice

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")