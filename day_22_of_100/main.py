from turtle import  Screen
from board import Board
WIDTH = 840
HEIGHT = 640

board_width = 800
board_height = 600


screen = Screen()
screen.tracer(0)
screen.setup(width=WIDTH,height=HEIGHT)
screen.bgcolor("black")
board =Board(width=board_width,height=board_height)

screen.update()
screen.exitonclick()