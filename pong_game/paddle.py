from turtle import Turtle

# constant in paddle class
PADDLE_MOVE_FORWARD_STEP = 70
PADDLE_MAX_Y = 240


class Paddle(Turtle):
    def __init__(self, position: tuple) -> object:
        super().__init__()
        """
        Constructor of the class make paddle object and control the behavior of the paddle.
            Parameters: shape:str - set the paddle shape, penup: - hide the paddle paint, 
                        goto(position): tuple - set the paddle position, color: str - set the paddle color,
                        shapesize(stretch_wid=5, stretch_len=1): tuple  - set the paddle size
            Returns: paddle object
        """

        self.shape("square")
        self.position = position
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)

    def move_paddle(self, moving_direction: int) -> None:
        """
        move the paddle up or down
            Parameters: moving_direction: int var that hold the wanted direction
            Returns: None
        """
        #if self.ycor() > PADDLE_MAX_Y:
         #   self.ycor(PADDLE_MAX_Y - 50)
        #elif self.ycor() < -PADDLE_MAX_Y:
         #   self.ycor(PADDLE_MAX_Y + 50)
        #else:
        paddle_starting_direction = self.heading()
        self.setheading(moving_direction)
        self.fd(PADDLE_MOVE_FORWARD_STEP)
        self.setheading(paddle_starting_direction)
        self.screen.update()
