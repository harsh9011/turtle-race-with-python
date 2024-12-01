import turtle
from random import random
from turtle import Turtle,Screen
import random


is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
user_bet = turtle.textinput(title="make your bet ", prompt="which turtle will win the race ? enter a color :- ")


colour = ["red","orange","yellow","green","blue","purple"]

all_turtles = []

y_position = [-70,-40,-10,20,50,80]

screen.bgpic("giphym.gif")

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colour[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

# random number
while is_race_on:



    for turtle in all_turtles:

        if turtle.xcor() > 230:
            print(turtle.color())
            is_race_on = False
            winning_colour = turtle.pencolor()


            if winning_colour == user_bet:
                print(f"You've won ! The {winning_colour} turtle is the Winner !")

            else:
                print(f"You've lost ! The {winning_colour} turtle is the winner !")




        random_distance = random.randint(0,10)
        turtle.forward(random_distance)


screen.exitonclick()