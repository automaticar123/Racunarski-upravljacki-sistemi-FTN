# Tezinski neusmereni grafovi
# Povezivanje svih cvorova tkd je suma tezina minimalna
# Razapinjuce stablo ce uvek imati V-1 grana da bi povezalo sve cvorove
# Osnovna razlika izmedju ova dva algoritma je sto prim krece od cvora a kruskal od grane


#modifikacija kako se cuvati duzina celog stabla

import math

class Graph:
    def __init__(self):
        self.graph={}
    
    def addEgde(self, u, v, w):
        if u not in self.graph:
            self.graph[u]=[]
        if v not in self.graph:
            self.graph[v]=[]
        # pristup 'u' i dodavanje u 'v' sa tezinom
        self.graph[u].append((v,w))
        self.graph[v].append((u,w))
        # dodali smo u oba smera jer je neusmeren graf
    
    # Primov    
    def prim(self):
        visited = [False] * len(self.graph)
        E=0  #vodimo racuna o broju zauzetih grana 
        visited[0]=True
        total_weight = 0

        while E<len(self.graph)-1 :
            minimum = math.inf
            source = 0
            dest = 0
            konacni_minimum = 0
            # obratiti paznju da ovo prolazi kroz indekse cvorova a ne kroz cvorove
            for v1 in range(len(self.graph)):
                if visited[v1]:
                    for v2 in range(len(self.graph)):
                        if not visited[v2]:
                            # da li su povezani
                            v1v2 = False
                            for (sused, w) in self.graph[v1]:
                                if v2 == sused:
                                    v1v2=True
                                    w12=w
                                if v1v2 == True :
                                    if w12 < minimum :
                                        minimum = w12
                                        source = v1
                                        dest =v2
                                        konacni_minimum = w12
            print(str(source)+" -> "+str(dest) + " ---- " + str(konacni_minimum))
            visited[dest] = True
            E+=1
            total_weight += konacni_minimum
        
        print("Ukupna minimalna tezina je:", total_weight)


g = Graph()
g.addEgde(0, 1, 4)
g.addEgde(0, 7, 8)
g.addEgde(1, 2, 8)
g.addEgde(1, 7, 11)
g.addEgde(2, 3, 7)
g.addEgde(2, 5, 4)
g.addEgde(2, 8, 2)
g.addEgde(3, 4, 9)
g.addEgde(3, 5, 14)
g.addEgde(4, 5, 10)
g.addEgde(5, 6, 2)
g.addEgde(6, 7, 1)
g.addEgde(6, 8, 6)
g.addEgde(7, 8, 7)
g.prim()