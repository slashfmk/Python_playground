# print(len(square))

def getRowSum(aList):
    sum = 0
    for rowElem in aList:
        sum += rowElem
    return int(sum)

def checkGame(square):
    if len(square[0]) == len(square[1]) == len(square[2]) == len(square):
        sumRow0 = getRowSum(square[0])
        sumRow1 = getRowSum(square[1])
        sumRow2 = getRowSum(square[2])

        sumCol0 = square[0][0] + square[1][0] + square[2][0]
        sumCol1 = square[0][1] + square[1][1] + square[2][1]
        sumCol2 = square[0][2] + square[1][2] + square[2][2]

        sumDiag = sumCol0 = square[2][0] + square[1][1] + square[0][2]

        print("The list below: ")
        print(square)
        if sumRow0 == sumRow1 == sumRow2 == sumCol0 == sumCol1 == sumCol2 == sumDiag:
            print("Is a valid Lo Shun Magic square")
        else:
            print("Is not a valid Lo Shun Magic square")
    else:
        quit("The provided list is invalid")

def main():
    myList = [[4, 9, 2], [3, 5, 7], [8, 1, 6, 9]]
    checkGame(myList)

main()
