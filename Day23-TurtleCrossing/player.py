import turtle

STARTING_POSITION = (0, -250)
MOVE_DISTANCE = 15


class Player(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.goto_start()

    def move_forward(self):
        self.forward(MOVE_DISTANCE)

    def goto_start(self):
        self.setheading(90)
        self.goto(STARTING_POSITION)