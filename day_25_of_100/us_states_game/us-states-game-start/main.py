# from turtle import Screen,Turtle
import turtle
screen = turtle.Screen()
screen.title("US GAME")
screen.bgpic("day_25_of_100/us_states_game/us-states-game-start/blank_states_img.gif")
screen.setup(width = 730,height = 500)


def get_mouse(x,y):
    print(x,y)


turtle.onscreenclick(get_mouse)
turtle.mainloop()