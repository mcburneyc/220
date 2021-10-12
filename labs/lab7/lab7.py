"""
Name: Cooper McBurney
lab7.py

Problem:
"""
import math

def main():
    radius = eval(input("What is the sphere's radius? "))
    surface_area = sphere_area(radius)
    volume = sphere_volume(radius)

def cash_conversion():
    amount = eval(input("Input your amount of money:"))
    cash = "${:,.2f}".format(amount)
    print("Your amount is", cash)

def encode():
    message = input("Input your message:")
    key = eval(input("Input a key value:"))
    for character in message:
        x = ord(character) + key
        print(chr(x), end="")

def sphere_area(radius):
    surface_area =  4 * math.pi * (radius)**2
    print("The surface area is", surface_area)
    return surface_area

def sphere_volume(radius):
    volume = 4 / 3 * math.pi * (radius)**3
    print("The volume is", volume)
    return volume











main()
cash_conversion()
encode()
sphere_area()
sphere_volume()

