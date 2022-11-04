import turtle
import random

color_list = ["blue", "green", "red", "cyan", "magenta", "yellow", "black", "white"]
screen = turtle.Screen()
pen_size = 2
TURTLE_STEP = 40


def main():
    change_pen_size(0)
    turtle.speed("fastest")
    turtle.title("liron draw program")
    turtle.write("liron_draw_program", font=("Verdana", 15, "normal"), align='center')
    print("""
    hii, welcome to liron draw program! the keys are:
    'w' - forward
    's' - 'backward
    'd' - clock_wise
    'a' - counter clock wise
    'p' - change color
    'f' - increase pen size
    'g' - decrease pen size 
    'c' - clear screen""")

    screen.listen()
    screen.onkey(fun=lambda: turtle.fd(40), key="w")
    screen.onkey(fun=lambda: turtle.fd(-40), key="s")
    screen.onkey(fun=lambda: turtle.left(15), key="d")
    screen.onkey(fun=lambda: turtle.right(15), key="a")
    screen.onkey(fun=turtle.clear, key="c")
    screen.onkey(fun=change_color, key="p")
    screen.onkey(fun=lambda: change_pen_size(1), key="f")
    screen.onkey(fun=lambda: change_pen_size(-1), key="g")

    screen.exitonclick()


def change_color() -> None:
    turtle.pencolor(random.choice(color_list))


def change_pen_size(size_change: int) -> None:
    global pen_size
    pen_size += size_change
    if (pen_size <= 0):
        pen_size = 1
    turtle.shapesize(int(pen_size / 2 + 0.5))
    turtle.pensize(pen_size)


if __name__ == "__main__":
    main()
