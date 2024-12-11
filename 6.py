
from sys import maxsize
from itertools import permutations

V = 4

def travelling_salesman_problem(graph, s):
    # Store all vertices except the source vertex
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)
    
    # Initialize minimum path to a large number
    min_path = maxsize
    # Generate all permutations of vertices to calculate possible paths
    next_permutation = permutations(vertex)
    
    for i in next_permutation:
        # Initialize the path weight of the current permutation
        current_pathweight = 0
        k = s
        
        # Compute path cost for this permutation
        for j in i:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][s]
        
        # Update minimum path
        min_path = min(min_path, current_pathweight)
    
    return min_path

# Driver code
if __name__ == "__main__":
    # Define the graph as an adjacency matrix
    graph = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    s = 0
    print(travelling_salesman_problem(graph, s))
