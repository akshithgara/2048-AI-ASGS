# Akshith Gara
# 2048 AI
# CS5400

# Function to grab the input from the input file and extract the necessary values.


def inputGrabber(inputFile):
    grabbed = False
    while not grabbed:
        try:
            with open(inputFile) as file:
                scrapedLines = list(file)
                grabbed = True
        except Exception as e:
            print("Error!")
            inputFile = input("Please enter another file name: ")

    # Removes the trailing new line characters
    for line in range(len(scrapedLines)):
        scrapedLines[line] = scrapedLines[line].replace('\n', '')

    goalNum = int(scrapedLines[0])

    gridSize = list(scrapedLines[1].split(' '))
    for num in range(len(gridSize)):
        gridSize[num] = int(gridSize[num])
    spawnList = list(scrapedLines[2].split(' '))
    for num in range(len(spawnList)):
        spawnList[num] = int(spawnList[num])

    # extracts the first state from the given 2048 puzzle and converts them to nested list of numbers
    for line in range(2, len(scrapedLines)):
        scrapedLines[line] = list(scrapedLines[line].split(' '))

    firstState = scrapedLines
    del firstState[0]
    del firstState[0]
    del firstState[0]

    for i in range(len(firstState)):
        for j in range(len(firstState[i])):
            firstState[i][j] = int(firstState[i][j])

    return firstState, goalNum, spawnList, gridSize
