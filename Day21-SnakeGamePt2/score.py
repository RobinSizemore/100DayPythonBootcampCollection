import turtle


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 275)
        self.color("white")
        self.high_score = 0
        self.draw_score()

    def draw_score(self):
        self.clear()
        self.color("white")
        self.write(f"Score: {self.score}  |  High Score: {self.high_score}", False,
                   "center", ("Arial", 10, "normal"))

    def add_score(self):
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
        self.draw_score()

    def reset_score(self):
        self.score = 0
        self.goto(0, 275)
        self.draw_score()

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER", False, "Center", ("Arial", 30, "normal"))
        self.goto(0, -45)
        self.write("Press 'r' to restart", False, "center", ("Arial", 25, "normal"))
        self.goto(0, 275)