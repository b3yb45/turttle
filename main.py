from turtle import *
from math import *


def triangle(x, y, turn, side_1, side_2, angle, border, brdclr="black", fill=''):
    """"
    x, y - position
    turn - starting side1 angle
    border - border width
    """

    # Setting the parameters.
    color(brdclr, fill)
    pensize(border)
    angle_1 = radians(angle)
    head = heading()
    posit = pos()

    side_3 = sqrt(side_1 ** 2 + side_2 ** 2 - 2 * side_1 * side_2 * cos(angle_1))
    angle_2 = degrees(acos((side_1 ** 2 + side_3 ** 2 - side_2 ** 2)/(2 * side_1 * side_3)))
    angle_3 = degrees(acos((side_2 ** 2 + side_3 ** 2 - side_1 ** 2)/(2 * side_2 * side_3)))

    # Drawing.
    pu()
    goto(x, y)
    lt(turn)
    pd()
    begin_fill()
    fd(side_1)
    lt(180 - angle_2)
    fd(side_3)
    lt(180 - angle_3)
    fd(side_2)
    lt(180 - degrees(angle_1))
    end_fill()

    # Return.
    pu()
    goto(posit)
    seth(head)


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
    head = heading()
    posit = pos()

    # Drawing.
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
    goto(posit)
    seth(head)
def rhomb(x, y, turn, length, angle, border, brdclr="black", fill=''):
    """
    x, y - position
    turn - starting a angle
    border - border width
    """

    # Setting the parameters.
    color(brdclr, fill)
    pensize(border)
    head = heading()
    posit = pos()

    # Drawing.
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
    goto(posit)
    seth(head)


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

def execute_main():

    bgcolor("dodgerblue")

    #Grass.
    arc(0, -350, 0, 1280, 450, 180, 3, brdclr="lawngreen", fill='lawngreen')

    #Tree: rec, many ovals.
    rectangle(630, -85, 90, 500, 105, 1, brdclr="sienna", fill='sienna')

    arc(590, -70, 0, 150, 100, 360, 1, brdclr="forestgreen", fill='forestgreen')
    arc(570, -110, 0, 150, 100, 360, 1, brdclr="forestgreen", fill='forestgreen')
    arc(600, -100, 0, 150, 100, 360, 1, brdclr="forestgreen", fill='forestgreen')
    arc(500, -75, 0, 150, 100, 360, 1, brdclr="forestgreen", fill='forestgreen')
    arc(500, -40, 0, 150, 100, 360, 1, brdclr="forestgreen", fill='forestgreen')
    arc(520, -10, 0, 150, 100, 360, 1, brdclr="forestgreen", fill='forestgreen')
    arc(580, 10, 0, 150, 100, 360, 1, brdclr="forestgreen", fill='forestgreen')

    #Sun.
    arc(375, 225, 0, 125, 125, 360, 1, brdclr="gold", fill='gold')

    #Clouds.
    arc(-450, 50, 0, 100, 75, 180, 1, brdclr="white", fill='white')
    arc(-380, 50, 0, 100, 75, 180, 1, brdclr="white", fill='white')
    arc(-415, 75, 0, 100, 75, 180, 1, brdclr="white", fill='white')

    arc(-150, 0, 0, 100, 75, 180, 1, brdclr="white", fill='white')
    arc(-80, 0, 0, 100, 75, 180, 1, brdclr="white", fill='white')
    arc(-115, 25, 0, 100, 75, 180, 1, brdclr="white", fill='white')

    arc(-220, 120, 0, 100, 75, 180, 1, brdclr="white", fill='white')
    arc(-150, 120, 0, 100, 75, 180, 1, brdclr="white", fill='white')
    arc(-185, 145, 0, 100, 75, 180, 1, brdclr="white", fill='white')

    # Duck.
    arc(-50, -55, 0, 50, 50, 360, 1, brdclr="yellow", fill='yellow')
    arc(-50, -55, 0, 10, 10, 360, 1, brdclr="black", fill='black')
    triangle(-99, -55, -17, 25, 25, 35, 1, brdclr="red", fill='red')

    triangle(0, -100, 250, 30, 30, 30, 1, brdclr="orange", fill='orange')
    triangle(20, -100, 270, 30, 30, 30, 1, brdclr="orange", fill='orange')

    arc(10, -80, 0, 100, 50, 360, 1, brdclr="yellow", fill='yellow')
    arc(-10, 75, 180, 65, 45, 180, 1, brdclr="black", fill='gold')

    # Duckling
    arc(110, -90, 0, 25, 25, 360, 1, brdclr="yellow", fill='yellow')
    arc(110, -90, 0, 5, 5, 360, 1, brdclr="black", fill='black')
    triangle(87, -90, -15, 10, 10, 30, 1, brdclr="red", fill='red')

    triangle(135, -115, 250, 15, 15, 30, 1, brdclr="orange", fill='orange')
    triangle(145, -115, 270, 15, 15, 30, 1, brdclr="orange", fill='orange')

    arc(140, -105, 0, 50, 25, 360, 1, brdclr="yellow", fill='yellow')
    arc(-140, 103, 180, 32, 22, 180, 1, brdclr="black", fill='gold')

    # Catepillar.
    arc(-400, -240, 0, 30, 30, 360, 1, brdclr="hotpink", fill='hotpink')
    arc(-405, -237, 0, 5, 5, 360, 1, brdclr="black", fill='black')
    arc(-395, -237, 0, 5, 5, 360, 1, brdclr="black", fill='black')
    arc(-390, -220, 0, 10, 10, 360, 1, brdclr="deeppink", fill='deeppink')
    arc(-410, -220, 0, 10, 10, 360, 1, brdclr="deeppink", fill='deeppink')

    arc(-375, -255, 0, 25, 25, 360, 1, brdclr="orchid", fill='orchid')
    arc(-350, -245, 0, 22, 22, 360, 1, brdclr="purple", fill='purple')
    arc(-332, -260, 0, 19, 19, 360, 1, brdclr="royalblue", fill='royalblue')
    arc(-312, -265, 0, 16, 16, 360, 1, brdclr="teal", fill='teal')

    done()


if __name__ == '__main__':
    execute_main()

execute_main()