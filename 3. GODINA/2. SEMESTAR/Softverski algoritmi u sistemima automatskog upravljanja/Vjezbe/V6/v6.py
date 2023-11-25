# memo = {1:1, 2:1}

# def fibonacci_memo(n):
#     if n in memo:
#         return memo[n]
    
#     memo[n] = fibonacci_memo(n-1) + fibonacci_memo(n-2)
#     return memo[n]

# def fibonacci_tab(n):
#     table = [1, 1]
#     for i in range(2, n):
#         table.append(table[i-1] + table[i-2])

#     return table[n-1]

# print(fibonacci_memo(7))
# print(fibonacci_tab(15))

# base = {0: 1, 1: 1, 2: 2}
# def func_memo(n):
#     if n in base:
#         return base[n]
    
#     base[n] = func_memo(n-1) + func_memo(n-2) + func_memo(n-3)

#     return base[n]

# def func_tab(n):
#     table = [1, 1, 2]
#     for i in range(3, n+1):
#         table.append(table[i-1] + table[i-2] + table[i-3])

#     return table[n]

# print(func_memo(4), func_tab(4))

def tabla_memo(memo_matrix, m, n): 
    if m == 0 or n == 0:
        memo_matrix[m][n] = 1

    if memo_matrix[m][n] != 0:
        return memo_matrix[m][n]

    memo_matrix[m][n] = tabla_memo(memo_matrix, m, n-1) + tabla_memo(memo_matrix, m-1, n)
    return memo_matrix[m][n]

def tabla_tab(m, n):
    matrix = [[0 for i in range(n)] for j in range(m)]
    
    for i in range(0, n):
        matrix[0][i] = 1

    for i in range(1, m):
        matrix[i][0] = 1

    for i in range(1, m):
        for j in range(1, n):
            matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]

    return matrix[m-1][n-1]

print(tabla_memo([[0 for i in range(4)] for j in range(3)], 3-1, 4-1))
