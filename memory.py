# implementation of card game - Memory

import simplegui
import random

card_height = 100
card_width = 50

card_one = -1
card_two = -1
pos_card_one = -1
pos_card_two = -1
turns = 0

listOne = range(8)
listTwo = range(8)
listThree = [ ]
listThree.extend(listOne)
listThree.extend(listTwo)
exposed = {}

# helper function to initialize globals
def new_game():
    global state, listThree, exposed, card_one, card_two, pos_card_one, pos_card_two, label, turns
    state = 0
    random.shuffle(listThree)
    for i in range(len(listThree)):
        exposed[i] = False
    card_one = -1
    card_two = -1
    pos_card_one = -1
    pos_card_two = -1
    turns = 0
    label.set_text("Turns = "+str(turns))
        
# define event handlers
def mouseclick(pos):
    global exposed,state,card_one,card_two,pos_card_one,pos_card_two,label,turns
    position_card = pos[0]/card_width
    if exposed[position_card] == 0:
        if state == 0:
            state = 1
            card_one = listThree[position_card]
            pos_card_one = position_card
            exposed[position_card] = True
        elif state == 1:
            turns += 1
            label.set_text("Turns = "+str(turns))
            state = 2
            card_two = listThree[position_card]
            pos_card_two = position_card
            exposed[position_card] = True
        else:
            if card_one == card_two:
                card_one = listThree[position_card]
                pos_card_one = position_card
                card_two = -1
                pos_card_two = -1
                state = 1
                exposed[position_card] = True
            else:
                for key in exposed.keys():
                    if key == pos_card_one:
                        exposed[key] = False
                    if key == pos_card_two:
                        exposed[key] = False
                card_one = listThree[position_card]
                pos_card_one = position_card
                card_two = -1
                pos_card_two = -1
                state = 1
                exposed[position_card] = state
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    p = 15
    pos = 0
    w_ini = 0
    
    for num in listThree:
        canvas.draw_text(str(num), (p, 65), 50, 'White')
        p = p + card_width
        pos = (p/card_width)
        if not exposed[pos-1]:
            canvas.draw_polygon([(((pos-1)*card_width), 0), (((pos-1)*card_width), card_height), ((pos*card_width), card_height), ((pos*card_width), 0)], 1, 'Black','Green')

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = "+str(turns))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric