
from turtle import Turtle,Screen


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.score = 0
        self.high_score=0
        self.penup()
        self.color("white")
        self.goto(0,270)
        self.update()
        
    def add(self):
        self.score += 1
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER",align="center",font=("Arial",20,"bold")) 
    def update (self):
        self.clear()
        self.write(f"SCORE : {self.score} HIGHSCORE{self.high_score}",align="center",font=("Arial",20,"bold"))   
        

if __name__ =="__main__":
    screen = Screen()
    scoreb = ScoreBoard()
    scoreb.add()
    scoreb.update()

    screen.exitonclick()