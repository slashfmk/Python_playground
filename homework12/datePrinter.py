def checkDate(n, max):
    if n > max or n < 1:
        return False
    else:
        return True


def main():
    monthList = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                 'November', 'December']

    userInput = input("Please enter a date in the format mm/dd/yyyy ")
    dates = userInput.split("/")

    if checkDate(int(dates[0]), 12) and checkDate(int(dates[1]), 31) and checkDate(int(dates[2]), 9999999):

        day = 0
        month = ""
        year = 00

        if checkDate(int(dates[0]), 12):
            month = monthList[int(dates[0]) - 1]
        if checkDate(int(dates[1]), 31):
            day = dates[1]
        if checkDate(int(dates[2]), 999999999):
            year = dates[2]

        print(month + " " + day + ", " + year)

    else:
        raise Exception("invalid date format")
        # print("invalid date")


main()
