import sys
input = sys.stdin.readline

n = int(input())
k = [int(x) for x in input().split()]
s = [int(x) for x in input().split()]
result = k[0] * s[0]

for i in range(2, len(k)):
    