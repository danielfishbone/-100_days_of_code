# from turtle import Screen,Turtle
import turtle
screen = turtle.Screen()
screen.title("US GAME")
screen.bgpic("day_25_of_100/us_states_game/us-states-game-start/blank_states_img.gif")
screen.setup(width = 730,height = 500)


new_guess = screen.textinput(title = "Guess the States", prompt = "Whats your next guess?")
turtle.mainloop()