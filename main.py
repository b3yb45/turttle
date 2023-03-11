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


def ellipse(x0, y0, turn, a, b, border, brdclr, bgclr):
    """"

    x0, y0 - position
    a, b - semi-axes
    turn - shape tilt
    border - border width
    brdclr, bgclr - shape colors

    """

    # setting shape parameters
    pensize(border)
    color(brdclr, bgclr)

    prev_pos = pos()
    head = heading()

    # start
    seth(turn)
    pu()
    goto(x0, y0)

    # defining constants
    alph = radians(turn)
    el_a = (cos(alph) / a) ** 2 + (sin(alph) / b) ** 2
    el_b = 2 * sin(alph) * cos(alph) * (a ** -2 - b ** -2)
    el_c = (cos(alph) / b) ** 2 + (sin(alph) / a) ** 2
    el_d = 2 * (y0 * sin(alph) / b ** 2 - x0 * cos(alph) / a ** 2)
    el_e = -2 * (y0 * cos(alph) / b ** 2 + x0 * sin(alph) / a ** 2)
    el_f = (x0 / a) ** 2 + (y0 / b) ** 2 - 1

    # drawing
    pd()
    begin_fill()
    for x in range(ceil(xcor()), ceil(x0 + a * cos(alph))):
        el_dis = (el_b * x + el_e) ** 2 - 4 * el_c * (el_a * x ** 2 + el_d * x + el_f)
        if el_dis >= 0:
            y1 = ceil((-(el_b * x + el_e) + sqrt(el_dis)) / 2 / el_c)
            goto(x, y1)

    for x in range(ceil(xcor()), ceil(x0)):
        el_dis = (el_b * x + el_e) ** 2 - 4 * el_c * (el_a * x ** 2 + el_d * x + el_f)
        if el_dis >= 0:
            y2 = ceil((-(el_b * x + el_e) - sqrt(el_dis)) / 2 / el_c)
            goto(x, y2)

    # returning
    pu()
    goto(prev_pos)
    seth(head)


def half_ellipse(x0, y0, turn, a, b, border, brdclr, bgclr, clockwise=False):
    """"

    x0, y0 - position
    a, b - semi-axes
    clockwise - arc position related to a side
    turn - shape tilt
    border - border width
    brdclr, bgclr - shape colors

    """
    # setting shape parameters
    pensize(border)
    color(brdclr, bgclr)

    prev_pos = pos()
    head = heading()

    # start
    seth(turn)
    pu()
    goto(x0, y0)

    # defining constants
    alph = radians(turn)
    el_a = (cos(alph) / a) ** 2 + (sin(alph) / b) ** 2
    el_b = 2 * sin(alph) * cos(alph) * (a ** -2 - b ** -2)
    el_c = (cos(alph) / b) ** 2 + (sin(alph) / a) ** 2
    el_d = 2 * (y0 * sin(alph) / b ** 2 - x0 * cos(alph) / a ** 2)
    el_e = -2 * (y0 * cos(alph) / b ** 2 + x0 * sin(alph) / a ** 2)
    el_f = (x0 / a) ** 2 + (y0 / b) ** 2 - 1

    # drawing
    pd()
    fd(a)
    begin_fill()
    for x in range(ceil(xcor()), ceil(x0)):
        el_dis = (el_b * x + el_e) ** 2 - 4 * el_c * (el_a * x ** 2 + el_d * x + el_f)
        if el_dis >= 0:
            if clockwise:
                y = ceil((-(el_b * x + el_e) + sqrt(el_dis)) / 2 / el_c)
            else:
                y = ceil((-(el_b * x + el_e) - sqrt(el_dis)) / 2 / el_c)
            goto(x, y)

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
