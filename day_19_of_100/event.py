from turtle import Turtle, Screen, pendown

orientation = 0
turtle1 = Turtle()
turtle1.speed("fast")
screen = Screen()

def move_forward():
    turtle1.forward(10)
def move_backward():
    turtle1.backward(10)
def move_left():
    global orientation
    turtle1.setheading(orientation)
    orientation += 5
def move_right():
    global orientation
    turtle1.setheading(orientation)
    orientation -= 5
def Clear():
    turtle1.clear()    

def pen():
    if turtle1.isdown():
        turtle1.penup()
    else:
        pendown()      

screen.listen()
screen.onkeypress(key="Up",fun=move_forward)
screen.onkeypress(key="Down",fun=move_backward)
screen.onkeypress(key="Left",fun=move_left)
screen.onkeypress(key="Right",fun=move_right)
screen.onkeypress(key="c",fun=Clear)
screen.onkeypress(key="p",fun= pen )

screen.exitonclick()