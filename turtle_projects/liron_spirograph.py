import random
import turtle

color_list = ["blue", "green", "red", "cyan", "magenta", "yellow", "black", "white"]


def main():
    turtle.speed(1000)
    s = turtle.Screen()
    turtle.title("liron_spirograph")
    draw_spirograph(2)


def draw_spirograph(tilt: int) -> None:
    for _ in range(int(360 / tilt)):
        turtle.color(random.choice(color_list))
        turtle.circle(100)
        turtle.setheading(turtle.heading() + tilt)

    turtle.exitonclick()


if __name__ == "__main__":
    main()
