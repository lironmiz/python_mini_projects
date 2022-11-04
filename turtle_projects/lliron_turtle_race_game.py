import turtle as turtle_module
import random

turtle = turtle_module.Turtle()
turtle1 = turtle_module.Turtle()
turtle2 = turtle_module.Turtle()
turtle3 = turtle_module.Turtle()
turtle4 = turtle_module.Turtle()

color_list = ["blue", "green", "red", "cyan", "magenta"]
turtle_list = [turtle, turtle1, turtle2, turtle3, turtle4]
turtle_forward_list = [10, 40, 60, 200, 5, 12, 56, 3, 7, 22, 77, 33, 88, 57, 125]


def main():
    turtle_module.title("liron race program")
    screen = turtle_module.Screen()
    screen.setup(width=1200, height=400)
    turtle_module.write("liron_race_program", font=("Verdana", 15, "normal"), align='center')
    set_turtles_starting_position()
    player_guss = turtle_module.textinput("guess_area ", "enter which turtle you think will win the game")
    
    winning_turtle = turtle1
    is_game_on = True
    while is_game_on:
        rand_turtle = random.choice(turtle_list)
        rand_turtle.fd(random.choice(turtle_forward_list))
        if rand_turtle.xcor() > 560:
            is_game_on = False
            winning_turtle = rand_turtle

    if player_guss.lower() == str(winning_turtle.pencolor()).lower():
        print("you win!!")
    else:
        print(F"you lose the wining turtle is the {winning_turtle.pencolor()}")

    turtle_module.exitonclick()


def set_turtles_starting_position() -> None:
    y_pos = 50
    for index, tur_object in enumerate(turtle_list):
        tur_object.color(color_list[index])
        tur_object.penup()
        tur_object.shapesize(2)
        tur_object.shape("turtle")
        tur_object.goto(-560, y_pos*index -90 )


if __name__ == "__main__":
    main()
