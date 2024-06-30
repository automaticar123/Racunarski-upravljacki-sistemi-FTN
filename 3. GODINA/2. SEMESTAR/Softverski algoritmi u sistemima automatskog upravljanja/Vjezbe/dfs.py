# Sa casa
graph = {
    5: [3, 7],
    3: [2, 4],
    7: [8],
    4: [8],
    2: [],
    8: [],
}

def dfs_cas(graph, V, visited):  
    if V not in visited:
        visited.append(V)
        for sused in graph[V]:
            dfs_cas(graph, sused, visited)
    return visited
    
visited=[]
print(dfs_cas(graph, 5, visited))




# NIJE SA CASA
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
    return adj_matrix


def nonEmptyGraph(adj_matrix):
    V = [Cvor('W', 0, 0) for i in range(len(adj_matrix))]
    return graph(adj_matrix, V)

def DFS(G):
    for u in range(len(G.AdjMatrix)):
        G.V[u].color = 'W'
        G.V[u].pred = -1

    for u in range(len(G.AdjMatrix)):
        if G.V[u].color == 'W':
            DFS_Visit(G, u)

def DFS_Visit(G, u):
    G.V[u].color = 'G'
    for v in [i for i in range(len(G.AdjMatrix[u])) if G.AdjMatrix[u][i] == 1]:
        if G.V[v].color == 'W':
            G.V[v].pred = u
            DFS_Visit(G, v)
    G.V[u].color = 'B'

def printGraph(G):
    n = len(G.AdjMatrix)
    for i in range(n):
        for j in range(n):
            print(" {}".format(G.AdjMatrix[i][j]), end="")
        print()
    print()
    for i in range(n):
        print("{} {} {}".format(G.V[i].color, G.V[i].d, G.V[i].pred))
        
# Define a graph
adj_matrix = [[0, 1, 1, 0, 0], [1, 0, 0, 1, 0], [0, 1, 0, 1, 0], [0, 0, 0, 0, 1], [0, 0, 0, 0, 0]]
G = nonEmptyGraph(adj_matrix)

DFS(G)

printGraph(G)