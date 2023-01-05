from turtle import Turtle,Screen
from random import choice 

turtl = Turtle()
turtl.shape("classic")
colors = ["red","green","blue","yellow","dark green", "sienna","magenta" , "orange", "hot pink", "olive drab", "gray"]
def draw_polygon(_num_of_sides,_size = 100,_turtl = turtl):
    """ this draws a polygon, takes number of sides length of line and turtle object as inputs"""

    for i in range(_num_of_sides):
        _turtl.forward(_size)
        _turtl.right(360/_num_of_sides)

def draw_dashed(_size,_turtl):
    """ this draws a dashed line, takes length of line in px and turtle object inputs"""
    _spacing = 10
    _num_of_pace = int(_size/_spacing)
    for i in range(_num_of_pace):
        if i%2 == 0:
            _turtl.penup()
            _turtl.forward(_spacing)
        else:
            _turtl.pendown()
            _turtl.forward(_spacing)  
            

def draw_all_shapes(_turtl):
    for shape in range(3,9):
        _turtl.pencolor(choice(colors))
        draw_polygon(shape,100,_turtl)



draw_dashed(100,turtl)
draw_all_shapes(turtl)
screen = Screen()
screen.exitonclick()