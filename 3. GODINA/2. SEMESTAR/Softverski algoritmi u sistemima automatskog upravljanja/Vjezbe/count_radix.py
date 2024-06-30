def countingSort(niz, exp1):
    n = len(niz)
    izlaz = [0] * (n)
    count = [0] * (10)
    
    for i in range(0, n):
        index = niz[i] // exp1
        count[index % 10] += 1
 
    for i in range(1, 10):
        count[i] += count[i - 1]
 
    i = n - 1
    while i >= 0:
        index = niz[i] // exp1
        izlaz[count[index % 10] - 1] = niz[i]
        count[index % 10] -= 1
        i -= 1
 
    i = 0
    for i in range(0, len(niz)):
        niz[i] = izlaz[i]
 
def radixSort(niz):
 
    max1 = max(niz)
 
    exp = 1
    while max1 / exp >= 1:
        countingSort(niz, exp)
        exp *= 10
 
 
niz = [170, 45, 75, 90, 802, 24, 2, 66]
niz1 = [ 6, 0, 7, 8, 7, 2, 0 ]
sortedniz1 = countingSort(niz1, len(niz1))
 
niz2 = [ 4, 8, 1, 0, 1, 1, 0, 0 ]
sortedniz2 = countingSort(niz2, len(niz2))

radixSort(niz)
for i in range(len(niz)):
    print(niz[i],end=" ")
