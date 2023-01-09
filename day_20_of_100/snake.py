import time
from turtle import Turtle, Screen


class Snake:
    def __init__(self) -> None:
        seg = Turtle("circle")
        seg.color("red")
        seg.penup()
        self.snake = []
        self.snake.append(seg)
        self.head = seg
        for i in range(3):
            seg = Turtle("circle")
            seg.color("white")
            seg.penup()
            seg.goto((-i*-20)-40,0)
            seg.fillcolor("blue")
            self.snake.append(seg)
    def new_segment(self,_x,_y):
        new_segment = Turtle(shape="circle")
        new_segment.color("white")
        new_segment.fillcolor("blue")
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
    
    def go_left(self):
        if self.snake[0].heading() != 0: 
            self.snake[0].setheading(180)
    def go_right(self):
        if self.snake[0].heading() != 180: 
            self.snake[0].setheading(0)
    def go_up(self):
        if self.snake[0].heading() != 270: 
            self.snake[0].setheading(90)
    def go_down(self):
        if self.snake[0].heading() != 90: 
            self.snake[0].setheading(270)




if __name__ == "__main__":
    screen = Screen()
    screen.bgcolor("black") # set background colour to black
    screen.tracer(0) # Turn off automatic screen updates
    snake1 = Snake() 
    while True:
        screen.listen()
        screen.onkeypress(key="Left",fun=snake1.go_left)
        screen.onkeypress(key="Right",fun=snake1.go_right)
        screen.onkeypress(key="Up",fun=snake1.go_up)
        screen.onkeypress(key="Down",fun=snake1.go_down)
        snake1.move()
        screen.update()

        time.sleep(0.1)
