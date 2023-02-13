

with open('text.txt', 'r') as fileContent:
    lCount = 0
    total_wordCount = 0
    lines = fileContent.readlines()
    for line in lines:
        lCount = lCount + 1
        wordCount = len(line.split())
        total_wordCount += wordCount

    print("The average is " + str(total_wordCount / lCount))

    fileContent.close()