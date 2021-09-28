"""
Name: Cooper McBurney
lab5.py

Problem: Learn how to use Python Graphics

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import *


def target():
    win_width = 500
    win_height = 500
    win = GraphWin("Archery Target", win_width, win_height)

    # Add code here to get the dimensions and draw the target

    # Wait for another click to exit
    win.getMouse()
    win.close()


def triangle():
    win_width = 500
    win_height = 500
    win = GraphWin("Draw a Triangle", win_width, win_height)

    inst_pt = Point(win_width / 2, win_height - 10)
    instructions = Text(inst_pt, "Click to create triangle")
    instructions.draw(win)

    # Add code here to accept the mouse clicks, draw the triangle.
    point_1 = win.getMouse()
    point_1.draw(win)
    point_2 = win.getMouse()
    point_2.draw(win)
    point_3 = win.getMouse()
    point_3.draw(win)

    shape = Polygon(point_1, point_2, point_3)
    shape.setOutline("blue")
    shape.setFill("blue")
    shape.draw(win)
    # and display its area in the graphics window.
    x1 = point_1.getX()
    x2 = point_2.getX()
    x3 = point_3.getX()
    y1 = point_1.getY()
    y2 = point_2.getY()
    y3 = point_3.getY()
    dx = x2 - x1
    dy = y2 -y1
    distance = ((dx ** 2)+(dy ** 2))**1/2
    dx2 = x3 - x2
    dy2 = y3 - y2
    distance2 = ((dx2 ** 2)+(dy2 ** 2))**1/2
    dx3 = x1 - x3
    dy3 = y1 - y3
    distance3 = ((dx3 ** 2)+(dy3 ** 2))**1/2
    perimeter = distance + distance2 + distance3

    s = (distance + distance2 + distance3) / 2
    area = (s * (s - distance) * (s - distance2) * (s - distance3)) ** 1/2

    instructions.undraw()
    msg_pt = (Point(win_width / 2, win_height - 50))
    perimeter_message = Text(msg_pt, "The perimeter is " +str(perimeter))
    perimeter_message.draw(win)

    msg2_pt = (Point(win_width / 2, win_height - 35))
    area_message = Text(msg2_pt, "The area is " +str(area))
    area_message.draw(win)

    end_pt = (Point(win_width / 2, win_height - 10))
    end_message = Text(end_pt, "Click again to quit")
    end_message.draw(win)


    # Wait for another click to exit
    win.getMouse()
    win.close()


def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")
    inputBoxR = Entry(Point(win_width / 2 - 15, win_height / 2 + 40), 3)
    inputBoxR.draw(win)

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")
    inputBoxG = Entry(Point(win_width / 2 - 10, win_height / 2 + 70), 3)
    inputBoxG.draw(win)

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")
    inputBoxB = Entry(Point(win_width / 2 - 15, win_height / 2 + 100), 3)
    inputBoxB.draw(win)

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    for i in range(5):
        win.getMouse()
        red = inputBoxR.getText()
        green = inputBoxG.getText()
        blue = inputBoxB.getText()
        shape_color = color_rgb(int(red), int(green), int(blue))
        shape.setFill(shape_color)


    # Wait for another click to exit
    win.getMouse()
    win.close()

def process_string():
    string = input("Input a string:")
    print("First character of string", string[0])
    print("Last character of string", string[-1])
    print("Characters 2-5", string[2], string[3], string[4], string[5])
    string_concatenation = string[0] + string[-1]
    print("First and last characters concatenated", string_concatenation)
    for i in range(10):
        print("First three characters repeated 10 times", string[0], string[1], string[2])



def main():
    triangle()
    color_shape()
    process_string()
    pass


main()
