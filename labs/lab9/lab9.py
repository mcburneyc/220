"""
Name: Cooper McBurney
lab9.py

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

def addTens(nums):
    for i in nums:
        i += 10

def squareEach(nums):
    for i in nums:
        i **= 2

def sumlist(nums):
    total = 0
    for i in nums:
        total = i + total
    return total

def toNumbers(strlist):
    for i in strlist:
        int(i)

def starter():
    weight = eval(input("Input Wrestler's Weight:"))
    numWins = eval(input("Input number of Wrestler's wins:"))

    if weight < 150 and numWins < 5:
        print("Wrestler does not meet weight and wins requirement, must weigh over 150 and have 5 wins")
    if weight >= 160 and numWins < 5:
        print("Wrestler does not meet wins requirement, if weight is over 161, must 5 wins")
    if weight < 199:
        print("Wrestler does not meet weight requirement, must weigh over 199")
    if numWins < 20:
        print("Wrestler does not meet weight requirement, must have over 20 wins")



def main():
    numlist = [5, 2, -3]
    addTens(numlist)

    squarelist =  [3, 5.7, 2]
    squareEach(squarelist)

    listofsums = [3, 5.7, 2]
    sumlist(listofsums)

    stringlist = [3, 5.7, 2]
    toNumbers(stringlist)

    starter()
main()




