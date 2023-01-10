from turtle import Turtle
BOARD_COLOR = "white"
PENSIZE = 10
PEN_COLOR = "red"
class Board(Turtle):
    def __init__(self,_width,_height):
        super().__init__(visible = False)
        self.width = _width/2 
        self.height = _height/2
        self.pen(fillcolor=BOARD_COLOR, pencolor=PEN_COLOR, pensize=PENSIZE)
        self.penup()
    def draw(self):
        self.goto(-self.width,-self.height)
        self.pendown()
        self.goto(self.width,-self.height)
        self.goto(self.width,self.height)
        self.goto(-self.width,self.height)
        self.goto(-self.width,-self.height)
        self.penup()
            
   
