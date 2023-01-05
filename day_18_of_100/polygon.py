from turtle import Turtle,Screen
from random import choice, random

screen = Screen()
turtl = Turtle()
turtl.shape("classic")
direction = ["left", "forward", "right","backward"]

colors = ["red","green","blue","yellow","dark green", "sienna","magenta" , "orange", "hot pink", "olive drab", "gray"]


screen.colormode(1)

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
    """ this draws a dashed line, takes length of line in px and turtle object inputs"""
    for shape in range(3,9):
        _turtl.pencolor(choice(colors))
        draw_polygon(shape,100,_turtl)


def random_walk(_steps,_turtl):
    """makes several random movements of several colors"""
    _turtl.pensize(10)
    _turtl.speed(4)
    for _step in range(_steps):
        _dir = choice(direction)
        R = random()
        G = random()
        B = random()

        _turtl.pencolor(R,G,B)
        if _dir == "left":
            _turtl.left(90)
        elif _dir == "right":
            _turtl.right(90)
        elif _dir == "backward":
            _turtl.right(180)    
        _turtl.forward(30)    colors = ["red","green","blue","yellow","dark green", "sienna","magenta" , "orange", "hot pink", "olive drab", "gray"]




random_walk(200,turtl)
# draw_dashed(100,turtl)
# draw_all_shapes(turtl)
screen.exitonclick()