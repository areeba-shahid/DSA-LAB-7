Lab 7: BFS, DFS, and Graphs
Objective
In this lab, we will explore graphs, focusing on two key graph traversal algorithms:

Breadth-First Search (BFS)
Depth-First Search (DFS)
These algorithms are fundamental for many graph-related problems, such as searching, pathfinding, and graph connectivity.

Graphs
Definition:
A graph is a collection of nodes (or vertices) and edges (or arcs) connecting these nodes. It can be:

Directed: where edges have a direction (from one node to another).
Undirected: where edges have no direction (the relationship is bidirectional).
Weighted: where each edge has a weight associated with it.
Unweighted: where all edges are treated equally.
Types of Graph Representations:
Adjacency Matrix: A 2D array where the element at [i][j] represents the edge between node i and node j.
Adjacency List: A list where each node has a list of nodes it is connected to.
Breadth-First Search (BFS)
Definition:
BFS is a traversal algorithm that explores the graph level by level. It starts from the root node and visits all of its neighbors before moving to the next level of neighbors. BFS uses a queue to keep track of the nodes to visit.

Steps of BFS:
Start from the root node.
Visit all the neighbors of the root node and add them to a queue.
Dequeue a node from the queue and visit its neighbors.
Repeat the process until all nodes are visited.
C++ Code Example (BFS):
cpp
Copy code
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

void bfs(int start, vector<vector<int>>& adjList) {
    vector<bool> visited(adjList.size(), false);
    queue<int> q;
    
    q.push(start);
    visited[start] = true;

    while (!q.empty()) {
        int node = q.front();
        q.pop();
        cout << node << " ";

        for (int neighbor : adjList[node]) {
            if (!visited[neighbor]) {
                q.push(neighbor);
                visited[neighbor] = true;
            }
        }
    }
}

int main() {
    int vertices = 5;
    vector<vector<int>> adjList(vertices);

    // Example graph:
    adjList[0].push_back(1);
    adjList[0].push_back(2);
    adjList[1].push_back(3);
    adjList[2].push_back(4);

    cout << "BFS traversal starting from node 0: ";
    bfs(0, adjList);  // Output: 0 1 2 3 4
}
Applications of BFS:
Shortest Path in unweighted graphs.
Graph Connectivity.
Level-order Traversal (e.g., trees).
Depth-First Search (DFS)
Definition:
DFS is a traversal algorithm that explores as far down a branch as possible before backtracking. It uses a stack (or recursion) to keep track of the nodes to visit.

Steps of DFS:
Start from the root node.
Visit a node and recursively visit all its neighbors.
Once all neighbors are visited, backtrack and explore other unvisited neighbors.
C++ Code Example (DFS):
cpp
Copy code
#include <iostream>
#include <vector>
using namespace std;

void dfs(int node, vector<vector<int>>& adjList, vector<bool>& visited) {
    visited[node] = true;
    cout << node << " ";

    for (int neighbor : adjList[node]) {
        if (!visited[neighbor]) {
            dfs(neighbor, adjList, visited);
        }
    }
}

int main() {
    int vertices = 5;
    vector<vector<int>> adjList(vertices);

    // Example graph:
    adjList[0].push_back(1);
    adjList[0].push_back(2);
    adjList[1].push_back(3);
    adjList[2].push_back(4);

    vector<bool> visited(vertices, false);
    cout << "DFS traversal starting from node 0: ";
    dfs(0, adjList, visited);  // Output: 0 1 3 2 4
}
Applications of DFS:
Topological Sorting in Directed Acyclic Graphs (DAGs).
Pathfinding in a graph.
Cycle Detection in a graph.
BFS vs DFS
Feature	BFS	DFS
Traversal Type	Level-order (Breadth-first)	Pre-order or Depth-first
Data Structure	Queue	Stack (or Recursion)
Space Complexity	O(V) (queue space)	O(V) (stack or recursion depth)
Time Complexity	O(V + E)	O(V + E)
Use Case	Shortest Path (unweighted graph)	Pathfinding, Cycle Detection
Example Problem: Shortest Path in Unweighted Graph
Problem:
Find the shortest path from a starting node to a target node in an unweighted graph using BFS.

Approach:
Use BFS to explore the graph level by level.
Track the distance from the starting node to each node.
Once the target node is reached, the distance will represent the shortest path.
C++ Code Example (Shortest Path using BFS):
cpp
Copy code
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

vector<int> bfsShortestPath(int start, int target, vector<vector<int>>& adjList) {
    vector<int> dist(adjList.size(), -1);  // -1 means unvisited
    queue<int> q;
    
    dist[start] = 0;
    q.push(start);

    while (!q.empty()) {
        int node = q.front();
        q.pop();

        for (int neighbor : adjList[node]) {
            if (dist[neighbor] == -1) {  // Not visited
                dist[neighbor] = dist[node] + 1;
                q.push(neighbor);
                if (neighbor == target) return dist;  // Early exit if target found
            }
        }
    }

    return dist;  // Return distances (if target not found, distance will remain -1)
}

int main() {
    int vertices = 6;
    vector<vector<int>> adjList(vertices);

    // Example graph:
    adjList[0].push_back(1);
    adjList[0].push_back(2);
    adjList[1].push_back(3);
    adjList[2].push_back(3);
    adjList[3].push_back(4);
    adjList[4].push_back(5);

    int start = 0, target = 5;
    vector<int> distances = bfsShortestPath(start, target, adjList);

    cout << "Shortest distance from node " << start << " to node " << target << " is: " << distances[target] << endl;
}
Example Output:
vbnet
Copy code
Shortest distance from node 0 to node 5 is: 3
Conclusion
In this lab, we explored the concepts of Breadth-First Search (BFS) and Depth-First Search (DFS). These algorithms are essential tools for navigating and analyzing graphs. Understanding how and when to use each algorithm will be crucial for solving various graph-related problems.
