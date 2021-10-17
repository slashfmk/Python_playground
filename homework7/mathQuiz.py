import random


def mathQuiz(x, y):
    return x + y


def randomizer():
    return random.randint(1, 999)


def main():
    num1 = randomizer()
    num2 = randomizer()

    userInput = int(input("What is the sum of " + str(num1) + " + " + str(num2) + "? "))

    result = mathQuiz(num1, num2)
    if result == userInput:
        print("Congratulations! you got it")
    else:
        print("Sorry! you have failed")
        print("The correct answer is " + str(result))


main()