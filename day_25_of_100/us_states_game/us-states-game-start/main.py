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

states = states_obj.to_list()
x_coordinates =  x_obj.to_list()
y_coordinates  =  y_obj.to_list()

states_guessed = []
while not game_over:
    new_guess = screen.textinput(title = "Guess the States", prompt = "Whats your next guess?").title()
    # new_guess = new_guess.capitalize()

    if new_guess in states:
        index = states.index(new_guess)
        cor_x = x_coordinates[index]
        cor_y = y_coordinates[index]
        writer.goto(cor_x,cor_y)
        writer.write(new_guess,align="center")
        if new_guess not in states_guessed:
            states_guessed.append(new_guess)
        if len(states) ==  len(states_guessed):
            print(f"Congratulations,  you've guessed the total {len(states)} States")       
        screen.title(f"{len(states_guessed)}/{len(states)} Correct")
turtle.mainloop()