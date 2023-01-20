# from turtle import Screen,Turtle
import turtle
import pandas as pd


screen = turtle.Screen()
screen.title("US GAME")
screen.bgpic("day_25_of_100/us_states_game/us-states-game-start/blank_states_img.gif")
screen.setup(width = 730,height = 500)

data = pd.read_csv("day_25_of_100/us_states_game/us-states-game-start/50_states.csv")

data_dict = data.to_dict()

print(data_dict["x"][0])

new_guess = screen.textinput(title = "Guess the States", prompt = "Whats your next guess?")
new_guess = new_guess.capitalize()




turtle.mainloop()