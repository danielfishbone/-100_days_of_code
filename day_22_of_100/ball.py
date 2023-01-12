from turtle import Screen, Turtle


class Ball(Turtle):
    def __init__(self,color = "red") -> None:
        super().__init__(shape="circle")
        self.Color = color
        self.multiplier_x = 1
        self.multiplier_y = 1
        self.x = 10
        self.y = 10
        self.shapesize(1,1)
        self.color(self.Color)
        self.penup()

    def move(self):    
        self.goto(self.xcor()+(self.x * self.multiplier_x),self.ycor()+(self.y*self.multiplier_y))
    
    def bounce_x(self):
        self.multiplier_x *= -1
    def bounce_y(self):
        self.multiplier_y *= -1

if __name__ == "__main__":
    screen = Screen()
    ball = Ball()
    for i in range(500):
        ball.move()
    screen.exitonclick()    