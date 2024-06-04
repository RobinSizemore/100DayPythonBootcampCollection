import turtle
import random

color_list = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "orchid"]


class Food(turtle.Turtle):
    def __init__(self):
        super().__init__("circle")
        self.shapesize(stretch_wid=.5, stretch_len=.5)
        self.penup()
        self.color(random.choice(color_list))
        self.respawn()

    def respawn(self):
        random_x = random.randint(-14, 14) * 20
        random_y = random.randint(-14, 14) * 20
        self.color(random.choice(color_list))
        self.speed("fastest")
        self.goto(random_x, random_y)
        print(f"Food at {random_x}, {random_y}")
