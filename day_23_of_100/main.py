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
car = Car()
game_over = False
while not game_over:
    sleep(0.1)
    screen.listen()
    screen.onkeypress(fun =player.move, key="Up" )

    car.move()



    screen.update()
screen.exitonclick()



