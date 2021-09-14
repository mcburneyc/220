"""
Name: Cooper McBurney
lab3.py

Certification of Authenticity:
I certify that this assignment is entirely my own work.

"""


def average():
    total = 0
    grades = eval(input("Enter the number of grades:"))
    for i in range (grades):
        x = eval(input("Enter a grade for HW"))
        total = total + x
    print("The average of the numbers is", total / grades)

def tip_jar():
    a = eval(input("Enter your donation:"))
    print("Your donation is $", a)
    b = eval(input("Enter your donation:"))
    print("Your donation is $", b)
    c = eval(input("Enter your donation:"))
    print("Your donation is $", c)
    d = eval(input("Enter your donation:"))
    print("Your donation is $", d)
    e = eval(input("Enter your donation:"))
    print("Your donation is $", e)
    total = a + b + c + d + e
    print("Your tip total is $",total)


def newton():
    x = eval(input(""))