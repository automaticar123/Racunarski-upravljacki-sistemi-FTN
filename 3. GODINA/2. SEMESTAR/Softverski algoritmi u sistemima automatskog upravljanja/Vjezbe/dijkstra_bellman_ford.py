# Pronalazak najkraceg puta - tezinski grafovi
import math

graph = {
    'A': [('B', 5), ('C', 2)],
    'B': [('C', 7), ('D', 8)],
    'C': [('D', 4), ('E', 8)],
    'D': [('E', 6), ('F', 4)],
    'E': [('F', 3)],
    'F': [],
}
graph2 = {
    'A': [('B', 5), ('C', 2)],
    'B': [('C', 7), ('D', 8)],
    'C': [('D', 4), ('E', 8)],
    'D': [('E', -6), ('F', 4)],
    'E': [('F', 3)],
    'F': [],
}

# Dijkstra ne radi sa negativnim tezinama jer oznacimo cvor kao posecen
# pre nego sto smo ispitali sve njegove mogucnosti
def dijkstra(graph, V):
    unvisited = graph
    r = {}    # distance
    for cvor in graph:
        r[cvor] = math.inf
    r[V]=0
    while unvisited:
        min_cvor = None
        for cvor in unvisited:
            if min_cvor is None or r[cvor]<r[min_cvor]:
                min_cvor=cvor
        for (sused, tezina) in graph[min_cvor]:
            if tezina + r[min_cvor] < r[sused]:
                r[sused]=tezina+r[min_cvor]
        unvisited.pop(min_cvor)

    print("Min udaljenost svakog cvora od cvora {} je: ".format(V), r)
    # for cvor in r:
    #     print("{0}/t/t{1}", format[cvor, r[cvor]])

dijkstra(graph, 'A')


# Bellman Ford radi i sa negativnim tezinama
def bellman_ford(graph, V):
    r = {}    # distance
    for cvor in graph:
        r[cvor] = math.inf
    r[V]=0

    for i in range(len(graph)-1):
        for cvor in graph:
            for (sused, tezina) in graph[cvor]:
                if r[cvor] !=math.inf and tezina + r[cvor] < r[sused]:
                    r[sused]=tezina+r[cvor]
    for cvor in graph:
            for (sused, tezina) in graph[cvor]:
                if r[cvor] !=math.inf and tezina + r[cvor] < r[sused]:
                    print("Nemoguce naci najmanju putanju - postoji nemagtivna kruzna putanja")       
                    return -1

    print("Min udaljenost svakog cvora od cvora {} je: ".format(V), r)

bellman_ford(graph2, 'A')