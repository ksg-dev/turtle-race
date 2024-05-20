from turtle import Turtle, Screen

t = Turtle()
screen = Screen()


def go_forward():
    t.forward(10)


def go_backward():
    t.backward(10)


def turn_left():
    t.left(10)


def turn_right():
    t.right(10)


def clear():
    screen.resetscreen()


screen.listen()
screen.onkey(fun=go_forward, key="w")
screen.onkey(fun=go_backward, key="s")
screen.onkey(fun=turn_left, key="a")
screen.onkey(fun=turn_right, key="d")
screen.onkey(fun=clear, key="c")

screen.exitonclick()
