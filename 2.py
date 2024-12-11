# Using a Python dictionary to act as an adjacency list graph
graph = { 
    '5': ['3', '7'], 
    '3': ['2', '4'], 
    '7': ['8'], 
    '2': [], 
    '4': ['8'], 
    '8': [] 
}

visited = set()  # Set to keep track of visited nodes of the graph

def dfs(visited, graph, node):  # Function for DFS
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
print("Following is the Depth-First Search")
dfs(visited, graph, '5')