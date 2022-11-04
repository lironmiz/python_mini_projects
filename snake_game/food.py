from turtle import Turtle
import random

# constant in food class
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SIZE_FOOD = 20
MAX_RANDOM_FOOD_SPOT = SCREEN_WIDTH / 2 - SIZE_FOOD


class Food(Turtle):

    def __init__(self) -> object:
        super().__init__()
        """
        Constructor of the class make food object and inheritance from turtle class.
        Parameters
        shape : str - set the food shap
        penup : None - set the pen of the food up
        shapesize: tuple - set the size of food
        color: str - set the color of the food 
        speed: str - set the speed of the food 
        goto: tuple -set the spot of the food on screen
        Returns: food object
        """
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.change_food_spot()

    def change_food_spot(self) -> None:
        """
        changes the food spot on screen
        Parameters: None
        Returns: None
        """
        random_x = random.randint(-MAX_RANDOM_FOOD_SPOT, MAX_RANDOM_FOOD_SPOT)
        random_y = random.randint(-MAX_RANDOM_FOOD_SPOT, MAX_RANDOM_FOOD_SPOT)
        self.goto(random_x, random_y)
