from random import randint
import time
from turtle import Turtle, Screen
screen = Screen()
screen.bgcolor("black")
screen.tracer(0)
class Snake:
    def __init__(self) -> None:
        seg = Turtle("square")
        seg.color("red")
        seg.penup()
        self.snake = []
        self.snake.append(seg)
        for i in range(3):
            seg = Turtle("square")
            seg.color("white")
            seg.penup()
            seg.goto((-i*-20)-40,0)
            self.snake.append(seg)

    def new_segment(self,_x,_y):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.setpos(_x,_y)
        self.snake.append(new_segment)    

    def add_segment(self):
        x_val = self.snake[-2].xcor()-self.snake[-1].xcor()
        y_val = self.snake[-2].ycor()-self.snake[-1].ycor()
        x = self.snake[-1].xcor() + (-1*x_val)
        y = self.snake[-1].ycor() + (-1*y_val)
        self.new_segment(x,y)  

    def move(self):
            for seg_num in range(len(self.snake)-1,0,-1):
                new_x = self.snake[seg_num-1].xcor()
                new_y = self.snake[seg_num-1].ycor()
                self.snake[seg_num].goto(x = new_x, y = new_y)
            self.snake[0].fd(20)





if __name__ == "__main__":
    snake1 = Snake() 
    c = 0    
    while True:
        snake1.move()
        screen.update()
        if c % 10 == 0:
            snake1.add_segment()
        time.sleep(1)
        c += 1
    screen.exitonclick() 
