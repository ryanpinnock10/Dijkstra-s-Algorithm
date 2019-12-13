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

import unittest, warnings
from makePathString import readFile, pathString
from myDijkstras import dijkstras

def ignore_warnings(testFunction):
    def startTest(self, *args, **kwargs):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            testFunction(self, *args, **kwargs)
    return startTest

#Unit tests to verify if the cost and paths are the same as for 
#every text file tested.

class TestDijkstra(unittest.TestCase):

    @ignore_warnings
    def test_0(self):
        adjMatrix, start, end = readFile(
        "./testCase0.txt")
        path, dist = dijkstras(adjMatrix, start, end)
        self.assertEqual(pathString(path, start, end), "1-5")
        self.assertAlmostEqual(dist, 2.8)
        self.assertNotEqual(dist, 8)
        self.assertNotEqual(dist, 8.4)
    
    @ignore_warnings
    def test_1(self):
        adjMatrix, start, end = readFile(
        "./testCase1.txt")
        path, dist = dijkstras(adjMatrix, start, end)
        self.assertEqual(pathString(path, start, end), "6-4-7")
        self.assertAlmostEqual(dist, 6.1)
        self.assertNotEqual(dist, 10.2)
        self.assertNotEqual(dist, 9.8)

    @ignore_warnings
    def test_2(self):
        adjMatrix, start, end = readFile(
        "./testCase2.txt")
        path, dist = dijkstras(adjMatrix, start, end)
        self.assertEqual(pathString(path, start, end), "1-15-2")
        self.assertAlmostEqual(dist, 2.7)
        self.assertNotEqual(dist, 11.0)
        self.assertNotEqual(dist, 11.4)

    @ignore_warnings
    def test_3(self):
        adjMatrix, start, end = readFile(
        "./testCase3.txt")
        path, dist = dijkstras(adjMatrix, start, end)
        self.assertEqual(pathString(path, start, end), "7-16-19")
        self.assertAlmostEqual(dist, 1.5)
        self.assertNotEqual(dist, 1.7)
        self.assertNotEqual(dist, 1.2)

    @ignore_warnings
    def test_4(self):
        adjMatrix, start, end = readFile(
        "./testCases.txt")
        path, dist = dijkstras(adjMatrix, start, end)
        self.assertEqual(pathString(path, start, end), "2-3-0")
        self.assertAlmostEqual(dist, 10.0)
        self.assertNotEqual(dist, 2)


if __name__ == '__main__':
    unittest.main()