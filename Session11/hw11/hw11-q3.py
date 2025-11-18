"""
Homework 11
Group assignment
Authors:
Class: DSA 16-198-512-03
Fall 2025
"""

# Question 3:

def build_graph_from_edges(num_vertices, edges):
    graph = {i: [] for i in range(num_vertices)}
    for u, v in edges:
        graph[u].append(v)
    return graph

def validTopologicalOrder(graph, sequence):
    position = {v: i for i, v in enumerate(sequence)}
    for u in graph:
        for v in graph[u]:
            if position[u] > position[v]:
                return False
    return True

# graphT from .txt file:
num_vertices = 7
edges = [
    (0,5),
    (0,2),
    (0,1),
    (3,6),
    (3,5),
    (5,4),
    (5,2),
    (6,0),
    (6,3),
    (2,1),
    (1,4)
]

G = build_graph_from_edges(num_vertices, edges)

seq1 = [3, 6, 0, 5, 2, 1, 4]
seq2 = [4, 3, 6, 0, 5, 2, 1]

print("Sequence 1 valid?", validTopologicalOrder(G, seq1))
print("Sequence 2 valid?", validTopologicalOrder(G, seq2))
