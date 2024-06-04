from turtle import Turtle
import math


class Level(Turtle):
    def __init__(self, screen_width=600, screen_height=600, lane_width=40):
        super().__init__()
        self.lane_centers = []
        lane_start_end = (screen_width / 2) - 50
        self.score_turtle = Turtle()
        self.score_turtle.hideturtle()
        self.score_turtle.penup()
        self.score_turtle.pencolor("white")
        self.score_turtle.goto(screen_width/-2 + 40, screen_height/2 - 40)
        self.level_num = 0
        self.level_up()
        self.draw_lanes(math.floor(lane_start_end * -1) + 20, math.floor(lane_start_end), lane_width)

    def draw_lanes(self, start_y, end_y, step):
        lane_turtle = Turtle("turtle")
        lane_turtle.penup()
        lane_turtle.pencolor("yellow")
        lane_turtle.pensize(2)
        lane_turtle.speed(50)

        for index, y in enumerate(range(start_y, end_y + 1, step)):
            if index % 2 == 0:  # If index is even
                lane_turtle.goto(-300, y)
                for _ in range(30):  # Assuming the width of the screen is 600 units
                    lane_turtle.pendown()
                    lane_turtle.forward(10)
                    lane_turtle.penup()
                    lane_turtle.forward(10)
            else:  # If index is odd
                lane_turtle.goto(300, y)
                for _ in range(30):  # Assuming the width of the screen is 600 units
                    lane_turtle.pendown()
                    lane_turtle.backward(10)
                    lane_turtle.penup()
                    lane_turtle.backward(10)
            self.lane_centers.append(y + (step / 2))

    def level_up(self):
        self.score_turtle.clear()
        self.level_num += 1
        self.score_turtle.write(f"LEVEL {self.level_num}", align="left", font=("Courier", 15, "normal"))
        pass

    def game_over(self):
        self.level_num = 0
        self.level_up()
