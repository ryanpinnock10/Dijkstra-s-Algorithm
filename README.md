Quick and dirty implementation of [Dijkstra's algorithm](http://en.wikipedia.org/wiki/Dijkstra's_algorithm) for finding 
shortest path distances in a connected graph.

This implementation has a *O((m+n) log n)* running time, where *n* is the number of
vertices and *m* is the number of edges. If the graph is connected (i.e. in one piece), *m* 
normally dominates over *n*, making the algorithm *O(m log n)* overall.

## Usage

```python
#!usr/bin/env python3

import unittest, warnings
from makePathString import readFile, pathString
from myDijkstras import dijkstras
```

The main function takes as arguments a graph structure and a starting vertex.  

```python
dijkstras(adjMatrix, sourceNode, destNode) 
```

The graph structure should be a dict of dicts, a mapping of each node `v` to its
successor nodes `w` and their respective edge weights (`v -> w`).

Dijkstra has to run for directed graphs. The node names should not be included in the data. 
Once you read them you may refer to them by their indices, in other words, you may label 
the nodes with their index, so if your index origin is 0, a data file like:
2 3
0.0 3.3 0.0 4.5
3.3 0.0 5.2 3.1
8.5 5.2 0.2.0.0
4.5 3.1 5.2 0.0

would mean, for example that the cost from node 0 to node 3 would be 4.5, from node 2 to node 0 would be 8.5, etc.


```python
graph = 
[0.0 3.3 5.1 6.5 8.9 4.1 0.5 1.3 5.1
6.8 0.0 2.3 0.5 2.1 7.1 0.0 8.6 7.6
6.0 6.2 0.0 9.0 7.2 6.4 6.6 2.7 5.0
7.3 8.2 8.6 0.0 0.1 7.7 0.1 1.4 2.1
2.2 6.3 6.6 5.7 0.0 6.2 9.5 2.4 3.7
6.3 9.8 8.7 0.3 1.3 0.0 3.9 8.1 9.1
9.1 1.0 3.7 3.9 0.4 4.6 0.0 7.4 0.0
5.8 1.0 5.0 8.6 2.1 5.2 2.3 0.0 7.6
3.2 5.6 1.4 2.8 2.6 2.9 8.1 5.8 0.0]

# 1. Mark all nodes unvisited and store them.
# 2. Set the distance to zero for our initial node 
# and to infinity for other nodes.
# 3. Select the unvisited node with the smallest distance, 
# it's current node now.
# 4. Find unvisited neighbors for the current node 
# and calculate their distances through the current node.
# Compare the newly calculated distance to the assigned 
# and save the smaller one.



In the command line, type following command python myDijkstra.py <filepath> 
For example: python myDijkstra.py './testCase0.txt'


```