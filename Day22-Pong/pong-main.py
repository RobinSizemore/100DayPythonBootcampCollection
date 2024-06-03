import turtle
import paddle
import ball
import time
import score

# Screen Setup
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
START_X = 2750
START_Y = 1500

# Game Setup
BALL_SPEED = 10

screen = turtle.Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT, START_X, START_Y)
screen.bgcolor("black")
screen.title("Turtle Pong")
scoreboard = score.Scoreboard()
screen.tracer(False)


# Initialize Paddles
right_paddle = paddle.Paddle()
left_paddle = paddle.Paddle(-350, 0)

# Initialize Ball
ball = ball.Ball()

# Create Controls
screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

score = [0, 0]

game_running = True
while game_running:
    time.sleep(0.05)
    someone_scored = ball.move(BALL_SPEED)  # detects collision with wall, bounces, and returns score if appropriate.
    if someone_scored:
        score[0] += someone_scored[0]
        score[1] += someone_scored[1]
        scoreboard.update_score(score)
        print(f"Score: Left ({score[0]}) | Right ({score[1]})")
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320:
        ball.right_bounce()
        time.sleep(0.25)
    elif ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.left_bounce()
        time.sleep(0.25)
    screen.update()

screen.exitonclick()
