
from turtle import Turtle,Screen


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.score = 0
        self.high_score=0
        self.penup()
        self.color("white")
        self.goto(0,270)
        self.get_highscore()
        self.update()
    def get_highscore(self):
        with open("/home/fishbone/python_100_days_of_code/day_20_of_100/highscore.txt")as hs_file:
            self.high_score = int(hs_file.read())  

    def add(self):
        self.score += 1
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER",align="center",font=("Arial",20,"bold")) 
    def update (self):
        self.clear()
        self.write(f"SCORE : {self.score} HIGHSCORE: {self.high_score}",align="center",font=("Arial",20,"normal"))   
        

if __name__ =="__main__":
    screen = Screen()
    scoreb = ScoreBoard()
    scoreb.add()
    scoreb.update()

    screen.exitonclick()