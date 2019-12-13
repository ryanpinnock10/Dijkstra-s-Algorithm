# Ryan Pinnock
# Date: 12/12/2019
# Class: CSC- 321A
# Professor: Salvador 
# Assignment: Implement a working version of Dijkstra's Algorithm following the implementation
#  guidelines shown in the Textbook and in the slides, subject to the following conditions:

# The program should take a directed graph as the input. 
# The input should be represented by an adjacency matrix whose 
# entries are the costs, i.e., M(i,j) is the cost of edge (i, j).
#  The nodes will be represented with single lower case letters. 
# The adjacency matrix should be read from a text file whose first 
# row will be the letters for the initial and final nodes, the costs 
# should be separated by blanks, so an excerpt from your input file 
# could look like:


#!usr/bin/env python3

import heapq, sys
from makePathString import readFile, pathString

def main():
    adjMatrix, start, end = readFile(sys.argv[1])
    path, dist = dijkstras(adjMatrix, start, end)
    print(pathString(path, start, end))
    print("Cost: " + str(dist))

def dijkstras(adjMatrix, sourceNode, destNode):
    # 1. Mark all nodes unvisited and store them.
    # 2. Set the distance to zero for our initial node 
    # and to infinity for other nodes.
    distances = {}
    path = {}
    for node in range(len(adjMatrix)):
        distances[node] = float(sys.maxsize)
        path[node] = None
    distances[sourceNode] = 0
     # 3. Select the unvisited node with the smallest distance, 
    # it's current node now.
    pq = []
    for node in range(len(adjMatrix)):
        heapq.heappush(pq, (node, distances[node]))

    while len(pq) != 0:
        currNode, currNodeDistance = heapq.heappop(pq)

        # 4. Find unvisited neighbors for the current node 
        # and calculate their distances through the current node.

        for neighborNode in range(len(adjMatrix[currNode])):
            if adjMatrix[currNode][neighborNode] != 0:
                weight = adjMatrix[currNode][neighborNode]
                distance = currNodeDistance + weight
                # Compare the newly calculated distance to the assigned 
              # and save the smaller one.
                if distance < distances[neighborNode]:
                    distances[neighborNode] = distance
                    heapq.heappush(pq, (neighborNode, distance))
                    path[neighborNode] = currNode

    return path, distances[destNode]
  
if __name__ == "__main__":
    main()