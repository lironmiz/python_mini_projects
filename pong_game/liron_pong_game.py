import turtle
import random
from paddle import Paddle
from ball import Ball
from pong_score_board import ScoreBoardPong
import time
import math

# constant in game
UP = 90
DOWN = 270
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_COLOR = "black"
PADDLE_MOVE_FORWARD_STEP = 100
RIGHT_PADDLR_FIRST_SPOT = (350, 0)
LEFT_PADDLR_FIRST_SPOT = (-350, 0)
BALL_START_SPOT = (0, 0)
BALL_SIZE = 20
MAX_DISTANCE_BALL_AND_PADDLE = 50
BALL_MAX_X_COORDINATE_WITE_PADDLE = 325
BALL_MAX_X_COORDINATE = 380
MAX_USER_SCORE = 10

paddle = turtle.Turtle("square")
screen = turtle.Screen()

# making the paddles and ball  objects
right_paddle = Paddle(RIGHT_PADDLR_FIRST_SPOT)
left_paddle = Paddle(LEFT_PADDLR_FIRST_SPOT)
game_ball = Ball()
score_board_pong = ScoreBoardPong()


def main():
    turtle.title("liron pong game")
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.bgcolor(SCREEN_COLOR)
    screen.tracer(0)

    # take user input
    screen.listen()
    screen.onkey(fun=lambda: right_paddle.move_paddle(UP), key="Up")
    screen.onkey(fun=lambda: right_paddle.move_paddle(DOWN), key="Down")
    screen.onkey(fun=lambda: left_paddle.move_paddle(UP), key="w")
    screen.onkey(fun=lambda: left_paddle.move_paddle(DOWN), key="s")

    # game loop
    game_loop()

    screen.exitonclick()


def game_loop() -> None:
    # game loop
    is_game_on = 0
    while is_game_on < MAX_USER_SCORE:
        time.sleep(game_ball.move_speed)
        screen.update()
        game_ball.move()

        # detect collision with up and down walls
        if game_ball.ycor() > SCREEN_HEIGHT / 2 - BALL_SIZE or game_ball.ycor() < -(SCREEN_HEIGHT / 2 - BALL_SIZE):
            game_ball.bounce("y")

        # detect collision with paddle
        if game_ball.distance(right_paddle) < MAX_DISTANCE_BALL_AND_PADDLE and game_ball.xcor() > BALL_MAX_X_COORDINATE_WITE_PADDLE or game_ball.distance(left_paddle) < MAX_DISTANCE_BALL_AND_PADDLE and game_ball.xcor() < -BALL_MAX_X_COORDINATE_WITE_PADDLE:
            game_ball.bounce("x")

        # detect collision with right and left walls and update score
        if game_ball.xcor() > BALL_MAX_X_COORDINATE:
            game_ball.goto(BALL_START_SPOT)
            game_ball.bounce("x")
            score_board_pong.right_score += 1
            score_board_pong.update_score(score_board_pong.left_score, score_board_pong.right_score)
        elif game_ball.xcor() < -BALL_MAX_X_COORDINATE:
            game_ball.goto(BALL_START_SPOT)
            game_ball.bounce("x")
            score_board_pong.left_score += 1
            score_board_pong.update_score(score_board_pong.left_score, score_board_pong.right_score)

        is_game_on = max(score_board_pong.right_score, score_board_pong.left_score)


if __name__ == "__main__":
    main()
