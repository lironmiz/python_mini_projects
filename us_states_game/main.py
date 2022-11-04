import turtle
import pandas

# constant in the game
BLANK_STATES_IMAGE_WIDTH = 725
BLANK_STATES_IMAGE_HEIGHT = 495
STATE_FONT = ("Verdana", 7, "normal")
WELL_DONE_FONT = ("Verdana", 40, "normal")
WELL_DONE_X_SPOT = 0
WELL_DONE_Y_SPOT = 0
ALIGN = 'center'
NUM_STATES = 50
X_COLUMN = 1
Y_COLUMN = 2
FIRST_USER_SCORE = 0
WELL_DONE_TEXT = "well done!!"

pen = turtle.Turtle()
screen = turtle.Screen()
screen.title("liron us states game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.setup(width=BLANK_STATES_IMAGE_WIDTH, height=BLANK_STATES_IMAGE_HEIGHT)
# making data frame
data = pandas.read_csv("50_states.csv")
# making the state list and lower all the items
data_state_list = data.state.to_list()
data_state_list = [each_state.lower() for each_state in data_state_list]


def main():
    user_need_to_learn_list = []
    user_score = FIRST_USER_SCORE
    user_right_answer = []
    print("welcome to liron us state game!!! if you done with the game enter 'Exit' ")
    while user_score < NUM_STATES:
        user_answer = screen.textinput(title=f"{user_score}/50", prompt="what's another state name?")
        if user_answer == "Exit":
            user_need_to_learn_list = [state for state in data.state if str(state).lower() not in user_right_answer]
            data_frame_user_need_to_learn = pandas.DataFrame(user_need_to_learn_list)
            data_frame_user_need_to_learn.to_csv("need_to_learn.csv")
            break
        for index, state in enumerate(data.state):
            if str(user_answer).lower() == str(data.iloc[index, 0]).lower() and str(
                    user_answer).lower() not in user_right_answer:
                write_on_screen(data.iloc[index, X_COLUMN], data.iloc[index, Y_COLUMN], user_answer.lower(), STATE_FONT)
                user_score += 1
                user_right_answer.append(user_answer)
        # looping for all the states and checking if the user was right

    if user_score == NUM_STATES:
        write_on_screen(WELL_DONE_X_SPOT, WELL_DONE_Y_SPOT, WELL_DONE_TEXT, WELL_DONE_FONT)
        turtle.mainloop()


def write_on_screen(x_loc: int, y_loc: int, text: str, font: tuple) -> None:
    """
    update the score of the users and show to screen
    Parameters: x_loc: int - the x coordinate of text, y_loc: int - the y coordinate of text
    text: str - the text data, font: tuple - the font style
    Returns: None
    """
    pen.penup()
    pen.hideturtle()
    pen.color("black")
    pen.goto(x_loc, y_loc)
    pen.write(text, font=font, align=ALIGN)


if __name__ == "__main__":
    main()
