from turtle import Turtle
import os

# constant in score board class
FONT = ("Verdana", 15, "normal")
ALIGN = 'center'
FIRST_SCORE = 0
MIDDLE_UP_SCREEN_x_POSITION = 0
MIDDLE_UP_SCREEN_Y_POSITION = 270


class ScoreBoard(Turtle):
    def __init__(self) -> object:
        super().__init__()
        """
        Constructor of the class make ScoreBoard object and control the text behavior in the code.
        Parameters: score : int - the score of the user
        pencolor: str - the color of the board
        penup: penup: - hide the pen of score board for first show on screen
        hideturtle: - hide the score board for first show on screen
        goto: - set the score board place on screen
        write: - set the score board text 
        Returns: score board object
        """
        self.score = FIRST_SCORE
        with open("data.txt") as data_file:
            self.high_score = int(data_file.read())
        self.pencolor("white")
        self.penup()
        self.hideturtle()
        self.goto(MIDDLE_UP_SCREEN_x_POSITION, MIDDLE_UP_SCREEN_Y_POSITION)
        self.update_score_board()

    def update_score_board(self) -> None:
        """
        updating the score board
        Parameters: None
        Returns: None
        """
        self.clear()
        self.write(F"Score: {self.score} High score {self.high_score}", font=FONT, align=ALIGN)

    def increase_score(self) -> None:
        """
        increase the score of the user
        Parameters: None
        Returns:None
        """
        self.score += 1

    def reset(self) -> None:
        """
        reset the score of the user
        Parameters: None
        Returns: None
        """
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data_file:
                data_file.write(f"{self.high_score}")
        self.score = 0
        self.update_score_board()
