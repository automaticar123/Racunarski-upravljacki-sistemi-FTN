def validPath(n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    ## convert to a dictionary
    def add_dict(d, k, v):
        if k in d:
            d[k].append(v)
        else:
            d[k] = [v]
    d = dict()
    for e in edges:
        add_dict(d, e[0], e[1])
        add_dict(d, e[1], e[0])
        
    ## edge cases
    if n==1: return True
    if source not in d or destination not in d: return False
    
    ## DFS
    l, visited = [source], set() # list, set
    while l:
        n = l.pop(0) # node
        if destination in d[n]:
            return True
        else:
            visited.add(n)
            for n1 in d[n]: # child nodes
                if n1 not in visited:
                    l.append(n1)
    return False         

