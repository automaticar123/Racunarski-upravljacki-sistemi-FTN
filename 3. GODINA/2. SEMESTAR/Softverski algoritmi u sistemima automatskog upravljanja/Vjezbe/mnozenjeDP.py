p = [35, 27, 5, 2, 12, 20, 26]
n = len(p) - 1
m = [[0 for j in range(n)] for i in range(n)]
s = [[0 for j in range(n)] for i in range(n)]

for l in range(2, n+1):
    for i in range(0, n-l+1):
        j = i + l - 1
        m[i][j] = float('inf')
        for k in range(i, j):
            q = m[i][k] + m[k+1][j] + p[i] * p[k+1] * p[j+1]
            if q < m[i][j]:
                m[i][j] = q
                s[i][j] = k

def print_parentheses(s, i, j):
    if i == j:
        print("A", i, end=" ")
    else:
        print("(", end=" ")
        print_parentheses(s, i, s[i][j])
        print_parentheses(s, s[i][j] + 1, j)
        print(")", end=" ")

print_parentheses(s, 0, 5)