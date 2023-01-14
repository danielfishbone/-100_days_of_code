from random import randint
from turtle import Screen 
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
# car = Car()
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

    for i in range(len(cars)):
        cars[i].move()
        if cars[i].xcor() <= -300:
            cars[i].hideturtle()
            cars[i] = 0
            cars.pop(i) 
            break   
    sleep(0.1)
    screen.listen()
    screen.onkeypress(fun =player.move, key="Up" )

    # car.move()


    counter += 1
    screen.update()
screen.exitonclick()



