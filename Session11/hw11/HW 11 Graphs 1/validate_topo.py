# Question 3


import sys


def load_directed_edges(filename):
    """
    Reads the graph file as a DAG
    returns a list of edges [(u, v), ...]
    """
    edges = []
    try:
        with open(filename, "r") as infile:

            V = int(infile.readline())
            E = int(infile.readline())

            lines = infile.readlines() # Read each edge line
            for line in lines:
                parts = line.split()
                if len(parts) >= 2:
                    u, v = int(parts[0]), int(parts[1])
                    edges.append((u, v))
    except FileNotFoundError:
        print(f"Error: Could not find file {filename}")
        sys.exit(1)

    return edges


def validTopologicalOrder(filename, sequence):

    edges = load_directed_edges(filename)

    # create a map to store the position (index) of each vertex in the proposed sequence, this allows us to check positions in O(1) time.
    # Ex: if sequence is [3, 6, 0...], position[3] = 0, position[6] = 1
    position = {vertex: i for i, vertex in enumerate(sequence)}

    # validate every edge; u must appear before v in the sequence.
    for u, v in edges:

        if u not in position or v not in position: # ensure vertices exist in the sequence
            print(f"Error: Vertex in edge ({u}->{v}) is missing from the sequence.")
            return False

        # check if the position of u after the position of v
        if position[u] > position[v]:
            print(f"Invalid: Edge {u} -> {v} violates the order.")
            print(f"{u} is at index {position[u]}")
            print(f"{v} is at index {position[v]}")
            return False

    return True # if no edges violated the rule, it is valid.


if __name__ == '__main__':

    graph_file = "graphT.txt"

    order_1 = [3, 6, 0, 5, 2, 1, 4]
    order_2 = [4, 3, 6, 0, 5, 2, 1]

    print(f"Validating Topological Orders for {graph_file} ---\n")

    # test 1
    print(f"Checking Sequence 1: {order_1}")
    result1 = validTopologicalOrder(graph_file, order_1)
    if result1:
        print("Result: VALID topological order.")
    else:
        print("Result: NOT a valid topological order.")
    print("-" * 40)

    # test 2
    print(f"Checking Sequence 2: {order_2}")
    result2 = validTopologicalOrder(graph_file, order_2)
    if result2:
        print("Result: VALID topological order.")
    else:
        print("Result: NOT a valid topological order.")
    print("-" * 40)