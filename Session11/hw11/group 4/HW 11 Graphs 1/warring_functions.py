
"""
Warring Functions
"""

from graph import Graph
from queueArrayBased import Queue
import sys

def separate_rooms(graph_file):
    # Load graph using existing Graph class
    print(f"Processing file: {graph_file}")
    G = Graph(filename=graph_file)
    print(f"Graph has {G.V} vertices and {G.E} edges")

    # Color array: -1 = uncolored, 0 = room1, 1 = room2
    color = [-1] * G.V

    # Check each connected component
    for start_vertex in range(G.V):
        if color[start_vertex] == -1:  # Unvisited component
            # Use existing Queue class for BFS
            queue = Queue()
            queue.enqueue(start_vertex)
            color[start_vertex] = 0  # Start with room 1

            while not queue.is_empty():
                current = queue.dequeue()
                current_room = color[current]
                opposite_room = 1 - current_room

                # Check all neighbors using Graph's adjacency structure
                for neighbor in G.adj[current]:
                    if color[neighbor] == -1:
                        # Assign to opposite room
                        color[neighbor] = opposite_room
                        queue.enqueue(neighbor)
                    elif color[neighbor] == current_room:
                        # Conflict! Same room assignment for connected attendees
                        print("CONFLICT DETECTED: Cannot separate attendees")
                        return False, None, None

    # If we reach here, separation is possible
    roomA = [v for v in range(G.V) if color[v] == 0]
    roomB = [v for v in range(G.V) if color[v] == 1]

    print("SUCCESS: Attendees can be separated!")
    print(f"Room A: {sorted(roomA)}")
    print(f"Room B: {sorted(roomB)}")
    print(f"Room A has {len(roomA)} attendees")
    print(f"Room B has {len(roomB)} attendees")
    return True, roomA, roomB

if __name__ == "__main__":
    test_files = ["graph.txt", "graph1.txt"]
    for filename in test_files:
        try:
            separate_rooms(filename)
        except FileNotFoundError:
            print(f"Error: File {filename} not found")
