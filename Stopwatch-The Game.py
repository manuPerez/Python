# template for "Stopwatch: The Game"

import simplegui


# define global variables
interval = 100
t = 0
x = 0
y = 0
started = False
D = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    A = 0
    B = 0
    C = t/10
    global D
    D = t%10
    if C > 9:
        B = C/10
        C = C%10
    if B > 5:
        A = B/6
        B = B%6    
    
    return str(A) + ':' + str(B) + str(C) + '.' + str(D)    
   
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def button_handler_start():
    timer.start()
    global started
    started = True

def button_handler_stop():
    timer.stop()
    global started
    if started:
        global y
        y = y + 1
        
        global D
        if D == 0:
            global x
            x = x + 1
        started = False
    
def button_handler_reset():
    timer.stop()
    global t
    t = 0
    global x
    x = 0
    global y
    y = 0
    format(t)
    
# define event handler for timer with 0.1 sec interval
def increment():
    global t
    t = t + 1
    

# define draw handler
def draw(canvas):
    canvas.draw_text(format(t), [110, 110], 36, "White")
    canvas.draw_text(str(x) + '/' + str(y), [230, 40], 36, "Green")
    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game", 300, 200)
frame.set_draw_handler(draw)
start = frame.add_button('Start', button_handler_start)
stop = frame.add_button('Stop', button_handler_stop)
reset = frame.add_button('Reset', button_handler_reset)

# register event handlers
timer = simplegui.create_timer(interval, increment)

# start frame
frame.start()

