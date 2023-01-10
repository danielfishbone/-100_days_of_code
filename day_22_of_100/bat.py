import time
from turtle import Turtle, Screen

class Bat(Turtle):
    def __init__(self,x_pos=0,y_pos=0,length = 100,color="blue") -> None:
        super().__init__(shape="square")
        self.length_factor = length/20
        self.x_pos = x_pos
        self.y_pos = y_pos
        self._color = color
        self.speed("fastest")
        self.color(self._color)
        self.penup()
        self.goto(self.x_pos, self.y_pos)
        self.shapesize(stretch_len=0.5,stretch_wid=self.length_factor)

    def move_up(self):
        self.y_pos += 10
        self.goto(self.x_pos, self.y_pos)
        
    def move_down(self):
        self.y_pos -= 10
        self.goto(self.x_pos, self.y_pos)


if __name__ =="__main__":
    screen = Screen()
    bat = Bat(600,0,100,"green")
    for _ in range(10):
        bat.move_up()
        time.sleep(0.1)
    for _ in range(10):
        bat.move_down()
        time.sleep(0.01)
    screen.exitonclick()
    