from collections import deque

def dfs(adj, s, visited):
    q = deque() # Create a queue for BFS 
    # Mark the source node as visited and enqueue it 
    visited[s] = True 
    q.append(s) 
    # Iterate over the queue 
    while q: 
      curr = q.popleft() # Dequeue a vertex 
      print(curr, end=" ") 
    # Get all adjacent vertices of curr 
      for x in adj[curr]: 
          if not visited[x]: 
            visited[x] = True # Mark as visited 
            q.append(x) # Enqueue it 
    # Function to add an edge to the graph 
   
        

