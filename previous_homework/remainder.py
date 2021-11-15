

pageFileNumber = int(input("Enter the number of page files "))
bufferPage = int(input("Enter the number of buffer page "))

sortedRunPage = pageFileNumber / bufferPage
leftOver = pageFileNumber % bufferPage

print(str(sortedRunPage)+" sorted runs of " + str(bufferPage)+" pages\n")
print("last run is only "+str(leftOver)+" pages\n")
