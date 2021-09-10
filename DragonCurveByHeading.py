import numpy as np
import turtle as Turtle

def NthTerm(n):
    c = 0
    for i in range( n.bit_length() + 1):
        c += ( ( ( n + (1 << i) ) >> (i + 1) ) % 2 )
    return(c % 4)

def main():
    screen = Turtle.Screen()
    screen.setup(width=1280, height=720, startx=0, starty=0)
    turtle = Turtle.RawTurtle(screen)
    turtle.penup()
    turtle.setposition(screen.window_width()*0.25,-screen.window_height()*0.25)
    turtle.pendown()
    turtle.hideturtle()
    turtle.speed(10)
    
    for i in range(256*256):
        turtle.setheading(NthTerm(i)*90)
        turtle.forward(3)


    screen.exitonclick()


if __name__ == "__main__":
    main()
