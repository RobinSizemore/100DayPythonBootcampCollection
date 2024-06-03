import turtle


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score_turtle = turtle.Turtle()
        self.score_turtle.hideturtle()
        self.score_turtle.penup()
        self.score_turtle.color("white")

        self.net_turtle = turtle.Turtle()
        self.net_turtle.pencolor("white")
        self.net_turtle.shape("turtle")
        self.net_turtle.pensize(3)
        self.draw_net()
        self.draw_score_boxes()

    def draw_net(self):
        self.net_turtle.penup()
        self.net_turtle.goto(0, 300)
        self.net_turtle.setheading(270)
        while self.net_turtle.ycor() > -300:
            self.net_turtle.pendown()
            self.net_turtle.forward(15)
            self.net_turtle.penup()
            self.net_turtle.forward(15)
            print(f"{self.xcor()}, {self.ycor()}")

    def draw_score_boxes(self):
        self.net_turtle.penup()
        self.net_turtle.goto(-50, 260)
        self.net_turtle.pendown()
        for _ in range(2):
            self.net_turtle.forward(50)
            self.net_turtle.right(90)
            self.net_turtle.forward(100)
            self.net_turtle.right(90)
        self.net_turtle.penup()
        self.net_turtle.goto(150, 260)
        self.net_turtle.pendown()
        for _ in range(2):
            self.net_turtle.forward(50)
            self.net_turtle.right(90)
            self.net_turtle.forward(100)
            self.net_turtle.right(90)
        self.net_turtle.hideturtle()

    def update_score(self, score):
        self.score_turtle.clear()
        self.score_turtle.showturtle()
        self.score_turtle.goto(-100, 200)
        self.score_turtle.write(score[0], align="center", font=("Courier", 24, "normal"))
        self.score_turtle.goto(100, 200)
        self.score_turtle.write(score[1], align="center", font=("Courier", 24, "normal"))
        self.score_turtle.hideturtle()
