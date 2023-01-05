from turtle import Turtle,Screen


turtl = Turtle()
turtl.shape("circle")

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
            

draw_dashed(200,turtl)
screen = Screen()
screen.exitonclick()