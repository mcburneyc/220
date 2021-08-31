"""
Name: Cooper McBurney
lab1.py

Problem: This function calculates the area of a rectangle
"""


def calc_area():
        length = 20
        width = 5
        area = length * width
        print("Area =", area)


def calc_volume():
        length = eval(input(""))
        width = eval(input(""))
        height = eval(input(""))
        volume = length * width * height
        print("Volume =", volume)

def shooting_percentage():
        total_shots = 20
        shots_made = 15
        shooting_percentage = shots_made / total_shots * 100
        print("Shooting Percentage =", shooting_percentage)


def coffee():
        cost_per_pound = 10.50
        shipping_per_pound = 0.86
        fixed_cost = 1.50
        pounds_of_coffee = eval(input(""))
        coffee = fixed_cost + (cost_per_pound + shipping_per_pound) * pounds_of_coffee
        print("Price =", coffee)


def kilometers_to_miles():
        kilometers = eval(input(""))
        kilometers_to_miles = kilometers *  0.6214
        print("Miles =", kilometers_to_miles)