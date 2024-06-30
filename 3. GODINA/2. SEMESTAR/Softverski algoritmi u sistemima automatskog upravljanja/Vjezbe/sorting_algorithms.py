# Bubble sort
def bubble(niz):
    for i in range(len(niz)):
        for j in range(0, len(niz)-i-1):
            if niz[j] > niz[j+1]:
                niz[j], niz[j+1] = niz[j+1], niz[j]
    return niz


# Selection Sort
def selection(niz):
    for i in range(len(niz)):
        mmin=i
        for j in range(i+1, len(niz)):
            if niz[mmin] > niz[j]:
                mmin=j
        niz[i], niz[mmin] = niz[mmin], niz[i]
    return niz

# Insertion Sort
def insertionSort(niz):
    for i in range(1, len(niz)):
        j=i-1
        tren=niz[i]
        while j>=0 and tren<niz[j]:
            niz[j+1]=niz[j]
            j-=1
        niz[j+1]=tren
    return niz


# Merge Sort
def mergeSort(niz):
    if len(niz) > 1:
        sred = len(niz)//2
        L = niz[:sred]
        R = niz[sred:]
        mergeSort(L)
        mergeSort(R)
        i=0
        j=0
        k=0

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                niz[k] = L[i]
                i += 1
            else:
                niz[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            niz[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            niz[k] = R[j]
            j += 1
            k += 1
    return niz


# Quicksort
def podela(niz, donja, gornja):
    pivot=niz[gornja]
    i=donja-1

    for j in range(donja, gornja):
        if niz[j]<=pivot:
            i+=1
            niz[j], niz[i]=niz[i],niz[j]
            
    niz[i+1], niz[gornja]=niz[gornja], niz[i+1]
    return i+1

def quickSort(niz, donja, gornja):
    if donja<gornja :
        indeks=podela(niz, donja, gornja)
        quickSort(niz, donja, indeks-1)
        quickSort(niz, indeks+1, gornja)
    return niz


niz=[4, 3, 9, 3, 7, 1]

print(bubble(niz))
print(insertionSort([4, 2, 6, 1, 3])) 
print(mergeSort(niz))
print(quickSort([3, 2, 6, 9, 4], 0, 4))
print(selection(niz))