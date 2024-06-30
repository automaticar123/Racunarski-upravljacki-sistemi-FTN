import math

# sa casa
graph = {
    5: [3, 7],
    3: [2, 4],
    7: [8],
    4: [8],
    2: [],
    8: [],
}

def bfs_cas(graph, V):
    visited = []
    unvisited = []
    visited.append(V)
    unvisited.append(V)

    while unvisited:
        m=unvisited.pop(0)    # FIFO
        for sused in graph[m]:
            if sused not in visited:
                unvisited.append(sused)
                visited.append(sused)
    return visited
            
print(bfs_cas(graph, 5))




# NIJE sa casa

class Cvor:
    def __init__(self, color, d, pred):
        self.color = color
        self.d = d
        self.pred = pred

class graph:
    def __init__(self, AdjMatrix, V):
        self.AdjMatrix = AdjMatrix
        self.V = V

def AdjMatrix(n, edges):
    # nxn matrica nula
    adj_matrix = [[0] * n for _ in range(n)]

    # Loop through the list of edges and update the matrix accordingly
    for edge in edges:
        u, v = edge
        adj_matrix[u][v] = 1
        adj_matrix[v][u] = 1

    V = [Cvor('W', 0, 0) for i in range(n)]
    return adj_matrix, V


def nonEmptyGraph(AdjMat):
    adj_matrix, V = AdjMat
    return graph(adj_matrix, V)


def BFS(G, s):
    v = list(range(len(G.AdjMatrix)))
    for u in v:
        if u != s:
            G.V[u].color = 'W'
            G.V[u].d = math.inf
            G.V[u].pred = -1

    G.V[s].color = 'G'
    G.V[s].d = 0
    G.V[s].pred = -1

    Q = []
    Q.append(s)
    while Q:
        u = Q[0]
        del Q[0]
        for v in [i for i in range(len(G.AdjMatrix[u])) if G.AdjMatrix[u][i] == 1]:
            if G.V[v].color == 'W':
                G.V[v].color = 'G'
                G.V[v].d = G.V[u].d + 1
                G.V[v].pred = u
                Q.append(v)
        G.V[u].color = 'B'


def getPath(G, idStart, idEnd):
    path = []
    temp = idEnd
    while temp != idStart:
        path.insert(0, temp)
        temp = G.V[temp].pred
    path.insert(0, idStart)
    return path

# Prvi nacin poziva

# n = 5
# edges = [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4), (2, 4)]
# adj_matrix = AdjMatrix(n, edges)

# Drugi nacin poziva

adj_matrix = [[0, 0, 1, 0, 0], 
              [1, 0, 0, 1, 0], 
              [0, 1, 0, 1, 0], 
              [0, 0, 0, 0, 1], 
              [0, 0, 0, 0, 0]]
nodes = [Cvor('W', 0, 0) for i in range(len(adj_matrix))]
g = graph(adj_matrix, nodes)

BFS(g, 0)

path = getPath(g, 0, 4)

print(path)
