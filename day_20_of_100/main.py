import time
from turtle import Screen
from snake import Snake
from food import Food 
from scoreboard import ScoreBoard

screen = Screen()
width  = 600
height = 600
screen.setup(width,height)
score = 0
screen.bgcolor("black") # set background colour to black
screen.tracer(0) # Turn off automatic screen updates
screen.title("Snake Game") 
my_snake = Snake()
food = Food(width,height)
scoreboard = ScoreBoard()
game_over = False
paused = False
def pause():
    global paused
    paused = not paused 
while not game_over:
    
    scoreboard.update()
    screen.update()
    time.sleep(0.1)
    screen.listen()
    screen.onkeypress(key="space",fun=pause)
    if not paused:
        my_snake.move()
        screen.onkeypress(key="Left",fun=my_snake.go_left)
        screen.onkeypress(key="Right",fun=my_snake.go_right)
        screen.onkeypress(key="Up",fun=my_snake.go_up)
        screen.onkeypress(key="Down",fun=my_snake.go_down)

        if my_snake.head.distance(food) <= 15:
            food.move()
            scoreboard.add()
            my_snake.add_segment()

        if my_snake.head.xcor() > 280 or my_snake.head.xcor() < -290 or my_snake.head.ycor() > 290 or my_snake.head.ycor() < -280 :
            game_over = True
            scoreboard.game_over()

        for segs in my_snake.snake[1:]:
            if my_snake.head.distance(segs) <10:
                game_over = True
                scoreboard.game_over()

screen.exitonclick()