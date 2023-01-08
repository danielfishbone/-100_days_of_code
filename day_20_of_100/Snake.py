from random import randint
import time
from turtle import Turtle, Screen


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
            self.snake.append(seg)

        
        