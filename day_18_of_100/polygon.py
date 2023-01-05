from turtle import Turtle,Screen
from random import choice, random

screen = Screen()
turtl = Turtle()
turtl.shape("classic")
direction = ["left", "forward", "right","backward"]


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
        _turtl.pencolor(random_color())
        draw_polygon(shape,100,_turtl)


def random_walk(_steps,_turtl):
    """makes several random movements of several colors"""
    _turtl.pensize(10)
    _turtl.speed(4)
    for _step in range(_steps):
        _dir = choice(direction)
       

        _turtl.pencolor(random_color())
        if _dir == "left":
            _turtl.left(90)
        elif _dir == "right":
            _turtl.right(90)
        elif _dir == "backward":
            _turtl.right(180)    
        _turtl.forward(30) 

def random_color():
    """Generates random colors """
    R = random()
    G = random()
    B = random()
    _color = (R,G,B)
    return _color
def spirograph(_size =100,_circles = 36,_turtle = turtl):
    """creates a spirograph with random colors"""
    _turtle.speed("fastest") 
       
    for i in range(_circles):
        _turtle.pencolor(random_color())
        _turtle.circle(_size)
        _turtle.right(360/_circles)


spirograph(_size =200)
# draw_dashed(200,turtl)
# random_walk(200,turtl)
# draw_dashed(200,turtl)
# draw_all_shapes(turtl)
screen.exitonclick()