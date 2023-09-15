import turtle
import random
s = turtle.getscreen()
t= turtle.Turtle
turtle.title("Turtle House")
turtle.bgcolor("gray12")



def random_stars():
    turtle.fillcolor("yellow")
    for x in range(15):
        x_position=random.randint(-350, 250)
        y_position=random.randint(50, 250)
        turtle.penup()
        turtle.goto(x_position, y_position)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(4)
        turtle.end_fill()

random_stars()

def building():
    turtle.penup()
    turtle.pensize(4)
    turtle.color("black","brown")
    turtle.begin_fill()
    turtle.goto(-200,-150)
    turtle.pendown()
    turtle.fd(400)
    turtle.lt(90)
    turtle.fd(200)
    turtle.lt(90)
    turtle.fd(400)
    turtle.lt(90)
    turtle.fd(200)
    turtle.lt(90)
    turtle.end_fill()

building()

def side():
    turtle.fd(100)
    turtle.lt(90)
    turtle.fd(200)
    turtle.lt(90)
    turtle.fd(100)
    turtle.end_fill()

side()


def roof():
    turtle.color("black", "grey")
    turtle.begin_fill()
    turtle.rt(120)
    turtle.fd(100)
    turtle.rt(120)
    turtle.fd(100)
    turtle.end_fill()
    turtle.begin_fill()
    turtle.backward(100)
    turtle.lt(60)
    turtle.fd(300)
    turtle.rt(60)
    turtle.fd(100)
    turtle.end_fill()

roof()

def door():
    turtle.penup()
    turtle.goto(-200,-150)
    turtle.setheading(0)
    turtle.pendown()
    turtle.color("black","pink")
    turtle.forward(230)
    turtle.left(90)
    turtle.begin_fill()
    turtle.forward(90)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(90)
    turtle.end_fill()
    turtle.penup()
    

door()



def grass():
    turtle.color("black","green")
    turtle.goto(-650,-150)
    turtle.left(90)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(1300)
    turtle.right(90)
    turtle.forward(180)
    turtle.right(90)
    turtle.forward(1300)
    turtle.right(90)
    turtle.forward(180)
    turtle.end_fill()
    turtle.penup()

grass()




i = input()