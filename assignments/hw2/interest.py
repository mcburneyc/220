"""
Name: Cooper McBurney
interest.py

Problem: Calculate the  the monthly interest charge on a credit card account.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

def main():
    print("This program calculate the  the monthly interest charge on a credit card account")
    apr = eval(input("Input the annual interest rate"))
    billing_cycle = eval(input("Input the amount of days in the billing cycle:"))
    previous_balance = eval(input("Input the previous (net) balance:"))
    payment = eval(input("Input the payment amount:"))
    day_of_payment = eval(input("Input the day of the billing cycle in which the payment was made:"))
    x = previous_balance * billing_cycle
    y = payment * (billing_cycle - day_of_payment)
    z = x - y
    average_daily_balance = z / billing_cycle
    monthly_interest_rate = apr / 12
    monthly_interest_charge = (average_daily_balance * monthly_interest_rate)/100
    print("the monthly interest charge is $", round(monthly_interest_charge, 2))

if __name__=="__main__":
     main()