from turtle import Turtle

class Writer(Turtle):
    def __init__(self) -> None:
        super().__init__(visible = False)
        self.pu()
        