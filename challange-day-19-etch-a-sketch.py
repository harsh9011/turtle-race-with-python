# w = forward
# s = backwards
# A = counter-clockwise
# D = clockwise
# C = clear-drawing

from turtle import Turtle,Screen

tim = Turtle()
screen = Screen()


# w = forward
def forward():
    tim.forward(20)


# s = backward
def backward():
    tim.backward(20)

# A = counter-clockwise

def counter_clock_left():
    tim.left(10)


 #D = clockwise
def clockwise_right():
    tim.right(10)


# c = clear
def clear():
    tim.clear()



screen.listen()
screen.onkey(key="w", fun=forward)
screen.onkey(key="s", fun=backward)
screen.onkey(key="a", fun=counter_clock_left)
screen.onkey(key="d", fun=clockwise_right)
screen.onkey(key="c", fun=clear)

screen.exitonclick()





