from turtle import Turtle

# constant in ball class
BALL_START_SPOT = (0, 0)
BALL_SPEED = 0.1


class Ball(Turtle):
    def __init__(self) -> object:
        super().__init__()
        """
        Constructor of the class make ball object and control the behavior of the ball.
            Parameters: shape:str - set the paddle shape, penup: - hide the ball paint, 
                        goto(BALL_START_SPOT): tuple - set the ball position, color: str - set the ball color,
                        shapesize(stretch_wid=1, stretch_len=1): tuple  - set the ball size,
                         x_move: int - move ball in x cordinate, y_move: int - move ball in y cordinate     
            Returns: ball object
        """
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(BALL_START_SPOT)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = BALL_SPEED

    def move(self) -> None:
        """
        move the ball in the game
        Parameters: None
        Returns: None
        """
        self.penup()
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        self.screen.update()

    def bounce(self, direction_bounce: str) -> None:
        """
        bounce the ball in the game
        Parameters: None
        Returns: None
        """
        if direction_bounce == "y":
            self.y_move *= -1
        else:
            self.x_move *= -1
            self.move_speed *= 0.95
