from turtle import Turtle

FONT = ("Courier", 24, "normal")
SCORE_POS = (-200,250)

class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__(visible = False)
        self.score = 0
        self.penup()
        self .goto(SCORE_POS)
        self.color("black")
        self.write(self.score,align="center",font=FONT)

    def level_up(self):
        self.score+=1