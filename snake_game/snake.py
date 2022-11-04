import turtle

# constant in snake class
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
SNAKE_MOVE_FORWARD_STEP = 20


class Snake():
    ### class that control the snake body###

    def __init__(self) -> object:
        """
        Constructor of the class make snake object.
        Parameters: snake_seg_list : list - list of snake segment
        Returns: snake object
        """
        self.snake_seg_list = []
        self.create_segment()
        self.snake_head = self.snake_seg_list[0]

    def create_segment(self) -> None:
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position) -> None:
        """
        extend the snake body
        Parameters: position: tuple
        Returns: None
        """
        new_seg = turtle.Turtle("square")
        new_seg.color("white")
        new_seg.penup()
        new_seg.goto(position)
        self.snake_seg_list.append(new_seg)

    def extend_snake(self) -> None:
        """
        extend the snake body
        Parameters: None
        Returns: None
        """
        self.add_segment(self.snake_seg_list[-1].position())

    def move_forward_snake_body(self) -> None:
        """
        move the snake body forward
        Parameters: None
        Returns: None
        """
        for snake_seg_num in range(len(self.snake_seg_list) - 1, 0, -1):
            new_x = self.snake_seg_list[snake_seg_num - 1].xcor()
            new_y = self.snake_seg_list[snake_seg_num - 1].ycor()
            self.snake_seg_list[snake_seg_num].goto(new_x, new_y)
        self.snake_seg_list[0].fd(SNAKE_MOVE_FORWARD_STEP)

    def change_snake_direction(self, heading_change: int) -> None:
        """
        change the snake direction
        Parameters: heading_change: int - set the number of  change in direction
        Returns: None
        """
        # checking that the user input and current hading not opposite from each other
        snake_heading_check = (self.snake_seg_list[0].heading() + 180) % 360
        if snake_heading_check != heading_change:
            self.snake_seg_list[0].setheading(heading_change)

    def reset(self) -> None:
        """
        reset the screen
        Parameters: None
        Returns: None
        """
        for seg in self.snake_seg_list:
            seg.goto(1000,1000)
        self.snake_seg_list.clear()
        self.create_segment()
        self.snake_head = self.snake_seg_list[0]
