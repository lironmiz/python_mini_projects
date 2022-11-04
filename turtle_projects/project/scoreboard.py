from tkinter.font import Font
from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", font=FONT, align="left")

    def update_level(self):
        self.level += 1
        self.update_scoreboard()
    
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=FONT)

