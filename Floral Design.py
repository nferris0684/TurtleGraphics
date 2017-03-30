import turtle

turtle.colormode(255)#brings in the colormode functions
turtle.bgcolor('black')

bob = turtle.Turtle()
bob.pensize(10)
bob.speed(11)

for n in range(255):#use the loop variable for the color values
    c = (255,n,n)
    bob.color(c)
    bob.circle(n)
    bob.right(200)
