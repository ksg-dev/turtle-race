from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.shape("turtle")


def go_forward():
    tim.forward(10)


screen.listen()
screen.onkey(key="space", fun=go_forward)

screen.exitonclick()
