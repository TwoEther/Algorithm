n, k = map(int, input().split())
memo = [[0 for x in range(1001)] for y in range(1001)]


def com(n, k):
    if k == 1 or k == n:
        return n
    elif memo[n][k] != 0:
        return memo[n][k]
    else:
        memo[n][k] =  com(n-1,k-1) + com(n-1,k)

print(com(n,k))