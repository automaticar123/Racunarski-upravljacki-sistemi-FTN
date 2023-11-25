def bubble_sort(A: list):
    for i in range(len(A)):
        for j in range(len(A)-i-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]

    return A

def selection_sort(A: list):
    for i in range(len(A)):
        min = i

        for j in range(i+1, len(A)):
            if A[j] < A[min]:
                min = j

        A[i], A[min] = A[min], A[i]

    return A

def insertion_sort(A: list):
    for i in range(1, len(A)):
        current = A[i]
        j = i - 1 

        while j >= 0 and current < A[j]:
            A[j+1] = A[j]
            j-=1

        A[j+1] = current
    
    return A

def merge_sort(A):
    if len(A) > 1:
        middle = len(A) // 2
        L = A[:middle]
        R = A[middle:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1

            k += 1

        while i < len(L):
            A[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            A[k] = R[j]
            j += 1
            k += 1

    return A

def quick_sort(A, start, end):
    if start < end:
        A[(start+end)//2], A[end] = A[end], A[(start+end)//2]

        i = start - 1
        for j in range(start, end):
            if A[j] <= A[end]:
                i += 1
                A[i], A[j] = A[j], A[i]

        A[i+1], A[end] = A[end], A[i+1]
        quick_sort(A, start, i)
        quick_sort(A,i+2, end)

    return A

A =[8, 5, 3, 1, 4, 7, 9]
# print(bubble_sort(A))
# print(selection_sort(A))
# print(insertion_sort(A))
# print(merge_sort(A))
# print(quick_sort(A, 0, len(A)-1))

class Graph:
    def __init__(self) -> None:
        self.graph = {}

    def add_edge(self, u, v) -> None:
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        
        self.graph[u].append(v)

    def topological_sort_work(self, u, visited, stack) -> None:
        visited[u] = True
        for v in self.graph[u]:
            if not visited[v]:
                self.topological_sort_work(v, visited, stack)

        stack.insert(0, u)

    def topological_sort(self) -> list:
        visited = {}
        for u in self.graph.keys():
            visited[u] = False
        stack = []

        for u in self.graph.keys():
            if not visited[u]:
                self.topological_sort_work(u, visited, stack)

        return stack
    
    def dfs_work(self, u, visited, unvisited: list) -> None:
        if u not in visited:
            visited.append(u)
            unvisited.remove(u)
            for v in self.graph[u]:
                self.dfs_work(v, visited, unvisited)

    def dfs(self, s) -> None:
        visited = []
        unvisited = [s]

        for u in self.graph.keys():
            if u != s:
                unvisited.append(u)

        while unvisited:
            u = unvisited.pop(0)
            if u not in visited:
                visited.append(u)
                for v in self.graph[u]:
                    self.dfs_work(v, visited, unvisited)

        return visited


graph = Graph()
graph.add_edge('u', 'v')
graph.add_edge('v', 'y')
graph.add_edge('y', 'x')
graph.add_edge('x', 'v')
graph.add_edge('w', 'y')
graph.add_edge('w', 'z')
graph.add_edge('z', 'z')

#print(graph.topological_sort())
print(graph.dfs('u'))

                
