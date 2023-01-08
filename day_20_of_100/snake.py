from random import randint
import time
from turtle import Turtle, Screen, color, xcor

snake = []

screen = Screen()
screen.tracer(0)

width  = 600
height = 600

def move_left():
    snake[0].left(90)
def move_right():
    snake[0].right(90)
def create_food():
    _food =Turtle("circle")
    _food.color("blue")
    _food.goto(randint(0,width),randint(0,height))
    return _food

x = y = 0

food_flag = False

for _ in range(5):
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.setpos(x,y)
    x-=20
    snake.append(new_segment)

screen.setup(width=width,height=height)
screen.bgcolor("black")
screen.title("Snakes")


game_over = False
while not game_over:
    screen.update()
    screen.listen()
    time.sleep(0.2)
    screen.onkeypress(key="Left",fun=move_left)
    screen.onkeypress(key="Right",fun=move_right)
    snake[0].fd(20)
    for seg_num in range(len(snake)-1,0,-1):
        new_x = snake[seg_num-1].xcor()
        new_y = snake[seg_num-1].ycor()
        snake[seg_num].goto(x = new_x, y = new_y)



screen.exitonclick()