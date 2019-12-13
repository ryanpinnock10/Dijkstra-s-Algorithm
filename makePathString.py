#!usr/bin/env python3

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

#Opens the files to read the start and end vertex of 
#where execution or traversal shoudl begin.

def readFile(filepath):
    matrixFile = list(open(filepath, "r"))
    matrix = []
    for i in range(1, len(list(matrixFile))):
        line = []
        for distance in matrixFile[i].strip().split(' '):
            line.append(float(distance))
        matrix.append(line)
    start = int(matrixFile[0].strip().split(' ')[0])
    end = int(matrixFile[0].strip().split(' ')[1])
    return matrix, start, end

#This program concatenates the string of all the 
#nodes found in the path. The cost of the minimum
#path is then calculated through this graph traversal.

def pathString(path, startVertex, endVertex):
    curr = endVertex
    listOfPaths = [curr]
    while(curr != startVertex):
        curr = path[curr]
        listOfPaths[:0] = [curr]
    s = str(listOfPaths[0])
    for i in range(1, len(listOfPaths)):
        if i < len(listOfPaths) - 1:
            s += "-" + str(listOfPaths[i])
        else:
            str(listOfPaths[i])
    return s