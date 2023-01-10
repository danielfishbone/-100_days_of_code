from turtle import Turtle
BOARD_COLOR = "white"
PENSIZE = 10
PEN_COLOR = "red"
class Board(Turtle):
    def __init__(self):
        super().__init__(visible = False)
        self.pen(fillcolor=BOARD_COLOR, pencolor=PEN_COLOR, pensize=PENSIZE)



