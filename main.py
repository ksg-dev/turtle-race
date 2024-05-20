from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 500)
screen.colormode(255)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")
color_list = ["red", "orange", "yellow", "green", "blue", "purple"]
lineup = [-100, -60, -20, 20, 60, 100]
turtles = []


def create_turtles(no_turtles):
    for i in range(0, no_turtles):
        y = lineup[i]
        col = color_list[i]
        i = Turtle(shape="turtle")
        i.penup()
        i.color(col)
        i.goto(x=-220, y=y)
        turtles.append(i)


def main():
    racing = False
    if user_bet:
        create_turtles(6)
        racing = True
    while racing:
        for turtle in turtles:
            if turtle.xcor() > 230:
                racing = False
                winner = turtle.pencolor()
                if winner == user_bet:
                    print(f"You've won! The {winner} turtle is the winner!")
                else:
                    print(f"You lose! The {winner} turtle is the winner!")
            else:
                distance = random.randint(0, 10)
                turtle.forward(distance)


main()


screen.exitonclick()
