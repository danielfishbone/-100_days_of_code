from turtle import Turtle

FONT = ("Courier", 24, "normal")
FONT_GO = ("Courier", 80, "bold")
SCORE_POS = (-220,250)
G_O_POS = (0,0)

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
        self.write(f"Level: {self.score}",align="center",font=FONT)
    def game_over(self):
        self.goto(G_O_POS)        
        self.write("GAME OVER",align="center",font=FONT)

