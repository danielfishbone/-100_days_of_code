from turtle import Turtle,  Screen 
screen =Screen()


red_turtle = Turtle()
yellow_turtle = Turtle()
green_turtle = Turtle()
blue_turtle = Turtle()
purple_turtle = Turtle()
orange_turtle = Turtle()
indigo_turtle = Turtle()

red_turtle.color("red")
yellow_turtle.color("yellow")  
green_turtle.color("green")  
blue_turtle.color("blue")
purple_turtle.color("purple") 
orange_turtle.color("orange")
indigo_turtle.color("indigo")

turtles = (red_turtle,yellow_turtle,green_turtle,blue_turtle,purple_turtle,orange_turtle,indigo_turtle)

def set_home():
    home_x = -200
    home_y = -150
    
    for i in range(len(turtles)):
        turtles[i].shape("turtle")
        turtles[i].speed("fastest")
        turtles[i].penup()
        turtles[i].setpos(x=home_x,y=home_y)
        home_y += 50









screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle would win?, Enter your color")

set_home()








screen.exitonclick()
