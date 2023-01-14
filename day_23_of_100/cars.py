from turtle import Turtle
from random import choice, randint 
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
SCREEN_HIEGHT = 280
class Cars(Turtle):
    def __init__(self )-> None:
        super().__init__(shape = "square")
        self.shapesize(3,0.5)
        self.color(choice(COLORS))
        self.penup()
        self.goto(0,randint(-SCREEN_HIEGHT,SCREEN_HIEGHT))




