import math

class Graph:
    def __init__(self):
        self.graph={}
        self.valueToIndex = {}
        self.indexToValue = {}
        self.index = 0
    
    def addEgde(self, u, v, w):
        if u not in self.valueToIndex:
            self.valueToIndex[u] = self.index
            self.indexToValue[self.index] = u
            self.graph[self.index] = []
            self.index += 1
        if v not in self.valueToIndex:
            self.valueToIndex[v] = self.index
            self.indexToValue[self.index] = v
            self.graph[self.index] = []
            self.index += 1
        # pristup 'u' i dodavanje u 'v' sa tezinom
        self.graph[self.valueToIndex[u]].append((self.valueToIndex[v],w))
        self.graph[self.valueToIndex[v]].append((self.valueToIndex[u],w))
        # dodali smo u oba smera jer je neusmeren graf
    
    # Primov    
    def prim(self):
        visited = [False] * len(self.graph)
        E=0  #vodimo racuna o broju zauzetih grana 
        visited[0]=True

        while E<len(self.graph)-1 :
            minimum = math.inf
            source = 0
            dest = 0
            konacni_minimum = 0
            # prolazimo kroz indekse cvorova a ne kroz cvorove
            for v1 in range(len(self.graph)):
                if visited[v1]:
                    for (v2, w) in self.graph[v1]:
                        if not visited[v2]:
                            if w < minimum :
                                minimum = w
                                source = v1
                                dest =v2
                                konacni_minimum = w
            print(str(self.indexToValue[source])+" -> "+str(self.indexToValue[dest]) + " ---- " + str(konacni_minimum))
            visited[dest] = True
            E+=1


g = Graph()
g.addEgde('A', 'B', 4)
g.addEgde('A', 'H', 8)
g.addEgde('B', 'C', 8)
g.addEgde('B', 'H', 11)
g.addEgde('C', 'D', 7)
g.addEgde('C', 'F', 4)
g.addEgde('C', 'I', 2)
g.addEgde('D', 'E', 9)
g.addEgde('D', 'F', 14)
g.addEgde('E', 'F', 10)
g.addEgde('F', 'G', 2)
g.addEgde('G', 'H', 1)
g.addEgde('G', 'I', 6)
g.addEgde('H', 'I', 7)
g.prim()
