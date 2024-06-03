import turtle


class Paddle(turtle.Turtle):
    def __init__(self, x_position=350, y_position=0):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x_position, y_position)

    def go_up(self):
        y_coord = self.ycor()
        if y_coord < 250:  # Don't move if at top of screen.
            self.goto(self.xcor(), self.ycor() + 10)

    def go_down(self):
        y_coord = self.ycor()
        if y_coord > -250:  # Don't move if at bottom of screen.
            self.goto(self.xcor(), self.ycor() - 10)
