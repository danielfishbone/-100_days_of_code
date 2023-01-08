import time
from turtle import Screen
from snake import Snake 

screen = Screen()
screen.bgcolor("black") # set background colour to black
screen.tracer(0) # Turn off automatic screen updates
my_snake = Snake()
game_over = False

while not game_over:
    my_snake.move()
    screen.update()
    time.sleep(0.2)
    screen.listen()
    screen.onkeypress(key="Left",fun=my_snake.go_left)
    screen.onkeypress(key="Right",fun=my_snake.go_right)
    screen.onkeypress(key="Up",fun=my_snake.go_up)
    screen.onkeypress(key="Down",fun=my_snake.go_down)
screen.exitonclick()