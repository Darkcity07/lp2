from collections import deque

class Graph:
    def __init__(self, v):
        self.V = v
        self.adj = [[] for _ in range(v)]
    
    def addEdge(self, v, w):
        self.adj[v].append(w)
    
    def BFS(self, s):
        visited = [False] * self.V
        queue = deque()
        visited[s] = True
        queue.append(s)
        while queue:
            s = queue.popleft()
            print(s, end=" ")
            for n in self.adj[s]:
                if not visited[n]:
                    visited[n] = True
                    queue.append(n)

g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
print("Following is Breadth First Traversal (starting from vertex 2)")
g.BFS(2)
