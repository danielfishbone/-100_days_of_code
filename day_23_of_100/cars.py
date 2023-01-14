from turtle import Turtle
from random import choice, randint 
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
SCREEN_HIEGHT = 280
SCREEN_WIDTH = 280
class Car(Turtle):
    def __init__(self )-> None:
        super().__init__(shape = "square")
        self.shapesize(1,2)
        self.color(choice(COLORS))
        self.penup()
        self.moving_distance = STARTING_MOVE_DISTANCE
        self.goto(SCREEN_WIDTH,randint(-SCREEN_HIEGHT,SCREEN_HIEGHT))

    def level_up(self):
        self.moving_distance += MOVE_INCREMENT
    def move(self):
        x = self.xcor()
        y = self.ycor()
        self.goto(x-self.moving_distance,y)    



