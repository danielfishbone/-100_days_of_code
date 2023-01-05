from turtle import Turtle,Screen

turtl = Turtle()
turtl.shape("circle")
num_of_sides = 17
size = 15
for i in range(num_of_sides):
    turtl.forward(size)
    turtl.right(360/num_of_sides)
    if i %  3 == 0:
        turtl.stamp()


screen = Screen()
screen.exitonclick()