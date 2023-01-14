from random import randint
from turtle import Screen
from scoreboard import ScoreBoard 
from player import Player
from cars import Car
from time import sleep

WIDTH  = 600
HEIGHT = 600
cars = []
screen = Screen()
screen.setup(WIDTH,HEIGHT)
screen.tracer(0)
player = Player()
scoreboard = ScoreBoard()
sleep_time = 0.1
new_car_flag = False
count = 0
counter = 0
cars.append(Car())
game_over = False
while not game_over:


    if new_car_flag:
        count = randint(1,10)
        new_car_flag =False

    if counter>=count:
        cars.append(Car())
        counter = 0
        new_car_flag = True

    if player.ycor()>= 280:
        scoreboard.level_up()
        player.reset_position()
        sleep_time * 0.66
        if sleep_time < 0.01:
            sleep_time = 0.01    

    for i in range(len(cars)):
        cars[i].move()
        if player.distance(cars[i]) <10:
            game_over = True
            print("gameover")
        if cars[i].xcor() <= -350:
            cars[i].hideturtle()
            cars[i] = None
            cars.pop(i) 
            break   
    
    screen.listen()
    screen.onkeypress(fun =player.move, key="Up" )



    counter += 1
    screen.update()
    sleep(sleep_time)
screen.exitonclick()



