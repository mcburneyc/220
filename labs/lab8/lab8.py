"""
Name: Cooper McBurney
lab8.py


"""

def number_words():
    walrus_output = open("Walrus.txt", "w+")
    content = walrus_output.read()
    list_output = content.split()
    list_output.write(content)
    print(list_output)


def hourly_wages():
    wages_output = open("hourly_wages.txt", "r")
    wage_info = wages_output.read()
    names_and_wages = wage_info.split()
    worker1_wage = int(float(names_and_wages[2]))
    worker1_hours = int(float(names_and_wages[3]))
    worker2_wage = int(float(names_and_wages[6]))
    worker2_hours = int(float(names_and_wages[7]))
    updated_wage1 = (worker1_wage + 1.65) * worker1_hours
    updated_wage2 = (worker2_wage + 1.65) * worker2_hours
    print(names_and_wages[0], names_and_wages[1], ":", updated_wage1)
    print(names_and_wages[4], names_and_wages[5], ":", updated_wage2)

def calc_checksum():
    isbn = input("Please input a 10 digit ISBN:")
    digit1 = int(isbn[0]) * 10
    digit2 = int(isbn[1]) * 9
    digit3 = int(isbn[2]) * 8
    digit4 = int(isbn[3]) * 7
    digit5 = int(isbn[4]) * 6
    digit6 = int(isbn[5]) * 5
    digit7 = int(isbn[6]) * 4
    digit8 = int(isbn[7]) * 3
    digit9 = int(isbn[8]) * 2
    digit10 = int(isbn[9]) * 1
    checksum = digit1 + digit2 + digit3 + digit4 +digit5 + digit6 +digit7 + digit8 +digit9 + digit10
    print(checksum)

def send_message():
    existing_message = open("message.txt", "w+")
    new_msg_content = existing_message.write()
    print(new_msg_content)


number_words()
hourly_wages()
calc_checksum()
send_message()
send_message()