# Binary search - normal method
def binary_search(A, key):
    start = 0
    end = len(A) - 1

    while start <= end:
        middle = (start+end) // 2

        if A[middle] == key:
            return middle
        elif A[middle] > key:
            end = middle - 1
        else:
            start = middle + 1

    return -1

# Recursive binary search 
def binary_search_recursive(A, start, end, key):
    if start > end:
        return -1
    middle = (start+end) // 2

    if A[middle] == key:
        return middle
    elif A[middle] > key:
        result = binary_search_recursive(A, start, middle-1, key)
    else:
        result = binary_search_recursive(A, middle+1, end, key)

    return result

# Selection sort 
def selection_sort(A):
    for i in range(len(A)):
        indmin = i
        for j in range(i, len(A)):
            if A[indmin] > A[j]:
                indmin = j

        A[i], A[indmin] = A[indmin], A[i]

def insertion_sort(A):
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j-=1
        A[j+1] = key

def merge_sort(A, start, end):
    if start < end:
        middle = (start+end) // 2
        merge_sort(A, start, middle)
        merge_sort(A, middle+1, end)

        L = A[start:middle+1]
        R = A[middle+1:end+1]

        i = j = 0
        k = start

        while i != len(L) and j != len(R):
            if L[i] <= R[j]:
                A[k] = L[i]
                i+=1
            else:
                A[k] = R[j]
                j+=1
            k+=1

        while i != len(L):
            A[k] = L[i]
            i+=1
            k+=1
        while j != len(R):
            A[k] = R[j]
            j+=1
            k+=1


A = [7, 5, 4, 1, 8, 3, 6]
# print(binary_search_recursive(A, 0, len(A)-1,key))
# selection_sort(A)
# insertion_sort(A)
merge_sort(A, 0, len(A)-1)
print(A)
