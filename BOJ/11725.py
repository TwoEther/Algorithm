from re import L
import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
results = [0 for x in range(n+1)]
visited = [False for x in range(n+1)]
tree = [[0 for x in range(n+1)] for y in range(n+1)]


for i in range(n-1):
    v1, v2 = map(int, input().split())
    tree[v1].append(v2)
    tree[v2].append(v1)

queue = deque([1])

while queue:
    target = queue.pop()
    visited[target] = True

    for t in tree[target]:
        if not visited[t]:
            queue.append(t)
            results[t] = target

for i in range(2,len(results)):
    print(results[i])