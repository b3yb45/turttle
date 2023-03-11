from turtle import *
from math import *


def triangle(x, y, turn, side1, side2, angle, border, brdclr, bgclr):
    """"

    x, y - position
    turn - starting side1 angle
    border - border width

    """

    x, y = map(float, input('x, y =').split())  # Parameters.
    turn = int(input('turn ='))
    brdclr, bgclr = input('colors =').split()  # Colors of border and figure.
    side1, side2 = map(float, input('sides=').split())  # Length of sides.
    border = float(input('pen size ='))
    angle1 = int(input('angle ='))  # Angle between two sides

    pu()
    setx(x)
    sety(y)
    color(brdclr, bgclr)
    pensize(border)
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
    done()


def arc(x0, y0, turn, a, b, angle=360, border=1, brdclr='black', fill=''):
    """

    x0, y0 - position
    a, b - semi-axes
    turn - shape tilt
    angle - part of ellipse
    border - border width
    brdclr, bgclr - shape colors


    """

    # setting shape parameters
    pensize(border)
    color(brdclr, fill)

    prev_pos = pos()
    head = heading()
    turn = radians(turn)

    # start
    if isdown():
        pu()
    goto(x0, y0)

    # drawing
    pd()
    color(brdclr, fill)
    begin_fill()
    for deg in range(angle + 1):
        rad = radians(deg)
        x = (a * cos(rad) + x0) * cos(turn) - (b * sin(rad) + y0) * sin(turn)
        y = (a * cos(rad) + x0) * sin(turn) + (b * sin(rad) + y0) * cos(turn)
        print(x, " ", y)
        goto(x, y)
    xs = (a * cos(0) + x0) * cos(turn) - (b * sin(0) + y0) * sin(turn)
    ys = (a * cos(0) + x0) * sin(turn) + (b * sin(0) + y0) * cos(turn)
    goto(xs, ys)
    end_fill()

    # returning
    pu()
    goto(prev_pos)
    seth(head)


def rectangle(x, y, turn, a, b, border, brdclr, bgclr):
    """"

    x, y - position
    turn - starting a angle
    border - border width

    """

    x, y = map(float, input('x, y = ').split())  # Parameters.
    turn = int(input('turn ='))
    brdclr, bgclr = input('colors = ').split()  # Color of border and figure.
    a, b = map(float, input('length, width =').split())  # Length and width of figure.
    border = float(input('pen size ='))

    pu()
    setx(x)
    sety(y)
    color(brdclr, bgclr)
    pensize(border)
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
    done()


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

    x, y = map(int, input('x, y =').split())  # Parameters.
    turn = int(input('turn ='))
    brdclr, bgclr = input('color =').split()  # Colors of border and figure.
    length = float(input('sides ='))  # Sides of figure.
    border = float(input('pensize ='))
    angle = int(input('angle ='))

    pu()
    setx(x)
    sety(y)
    pensize(border)
    color(brdclr, bgclr)
    rt(turn)
    pd()
    begin_fill()
    for i in range(2):
        fd(length)
        lt(180 - angle)
        fd(length)
        lt(angle)
    end_fill()
    pu()
    done()


def trap(x0, y0, turn, a, b, h, border=1, brdclr="black", fill=''):
    """

    x0, y0 - position
    a, b - bases
    h - trapezoid height
    turn - shape tilt
    border - border width
    brdclr, bgclr - shape colors

    """

    # setting shape parameters
    pensize(border)
    color(brdclr, fill)

    prev_pos = pos()
    head = heading()
    lt(turn)

    # start
    if isdown():
        pu()
    goto(x0, y0)

    if b > a:
        a, b = b, a

    # drawing
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

    # returning
    pu()
    goto(prev_pos)
    seth(head)


def left():
    """

    Igor
    x: [-900; -300]
    y: [-500; 500]

    """
    speed(1)
    trap(500, 200, 90, 100, 50, 50)
    trap(900, 500, 180, 100, 50, 50)
    arc(200, 100, 45, 50, 20)


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
