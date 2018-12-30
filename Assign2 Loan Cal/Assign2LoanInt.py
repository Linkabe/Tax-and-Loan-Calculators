"""
Program: AnnualTaxCal.py
Assignment: 2, Lennon's Computer Shop
Name: Niall quinn

Inputs 
The credit plan at “Lennon’s Computer Shop” specifies a 10% DEPOSIT and an annual interest rate of 12%.
Monthly payments are 5% of the listed purchase price, minus the DEPOSIT payment.
Write a program that takes the purchase price as input.
The program should display a table, with appropriate headers, of a payment schedule for the lifetime of the loan.

Outputs
a. the month number (beginning with 1)
b. the current total balance owed
c. the interest owed for that month
d. the amount of principal owed for that month
e. the payment for that month
f. the balance remaining after payment
The amount of interest for a month is equal to
"""

# Description of script
print("=====================================================")
print("Author: Niall Quinn", "Student No.: A00258874", " Script: Assignment 2 - LOAN")
print("=====================================================")
print(" ")
print("=====================================================")
print("         Assignment 2: Annual Tax Calculator         ")
print("=====================================================")

DEPOSIT = 0.10
ANNUAL_INTEREST = 0.12
MONTHLY_INTEREST = 0.05


# Getting the users input and defining function
def main():
    while True:
        try:
            loan_amount = float(input("Enter Your Loan Amount: €"))
        except ValueError:
                print("That was not a valid number.  Try again...")
                continue
        if loan_amount <= 0:
            print("Please Enter A Higher Loan Amount.")
            continue

# Calculations for DEPOSIT and interest
        print("%-10s%10s%18s%18s%14s%18s" % ("Month", "Current Balance", "Monthly Payment", "Monthly Interest",
                                             "Principal", "Ending Balance"))
        deposit_amount = loan_amount * DEPOSIT
        current_balance = loan_amount - deposit_amount
        monthly_payment = current_balance * MONTHLY_INTEREST

# Printing out the table with calculations
        for month in range(1, 21):

            monthly_interest = current_balance * ANNUAL_INTEREST / 12
            principal = monthly_payment - monthly_interest
            ending_balance = current_balance - monthly_payment
    
            print("==============================================================================================")
            print("%-10d%10.2f%18.2f%18.2f%18.2f%18.2f" % (month, current_balance, monthly_payment, monthly_interest,
                                                           principal, ending_balance))
            current_balance = ending_balance

        print("==============================================")
# Does the user want to continue
        choice = input("Do you want to Continue? (y/n): ")
        print("==============================================")
        if choice.lower() != "y":
            break
    exit()


while True:
    if __name__ == "__main__":
        main()