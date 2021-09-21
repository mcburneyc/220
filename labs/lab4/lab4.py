"""
Name: Cooper McBurney
lab4.py
Problem: Learn to Use Python Graphics and approximate pi.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import *


def squares():
    """  <---  You can use tripled quotes to write a multi-line comment....

    Modify the following function to:

    Draw squares (20 X 20) instead of circles. Make sure that the center of the square
    is at the point where the user clicks. Make the window 400 by 400.

    Have each successive click draw an additional square on the screen (rather
    than just moving the existing one).

    Display a message on the window "Click again to quit" after the loop, and
    wait for a final click before closing the window.
    """
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to move square")
    instructions.draw(win)

    # builds a circle
    shape = Rectangle(Point(50, 50), Point(100, 100))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the circle
    for i in range(num_clicks):
        p = win.getMouse()
        c = shape.getCenter()  # center of circle

        shape2 = shape.clone()
        shape2.draw(win)

        # move amount is distance from center of circle to the
        # point where the user clicked
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        shape.move(dx, dy)

    instructions.undraw()
    msg_pt = (Point(width / 2, height - 10))
    end_message = Text(msg_pt, "Click again to quit")
    end_message.draw(win)



    win.getMouse()
    win.close()


def rectangle():
    """
    This program displays information about a rectangle drawn by the user.
    Input: Two mouse clicks for the opposite corners of a rectangle.
    Output: Draw the rectangle.
         Print the perimeter and area of the rectangle.
    Formulas: area = (length)(width)   and    perimeter = 2(length+width)
    """

    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to create rectangle")
    instructions.draw(win)

    point_1 = win.getMouse()
    point_1.draw(win)
    point_2 = win.getMouse()
    point_2.draw(win)

    shape = Rectangle(point_1, point_2)
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    win.getMouse()
    win.close()

    a = point_1.getX()
    b = point_2.getX()
    length = b - a

    c = point_1.getY()
    d = point_2.getY()
    width = d - c

    perimeter = 2 * (length + width)
    area = length * width

    print("The Perimeter is", perimeter)
    print("The Area is", area)


def circle():
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to create circle")
    instructions.draw(win)

    center = win.getMouse()
    center.draw(win)
    circumference = win.getMouse()
    circumference.draw(win)

    x1 = center.getX()
    x2 = circumference.getX()
    y1 = center.getY()
    y2 = circumference.getY()

    radius = ((x1-x2) ** 2 + (y1 - y2) ** 2) ** (1/2)

    shape = Circle(center, radius)
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)


    win.getMouse()
    win.close()

    print(" Your radius is", radius)

def pi2():
    n = eval(input"Enter value for n:")
    terms_to_sum = eval(input"Enter the number of terms to sum:")
    sum = 0
    for i in range (terms_to_sum):



def main():
    # squares()
    # rectangle()
    circle()
    # pi2()


main()
