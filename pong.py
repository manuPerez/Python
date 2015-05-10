# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [-40.0 / 20.0,  5.0 / 20.0]
paddle1_pos = [[0, (HEIGHT / 2)+HALF_PAD_HEIGHT],[0, (HEIGHT / 2)-HALF_PAD_HEIGHT]]
paddle2_pos = [[WIDTH, (HEIGHT / 2)+HALF_PAD_HEIGHT],[WIDTH, (HEIGHT / 2)-HALF_PAD_HEIGHT]]
paddle1_vel = [0, 0]
paddle2_vel = [0, 0]
score1 = 0
score2 = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    #ball_vel = [random.randrange(120, 240)*(-1)/1000, random.randrange(60, 180)/1000]
    if direction == RIGHT:
        ball_vel = [random.randrange(120, 240)*(-1)/80, random.randrange(60, 180)/80]
        ball_pos[0] -= ball_vel[0]
        ball_pos[1] -= ball_vel[1]
    if direction == LEFT:
        ball_vel = [random.randrange(120, 240)/80, random.randrange(60, 180)/80]
        ball_pos[0] += ball_vel[0]
        ball_pos[1] += ball_vel[1]    

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel
    global score1, score2
    score1 = 0
    score2 = 0
    
    global RIGHT, LEFT
    if RIGHT:
        spawn_ball(RIGHT)
    if LEFT:
        spawn_ball(LEFT)

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] -= ball_vel[0]
    ball_pos[1] -= ball_vel[1]
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos[0][1] -= paddle1_vel[1]
    paddle1_pos[1][1] -= paddle1_vel[1]
    paddle2_pos[0][1] -= paddle2_vel[1]
    paddle2_pos[1][1] -= paddle2_vel[1]
    if paddle1_pos[1][1] < 0:
        paddle1_pos[1][1] = 0
        paddle1_pos[0][1] = PAD_HEIGHT
    if paddle1_pos[1][1] > HEIGHT - PAD_HEIGHT:
        paddle1_pos[1][1] = HEIGHT - PAD_HEIGHT
        paddle1_pos[0][1] = HEIGHT
    if paddle2_pos[1][1] < 0:
        paddle2_pos[1][1] = 0
        paddle2_pos[0][1] = PAD_HEIGHT
    if paddle2_pos[1][1] > HEIGHT - PAD_HEIGHT:
        paddle2_pos[1][1] = HEIGHT - PAD_HEIGHT
        paddle2_pos[0][1] = HEIGHT    
    
    
    # draw paddles
    canvas.draw_line(paddle1_pos[0], paddle1_pos[1], PAD_WIDTH * 2, 'White')
    canvas.draw_line(paddle2_pos[0], paddle2_pos[1], PAD_WIDTH * 2, 'White')
    
    # determine whether paddle and ball collide    
    # collide and reflect off of left hand side of canvas
    if ball_pos[0] <= (BALL_RADIUS + PAD_WIDTH):
        if ball_pos[1] <= paddle1_pos[0][1] and ball_pos[1] >= paddle1_pos[1][1]:
            ball_vel[0] = - ball_vel[0] * 1.1
        else:
            score2 += 1
            spawn_ball(LEFT)
            
    # collide and reflect off of right hand side of canvas
    if ball_pos[0] > (WIDTH - (BALL_RADIUS + PAD_WIDTH)):
        if ball_pos[1] <= paddle2_pos[0][1] and ball_pos[1] >= paddle2_pos[1][1]:
            ball_vel[0] = (ball_vel[0] * (-1)) * 1.1
        else:
            score1 += 1
            spawn_ball(RIGHT)
        
    # collide and reflect off of up hand side of canvas
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    # collide and reflect off of bottom hand side of canvas
    if ball_pos[1] >= (HEIGHT - BALL_RADIUS):
        ball_vel[1] = ball_vel[1] * (-1)
        
    # draw scores
    canvas.draw_text(str(score1), ((WIDTH / 2) - (PAD_HEIGHT + 20), 50), 40, 'White', 'monospace')
    canvas.draw_text(str(score2), ((WIDTH / 2) + PAD_HEIGHT, 50), 40, 'White', 'monospace')
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel[1] += 3
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel[1] -= 3
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel[1] += 3
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel[1] -= 3
        
def keyup(key):
    global paddle1_vel, paddle2_vel
    if chr(key) == "W":
        paddle1_vel[1] = 0
    elif chr(key) == 'S':
        paddle1_vel[1] = 0
    elif chr(key) == '&':
        paddle2_vel[1] = 0
    elif chr(key) == '(':
        paddle2_vel[1] = 0
        
def button_handler():
    new_game()
    
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
button1 = frame.add_button("Restart", button_handler)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()
