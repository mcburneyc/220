"""
Name: Cooper McBurney
lab6.py

Problem: Use and manipulate python strings.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def name_reverse():
    name = input("Input First and Last name:")
    first_name, last_name = name.split(" ")
    fullname_reverse = last_name + ", " + first_name
    print(fullname_reverse)

def company_name():
    domain_name = input("Enter a full domain name:")
    world_wide_web, website_name, end_address = domain_name.split(".")
    print(website_name)

def initials():
    students = eval(input("Input the amount of students in class:"))
    for i in range(students):
        first_name = input("Enter the first name of student " + str(i + 1) + ":")
        last_name = input("Enter " + first_name + "'s last name:")
        print(first_name,"'s initials are " + first_name[0] + last_name[0])

def names():
    names = input("Enter people's names, separated by commas:")
    split_names = names.split(",")
    for i in range(len(split_names)):
        names = split_names[i].split(" ")
        first_name = names[0]
        last_name = names[1]
        first_initial = first_name[0]
        last_initial = last_name[0]
        print(first_initial + last_initial)

def thirds():
    number_of_sentences = eval(input("How many sentences will be inputted?"))
    for i in range(number_of_sentences):
        sentences = input("Input sentence " + str(i + 1))
        for j in range(2, len(sentences), 3):
            print(sentences[j])
def word_average():
    number_of_sentences = eval(input("How many sentences will be inputted?"))
    for i in range(number_of_sentences):
        sentences = input("Input sentence " + str(i + 1))
        words = sentences.split(" ")
        average = len(words)















def main():
    name_reverse()
    company_name()
    initials()
    names()
    thirds()
    word_average()
    pass


main()
