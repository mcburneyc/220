"""
Name: Cooper McBurney
buttons.py

Problem:

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import GraphWin, Rectangle, Text, Point

def draw_button(button_text):
    outline = Rectangle(Point(2,1), Point(4,3))
    center = outline.getCenter()
    label = Text(center, button_text)
    outline.draw(win)
    label.draw(win)

def main():
    win = GraphWin("Test Button", 700,500)
    win.setCoords(0, 0, 10, 10)

    draw_button("Press Me")
    outline = Rectangle(Point(2, 1), Point(4, 3))
    center = outline.getCenter()
    label = Text(center, "Button One")
    outline.draw(win)
    label.draw(win)

