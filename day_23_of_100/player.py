from turtle import Turtle

class Player(Turtle):
    def __init__(self, shape: str = "turtle") -> None:
        super().__init__(shape)
        self.setheading(90)
        self.penup()
        self.goto(0,-280)

    def move(self):
        new__y = self.ycor +10    
        self.goto(0,new__y)