# Pronalazak najkraceg puta - tezinski grafovi
# Dijkstra i Bellman Ford

import math

graph = {
    'A': [('B', 5), ('C', 2)],
    'B': [('C', 7), ('D', 8)],
    'C': [('D', 4), ('E', 8)],
    'D': [('E', 6), ('F', 4)],
    'E': [('F', 3)],
    'F': [],
}
# Dijkstra ne radi sa negativnim tezinama jer oznacimo cvor kao posecen pre nego sto smo ispitali 
# sve njegove mogucnosti
def dijkstra(graph, V):
    unvisited = graph
    r = {}    # distance
    prethodni = {}

    for cvor in graph:
        r[cvor] = math.inf
    r[V]=0

    for cvor in graph:
        prethodni[cvor]=None

    while unvisited:
        min_cvor = None
        for cvor in unvisited:
            if min_cvor is None or r[cvor]<r[min_cvor]:
                min_cvor=cvor
        for (sused, tezina) in graph[min_cvor]:
            if tezina + r[min_cvor] < r[sused]:
                r[sused]=tezina+r[min_cvor]
                prethodni[sused] = min_cvor
        unvisited.pop(min_cvor)

    print("Minimalna udaljenost od cvora {} do ostalih cvorova je:".format(V))
    print(r)
    print("Najkraci putevi od {} do ostalih cvorova:".format(V))
    
    for cvor in prethodni:
        put = []
        n = cvor
        while n is not None:
            put.append(n)
            n = prethodni[n]
        put.reverse()
        print(cvor, ":", "->".join(put))

#dijkstra(graph, 'A')


graph2 = {
    'A': [('B', 5), ('C', 2)],
    'B': [('C', 7), ('D', 8)],
    'C': [('D', 4), ('E', 8)],
    'D': [('E', -6), ('F', 4)],
    'E': [('F', 3)],
    'F': [],
}

# Radi i sa negativnim tezinama
def bellman_ford(graph, V):
    r = {}    # distance
    prethodni = {}

    for cvor in graph:
        r[cvor] = math.inf
    r[V]=0
    for cvor in graph:
        prethodni[cvor]=None

    for i in range(len(graph)-1):
        for cvor in graph:
            for (sused, tezina) in graph[cvor]:
                if r[cvor] !=math.inf and tezina + r[cvor] < r[sused]:
                    r[sused]=tezina+r[cvor]
                    prethodni[sused] = cvor
    for cvor in graph:
            for (sused, tezina) in graph[cvor]:
                if r[cvor] !=math.inf and tezina + r[cvor] < r[sused]:
                    print("Nemoguce naci najmanju putanju - postoji nemagtivna kruzna putanja")       
                    return -1

    print("Minimalna udaljenost od cvora {} do ostalih cvorova je:".format(V))
    print(r)
    print("Najkraci putevi od {} do ostalih cvorova:".format(V))
    
    for cvor in prethodni:
        put = []
        n = cvor
        while n is not None:
            put.append(n)
            n = prethodni[n]
        put.reverse()
        print(cvor, ":", "->".join(put))

bellman_ford(graph, 'A')