from collections import deque, defaultdict

def bfs_shortest_path(graph, start, target):
    queue = deque([(start, 0)])  # (current_node, distance)
    visited = set()
    visited.add(start)

    while queue:
        node, distance = queue.popleft()
        
        if node == target:
            return distance
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))
                
    return -1  # if no path found

def dfs(graph, current, target, visited):
    if current == target:
        return True
    visited.add(current)
    
    for neighbor in graph[current]:
        if neighbor not in visited:
            if dfs(graph, neighbor, target, visited):
                return True
    return False

def solve_forest_problem(N, edges, start, person, hq):
    # Step 1: Build the graph as an adjacency list
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Step 2: Find shortest path from start to person using BFS
    shortest_path_length = bfs_shortest_path(graph, start, person)

    # Step 3: Check if there's a direct path from person to hq using DFS
    visited = set()
    direct_path_exists = dfs(graph, person, hq, visited)

    # Step 4: Calculate total number of clearings (nodes in the forest)
    total_clearings = N

    # Output results
    print("Shortest path length from start to person:", shortest_path_length)
    print("Direct path from person to hq:", "Yes" if direct_path_exists else "No")
    print("Total number of clearings in the forest:", total_clearings)

# Example input
N = 6
edges = [
    (1, 2),
    (1, 3),
    (2, 4),
    (3, 5),
    (5, 6)
]
start = 1
person = 4
hq = 6

solve_forest_problem(N, edges, start, person, hq)
