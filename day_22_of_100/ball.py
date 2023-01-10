from turtle import Turtle


class Ball(Turtle):
    def __init__(self,color = "red") -> None:
        super().__init__(shape="circle")
        self.Color = color
        self.shapesize(0.5 ,0.5)
        self.color(self.Color)
        self.penup
        