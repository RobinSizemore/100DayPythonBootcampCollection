import turtle


class Snake:
    def __init__(self, body_length):
        self.snake_body = []
        self.body_length = body_length
        self.create_snake()

    def create_snake(self):
        for i in range(0, self.body_length, 1):
            new_body_piece = turtle.Turtle(shape="square")
            new_body_piece.penup()
            new_body_piece.setpos(20 * -i, 0)  # 'Turtle' starts at 20 pixels.
            new_body_piece.color("white")
            self.snake_body.append(new_body_piece)

    def reset(self):
        for body_segment in self.snake_body:
            body_segment.hideturtle()
            body_segment.clear()
        self.snake_body = []
        self.create_snake()

    def move(self, move_distance):
        for seg_index in range(len(self.snake_body) - 1, 0, -1):
            xpos = self.snake_body[seg_index - 1].pos()[0]
            ypos = self.snake_body[seg_index - 1].pos()[1]
            self.snake_body[seg_index].setpos(xpos, ypos)
        self.snake_body[0].forward(move_distance)

    def turn(self, heading):
        self.snake_body[0].setheading(heading)
        print(f"Turning to {heading}")

    def off_screen(self):
        if (self.snake_body[0].xcor() > 290 or self.snake_body[0].xcor() < -290 or
                self.snake_body[0].ycor() > 290 or self.snake_body[0].ycor() < -290):
            return True
        return False

    def snake_bite(self):
        for segments in self.snake_body[1:]:
            if self.snake_body[0].distance(segments) < 10:
                return True
        return False

    def grow(self):
        new_body_piece = turtle.Turtle(shape="square")
        new_body_piece.penup()
        new_body_piece.color("white")
        pos_in_2d_vector = self.snake_body[len(self.snake_body) - 1].pos()
        new_body_piece.goto(pos_in_2d_vector[0], pos_in_2d_vector[1])
        self.snake_body.append(new_body_piece)
