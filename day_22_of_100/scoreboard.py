from turtle import Turtle, Screen

s =Screen()

class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__(visible = False)
        self.penup()
        # self.color("white")
        self.color("black")
        self.l_score = 0
        self.r_score = 0
        self.write(self.l_score,align="center", font=("courier",80,"normal"))
        self.goto(self.xcor()+80,10)
        self.write(":",align="center", font=("courier",80,"normal"))
        self.goto(self.xcor()+80,0)
        self.write(self.r_score,align="center", font=("courier",80,"normal"))
        

sc = ScoreBoard()
s.exitonclick()