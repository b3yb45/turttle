from turtle import *
from math import *


def triangle(x, y, turn, side1, side2, angle, border, brdclr="black", fill=''):
    """"

    x, y - position
    turn - starting side1 angle
    border - border width

    """

    # Setting the parameters.
    color(brdclr, fill)
    pensize(border)
    angle1 = angle

    # Start.
    pu()
    goto(x, y)
    rt(turn)
    pd()
    begin_fill()
    side3 = sqrt(side1 ** 2 + side2 ** 2 - 2 * side1 * side2 * cos(angle1))
    angle2 = degrees(acos((side3 ** 2 + side2 ** 2 - side1 ** 2) / (2 * side2 * side3)))
    angle3 = degrees(acos((side1 ** 2 + side3 ** 2 - side2 ** 2) / (2 * side1 * side3)))
    fd(side1)
    rt(180 - angle3)
    fd(side3)
    rt(180 - angle2)
    fd(side2)
    rt(180 - angle1)
    end_fill()
    pu()
    goto(0, 0)
    done()


def arc(x0=0, y0=0, turn=0, a=50, b=25, angle=360, border=1, brdclr='black', fill=''):
    """

    x0, y0 - position.
    a, b - semi-axes.
    turn - shape tilt.
    angle - part of ellipse.
    border - border width.
    brdclr, bgclr - shape colors.


    """

    # Setting shape parameters.
    pensize(border)
    color(brdclr, fill)

    prev_pos = pos()
    head = heading()

    # Start.
    pu()
    goto(x0, y0)

    # Constants.
    turn = radians(turn)
    a /= 2
    b /= 2
    s = sin(turn)
    c = cos(turn)
    xs0 = x0 * s
    xc0 = x0 * c
    ys0 = y0 * s
    yc0 = y0 * c

    # Drawing.
    color(brdclr, fill)
    begin_fill()
    for deg in range(0, angle + 1, 5):
        rad = radians(deg)
        x = a * cos(rad) * c + xc0 - b * sin(rad) * s - ys0
        y = a * cos(rad) * s + xs0 + b * sin(rad) * c + yc0
        goto(x, y)
        pd()
    xs = a * c + xc0 - ys0
    ys = a * s + xs0 + yc0
    goto(xs, ys)
    end_fill()

    # Returning.
    pu()
    goto(prev_pos)
    seth(head)


def rectangle(x, y, turn, a, b, border, brdclr="black", fill=''):
    """"

    x, y - position
    turn - starting a angle
    border - border width

    """

    # Setting the parameters.
    color(brdclr, fill)
    pensize(border)

    # Start.
    pu()
    goto(x, y)
    rt(turn)
    pd()
    begin_fill()
    for i in range(2):
        fd(a)
        rt(90)
        fd(b)
        rt(90)
    end_fill()
    pu()
    goto(0, 0)


def n_shape(x, y, turn, length, n, border, brdclr="black", fill=''):
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


def rhomb(x, y, turn, length, angle, border, brdclr="black", fill=''):
    """

    x, y - position
    turn - starting a angle
    border - border width

    """

    # Setting the parameters.
    color(brdclr, fill)
    pensize(border)

    # Start.
    pu()
    goto(x, y)
    rt(turn)
    pd()
    begin_fill()
    for i in range(2):
        print(isvisible(), "", isdown())
        fd(length)
        lt(180 - angle)
        fd(length)
        lt(angle)
    end_fill()
    pu()
    goto(0, 0)


def trap(x0=0, y0=0, turn=0, a=50, b=25, h=20, border=1, brdclr="black", fill=''):
    """

    x0, y0 - position.
    a, b - bases.
    h - trapezoid height.
    turn - shape tilt.
    border - border width.
    brdclr, bgclr - shape colors.

    """

    # Setting shape parameters.
    pensize(border)
    color(brdclr, fill)

    prev_pos = pos()
    head = heading()
    lt(turn)

    # Start.
    if isdown():
        pu()
    goto(x0, y0)

    if b > a:
        a, b = b, a

    # Drawing.
    pd()
    color(brdclr, fill)
    begin_fill()
    fd(a)
    a1 = abs(a - b) / 2
    c = sqrt(h ** 2 + a1 ** 2)
    alph = degrees(asin(h / c))
    lt(180 - alph)
    fd(c)
    lt(alph)
    fd(b)
    lt(alph)
    fd(c)
    end_fill()

    # Returning.
    pu()
    goto(prev_pos)
    seth(head)


def left():
    """

    Igor
    x: [-900; -300]
    y: [-500; 500]

    """
    """"speed(10)
    rectangle(-500, 500, 0, 1000, 1000, 1, "blue", "blue")
    arc(0, -400, 0, 3000, 500, 180, 4, "black", "green")
    arc(450, 350, 0, 200, 200, 360, 4, "black", "yellow")
    goto(0, -200)"""


def middle():
    """

    Ira
    x: [-300; 300]
    y: [-500; 500]

    """
    pass


def right():
    """

    Sasha
    x: [300; 900]
    y: [-500; 500]

    """
    pass


def execute_main():
    left()
    middle()
    right()
    done()


if __name__ == '__main__':
    execute_main()
