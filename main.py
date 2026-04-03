from turtle import *

window = Screen()
window.bgcolor("black")
window.title("Write your name")
window.setup(width = 1000, height = 500)

tur = Turtle()
tur.color("lightgreen")

tur.shape("turtle")
tur.shapesize(0.5)
tur.pensize(5)

tur.penup()
tur.left(180)
tur.forward(450)
tur.right(90)
tur.forward(100)
tur.pendown()
#R
tur.forward(100)
tur.right(90)
for i in range(14) :
    tur.forward(6)
    tur.right(5+i)
tur.right(14)
tur.forward(32)
tur.left(130)
tur.forward(65)

tur.penup()
tur.left(42)
tur.forward(50)
tur.pendown()
#Y
tur.left(93)
tur.forward(50)
tur.left(35)
tur.forward(60)
tur.left(180)
tur.forward(60)
tur.left(105)
tur.forward(60)

tur.penup()
tur.right(50)
tur.forward(25)
tur.right(90)
tur.pendown()
#U
tur.forward(65)
for i in range(45):
    tur.left(4)
    tur.forward(2)
tur.forward(60)














window.exitonclick()