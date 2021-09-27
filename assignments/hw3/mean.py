"""
Name: Cooper McBurney
mean.py

Problem:

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

def a_mean():
    variable = eval(input("Input number of variables:"))
    for i in range(variable):
        value = eval(input("Enter the value:"))
    sum_of_values = sum(value)
    arithmetic_mean = sum_of_values / variable
    print("The arithmetic mean is", arithmetic_mean)

    for i in range(variable):
        multiplication_of_variables = value * i
    geometric_mean = (multiplication_of_variables) ** (1 / variable)
    print("The Geometric Mean is", geometric_mean)




def main():
    a_mean()


main()
