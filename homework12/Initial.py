firstname = input("First name ")
middleName = input("Middle name ")
lastname = input("Last name ")

def initial(name):
    if (name == ""):
        return ""
    else:
        return name[0].capitalize() + "."


print(initial(firstname) + initial(middleName) + initial(lastname))
