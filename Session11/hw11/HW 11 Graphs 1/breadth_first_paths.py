"""
 *  Execution    python bread_first_paths.py G s
 *  Dependencies: Graph.java Queue.java Stack.java  
 *  Data files:   tinyCG.txt
 *
 *               
 *
 *  Run breadth first search on an undirected graph.
 *  Runs in O(E + V) time.
 *
"""

from stack import Stack
from graph import Graph
from queueArrayBased import Queue

class BreadthFirstPaths:

    def __init__(self, G, s):
        self._marked = [False] * G.V
        self.edge_to = [None] * G.V
        self.s = s
        self.bfs(G, s)

    def bfs(self, G, s):
        self._marked[s] = True
        queue = Queue()
        queue.enqueue(s)
        while not queue.is_empty():
            v = queue.dequeue()
            for w in G.adj[v]:
                if not self._marked[w]:
                    self.edge_to[w] = v
                    self._marked[w] = True
                    queue.enqueue(w)

    def has_path_to(self, v):
        return self._marked[v]

    def path_to(self, v):
        if not self.has_path_to(v):
            return
        path = Stack()
        x = v
        while x != self.s:
            path.push(x)
            x = self.edge_to[x]
        path.push(self.s)
        return path
    
    def distTo(self, v):
        if not self.has_path_to(v):
            return -1
        counter = 0
        looker = v
        while looker != self.s:
            looker = self.edge_to[looker]
            counter += 1
        return counter
    
    def path_to_start(self, v):
        if not self.has_path_to_start(v):
            return -1
        path = []
        x = v
        while x!=self.s:
            path.append(x)
            x = self.edge_to[x]
        path.append(self.s)
        return path[::-1]


    def has_path_to_start(self, v):
        return self.has_path_to(v)

if __name__ == '__main__':
    
    import sys
    s = int(sys.argv[2])
    
    g = Graph(filename=sys.argv[1])
    
    bfs = BreadthFirstPaths(g, s)
    for v in range(g.V):
        if bfs.has_path_to(v):
            distance = -1
            print("%d to %d [%d]: " % (s, v, bfs.distTo(v)), end='')
            for x in bfs.path_to(v):
                if x == s:
                    print(x, end='')
                else:
                    print('-%s' % x, end='')
            print()
        else:
            print("%d and %d: not connected" % (s, v))
            
    print()            
    for v in range(g.V):
        print(v, bfs.path_to_start(v))
