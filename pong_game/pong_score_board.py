from turtle import Turtle

# constant in score board class
FONT = ("Verdana", 60, "normal")
ALIGN = 'center'
MIDDLE_UP_SCREEN_x_POSITION = 0
MIDDLE_UP_SCREEN_Y_POSITION = 220


class ScoreBoardPong(Turtle):
    def __init__(self) -> object:
        super().__init__()
        """
        Constructor of the class make ScoreBoard object and control the text behavior in the code.
        Parameters:  score : tuple the score of the users - pencolor: str the color of the board 
                     penup: penup: hide the pen of score board for first show on screen 
                     hideturtle: - hide the score board for first show on screen -  goto:  set the score board place on screen
                     write: set the score board text 
        Returns:     score board object
        """

        self.pencolor("white")
        self.penup()
        self.hideturtle()
        self.goto(MIDDLE_UP_SCREEN_x_POSITION, MIDDLE_UP_SCREEN_Y_POSITION)
        self.right_score = 0
        self.left_score = 0
        self.update_score(self.left_score, self.right_score)

    def update_score(self, new_score_right_update: int, new_score_left_update: int) -> None:
        """
        update the score of the users and show to screen
        Parameters: -> str
        Returns: None
        """
        self.clear()
        self.write(F" {new_score_left_update} {new_score_right_update}", font=FONT, align=ALIGN)

