n, k = map(int, input().split())
memo = [[0 for x in range(1001)] for y in range(1001)]


for i in range(1, n+1):
    for j in range(0, i+1):
        if j == 0 or j == i:
            memo[i][j] = 1
        else:
            memo[i][j] = (memo[i-1][j] + memo[i-1][j-1])% 10007

print(memo[n][k])