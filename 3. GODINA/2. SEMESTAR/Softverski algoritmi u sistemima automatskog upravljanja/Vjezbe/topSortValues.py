# sad cvorovi nisu indeksi nego konkretne vrednosti

class Graph:
    def __init__(self):
        self.graph = {}

    def addEgde(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)

    def topSortHelp(self, v, visited_dict, stack):
        visited_dict[v] = True
        for sused in self.graph[v]:
            if not visited_dict[sused]:
                self.topSortHelp(sused, visited_dict, stack)
        stack.insert(0, v)

    def topSort(self):
        visited_dict = {v: False for v in self.graph}
        stack = []
        for v in self.graph:
            if not visited_dict[v]:
                self.topSortHelp(v, visited_dict, stack)
        print(stack)

# poziv init
g = Graph()
g.addEgde(9, 7)
g.addEgde(9, 0)
g.addEgde(8, 0)
g.addEgde(8, 1)
g.addEgde(7, 3)
g.addEgde(3, 1)
g.topSort()
