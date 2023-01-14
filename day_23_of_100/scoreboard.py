from turtle import Turtle

FONT = ("Courier", 24, "normal")
SCORE_POS = (-200,250)

class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__(visible = False)
        self.score = 0
        self.penup()
        self.color("black")
        self.update_score()

    def level_up(self):
        self.score+=1
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(SCORE_POS)        
        self.write(self.score,align="center",font=FONT)
