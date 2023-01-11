import time
from turtle import  Screen
from board import Board
from bat import Bat
from ball import Ball

WIDTH = 840
HEIGHT = 640

board_width = 800
board_height = 600


screen = Screen()
screen.tracer(0)
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=WIDTH,height=HEIGHT)

board =Board(width=board_width,height=board_height)
player1 = Bat(-350,color="green")
player2 = Bat(350,color="purple")
ball = Ball()

running =True
while running:
    ball.move()
    screen.listen()
    screen.onkey(fun=player1.move_up,key="w")
    screen.onkey(fun=player1.move_down,key="s")
    screen.onkey(fun=player2.move_up,key="Up")
    screen.onkey(fun=player2.move_down,key="Down")

    if ball.xcor() >= player2.xcor()-20 and ball.distance(player2) <=50:
        print("collision on player 2")
        ball.bounce()
        print(f"x cor ={ball.xcor()}")
        print(f"y cor ={ball.ycor()}")

    screen.update()
    time.sleep(0.1)
screen.exitonclick()