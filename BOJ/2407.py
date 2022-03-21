n, m = map(int, input().split())
dp = [[1 for x in range(101)] for y in range(101)]

dp[1][0] = 1
dp[1][1] = 1

for y in range(2, n+1):
    for x in range(1, y+1):
        dp[y][x] = dp[y-1][x] + dp[y-1][x-1]
        
print(dp[n][m])