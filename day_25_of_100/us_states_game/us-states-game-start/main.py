# from turtle import Screen,Turtle
from asyncore import write
import turtle
import pandas as pd
from writer import Writer

states = []
x_coordinates = []
y_coordinates = []

game_over = False
screen = turtle.Screen()
writer = Writer()
screen.title("US GAME")
screen.bgpic("day_25_of_100/us_states_game/us-states-game-start/blank_states_img.gif")
screen.setup(width = 730,height = 500)

data = pd.read_csv("day_25_of_100/us_states_game/us-states-game-start/50_states.csv")

states_obj = data.state
x_obj = data.x
y_obj = data.y

missed_states = {
    "state":[],
    "x":[],
    "y":[]
}
states = states_obj.to_list()
x_coordinates =  x_obj.to_list()
y_coordinates  =  y_obj.to_list()
new_guess = screen.textinput(title = "Guess the state", prompt = "Whats your next guess?").title()
states_guessed = []
while not game_over:

    if new_guess == "Exit":
        game_over = True
        break
    elif new_guess in states:
        index = states.index(new_guess)
        cor_x = x_coordinates[index]
        cor_y = y_coordinates[index]
        writer.goto(cor_x,cor_y)
        writer.write(new_guess,align="center")
        if new_guess not in states_guessed:
            states_guessed.append(new_guess)
        if len(states) ==  len(states_guessed):
            print(f"Congratulations,  you've guessed the total {len(states)} States") 
    new_title = f"{len(states_guessed)}/{len(states)} Correct"          
    new_guess = screen.textinput(title = new_title, prompt = "Whats your next guess?").title()        

for _state in states:
    if _state not in states_guessed:
        missed_states["state"].append(_state)
        index = states.index(_state)
        missed_states["x"].append(x_coordinates[index])
        missed_states["y"].append(y_coordinates[index])

print(missed_states["state"])

dataframe =pd.DataFrame(missed_states)
dataframe.to_csv("Missed_states.csv")
