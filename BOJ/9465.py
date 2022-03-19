import sys

input = sys.stdin.readline
t = int(input())


for _ in range(t):
    n = int(input())
    scores = [[int(x) for x in input().split()] for y in range(2)]
    dp = [[0 for x in range(n)] for y in range(3)]
    dp[0][0] = 0 
    dp[1][0] = scores[0][0]
    dp[2][0] = scores[1][0]
    
    for j in range(1,n):
        dp[0][j] = max(dp[1][j-1], dp[2][j-1])
        dp[1][j] = max(dp[0][j-1], dp[2][j-1]) + scores[0][j]
        dp[2][j] = max(dp[0][j-1], dp[1][j-1]) + scores[1][j]
    
    print(max(dp[0][n-1], dp[1][n-1], dp[2][n-1]))

