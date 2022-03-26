import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin = [0 for x in range(k+1)]
INF = 10^7
dp = [INF for x in range(k+1)]
dp[0] = 0
for c in range(n):
    coin[c] = int(input())

     
for i in range(n):     # 코인 개수
    for j in range(coin[i], k+1): # 금액
        dp[j] = min(dp[j], dp[j] + dp[j-coin[i]] + 1)

print(dp)