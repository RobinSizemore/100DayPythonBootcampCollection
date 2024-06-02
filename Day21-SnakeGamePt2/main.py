import turtle
# I *REALLY* want to call this "Turtle Centipede" instead of Snake...
import time
from snake import Snake
from food import Food
from score import Scoreboard

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


# Initialize Scoreboard.
scoreboard = Scoreboard()

screen.listen()
game_running = False


def start_game():
    global game_running
    if game_running:
        print("Cannot restart. Game is running.")
        return
    # Create the snake
    screen.clear()
    screen.bgcolor("black")
    screen.tracer(0)

    scoreboard.reset_score()
    snake = Snake(3)
    food = Food()
    screen.update()
    time.sleep(1)

    # controls
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
        screen.update()
        time.sleep(.2)
        if snake.snake_body[0].distance(food) < 15:
            snake.grow()
            food.respawn()
            scoreboard.add_score()
        if snake.off_screen():
            print("Player went off screen!")
            game_running = False
        elif snake.snake_bite():
            print("Player bit themselves!")
            game_running = False

    scoreboard.game_over()


start_game()

# Controls
screen.onkey(start_game, "r")

# Keep Alive
screen.exitonclick()
