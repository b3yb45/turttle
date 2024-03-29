'''

    Igor Andreev - 35
    Aronova Alexandra - 40
    Murashova Irina - 50

'''


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
    a_s = a * s
    a_c = a * c
    b_s = b * s
    b_c = b * c

    # Drawing.
    color(brdclr, fill)
    begin_fill()
    for deg in range(0, angle + 1, 5):
        rad = radians(deg)
        x = a_c * cos(rad) + xc0 - b_s * sin(rad) - ys0
        y = a_s * cos(rad) + xs0 + b_c * sin(rad) + yc0
        goto(x, y)
        pd()
    xs = a_c + xc0 - ys0
    ys = a_s + xs0 + yc0
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


def execute_main():
    setup(1200, 600)
    speed(10)

    bgcolor("dodgerblue")

    # Grass.
    arc(0, -350, 0, 1280, 450, 180, 3, "lawngreen", 'lawngreen')

    # Lake.
    arc(100, -300, 0, 600, 150, 270, 3, "blue", 'blue')

    # Flowers.
    for i in range(5):
        arc(-150, 200 + i * 50, 90, 50, 15, 180, 1, "forestgreen", 'forestgreen')
        triangle(-200 - i * 50, -125, 67.5, 20, 20, 45, 1, "red", "red")

    # Tree: rec, many ovals.
    rectangle(630, -85, 90, 500, 105, 1, "sienna", 'sienna')

    arc(590, -70, 0, 150, 100, 360, 1, "forestgreen", 'forestgreen')
    arc(570, -110, 0, 150, 100, 360, 1, "forestgreen", 'forestgreen')
    arc(600, -100, 0, 150, 100, 360, 1, "forestgreen", 'forestgreen')
    arc(500, -75, 0, 150, 100, 360, 1, "forestgreen", 'forestgreen')
    arc(500, -40, 0, 150, 100, 360, 1, "forestgreen", 'forestgreen')
    arc(520, -10, 0, 150, 100, 360, 1, "forestgreen", 'forestgreen')
    arc(580, 10, 0, 150, 100, 360, 1, "forestgreen", 'forestgreen')

    # Sun.
    arc(375, 225, 0, 125, 125, 360, 1, "gold", 'gold')

    # Clouds.
    arc(-450, 50, 0, 100, 75, 180, 1, "white", 'white')
    arc(-380, 50, 0, 100, 75, 180, 1, "white", 'white')
    arc(-415, 75, 0, 100, 75, 180, 1, "white", 'white')

    arc(-150, 0, 0, 100, 75, 180, 1, "white", 'white')
    arc(-80, 0, 0, 100, 75, 180, 1, "white", 'white')
    arc(-115, 25, 0, 100, 75, 180, 1, "white", 'white')

    arc(-220, 120, 0, 100, 75, 180, 1, "white", 'white')
    arc(-150, 120, 0, 100, 75, 180, 1, "white", 'white')
    arc(-185, 145, 0, 100, 75, 180, 1, "white", 'white')

    # Duck.
    arc(-50, -55, 0, 50, 50, 360, 1, "yellow", 'yellow')
    arc(-50, -55, 0, 10, 10, 360, 1, "black", 'black')
    triangle(-99, -55, -17, 25, 25, 35, 1, "red", 'red')

    triangle(0, -100, 250, 30, 30, 30, 1, "orange", 'orange')
    triangle(20, -100, 270, 30, 30, 30, 1, "orange", 'orange')

    arc(10, -80, 0, 100, 50, 360, 1, "yellow", 'yellow')
    arc(-10, 75, 180, 65, 45, 180, 1, "black", 'gold')

    # Duckling
    arc(110, -90, 0, 25, 25, 360, 1, "yellow", 'yellow')
    arc(110, -90, 0, 5, 5, 360, 1, "black", 'black')
    triangle(87, -90, -15, 10, 10, 30, 1, "red", 'red')

    triangle(135, -115, 250, 15, 15, 30, 1, "orange", 'orange')
    triangle(145, -115, 270, 15, 15, 30, 1, "orange", 'orange')

    arc(140, -105, 0, 50, 25, 360, 1, "yellow", 'yellow')
    arc(-140, 103, 180, 32, 22, 180, 1, "black", 'gold')

    # Caterpillar.
    arc(-400, -240, 0, 30, 30, 360, 1, "hotpink", 'hotpink')
    arc(-405, -237, 0, 5, 5, 360, 1, "black", 'black')
    arc(-395, -237, 0, 5, 5, 360, 1, "black", 'black')
    arc(-390, -220, 0, 10, 10, 360, 1, "deeppink", 'deeppink')
    arc(-410, -220, 0, 10, 10, 360, 1, "deeppink", 'deeppink')

    arc(-375, -255, 0, 25, 25, 360, 1, "orchid", 'orchid')
    arc(-350, -245, 0, 22, 22, 360, 1, "purple", 'purple')
    arc(-332, -260, 0, 19, 19, 360, 1, "royalblue", 'royalblue')
    arc(-312, -265, 0, 16, 16, 360, 1, "teal", 'teal')
    done()


if __name__ == '__main__':
    execute_main()
