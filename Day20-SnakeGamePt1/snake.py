import turtle


class Snake:
    def __init__(self, body_length):
        self.snake_body = []
        body_length = body_length
        for i in range(0, body_length, 1):
            new_body_piece = turtle.Turtle(shape="square")
            new_body_piece.penup()
            new_body_piece.setpos(20 * -i, 0)  # 'Turtle' starts at 20 pixels.
            new_body_piece.color("white")
            self.snake_body.append(new_body_piece)

    def move(self, MOVE_DISTANCE):
        for seg_index in range(len(self.snake_body) - 1, 0, -1):
            xpos = self.snake_body[seg_index - 1].pos()[0]
            ypos = self.snake_body[seg_index - 1].pos()[1]
            self.snake_body[seg_index].setpos(xpos, ypos)
        self.snake_body[0].forward(MOVE_DISTANCE)

    def turn(self, heading):
        self.snake_body[0].setheading(heading)
        print(f"Turning to {heading}")

    def off_screen(self):
        if (self.snake_body[0].xcor() > 300 or self.snake_body[0].xcor() < -300 or
                self.snake_body[0].ycor() > 300 or self.snake_body[0].ycor() < -300):
            return True
        return False

    def snake_bite(self):
        for segments in self.snake_body[1:]:
            if self.snake_body[0].distance(segments) < 10:
                return True
        return False

