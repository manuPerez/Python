# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

stand = False


# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
    
# define hand class
class Hand:
    def __init__(self):
        self.hand = []  # create Hand object

    def __str__(self):
        h = ""
        for card in self.hand:
            # return a string representation of a hand
            h += " " + card.__str__()
        return "hand contains " + h

    def add_card(self, card):
        self.hand.append(card)  # add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        value = 0
        
        for card in self.hand:
            value += VALUES[card.rank]
        
        if self.has_aces():
            if value + 10 <= 21:
                return value + 10
            else:
                return value
        else:
            return value
            
    def has_aces(self):
        for card in self.hand:
            if card.rank == 'A':
                return True
        return False
        
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        for card in self.hand:
            card.draw(canvas, pos)
            pos = [pos[0]+CARD_SIZE[0]+20,pos[1]]
    
        
# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                card = Card(suit, rank)
                self.deck.append(card)

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck)

    def deal_card(self):
        # deal a card object from the deck
        self.shuffle()
        return self.deck[0]
    
    def remove(self, c):
        self.deck.remove(c)
        
    def __str__(self):
        # return a string representing the deck
        h = ""
        for card in self.deck:
            # return a string representation of a hand
            h += " " + card.__str__()
        return "Deck contains " + h


#define event handlers for buttons
def deal():
    global outcome, in_play, deck, dealer, player, stand

    # your code goes here
    deck = Deck()
    dealer = Hand()
    player = Hand()
    c1 = deck.deal_card()
    c2 = deck.deal_card()
    dealer.add_card(c1)
    player.add_card(c2)
    deck.remove(c1)
    deck.remove(c2)
    c3 = deck.deal_card()
    c4 = deck.deal_card()
    dealer.add_card(c3)
    player.add_card(c4)
    deck.remove(c3)
    deck.remove(c4)
    print "Dealer", dealer, dealer.get_value()
    print "Player", player, player.get_value()
    
    in_play = True
    stand = False

def hit():
    global player, in_play, score
        
    # if the hand is in play, hit the player
    if in_play:
        c1 = deck.deal_card()
        player.add_card(c1)
        deck.remove(c1)
        if player.get_value() <= 21:
            print "Player", player, player.get_value()
        else:
            # if busted, assign a message to outcome, update in_play and score 
            print "You have busted", player.get_value()
            in_play = False
            score -= 1
    else:
        print "The play is finished", player.get_value()
        
    
       
def stand():
    global canvas, dealer, player, in_play, score, stand
    
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play:
        stand = True
        while dealer.get_value() < 17:
            c1 = deck.deal_card()
            dealer.add_card(c1)
            deck.remove(c1)
            print "Dealer", dealer, dealer.get_value()
        if dealer.get_value() > 21:
            print "Player wins"
            score += 1
        else:
            if dealer.get_value() >= player.get_value():
                print "Dealer wins"
                score -= 1
            else:
                print "Player wins"
                score += 1
        
        in_play = False
    else:
        print "The play is finished", player.get_value()
        
    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    global outcome, score, card_back, stand, dealer
    
    outcome = "Blackjack"
    canvas.draw_text(outcome, (240, 60), 40, '#00aacc')
    
    outcome = "score : " + str(score)
    canvas.draw_text(outcome, (450, 120), 30, 'Black')
    
    outcome = "Dealer"
    canvas.draw_text(outcome, (100, 120), 24, 'Black')
    dealer.draw(canvas, [100, 140])
    if not stand:
        canvas.draw_image(card_back, [CARD_CENTER[0],CARD_CENTER[1]], CARD_SIZE, [100 + CARD_CENTER[0], 140 + CARD_CENTER[1]], CARD_SIZE)
    else:
        dealer.draw(canvas, [100, 140])
    
    
    outcome = "Player"
    canvas.draw_text(outcome, (100, 380), 24, 'Black')
    player.draw(canvas, [100, 400])
    
    outcome = "Hit or Stand?"
    canvas.draw_text(outcome, (300, 380), 24, 'Black')
    player.draw(canvas, [100, 400])
    

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deck = Deck()
dealer = Hand()
player = Hand()
deal()
frame.start()


# remember to review the gradic rubric