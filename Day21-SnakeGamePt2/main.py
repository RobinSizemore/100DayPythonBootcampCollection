import turtle
# I *REALLY* want to call this "Turtle Centipede" instead of Snake...
import time
from snake import Snake

# Screen setting exclusive to my setup
SCREEN_X_POS = 3000
SCREEN_Y_POS = 1750

# General screen settings
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Other magic numbers
STARTING_LENGTH = 3
MOVE_DISTANCE = 20

# Screen Setup
screen = turtle.Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, startx=SCREEN_X_POS, starty=SCREEN_Y_POS)
screen.bgcolor("black")
screen.tracer(0)

# Create the snake
snake = Snake(5)
screen.update()
time.sleep(1)

# Controls
screen.listen()
screen.onkey(lambda: snake.turn(90), "w")
screen.onkey(lambda: snake.turn(90), "Up")
screen.onkey(lambda: snake.turn(180), "a")
screen.onkey(lambda: snake.turn(180), "Left")
screen.onkey(lambda: snake.turn(270), "s")
screen.onkey(lambda: snake.turn(270), "Down")
screen.onkey(lambda: snake.turn(0), "d")
screen.onkey(lambda: snake.turn(0), "Right")

game_running = True

while game_running:
    snake.move(MOVE_DISTANCE)
    if snake.off_screen():
        print("Player went off screen!")
        game_running = False
    elif snake.snake_bite():
        print("Player bit themselves!")
        game_running = False
    screen.update()
    time.sleep(.2)

# Keep Alive
screen.exitonclick()
