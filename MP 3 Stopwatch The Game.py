# template for "Stopwatch: The Game"
import simplegui

# define global variables
interval = 100 # interval .1 second (1000 ms = 1 second) = 10/60

is_running = False # set if the timer is running, starts OFF

total_time = 0
total_stops = 0
stopped_on_whole_second = 0
reset_clicked = False
total_turns = 10 # set default total turns
turn_number = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    t = int(t)
    
    # calculate total_seconds from interval passed
    # total_time is passed in as t in draw event
    seconds = t // 1000
    
    # calculate total minutes from the time in seconds
    # total_seconds divided by 60 seconds per minute
    minutes = seconds // 60    
            
    # calculate the tens of seconds
        
    sec_rem = seconds - (minutes * 60)
    tens_seconds = sec_rem // 10
 
    ones_seconds = sec_rem % 10
    
    tenths_second = t - (seconds * 1000)
    
    global hundreds_tenths # so we can score
    hundreds_tenths = tenths_second // 100
    
    global text_string
    text_string = str(minutes) + ":" + str(tens_seconds) + str(ones_seconds) + "." + str(hundreds_tenths)
    return text_string

# define event handlers for buttons; "Start", "Stop", "Reset"
def start_timer():
    global is_running
    global turn_number
    
    global total_time
    start_time = total_time
    total_time += 100
    
    # print "Start: " + str(start_time) 

    timer.start()
    
    if turn_number < total_turns and is_running == False:
        turn_number += 1
    
    # print "Started. Turn " + str(turn_number) + " of " + str(total_turns)
    is_running = True

def stop_timer():
    global is_running
    global total_stops
    global stopped_on_whole_second
    global hundreds_tenths
    
    if is_running == True:# update to show it was clicked
    
        timer.stop()
        is_running = False
        
        total_stops += 1
        
        print "Stopped. End Turn " + str(turn_number) + " of " + str(total_turns)

        if hundreds_tenths == 0:
            stopped_on_whole_second += 1 
    
            timer.stop()
            #print "Success!"
    else:
        #print "The timer isn't running"
        return
    
    
    # print "End: " + str(total_time)
    
def reset_all():
    global reset_clicked
    reset_clicked = True
    
    global total_time
    global is_running
    global total_stops
    global stopped_on_whole_second
    global total_turns
    
    timer.stop()
    
    total_time = 0
    is_running = False
    total_stops = 0
    stopped_on_whole_second = 0
    total_turns = 0
    
    print "Reset all"

# define event handler for timer with 0.1 sec interval
def tick():
    global total_time
    total_time += 100

# define draw handler
def draw(canvas):
    global text_string
    global total_time
    global total_stops
    global stopped_on_whole_second
    
    canvas.draw_text(format(total_time), [125, 165], 60, "black", "sans-serif")
    
    score_text = str(stopped_on_whole_second) + " / " + str(total_stops)
    canvas.draw_text(score_text, [320, 30], 30, "darkgreen", 'sans-serif')
 
# create frame
frame = simplegui.create_frame("Stopwatch: The Game", 400, 300)
frame.set_canvas_background("lightskyblue")
frame.set_draw_handler(draw)

timer = simplegui.create_timer(100, tick)

# register event handlers
frame.add_button("Start", start_timer, 100)
frame.add_button("Stop", stop_timer, 100)
frame.add_button("Reset", reset_all, 100)

# start frame
frame.start()

# Please remember to review the grading rubric
