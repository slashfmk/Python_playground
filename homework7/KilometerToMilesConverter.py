
def ktoMiles(kilometers):
    return kilometers * 0.6214

def main():
    userInput = int(input("Please enter your kilometers "))
    print(str(userInput) + " kilometers = " + format(ktoMiles(userInput), ".4f") + " miles")

main()