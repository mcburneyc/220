"""
Name: Cooper McBurney
traffic.py

Problem:

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def main():
    number_of_roads = eval(input("How many roads were surveyed?"))
    cars_total = 0
    for i in range(number_of_roads):
        per_day = eval(input("How many days was road " + str(i + 1) + " surveyed"))
        for i in range(per_day):
            vehicles_per_day = eval(input("How many cars traveled on day " + str(i + 1) + "?"))
            cars_average = (cars_total + vehicles_per_day) / (per_day)
        print("Road " + str(number_of_roads) + "average vehicles per day", cars_average)


if __name__ == '__main__':
    main()