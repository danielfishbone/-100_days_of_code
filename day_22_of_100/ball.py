from turtle import Screen, Turtle


class Ball(Turtle):
    def __init__(self,color = "red") -> None:
        super().__init__(shape="circle")
        self.Color = color
        self.multiplier = 1
        self.x = 1
        self.y = 1
        self.shapesize(1,1)
        self.color(self.Color)
        self.penup()

    def move(self):    
        if self.ycor() >290 or self.ycor() < -290:
            self.multiplier *= -1
        self.goto((self.xcor()+self.x),self.ycor()+(self.y*self.multiplier))


if __name__ == "__main__":
    screen = Screen()
    ball = Ball()
    for i in range(500):
        ball.move()
    screen.exitonclick()    