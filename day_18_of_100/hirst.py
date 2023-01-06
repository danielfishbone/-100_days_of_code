from random import choice
import turtle as t
from turtle import Turtle,Screen, circle

s =Screen()
t.colormode(255)
x = -400
y = -350
gap = 50
size_x = 15
size_y = 15
color_set = [(237, 233, 84), (205, 160, 101), (118, 177, 201), (32, 115, 162), (171, 17, 69), (213, 132, 164), (157, 80, 41), (172, 169, 37), (175, 47, 92), (223, 57, 103), (132, 183, 149), (12, 31, 68), (39, 129, 84), (228, 76, 51), (234, 166, 192), (72, 16, 59)]

turtl = Turtle()
turtl.penup()
turtl.speed("fastest")
turtl.setpos(x,y)
turtl.speed("fast")

for _ in range(size_y):
    turtl.setpos(x,y)
    y += gap
    for i in range(size_x):
        turtl.dot(28,choice(color_set))
        turtl.forward(50)

s.exitonclick()