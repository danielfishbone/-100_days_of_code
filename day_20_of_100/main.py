import time
from turtle import Screen, window_width
from snake import Snake
from food import Food 

screen = Screen()
width  = 600
height = 600
score = 0
screen.bgcolor("black") # set background colour to black
screen.tracer(0) # Turn off automatic screen updates
my_snake = Snake()
food = Food(width,height)
game_over = False

while not game_over:
    my_snake.move()
    screen.update()
    time.sleep(0.1)
    screen.listen()
    screen.onkeypress(key="Left",fun=my_snake.go_left)
    screen.onkeypress(key="Right",fun=my_snake.go_right)
    screen.onkeypress(key="Up",fun=my_snake.go_up)
    screen.onkeypress(key="Down",fun=my_snake.go_down)

    if my_snake.head.distance(food) <= 15:
        food.move()
        score += 1
        my_snake.add_segment()
        screen.title(score)




screen.exitonclick()