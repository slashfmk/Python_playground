
def caloriesFromFat(fatGram):
    return fatGram * 9


def caloriesFromCarbs(carbGram):
    return carbGram * 4


def main():
    fatGramAmount = int(input("Fat gram amount consumed daily: "))
    carbGramAmount = int(input("Carb gram amount consumed daily: "))

    output = "Result\n"
    output += "-------\n"
    output += "Calories from fat: " + str(caloriesFromFat(fatGramAmount)) + "\n"
    output += "Calories from carbs: " + str(caloriesFromCarbs(carbGramAmount))

    print(output)

main()