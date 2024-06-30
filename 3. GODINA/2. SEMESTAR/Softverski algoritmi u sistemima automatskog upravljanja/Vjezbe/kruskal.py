class Graph:
    def __init__(self):
        self.graph={}
        self.list=[]
        self.total_weight = 0
    
    def addEgde(self, u, v, w):
        if u not in self.graph:
            self.graph[u]=[]
        if v not in self.graph:
            self.graph[v]=[]
        # pristup 'u' i dodavanje u 'v' sa tezinom
        self.graph[u].append((v,w))
        self.graph[v].append((u,w))
        # dodali smo u oba smera jer je neusmeren graf
        # lista sluzi samo za sortiranje tezina
        self.list.append([u,v,w]) 

        self.total_weight += w

    # Kruskalov
    # Krecemo od grane sa minimalnom tezinom - sortiran niz!
    # Moramo da imamo podatak o tome koji cvor je kom prethodnik - svaki sam sebi predak
    def findParent(self, i, parent):
        if parent[i]!=i :
            self.findParent(parent[i], parent)
        return parent[i]

    def setParent(self, parent, rank, x, y):
        if rank[x] < rank[y]:
            parent[x]=y
        elif rank[x] > rank[y]:
            parent[y]=x
        else:
            parent[x]=y     #svj
            rank[x]+=1

    def kruskal(self):
        E=0
        #niz dodatih grana
        MST=[]
        edge_cnt = 0

        self.list = sorted(self.list, key=lambda item: item[2])
        parent = []
        rank =[]
        for i in range(len(self.graph)):
            parent.append(i)
            rank.append(0) # na pocetku svako ima 0 potomaka

        while E<len(self.graph)-1 :
            u, v, w = self.list[edge_cnt]
            edge_cnt+=1
            x = self.findParent(u, parent)
            y = self.findParent(v, parent)
            # ova sl linija nam omogucava da nikad ne zatvorimo konturu
            if x!=y :
                E+=1
                MST.append([u,v,w])
                self.setParent(parent, rank, x, y)
        for u, v, w in MST:
            print(str(u)+" -> "+str(v) + " ---- " + str(w))
        
        print("Ukupna minimalna tezina je:", sum([w for u, v, w in MST]))
        


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

g.kruskal()