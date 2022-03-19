import queue
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
start, end = map(int, input().split())
graph = [[] for y in range(n+1)]
visited = [False for x in range(n+1)]
j = int(input())

for _ in range(j):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
'''
def dfs(v, end, graph, visited, depth):
    print(f'v = {v}')
    for i in graph[v]:
        if i == end:
            return depth
        else:
            if not visited[i]:
                visited[i] = True
                return dfs(i, end, graph, visited, depth+1)
    return -1
'''

def bfs(v, end, graph, visited, depth):
    print(f'v = {v}')
    visited[v] = True
    queue = deque([v])
    t_queue = deque([])
    
    while queue:
        t = queue.pop()
        s = len(graph[s])
        
        for i in graph[t]:
            if i == end:
                return depth
            else:
                t_queue.append(i)
        
        

print(dfs(start, end, graph, visited, 1))

