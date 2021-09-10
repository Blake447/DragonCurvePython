import numpy as np
import turtle as Turtle

def NthTerm(n):
    c = 0
    for i in range( n.bit_length() + 1):
            c += ( ( ( n + (1 << i) ) >> (i + 1) ) & 1 )
    return c

def cursed_n_choose_c(n, c):
    j = 1 << n
    count = 0
    for i in range (j):
        if (NthTerm(i) == c):
            count += 1
    return count

def NthVector(n, p):
    vx = [0, 1, 0,-1]
    vy = [1, 0,-1, 0]

    a = (NthTerm(n) + (p >> 1)     ) & 3
    b = (NthTerm(n) + (p >> 1) + 1 ) & 3

    s = 1 << (p >> 1)

    return [ ( vx[a] + vx[b]*(p & 1) )*s, ( vy[a] + vy[b]*(p & 1) )*s ]

def NthPosition(n):
    max_iterations = 29
    p = 0
    c = 1 << max_iterations
    v = [0,0]

    for i in range(max_iterations + 1):
        j = max_iterations - i

        if ( (n & c) == c ):
            dv = NthVector(p, j)
            v = [ v[0] + dv[0], + v[1] + dv[1] ]
            p += c
        c = (c >> 1)

    return v


def main():
    print("Hello world!")

    print("4 choose 3 = " + str(cursed_n_choose_c(4, 3)))

    iterations = 21
    scale = 3

    screen = Turtle.Screen()
    screen.setup(width=1280, height=720, startx=0, starty=0)
    turtle = Turtle.RawTurtle(screen)
    turtle.penup()
    turtle.setposition(0,0)
    turtle.pendown()

    for i in range( (1 << iterations) + 1):
        v = NthPosition(i)
        turtle.setposition(v[0]*scale, v[1]*scale)

    screen.exitonclick()

if __name__ == "__main__":
    main()
