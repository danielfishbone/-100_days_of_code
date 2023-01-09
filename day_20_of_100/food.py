import time
from turtle import Turtle,Screen
from random import randint

class Food(Turtle):
    def __init__(self,_width,_hieght):
        super().__init__()
        self._width = _width
        self._hieght = _hieght   
        self.shape("circle")
        self.speed("fastest")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("red")

    def move(self):
        self.x = randint(((-self._width)/2)+10,((self._width)/2)-10)
        self.y = randint(((-self._hieght)/2)+10,((self._hieght)/2)-10)
        self.goto(self.x,self.y)   


if __name__ =="__main__":
    screen = Screen()
    food = Food(600,600)
    for i in range(50):
        food.move()
        time.sleep(.5)
    screen.exitonclick()