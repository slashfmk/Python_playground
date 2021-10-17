import math


def compound_interest(p, r, n, t):
    return p * ((1 + ((r/100) / n)) ** (n*t))


original_amount_of_principal = int(input("Enter your deposit: "))
annual_interest_rate = int(input("Enter your annual interest rate: "))
time_per_year_interest_compounding = int(input("Enter number of time that the interest is compounded (in a years): "))
num_of_years_left_to_earn_interest = int(input("Enter the number of years the account will be left to earn interest: "))

print("the amount of money left is ",
      format(compound_interest(original_amount_of_principal, annual_interest_rate, time_per_year_interest_compounding, num_of_years_left_to_earn_interest), ".2f")
      )
