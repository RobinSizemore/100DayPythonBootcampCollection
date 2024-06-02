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

    def move(self):
        for seg_index in range(len(self.snake_body) - 1, 0, -1):
            xpos = self.snake_body[seg_index - 1].pos()[0]
            ypos = self.snake_body[seg_index - 1].pos()[1]
            self.snake_body[seg_index].setpos(xpos, ypos)
        self.snake_body[0].forward(20)

    def turn(self, heading):
        self.snake_body[0].setheading(heading)
        print(f"Turning to {heading}")

