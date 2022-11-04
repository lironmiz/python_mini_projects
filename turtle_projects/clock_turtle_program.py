import turtle
from datetime import datetime

FONT_TEXT = ("Verdana", 15, "normal")
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
ANGLE_DIFFERENCE_BETWEEN_HOUR = 30
ANGLE_DIFFERENCE_BETWEEN_MINUTE = 6
CLOCK_RADUIS = 250
NUM_HOUR = 12
SMALL_HAND_LEN = 100
BIG_HAND_LEN = 150
hour_dict = {1: 60, 2: 30, 3: 360, 4: 330, 5: 300, 6: 270, 7: 240, 8: 210, 9: 180, 10: 150, 11: 130, 12: 90}

# Clock object
clock = turtle.Turtle()
# Screen object
screen = turtle.Screen()
# Small hand clock object
clock_small_hand = turtle.Turtle()
# Big hand clock object
clock_big_hand = turtle.Turtle()
# Time
current_time = datetime


def main():
    # Turtle object
    turtle.title("liron clock program")
    turtle.hideturtle()
    turtle.penup()
    turtle.setheading(UP)
    turtle.fd(280)
    turtle.write("liron_clock_program", font=FONT_TEXT, align='center')

    clock.speed('fastest')
    clock.hideturtle()

    screen.tracer()

    clock_small_hand.color("red")
    clock_small_hand.pensize(10)
    clock_small_hand.shape('arrow')

    clock_big_hand.color("black")
    clock_big_hand.pensize(10)
    clock_big_hand.shape("arrow")

    # Make body of the clock
    clock.pensize(10)
    clock.pencolor("black")
    clock.penup()
    clock.setheading(DOWN)
    clock.fd(250)
    clock.pendown()
    clock.setheading(0)
    for num in range(NUM_HOUR * 5):
        if num % 5 == 0:
            clock.setheading(clock.heading() + UP)
            clock.fd(80)
            clock.bk(80)
            clock.setheading(clock.heading() - UP)
            clock.circle(CLOCK_RADUIS, ANGLE_DIFFERENCE_BETWEEN_HOUR / 5)
        else:
            clock.setheading(clock.heading() + UP)
            clock.fd(50)
            clock.bk(50)
            clock.setheading(clock.heading() - UP)
            clock.circle(CLOCK_RADUIS, ANGLE_DIFFERENCE_BETWEEN_HOUR / 5)

    while True:
        set_minute = calclute_hading_min()
        update_time(set_minute)
        screen.update()

    turtle.exitonclick()


def calclute_hading_min() -> None:
    return 90 - (current_time.now().minute / 60) * 360


def update_time(hading_minute: int) -> None:
    # Make hand of clock
    clock_small_hand.clear()
    clock_big_hand.clear()
    if current_time.now().hour % NUM_HOUR == 0:
        clock_small_hand.setheading(hour_dict[NUM_HOUR])
        clock_big_hand.setheading(hading_minute)
    else:
        clock_small_hand.setheading(hour_dict[current_time.now().hour % NUM_HOUR])
        clock_big_hand.setheading(hading_minute)
    clock_small_hand.fd(SMALL_HAND_LEN)
    clock_small_hand.bk(SMALL_HAND_LEN)
    clock_big_hand.fd(BIG_HAND_LEN)
    clock_big_hand.bk(BIG_HAND_LEN)


if __name__ == "__main__":
    main()
