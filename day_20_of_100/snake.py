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
    _food.penup()
    _food.goto(randint(-width/2,width/2),randint(-height/2,height/2))
    return _food
def move_food(_food):
    _food.goto(randint(-width/2,width/2),randint(-height/2,height/2))

def draw_boundary():
    bt = Turtle()
    bt.color("red")
    bt.penup()
    bt.goto(-1*width/2,-1*height/2)
    bt.pendown()
    bt.goto(1*width/2,-1*height/2)
    bt.goto(1*width/2,1*height/2)
    bt.goto(-1*width/2,1*height/2)
    bt.goto(-1*width/2,-1*height/2)
    bt.ht()

def new_segment(_snake,_x,_y):
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.setpos(_x,_y)
    _snake.append(new_segment)

def add_segment(_snake):
    x_val = _snake[-2].xcor()-_snake[-1].xcor()
    y_val = _snake[-2].ycor()-_snake[-1].ycor()
    x = _snake[-1].xcor() + (-1*x_val)
    y = _snake[-1].ycor() + (-1*y_val)
    new_segment(_snake,x,y)

x = y = 0

food_flag = False
score = 0
draw_boundary()
for _ in range(5):
    new_segment(snake,x,y)
    x-=20    
screen.setup(width=width,height=height)
screen.bgcolor("black")
screen.title("Snakes")


food = create_food()
game_over = False
while not game_over:
    screen.update()
    screen.listen()
    time.sleep(0.1)
    screen.onkeypress(key="Left",fun=move_left)
    screen.onkeypress(key="Right",fun=move_right)
    
    snake[0].fd(10)
    for seg_num in range(len(snake)-1,0,-1):
        new_x = snake[seg_num-1].xcor()
        new_y = snake[seg_num-1].ycor()
        snake[seg_num].goto(x = new_x, y = new_y)
        if not food_flag:
            move_food(food)
            food_flag = True
        if  food_flag:
            if ( snake[0].xcor() >= food.xcor()-10 and snake[0].xcor()  <= food.xcor()+10 ) and ( snake[0].ycor() >= food.ycor()-10 and snake[0].ycor() <= food.ycor() +10 ):
                score += 1  
                screen.title(score) 
                add_segment(snake)
                food_flag = False

screen.exitonclick()