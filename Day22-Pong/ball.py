import turtle
import random


class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.reset()

    def move(self, speed):
        self.forward(speed)
        return self.wall_bounce()

    def wall_bounce(self):
        if self.xcor() <= -390:
            # left wall
            self.reset()
            return [0, 1]
        elif self.xcor() > 390:
            # right wall.
            self.reset()
            return [1, 0]
        elif self.ycor() <= -290:
            # bottom wall
            self.setheading(360 - self.heading())
            print("BOTTOM WALL!")
        elif self.ycor() > 290:
            # top wall
            self.setheading(360 - self.heading())
            print("TOP WALL!")
        else:
            pass

    def reset(self):
        self.goto(0, 0)
        ranges = [(0, 45), (135, 225), (315, 360)]
        selected_range = random.choice(ranges)
        self.setheading(random.randint(*selected_range))

    def right_bounce(self):
        self.setheading(540 - self.heading())

    def left_bounce(self):
        self.setheading(180 - self.heading())
