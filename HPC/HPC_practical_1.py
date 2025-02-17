import queue
import threading
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor

class Graph:
    def __init__(self, vertices):
        self.numVertices = vertices
        self.adj = defaultdict(list)

    def add_edge(self, src, dest):
        """Add an edge to the graph."""
        self.adj[src].append(dest)
        self.adj[dest].append(src)

    def view_graph(self):
        """Print the adjacency list representation of the graph."""
        print("Graph:")
        for vertex in self.adj:
            print(f"Vertex {vertex} -> {' '.join(map(str, self.adj[vertex]))}")

    def bfs(self, start_vertex):
        """Perform parallel BFS using multithreading."""
        visited = {i: False for i in range(self.numVertices)}
        q = queue.Queue()
        lock = threading.Lock()

        visited[start_vertex] = True
        q.put(start_vertex)

        def process_node():
            while not q.empty():
                current_vertex = q.get()
                print(current_vertex, end=" ")

                with lock:
                    for neighbor in self.adj[current_vertex]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            q.put(neighbor)

        with ThreadPoolExecutor() as executor:
            executor.submit(process_node)

    def dfs(self, start_vertex):
        """Perform parallel DFS using multithreading."""
        visited = {i: False for i in range(self.numVertices)}
        stack = []
        lock = threading.Lock()

        visited[start_vertex] = True
        stack.append(start_vertex)

        def process_node():
            while stack:
                current_vertex = stack.pop()
                print(current_vertex, end=" ")

                with lock:
                    for neighbor in self.adj[current_vertex]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            stack.append(neighbor)

        with ThreadPoolExecutor() as executor:
            executor.submit(process_node)


# Main function to run the graph operations
if __name__ == "__main__":
    num_vertices = int(input("Enter the number of vertices in the graph: "))
    graph = Graph(num_vertices)

    num_edges = int(input("Enter the number of edges in the graph: "))
    print("Enter the edges (source destination):")
    
    for _ in range(num_edges):
        src, dest = map(int, input().split())
        graph.add_edge(src, dest)

    graph.view_graph()

    start_vertex = int(input("Enter the starting vertex for BFS and DFS: "))

    print("Breadth First Search (BFS): ", end="")
    graph.bfs(start_vertex)
    print()

    print("Depth First Search (DFS): ", end="")
    graph.dfs(start_vertex)
    print()
