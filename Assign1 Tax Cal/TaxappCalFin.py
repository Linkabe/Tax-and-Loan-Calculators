#!/usr/bin/env python3

# Description of project
print("Author: Niall, StudentNo: A00258874 Script: Tax App")
print("===================================================")
print("")
print("===========================")
print("Income Tax Calculator")
print("===========================")

STANDARD_DEDUCTION = 3600
NO_KIDS = 1500
TAX_DEDUCTION = 0.2


# Get user inputs
# and defining main function
def main():
    while True:
        try:
            gross_income = float(input("Please Enter Your Tax Income to the Nearest Penny!: "))
            no_children = int(input("Please Enter Your Number of Dependants!: "))
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
            continue

        if gross_income <= 0:
            print("Please Enter A Higher Income")
            continue
    # Getting the tax calculations
        if gross_income <= STANDARD_DEDUCTION:
            TAX_DEDUCTION = 0
        else:
            TAX_DEDUCTION = 0.2

    # calculate the total cost
        total_cost_kids = int(no_children * NO_KIDS)
        non_taxed_income = float(STANDARD_DEDUCTION + total_cost_kids)
        total_cost_tax = round(float(gross_income - non_taxed_income), 2)
        if total_cost_tax < 0:
            print("Your income is Not taxable")
            continue
        else:    
            income_tax = round(float(total_cost_tax * 0.2),2)

        print("==============================================")
    # Printing Result
        print("Total Gross Income: ", gross_income)
        print("Total Non-Tax Income: ", non_taxed_income)
        print("Taxed Income: ", total_cost_tax)
        print("Your Income Tax: ", income_tax)
        print("")
        print("==============================================")
    # Does the user want to continue
        choice = input("Do you want to Continue? (y/n): ")
        print("==============================================")
        if choice.lower() != "y":
            print("Bye")
            exit()
# calling main function


if __name__ == "__main__":
    main()
    exit()
