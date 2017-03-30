#used functions that include functions
#Brianna Odell and Nicole Ferris
#project

import turtle
from functionfile2 import*
bob = turtle.Turtle()
bob.pensize(3)
bob.speed(11)
turtle.bgcolor('medium aquamarine')

for times in range(50):
    cool(bob,55-times*5)
    bob.forward(times*6)
    bob.right(70)

