# 1. zadatak
def binary_search_1(A, start, end):
    if start == end:
        if start == 0:
            return 0
        else:
            return len(A)

    middle = (start + end) // 2

    if A[middle] != middle:
        # Left tree
        if A[middle] - 1 == A[middle-1]:
            result = binary_search_1(A, start, middle-1)
            if result != -1:
                return result
        else:
            return A[middle] - 1
    else:
        # Right tree
        if A[middle] + 1 == A[middle+1]:
            result = binary_search_1(A, middle+1, end)
            if result != -1:
                return result
        else:
            return A[middle] + 1
            
    return -1

def testiraj_prvi():
    A = [0, 1, 2, 3, 4, 5, 6, 8]
    print(binary_search_1(A, 0, len(A)-1))

# testiraj_prvi()

# 2. zadatak
def binary_search_2(A, start, end):
    if start > end:
        return -1
    
    middle = (start+end) // 2

    if A[middle] == middle:
        return middle
    elif A[middle] > middle:
        result = binary_search_2(A, start, middle-1)
        if result != -1:
            return result
    else:
        binary_search_2(A, middle+1, end)
        if result != -1:
            return result
        
    return -1

def testiraj_drugi():
    A = [1, 4, 6, 7, 9]
    print(binary_search_2(A, 0, len(A)-1))

# testiraj_drugi()

# 3. zadatak - Napomena: moze bilo koji algoritam složenosti O(nlogn)
def quick_sort(A, start, end):
    # Koristim srednji element kao pivot
    if start >= end:
        return
    
    pivot = A[(start+end) // 2]
    last_item = A[end]
    A[end] = pivot
    A[(start+end) // 2] = last_item

    while(True):
        i = 0
        j = end - 1
        while(A[i] < pivot):
            i+=1
        while(A[j] > pivot):
            j-=1
        if i > j:
            break
        A[i], A[j] = A[j], A[i]
    
    temp = A[i]
    A[i] = pivot
    A[end] = temp

    quick_sort(A, start, i-1)
    quick_sort(A, i+1, end)

    return A

def find_largest_product(A):
    if A[0]*A[1] < A[len(A)-2]*A[len(A)-1]:
        return A[len(A)-2]*A[len(A)-1]
    else:
        return A[0]*A[1]
    
def testiraj_treci():
    A = [2, 1, 0, 5, 8, 7, 6, 3]
    print("Sorted array: {array}.\r\nThe largest product is {product}."
          .format(array=quick_sort(A, 0, len(A)-1), product=find_largest_product(A)))

# testiraj_treci()

# 4. Zadatak
def triplets(A, sum):
    # Najbolja slozenost koju sam uspio jeste O(n^2), nisam siguran moze li
    # mozda sa O(nlogn) 
    quick_sort(A, 0, len(A)-1)
    founded = []
    for i in range(len(A)-2):
        j = i + 1
        k = len(A) - 1

        while(k >= j):
            if A[i] + A[j] + A[k] == sum:
                founded.append((A[i], A[j], A[k]))
            if A[i] + A[j] + A[k] > sum:
                k-=1
            else:
                j += 1

    return founded

def testiraj_cetvrti():
    A = [1, 3, 10, 18, 23, 67, 87, 110, 124]
    print(triplets(A, 100))

# testiraj_cetvrti()



