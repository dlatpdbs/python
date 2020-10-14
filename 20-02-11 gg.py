import turtle as t
import random as r
t.shape("turtle")

def turn_up():
    t.lt(5)

def turn_down():
    t.rt(5)

def fire():
    





t.goto(-950,0)
t.down()
t.goto(950,0)

ta= r.randint(50,150)
t.pensize(10)
t.color("green")
t.up()
t.goto (ta+700,2)
t.down()
t.goto(ta+710,2)

t.color("black")
t.up()
t.goto (ta-700,2)
t.setheading(20)

t.onkeypress(turn_up,"Up")
t.onkeypress(turn_down,"Down")
t.onkeypress(fire,"space")

t.listen()



