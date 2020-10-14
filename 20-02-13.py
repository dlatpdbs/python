import turtle as t
import random

te =t.Turtle()      #나쁜 놈
te.shape("turtle")
te.speed(0)
te.color("blue")  
te.up()
te.goto(0,200)

tt =t.Turtle()      #나쁜 놈
tt.shape("turtle")
tt.speed(0)
tt.color("green")  
tt.up()
tt.goto(-200,0)





def turn_rt():
    t.setheading(0)
def turn_lt():
    t.setheading(180)
def turn_up():
    t.setheading(90)
def turn_down():
    t.setheading(270)
def play():
    t.forward(20)
    ang = te.towards(t.pos())
    te.setheading(ang)
    te.forward(19)

    ang = tt.towards(t.pos())
    tt.setheading(ang)
    tt.forward(19)


    



    if t.distance(te)  >= 12 :
        t.ontimer(play,100)

    if t.distance(tt)  >= 12 :
        t.ontimer(play,100)

    if t.distance(tq)  >= 12 :
        t.ontimer(play,100)


    if t.distance(ts) <12:
        x = random.randint(-950,950)
        y = random.randint(-500,500)
        ts.goto(x,y)


        
t.setup(500,500)
t.bgcolor("sky blue")
t.shape("turtle")
t.speed(0)
t.up()
t.color("sky blue")




t.onkeypress(turn_rt,"Right")
t.onkeypress(turn_lt,"Left")
t.onkeypress(turn_up,"Up")
t.onkeypress(turn_down,"Down")
t.listen()
play()
