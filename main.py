from turtle import *
from math import *


def triangle(x, y, turn, side1, side2, angle, border, brdclr, bgclr):
    """"

    x, y - position
    turn - starting side1 angle
    border - border width

    """

    pass


def ellipse(x, y, turn, a, b, border, brdclr, bgclr):
    """"

    x, y - position
    a, b - semi-axes
    turn - starting a angle
    border - border width

    """

    pass


def half_ellipse(x, y, turn, a, b, border, brdclr, bgclr):
    """"

    x, y - position
    a, b - semi-axes
    turn - starting a angle
    border - border width

    """

    pass


def rectangle(x, y, turn, a, b, border, brdclr, bgclr):
    """"

    x, y - position
    turn - starting a angle
    border - border width

    """

    pass


def n_shape(x, y, turn, length, n, border, brdclr, bgclr):
    """

    x, y - position
    turn - starting a angle
    border - border width

    """
    shape("turtle")

    a, b = map(float, input("Enter coordinates x, y: ").split())
    length = float(input("Enter side length: "))
    n = int(input("Enter the amount of angles: "))
    border = float(input("Enter border width: "))
    color("pink", "cyan")

    setx(a)
    sety(b)
    pensize(border)

    begin_fill
    pd()
    for i in range(n):
        fd(length)
        rt(360 / n)
    end_fill
    pu()
    done()



    pass


def rhomb(x, y, turn, length, angle, border, brdclr, bgclr):
    """

    x, y - position
    turn - starting a angle
    border - border width

    """

    pass


def trap(x, y, turn, a, b, h, angle, border, brdclr, bgclr):
    """

    x, y - position
    a, b - bases
    h - height
    turn - starting a angle
    border - border width

    """

    pass


def left():
    """

    Igor
    x: [-400; -133]

    """
    pass


def middle():
    """

    Ira
    x: [-134; 133]

    """
    pass


def right():
    """

    Sasha
    x: [134; 400]

    """
    pass


def execute_main():
    left()
    middle()
    right()


if __name__ == '__main__':
    execute_main()
