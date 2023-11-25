import math

class Graph:
    def __init__(self):
        self.graph = {}
        self.list = []

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []

        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))

        self.list.append([u, v, weight])

    def top_sort_help(self, visited, stack, u):
        visited[u] = True
        for v in self.graph[u]:
            if not visited[v]:
                self.top_sort_help(visited, stack, v)

        stack.insert(0, u)

    def top_sort(self):
        visited = [False] * len(self.graph) 
        stack = []

        for i in range(len(self.graph)):
            if not visited[i]:
                self.top_sort_help(visited, stack, i)

        return stack
    
    def prim(self):
        visited = [False] * len(self.graph)
        E = 0
        visited[0] = True

        while E < len(self.graph) - 1:
            minimum = math.inf
            source = 0
            dest = 0
            final_minimum = 0

            for cvor1 in range(len(self.graph)):
                if visited[cvor1]:
                    for cvor2 in range(len(self.graph)):
                        if not visited[cvor2]:
                            cvor12_veza = False
                            for (sused, w) in self.graph[cvor1]:
                                if cvor2 == sused:
                                    cvor12_veza = True
                                if cvor12_veza:
                                    if w < minimum:
                                        minimum = w
                                        source = cvor1
                                        dest = cvor2
                                        final_minimum = w

                print(str(source) + " " + str(dest) + " " + str(final_minimum))
                visited[dest] = True
                E += 1

    def find_parent(self, parent, u):
        if parent[u] != u:
            self.find_parent(parent, parent[u])
        return parent[u]
    
    def self_parent(self, parent, rank, x, y):
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[y] = x
            rank[x] += 1

    def kruskal(self):
        MST = []
        E = 0
        edge_counter = 0

        self.list = sorted(self.list, key=lambda elem: elem[2])

        parent = []
        rank = []

        for index in range(len(self.graph)):
            parent.append(index)
            rank.append(0)

        while E < len(self.graph) - 1:
            u, v, w = self.list[edge_counter]
            edge_counter += 1
            x = self.find_parent(parent, u)
            y = self.find_parent(parent, v)

            if x != y:
                E += 1
                MST.append((u, v, w))
                self.set_parent(parent, rank, x, y)

        for u, v, w in MST:
            print(u, v, w)

g = Graph()

"""
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)
"""

g.add_edge(0, 1, 4)
g.add_edge(0, 7, 8)
g.add_edge(1, 2, 8)
g.add_edge(1, 7, 11)
g.add_edge(2, 3, 7)
g.add_edge(2, 5, 4)
g.add_edge(2, 8, 2)
g.add_edge(3, 4, 9)
g.add_edge(3, 5, 14)
g.add_edge(4, 5, 10)
g.add_edge(5, 6, 2)
g.add_edge(6, 7, 1)
g.add_edge(6, 8, 6)
g.add_edge(7, 8, 7)

#print(g.top_sort())
print(g.prim())




