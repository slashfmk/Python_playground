import random

file = open("8_ball_responses.txt", "r")

responsesList = []
for x in file:
    responsesList.append(x)

file.close()

response = 'y'

while response != 'q':
    userInput = input("Ask a question ")
    print(responsesList[random.randint(0, 11)])
    response = input("Press q if you want to quit ")

