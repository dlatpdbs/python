import turtle as t

def turn_rt():
    t.pensize(1)
    t.color("red")
    t.setheading(0)
    t.forward(3)
    
def turn_lt():
    t.pensize(5)
    t.color("blue")
    t.setheading(180)
    t.forward(3)
    
def turn_up():
    t.pensize(10)
    t.color("magenta")
    t.setheading(90)
    t.forward(3)
    
def turn_down():
    t.pensize(15)
    t.color("green")
    t.setheading(270)
    t.forward(3)
    
def blank():
    t.clear()

t.shape("turtle")

t.speed(0)
t.onkeypress(turn_rt,"Right")
t.onkeypress(turn_lt,"Left")
t.onkeypress(turn_up,"Up")
t.onkeypress(turn_down,"Down")
t.onkeypress(blank,"Escape")
t.listen()
