import sys
input = sys.stdin.readline

n = int(input())
grapes = [0 for x in range(10002)]
for i in range(n):
    grapes[i+1] = int(input())

dp = [[0 for x in range(3)] for y in range(n+1)]

if n < 3:
    print(sum(grapes))
else:
    dp[1][1] = grapes[1]
    dp[1][2] = 0
    dp[2][1] = grapes[2]
    dp[2][2] = grapes[1] + grapes[2]

    for i in range(3, n):
        dp[i][1] = max(dp[i-2][1], dp[i-2][2]) + grapes[i]
        dp[i][2] = dp[i-1][1] + grapes[i]
    
    print(dp)
    print(max(dp[i][1], dp[i][2]))

'''
if n == 1:
    print(stair[1])
elif n == 2:
    print(stair[1]+stair[2])
else:
    dp[1][1] = stair[1]
    dp[1][2] = 0
    dp[2][1] = stair[2]
    dp[2][2] = stair[1] + stair[2]

    for i in range(3, n+1):
        dp[i][1] = max(dp[i-2][1], dp[i-2][2]) + stair[i]
        dp[i][2] = dp[i-1][1] + stair[i]

    print(max(dp[n][1], dp[n][2]))
'''