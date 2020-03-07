# Akshith Gara
# 2048 AI
# CS5400

import sys
from datetime import datetime
from astargs import Asgs

from scraper import *

if __name__ == '__main__':

    if len(sys.argv) > 1:
        inputFile = sys.argv[1]
    else:
        inputFile = input("Please enter the filename: ")

    firstState, goal, spawnList, gridSize = inputGrabber(inputFile)
    # Timer to measure the execution time.
    startTime = datetime.now()
    sol = Asgs(firstState, goal, spawnList, gridSize)
    endTime = datetime.now()
    execTime = endTime - startTime
    print(execTime.microseconds)
    # Prints the solution only if there is one.
    if sol:
        print(len(sol[0]))
        print(sol[0])
        for line in sol[1].STATE:
            print(' '.join([str(x) for x in line]))
