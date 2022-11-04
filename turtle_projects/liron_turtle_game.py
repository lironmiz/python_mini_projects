import random
import turtle

player_one = turtle.Turtle()
player_two = turtle.Turtle()


def main():


    s = turtle.Screen()
    turtle.title("liron_race_game")
    turtle.write("race game:", font=("Verdana", 15, "normal"), align='center')
    turtle.hideturtle()
    start_position_turtle()
    make_circles()
    player_turn = 0
    while chack_state_turtle():
        p = player_turn % 2
        if p == 0:
            die_outcome = game_input_user(p + 1)
            player_one.fd(20 * die_outcome)
        else:
            die_outcome = game_input_user(p + 1)
            player_two.fd(20 * die_outcome)
        player_turn += 1

    turtle.exitonclick()

def game_input_user(num_player: int) -> int:
    # take user input
    turtle.textinput("promt ", F"player {num_player} enter roll to roll the dice")
    die_outcome = random.randint(1, 6)
    return die_outcome


def chack_state_turtle() -> bool:
    # chack if turtle is got to final place
    if player_one.pos()[0] >= 300:
        print("player 1 win!")
        return False
    elif player_two.pos()[0] >= 300:
        print("player 2 win!")
        return False
    return True


def start_position_turtle() -> None:
    # starting point
    player_one.color("red")
    player_one.shape("turtle")
    player_one.penup()
    player_one.goto(-200, 100)
    player_two.color("blue")
    player_two.shape("turtle")
    player_two.penup()
    player_two.goto(-200, -100)


def make_circles() -> None:
    # make circles
    player_one.speed(20)
    player_one.goto(300, 60)
    player_one.pendown()
    player_one.begin_fill()
    player_one.circle(40)
    player_one.end_fill()
    player_one.penup()
    player_one.goto(-200, 100)
    player_two.speed(20)
    player_two.goto(300, -140)
    player_two.pendown()
    player_two.begin_fill()
    player_two.circle(40)
    player_two.end_fill()
    player_two.penup()
    player_two.goto(-200, -100)


if __name__ == "__main__":
    main()
