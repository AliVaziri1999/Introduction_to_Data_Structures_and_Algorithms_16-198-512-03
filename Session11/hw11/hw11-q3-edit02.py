"""
Homework 11
Group assignment
Authors: Ali Vaziri, Andy Chen, Advait Ashtikar
Class: DSA 16-198-512-03
Fall 2025
"""

# Question 3:
class Graph:
    def __init__(self, filename):
        infile = open(filename, "r")
        self.V = int(infile.readline().strip())
        self.E = 0
        self.adj = [list() for _ in range(self.V)]
        E = int(infile.readline().strip())
        for _ in range(E):
            parts = infile.readline().split()
            if len(parts) < 2:
                continue
            v, w = int(parts[0]), int(parts[1])
            self.add_edge(v, w)
        infile.close()

    def add_edge(self, v, w):
        self.adj[v].append(w)
        self.E += 1

def validTopologicalOrder(graph, sequence):
    position = {v: i for i, v in enumerate(sequence)}
    if set(position.keys()) != set(range(graph.V)):
        return False
    for u in range(graph.V):
        for v in graph.adj[u]:
            if position[u] > position[v]:
                return False
    return True



G = Graph("graphT.txt")

seq1 = [3, 6, 0, 5, 2, 1, 4]
seq2 = [4, 3, 6, 0, 5, 2, 1]

print("Sequence 1 valid?", validTopologicalOrder(G, seq1))
print("Sequence 2 valid?", validTopologicalOrder(G, seq2))