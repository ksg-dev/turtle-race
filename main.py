from turtle import Turtle, Screen


screen = Screen()
screen.setup(500, 500)
screen.colormode(255)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")
color_list = ["red", "orange", "yellow", "green", "blue", "purple"]
lineup = [-100, -60, -20, 20, 60, 100]


def create_turtles(no_turtles):
    for i in range(0, no_turtles):
        y = lineup[i]
        col = color_list[i]
        i = Turtle(shape="turtle")
        i.penup()
        i.color(col)
        i.goto(x=-220, y=y)


create_turtles(6)


screen.exitonclick()
