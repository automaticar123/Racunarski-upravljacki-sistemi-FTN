class Graph:
    def __init__(self):
        self.g = {}

    def add_edge(self, u, v):
        if u not in self.g:
            self.g[u] = []
        if v not in self.g:
            self.g[v] = []

        self.g[u].append(v)
        self.g[v].append(u)

    def bfs(self, s):
        visited = {}
        unvisited = {}

        distances = {}

        unvisited[s] = 0
        distances[0] = [s]

        while unvisited:
            u = list(unvisited.keys())[0]
            for v in self.g[u]:
                if v not in visited:
                    if v not in unvisited:
                        unvisited[v] = unvisited[u] + 1
                        if unvisited[v] not in distances:
                            distances[unvisited[v]] = []
                        distances[unvisited[v]].append(v)
                        

            visited[u] = unvisited.pop(u)
        
        groups = {}
        groups['A'] = []
        groups['B'] = []

        for distance in distances:
            if distance % 2 == 0:
                for node in distances[distance]:
                    groups['A'].append(node)
            else:
                for node in distances[distance]:
                    groups['B'].append(node)

        for group in groups:
            groups[group].sort()

        return groups

"""     def dfs_helper(self, visited, u):
        if not visited[u]:
            visited[u] = True
        for v in self.g[u]:
            if not visited[v]:
                self.dfs_helper(visited, v)

    def dfs(self, u):
        iter = 0
        candidates = [u]
        while iter != len(self.g):
            u = candidates[0]
            visited = [False] * len(self.g)
            self.dfs_helper(visited, u)
            
            if False in visited:
                candidates.clear()
                for node in range(len(self.g)):
                    if visited[node] == False:
                        candidates.append(node)
                iter+=1
            else:
                return u
            
        return -1 """

g = Graph()

""" 
g.add_edge(0, 4)
g.add_edge(1, 0)
g.add_edge(1, 2)
g.add_edge(2, 4)
g.add_edge(2, 1)
g.add_edge(3, 1)
g.add_edge(3, 2)
g.add_edge(4, 3)

g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 0)
g.add_edge(4, 3)
g.add_edge(4, 5)
g.add_edge(5, 0)

g.add_edge(0, 5)
g.add_edge(1, 5)
g.add_edge(1, 6)
g.add_edge(2, 7)
g.add_edge(2, 8)
g.add_edge(3, 6)
g.add_edge(4, 5)
g.add_edge(4, 8)

#print(g.bfs(0))
"""
graph = Graph()
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 1)

print(g.bfs(1))
