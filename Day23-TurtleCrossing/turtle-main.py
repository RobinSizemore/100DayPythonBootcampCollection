from turtle import Screen
import time
from player import Player
import level_manager
import car_manager

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
START_X = 2750
START_Y = 1750

screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT, START_X, START_Y)
screen.bgcolor("black")

time.sleep(3)
level = level_manager.Level()
cars = car_manager.CarManager(level.lane_centers[:-1])  # level returns one too many "centers"

screen.tracer(0)

# Create the player
player = Player()
screen.listen()
screen.onkey(player.move_forward, "Up")

game_running = True
while game_running:
    time.sleep(0.1)
    player_hit = cars.run(player.position())
    if player.ycor() > 270:
        player.goto_start()
        level.level_up()
        cars.speed_up()
    if player_hit:
        player.goto_start()
        cars.reset()
        level.game_over()
    screen.update()
