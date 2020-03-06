# Akshith Gara
# 2048 AI
# CS5400

import queue
from grid import grid


# Function to check if the goal state has been achieved.
def isGoal(state, goal):
    win = goal
    for line in state:
        for i in line:
            if i == win:
                return True
    return False


# Implementation of Greedy Best First Search
def gbfs(state, goal, spawnList, gridSize):
    frontier = queue.PriorityQueue()  # Priority Queue Implementation

    root = grid(state, '', 0, spawnList, gridSize)
    frontier.put(root)

    explored = set()  # A python set to store explored states. Using a set as it has O(1) look up time.

    while not frontier.empty(): # Exits when the frontier is out of states to explore.

        curNode = frontier.get()
        if isGoal(curNode.STATE, goal):
            return curNode.PATH, curNode
        else:
            for child in curNode.CHILDREN(spawnList, gridSize):
                visited = child in explored # Checks if the child node is in explored set.
                if not visited:
                    frontier.put(child)
                    explored.add(child) # Adds child node to visited set if it has just been explored.

