import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.listen()
screen.setup(width=600, height=600)
screen.tracer(0)
player= Player()
carmanager=CarManager()
scoreboard=Scoreboard()


screen.onkey(player.move_up,"Up")
screen.onkey(player.move_down,"Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    carmanager.create_car()
    carmanager.car_move()

    for car in carmanager.all_cars:
        if car.distance(player)<20:
            game_is_on = False
            scoreboard.game_over()

    if player.is_at_finish():
        player.go_to_start()
        carmanager.level_up()
        scoreboard.next_level()

screen.exitonclick()
