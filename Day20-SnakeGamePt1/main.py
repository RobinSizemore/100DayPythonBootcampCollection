import turtle
# I *REALLY* want to call this "Turtle Centipede" instead of Snake...
import time


def move_snake():
    for seg_index in range(len(snake) - 1, 0, -1):
        snake[seg_index].setpos(snake[seg_index - 1].pos())
    snake[0].forward(20)
    screen.update()
    time.sleep(.25)


def create_snake():
    snake_head = turtle.Turtle(shape="square")
    snake_head.color("white")
    snake_head.penup()
    snake.append(snake_head)

    body_length = STARTING_LENGTH
    for i in range(1, body_length + 1, 1):
        new_body_piece = turtle.Turtle(shape="square")
        new_body_piece.penup()
        new_body_piece.setpos(20 * -i, 0)  # 'Turtle' starts at 20 pixels.
        new_body_piece.color("white")
        snake.append(new_body_piece)
    screen.update()


def turn_up():
    snake[0].setheading(90)


def turn_right():
    snake[0].setheading(0)


def turn_left():
    snake[0].setheading(180)


def turn_down():
    snake[0].setheading(270)

# Screen setting exclusive to my setup
SCREEN_X_POS = 3000
SCREEN_Y_POS = 1750

# General screen settings
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Other magic numbers
STARTING_LENGTH = 2  # Does not include head.

# Screen Setup
screen = turtle.Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, startx=SCREEN_X_POS, starty=SCREEN_Y_POS)
screen.bgcolor("black")
screen.tracer(0)

# Create the snake
snake = []
create_snake()

# Setup controls
screen.listen()
screen.onkey(fun=turn_up, key="w")
screen.onkey(fun=turn_down, key="s")
screen.onkey(fun=turn_left, key="a")
screen.onkey(fun=turn_right, key="d")

game_running = True

while game_running:
    move_snake()


# Keep Alive
screen.exitonclick()
