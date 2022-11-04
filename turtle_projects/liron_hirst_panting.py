import turtle
import random

color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40),
              (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148),
              (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171),
              (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100),
              (107, 127, 153), (174, 94, 97), (176, 192, 209)]

def main():
    turtle.title("liron hirst program")
    turtle.colormode(255)
    turtle.speed("fastest")
    turtle.penup()
    turtle.hideturtle()
    turtle.setheading(225)
    turtle.forward(300)
    turtle.setheading(0)
    number_of_dots = 100

    for dot_count in range(1, number_of_dots + 1):
        turtle.dot(20, random.choice(color_list))
        turtle.forward(50)
        if dot_count % 10 == 0:
            turtle.setheading(90)
            turtle.forward(50)
            turtle.setheading(180)
            turtle.forward(500)
            turtle.setheading(0)
    screen = turtle.Screen()
    screen.exitonclick()

if __name__ == "__main__":
    main()