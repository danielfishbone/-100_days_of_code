from turtle import  Screen
from board import Board
from bat import Bat
WIDTH = 840
HEIGHT = 640

board_width = 800
board_height = 600


screen = Screen()
screen.tracer(0)
screen.title("Pong")
screen.setup(width=WIDTH,height=HEIGHT)
screen.bgcolor("black")
board =Board(width=board_width,height=board_height)
player1 = Bat(-350,color="green")
player2 = Bat(350,color="purple")
screen.update()
screen.exitonclick()