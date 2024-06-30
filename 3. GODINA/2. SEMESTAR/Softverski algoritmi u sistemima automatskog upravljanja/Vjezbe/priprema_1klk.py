def prviZadatak(niz):
    donjaGranica = 0
    gornjaGranica = len(niz)-1
    while donjaGranica <= gornjaGranica:
        sredina = (donjaGranica+gornjaGranica) // 2
        if niz[sredina] % 2 == 0:
            return niz[sredina]
        elif niz[sredina] > (sredina*2-1):
            donjaGranica = sredina+1
        else:
            gornjaGranica = sredina-1
    
    return -1


niz1=[1, 3, 5, 6, 7, 9, 11, 13, 15, 17, 19]
niz2=[1, 3, 5, 7, 9, 11, 13, 14, 15, 17, 19]
niz3=[1, 2, 3, 5, 7, 9, 11, 13, 15, 17, 19]
niz4=[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 20]
niz5=[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 40]
print("Paran broj ubacen u niz je", prviZadatak(niz3))
print(" ")

# Drugi zadatak

class Graph:
    def __init__(self):
        self.graph = {}

    def addEdge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []

        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def addEdge_directed(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []

        self.graph[u].append(v)

    def bfs(self, V):
        visited = []
        unvisited = []
        visited.append(V)
        unvisited.append(V)
        
        graph2 = Graph()

        while unvisited:
            m = unvisited.pop(0)
            for sused in self.graph[m]:
                if sused not in visited:
                    unvisited.append(sused)
                    visited.append(sused)
                    graph2.addEdge_directed(sused, m)
    
        return graph2
    
if __name__ == '__main__':
    graph = Graph()
    graph.addEdge(0, 1)
    graph.addEdge(1, 3)
    graph.addEdge(2, 3)
    graph.addEdge(2, 0)
    graph.addEdge(4, 2)
    graph.addEdge(3, 5)
    graph.addEdge(4, 3)
    usmereni = graph.bfs(0)
    print("Grane usmerenog grafa:")
    for u in usmereni.graph:
        for v in usmereni.graph[u]:
            print("({0} -> {1})".format(u, v))
        