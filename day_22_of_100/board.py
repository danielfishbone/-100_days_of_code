from turtle import Turtle, Screen, width
PENSIZE = 5
PEN_COLOR = "yellow"
FILL_COLOR = "white"
SPACING = 10

class Board(Turtle):
    def __init__(self,width =800,height=600):
        super().__init__(visible = False)
        self.width = width/2 
        self.height = height/2
        self.pen(fillcolor=FILL_COLOR, pencolor=PEN_COLOR, pensize=PENSIZE)
        self.speed("fastest")
        self.penup()
        self.draw_board()
        self.draw_centre_line()

    def draw_board(self):
        self.goto(-self.width,-self.height)
        self.pendown()
        self.goto(self.width,-self.height)
        self.goto(self.width,self.height)
        self.goto(-self.width,self.height)
        self.goto(-self.width,-self.height)
        self.penup()
            
    def draw_centre_line(self):
        _size = self.height*2
        _num_of_pace = int(_size/SPACING)

        self.goto(0,-self.height)
        self.pendown()
        current_heading = self.heading() 
        self.setheading(90)
        for i in range(_num_of_pace):
            if i%2 == 0:
                self.penup()
                self.forward(SPACING)
            else:
                self.pendown()
                self.forward(SPACING)

        self.goto(0,self.height)
        self.penup()
        self.setheading(current_heading)


if __name__ == "__main__":
    screen = Screen()
    screen.bgcolor("black")
    board =Board(width=800,height = 600)

    screen.exitonclick()

