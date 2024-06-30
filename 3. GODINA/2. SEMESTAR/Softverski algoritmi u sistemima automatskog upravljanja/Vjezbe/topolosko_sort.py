# Da bi graf mogao topoloski da se sortira 
# mora da bude usmeren, ne mora da bude tezinski
# Nebitno je od kog cvora krecemo jer prolazimo kroz svaki cvor
# U ovom primeru smo poistovetili indexe cvorova sa njihovim vrednostima

# modifikovati ovo tkd radi sa vrednostima cvorova 
class Graph:
    def __init__(self):
        self.graph={}
    
    def addEgde(self, u, v):
        if u not in self.graph:
            self.graph[u]=[]
        if v not in self.graph:
            self.graph[v]=[]
        # pristup 'u' i dodavanje u 'v'
        self.graph[u].append(v)
    
    def topSortHelp(self, rbr, visited, stack):
        # Kao kod DFS samo sto je tamo niz bio prazan
        visited[rbr]=True
        for sused in self.graph[rbr]:
            if not visited[sused]:
                self.topSortHelp(sused, visited, stack)
        stack.insert(0, rbr)

    def topSort(self):
        # vodimo racuna o posecenim cvorovima preko bool niza
        visited = [False] * len(self.graph)
        # LIFO struktura nam je potrebna za cuvanje stanja sorta
        stack=[]
        for i in range(len(self.graph)):
            if not visited[i]:
                self.topSortHelp(i, visited, stack)
        print(stack)


# poziv init
g= Graph()
g.addEgde(5, 2)
g.addEgde(5, 0)
g.addEgde(4, 0)
g.addEgde(4, 1)
g.addEgde(2, 3)
g.addEgde(3, 1)
g.topSort()