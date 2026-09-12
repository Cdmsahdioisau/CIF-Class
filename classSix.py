import turtle
import random

def makeSparks():
    t.penup()
    t.goto(random.randint(randx1, randx2), random.randint(randy1, randy2))
    t.pendown()
    t.stamp()

slowdown = 45

randx1 = -25
randx2 = 25

randy1 = 125
randy2 = 175


sc = turtle.Screen()
t = turtle.Turtle()

t.speed(1)
t.color("gray")
t.pensize(5)
sc.bgcolor("black")
t.fillcolor("red")  

t.penup()
t.goto(250, -200)
t.pendown()

t.begin_fill()

for i in range(4):
    t.forward(50)
    t.right(90)

t.end_fill()

t.color("yellow")
t.shape("circle")

t.penup()
t.goto(275, -200)
t.pendown()

t.left(90)

for i in range(18):
    t.left(5)
    t.forward(slowdown)

    slowdown -= 2

t.speed(10)
t.pencolor("goldenrod")
t.pensize(1)
t.shapesize(0.1, 0.1,)

sc.bgcolor("gray10")

for i in range(50):
    makeSparks()         

    randx1 -= 2 
    randx2 += 2
    randy1 -= 2
    randy2 += 2


sc.bgcolor("black")

turtle.done()