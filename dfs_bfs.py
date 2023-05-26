# BFS

from collections import deque

# Function to perform BFS traversal
def bfs(graph, start):
    visited = set()  # Keep track of visited vertices
    queue = deque([start])  # Initialize the queue with the starting vertex
    
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex, end=' ')
            queue.extend(graph[vertex] - visited)  # Add unvisited neighbors to the queue

# Example usage
if __name__ == '__main__':
    # Get user input for the graph and starting vertex
    graph = {}
    edges = int(input("Enter the number of edges: "))
    for i in range(edges):
        v1, v2 = input(f"Enter the vertices for edge {i + 1}: ").split()
        if v1 not in graph:
            graph[v1] = set()
        if v2 not in graph:
            graph[v2] = set()
        graph[v1].add(v2)
        graph[v2].add(v1)
    start = input("Enter the starting vertex: ")
    
    # Perform BFS traversal
    print("BFS traversal:")
    bfs(graph, start)

# output:Enter the number of edges: 4
# Enter the vertices for edge 1: A B
# Enter the vertices for edge 2: B C
# Enter the vertices for edge 3: C D
# Enter the vertices for edge 4: D E
# Enter the starting vertex: A

# DFS:

# Function to perform DFS traversal
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()  # Keep track of visited vertices
    visited.add(start)
    print(start, end=' ')
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Example usage
if __name__ == '__main__':
    # Get user input for the graph and starting vertex
    graph = {}
    edges = int(input("Enter the number of edges: "))
    for i in range(edges):
        v1, v2 = input(f"Enter the vertices for edge {i + 1}: ").split()
        if v1 not in graph:
            graph[v1] = set()
        if v2 not in graph:
            graph[v2] = set()
        graph[v1].add(v2)
        graph[v2].add(v1)
    start = input("Enter the starting vertex: ")
    
    # Perform DFS traversal
    print("DFS traversal:")
    dfs(graph, start)
