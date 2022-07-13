from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def move_left():
    tim.left(25)


def move_right():
    tim.right(25)


def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_right, "d")
screen.onkey(move_left, "a")
screen.onkey(move_backwards, "s")
screen.onkey(clear_screen, "c")
screen.exitonclick()
