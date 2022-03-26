import queue
from re import T
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
INF = 102
start, end = map(int, input().split())
graph = [[INF for x in range(n+1)] for y in range(n+1)]
visited = [False for x in range(n+1)]
root = []
j = int(input())

for _ in range(j):
    v1, v2 = map(int, input().split())
    graph[v1][v2] = 1
    graph[v2][v1] = 1


# Floyd-warshall
for k in range(1, n+1):
    for j in range(1, n+1):
        for i in range(1, n+1):
            if i == j:
                graph[i][j] = 0
                
for k in range(1, n+1):
    for j in range(1, n+1):
        for i in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

if graph[start][end] == INF:
    print(-1)
else:
    print(graph[start][end])