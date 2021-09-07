"""
Name: Cooper McBurney
lab2.py
"""


import math


def sum_of_threes():
    upperbound = eval(input("Input your Upper Bound:"))
    x = 0
    for num in range(3, upperbound + 1, 3):
        x= x + num
        print(x)
        #end for loop


def multiplication_table():
    for table in range(1,11):
        print(table, table * 1, table * 2, table * 3, table * 4, table * 5, table * 6, table * 7, table * 8, table * 9, table * 10)


def triangle_area():
    a = eval(input("Input A value:"))
    b = eval(input("Input B value:"))
    c = eval(input("Input C value:"))
    s = (a + b + c)/2
    x = s * (s-a) * (s-b) * (s-c)
    print(math.sqrt (x))


def sumSquares():
    a = eval(input("Input Lower Range:"))
    b = eval(input("Input Upper Range:"))
    num = 0
    for x in range(a,b + 1):
        num = x * x
        print(num)


def power():
    base = eval(input("Input your base:"))
    exponent = eval(input("Input your exponent"))
    total = 1
    for num in range(exponent):
        total = total * base
    print (total)

