from random import randint
import time
from turtle import Turtle, Screen
screen = Screen()
screen.bgcolor("black")

class Snake:
    def __init__(self) -> None:
        seg = Turtle("square")
        seg.color("red")
        seg.penup()
        self.snake = []
        self.snake.append(seg)
        for i in range(2):
            seg = Turtle("square")
            seg.color("white")
            seg.penup()
            seg.goto((-i*-20)-40,0)
            self.snake.append(seg)
    def move(self):
            for seg_num in range(len(self.snake)-1,0,-1):
                new_x = self.snake[seg_num-1].xcor()
                new_y = self.snake[seg_num-1].ycor()
                self.snake[seg_num].goto(x = new_x, y = new_y)
            self.snake[0].fd(10)


snake1 = Snake()       
screen.exitonclick() 
