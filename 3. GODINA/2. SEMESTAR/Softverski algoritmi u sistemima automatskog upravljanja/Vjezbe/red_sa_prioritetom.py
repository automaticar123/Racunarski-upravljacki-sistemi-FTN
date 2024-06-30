class Hip:
    def __init__(self):
        self.A = []
        
    def __str__(self):
        return f"Hip {self.A}"
        
def roditelj(i):
    return i // 2

def levoDete(i):
    return 2 * i

def desnoDete(i):
    return 2 * i + 1

def reorganizujHip(A, i):
    n = len(A)
    l = levoDete(i)
    d = desnoDete(i)
    najveci = l if (l <= n and A[i-1] < A[l-1]) else i
    if d <= n and A[najveci-1] < A[d-1]:
        najveci = d
    if najveci != i:
        A[i-1], A[najveci-1] = A[najveci-1], A[i-1]
        reorganizujHip(A, najveci)
        
def maksimumHipa(h):
    if len(h.A) > 0:
        print(h.A[0])
        return h.A[0]
    else:
        raise Exception("Hip nema elemenata")

def izdvojMaksimumHipa(h):
    if len(h.A) < 1:
        raise Exception("Hip nema elemenata")
    max_val = h.A[0]
    h.A[0] = h.A[-1]
    h.A.pop()
    reorganizujHip(h.A, 1)
    print(max_val)
    return max_val

def postaviKljucHipa(h, i, key):
    if key < h.A[i-1]:
        raise Exception("Nedovoljna vrednost ključa")
    h.A[i-1] = key
    while i > 1 and h.A[roditelj(i)-1] < h.A[i-1]:
        k = roditelj(i)
        h.A[k-1], h.A[i-1] = h.A[i-1], h.A[k-1]
        i = k

def dodajUHip(h, key):
    h.A.append(float('-inf'))
    postaviKljucHipa(h, len(h.A), key)
    

h = Hip()
dodajUHip(h, 10)
dodajUHip(h, 20)
dodajUHip(h, 100)
dodajUHip(h, 50)
print(h)
print('\n')

maksimumHipa(h)
postaviKljucHipa(h, 3, 200)
print(h)
print('\n')

izdvojMaksimumHipa(h)
maksimumHipa(h)
print(h)
