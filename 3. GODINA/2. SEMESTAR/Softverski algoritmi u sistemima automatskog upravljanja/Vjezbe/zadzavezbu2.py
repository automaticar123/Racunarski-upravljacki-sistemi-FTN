class Graph:
    def __init__(self):
        self.graph = {}

    def addEdge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)

    def DFS(self, v, visited):
        visited[v] = True
        for u in self.graph[v]:
            if not visited[u]:
                self.DFS(u, visited)

    # graf je jako povezan ako se iz svakog cvora moze stici do svakog drugog cvora u grafu
    def jakoPovezan(self):
        n = len(self.graph)
        for i in range(n):
            visited = [False] * n
            self.DFS(i, visited)
            for b in visited:
                if not b:
                    return False
        return True
    
    # izvorni je onaj od kog se moze stici do svakog drugog cvora u grafu
    def pronadjiIzvorniCvor(self):
        n = len(self.graph)
        visited = [False] * n
        v = 0
        for i in range(n):
            if not visited[i]:
                self.DFS(i, visited)
                v = i

        visited = [False] * n
        self.DFS(v, visited)
        for i in range(n):
            if not visited[i]:
                return -1
            
        return v
    
    # bipartitan graf je onaj kod kog se cvorovi mogu podeliti u 2 grupe, pri cemu 
    # je svaki cvor iz jedne grupe povezan sa bar jednim iz druge grupe, dok cvorovi 
    # iz iste grupe ne formiraju veze
    def addEdge_neusmeren(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def bipartitanGraf(self):
        n = len(self.graph)
        v = 0
        visited = [False] * n
        level = [None] * n
        visited[v] = True
        level[v] = 0

        queue = []
        queue.append(v)

        while queue:
            v = queue.pop(0)
            for u in self.graph[v]:
                if not visited[u]:
                    visited[u] = True
                    level[u] = level[v] + 1
                    queue.append(u)
                elif level[v] == level[u]:
                    return False
                
        return True
    
if __name__ == '__main__':
    graph = Graph()
    graph.addEdge(0, 4)
    graph.addEdge(1, 0)
    graph.addEdge(1, 2)
    graph.addEdge(2, 1)
    graph.addEdge(2, 4)
    graph.addEdge(3, 1)
    graph.addEdge(3, 2)
    graph.addEdge(4, 3)
    if graph.jakoPovezan():
        print('Graf je jako povezan')
    else:
        print('Graf nije jako povezan')

    graph2 = Graph()
    graph2.addEdge(0, 1)
    graph2.addEdge(1, 2)
    graph2.addEdge(2, 3)
    graph2.addEdge(3, 0)
    graph2.addEdge(4, 3)
    graph2.addEdge(4, 5)
    graph2.addEdge(5, 0)
    root = graph2.pronadjiIzvorniCvor()
    if root != -1:
        print('Izvorni cvor je', root)
    else:
        print('Izvorni cvor ne postoji')

    graph3 = Graph()
    graph3.addEdge_neusmeren(0, 5)
    graph3.addEdge_neusmeren(1, 5)
    graph3.addEdge_neusmeren(1, 6)
    graph3.addEdge_neusmeren(2, 7)
    graph3.addEdge_neusmeren(2, 8)
    graph3.addEdge_neusmeren(3, 6)
    graph3.addEdge_neusmeren(4, 5)
    graph3.addEdge_neusmeren(4, 8)
    if graph3.bipartitanGraf():
        print('Graf je bipartitan')
    else:
        print('Graf nije bipartitan')