import time
from turtle import  Screen
from board import Board
from bat import Bat
from ball import Ball
from scoreboard import ScoreBoard

WIDTH = 840
HEIGHT = 640
START_SPEED = 0.05
board_width = 800
board_height = 600

play_speed = START_SPEED

screen = Screen()
screen.tracer(0)
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=WIDTH,height=HEIGHT)

board =Board(width=board_width,height=board_height)
player1 = Bat(-350,color="green")
player2 = Bat(350,color="purple")
ball = Ball()
scoreboard = ScoreBoard()
running =True
while running:
    ball.move()
    screen.listen()
    screen.onkey(fun=player1.move_up,key="w")
    screen.onkey(fun=player1.move_down,key="s")
    screen.onkey(fun=player2.move_up,key="Up")
    screen.onkey(fun=player2.move_down,key="Down")

    if ball.ycor() >290 or ball.ycor() < -290:
        ball.bounce_y()

    if ball.xcor() >= player2.xcor()-20 and ball.distance(player2) <=50:
        print("collision on player 2")
        play_speed -= 0.002
        ball.bounce_x()

    if ball.xcor() <= player1.xcor()+20 and ball.distance(player1) <=50:
        print("collision on player 1")
        play_speed -= 0.002
        ball.bounce_x()
    if ball.xcor() >= player2.xcor()+20:
        print("player 2 Missed")
        player1.score += 1
        scoreboard.l_score = player1.score
        ball.centre()
        play_speed = START_SPEED

        print(f"Player1 {player1.score} : {player2.score } Player2")
    if ball.xcor() <= player1.xcor()-20:
        print("player 1 Missed")
        player2.score += 1
        scoreboard.r_score = player2.score
        ball.centre()
        play_speed = START_SPEED
        print(f"Player1 {player1.score} : {player2.score } Player2")
    if play_speed < 0.002:
        play_speed = 0.002
    scoreboard.update()
    screen.update()
    time.sleep(play_speed)
screen.exitonclick()