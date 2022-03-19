import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dp = [0 for x in range(k+1)]

for c in range(n):
    coin = int(input())
    dp[coin] = 1
     
