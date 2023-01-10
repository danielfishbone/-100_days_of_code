from turtle import Turtle
class Bat(Turtle):
    def __init__(self) -> None:
        super().__init__(shape="square")
        self.shapesize(stretch_len=1,stretch_wid=5)
        