# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math

n_range = int(100)
secret_number = 100
remaining_guesses = 7

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    print "Number of remaining guesses is",remaining_guesses


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global secret_number 
    secret_number = random.randrange(0, 100)
    global remaining_guesses 
    remaining_guesses = 7
    global n_range
    n_range = int(100)
    print " "
    print "New game. Range is from 0 to",n_range
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global secret_number 
    secret_number = random.randrange(0, 1000)
    global remaining_guesses 
    remaining_guesses = 10
    global n_range
    n_range = int(1000)
    print " "
    print "New game. Range is from 0 to",n_range
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    int_guess = int(guess)
    print " "
    print "Guess was",int_guess
    
    global secret_number
    global remaining_guesses
    
    print "Number of remaining guesses is",remaining_guesses - 1
    if (remaining_guesses - 1) <= 0:
        print "You Lost"
        if n_range == 100:
            range100()
        else:
            range1000()
    else:
        if secret_number > int_guess:
            remaining_guesses = remaining_guesses - 1
            print "Higher!"
        elif secret_number < int_guess:
            remaining_guesses = remaining_guesses - 1
            print "Lower!"
        else:
            print "Correct!"
            if n_range == 100:
                range100()
            else:
                range1000()
    
# create frame
frame = simplegui.create_frame('Guess the number',200,200)

# register event handlers for control elements and start frame
frame.add_button("Range is [0 - 100]", range100, 200)
frame.add_button("Range is [0 - 1000]", range1000, 200)
frame.add_input("Enter a guess", input_guess, 200)


# call new_game 
range100()


# always remember to check your completed program against the grading rubric
