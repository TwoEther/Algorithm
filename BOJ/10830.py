import sys
input = sys.stdin.readline
n,k = map(int, input().split())
matrix = [[int(x) for x in input().split()] for y in range(n)]
P = 10**3

def square_matrix(matrix1, matrix2):
    r_matrix = [[0 for x in range(n)] for y in range(n)]
    for y in range(n):
        for x in range(n):
            for i in range(n):
                r_matrix[y][x] += matrix1[y][i] * matrix2[i][x]
            r_matrix[y][x] %= P
    

    return r_matrix

def power(m, s):
    ret = [[0 for x in range(n)] for y in range(n)]
    for y in range(n):
        for x in range(n):
            if x == y:
                ret[y][x] = 1

    while s > 0:
        if s % 2: 
            ret = square_matrix(ret, m)
        
        m = square_matrix(m,m)
        s //= 2
    
    return ret;


result = power(matrix, k)
for y in range(n):
    for x in range(n):
        print(result[y][x], end=' ')
    print()