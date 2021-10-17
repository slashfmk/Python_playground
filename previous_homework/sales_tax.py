
def county_tax(amount):
    return (amount * 2.5) / 100


def state_tax(amount):
    return (amount * 5) / 100

def total_sales_tax(amount):
    return county_tax(amount) + state_tax(amount)

def total (amount):
    return amount + total_sales_tax(amount)


amount = int(input("Enter the amount of the purchase: "))

print("The purchase amount", amount)
print("The county sales tax is ", county_tax(amount))
print("The state sales tax is ", state_tax(amount))
print("The total sales tax is ", total_sales_tax(amount))
print("The total amount including all sales taxes is ", total(amount))