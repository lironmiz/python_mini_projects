import turtle
import random
import time
from snake import Snake
from food import Food
from score_board import ScoreBoard

# constant in game
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
ADJUST_MAX_SNAKE_SPOT = 0.2
MAX_SNAKE_SPOT = SCREEN_WIDTH / 2 - ADJUST_MAX_SNAKE_SPOT
FONT = ("Verdana", 15, "normal")
ALIGN = 'center'

# making instances of snake food and score_board class
snake = Snake()
food = Food()
score_board = ScoreBoard()


def main():
    turtle.title("liron snake game")
    screen = turtle.Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.tracer(0)
    # updating the screen
    screen.update()

    # listening to user inputs
    screen.listen()
    screen.onkey(fun=lambda: snake.change_snake_direction(UP), key="Up")
    screen.onkey(fun=lambda: snake.change_snake_direction(DOWN), key="Down")
    screen.onkey(fun=lambda: snake.change_snake_direction(RIGHT), key="Right")
    screen.onkey(fun=lambda: snake.change_snake_direction(LEFT), key="Left")

    is_game_on = True
    while is_game_on:
        # update the screen after snake body done moving forward
        screen.update()
        time.sleep(0.1)
        snake.move_forward_snake_body()

        # detect collision with food and update score board and extand snake
        if snake.snake_seg_list[0].distance(food) < 15:
            food.change_food_spot()
            score_board.increase_score()
            score_board.update_score_board()
            snake.extend_snake()

        # detect collision with walls
        if snake.snake_seg_list[0].xcor() > MAX_SNAKE_SPOT or snake.snake_seg_list[0].xcor() < -MAX_SNAKE_SPOT or \
                snake.snake_seg_list[0].ycor() < -MAX_SNAKE_SPOT or snake.snake_seg_list[0].ycor() > MAX_SNAKE_SPOT:
            score_board.reset()
            snake.reset()
        # detect collision with tall
        for snake_segment in snake.snake_seg_list[1:]:
            if snake.snake_seg_list[0].distance(snake_segment) < 10:
                score_board.reset()
                snake.reset()
    screen.exitonclick()


if __name__ == "__main__":
    main()
