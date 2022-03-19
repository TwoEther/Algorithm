'''
import heapq
import sys

input = sys.stdin.readline

n = int(input())
queue = []

for i in range(n):
    heapq.heappush(queue, int(input()))

print(queue)

result = queue[0] * (len(queue) -1)
for i in range(1, len(queue)):
    result += queue[i] * (len(queue)-i) 
print(result)
'''

import heapq
import sys

input = sys.stdin.readline

n = int(input())
queue = []

for i in range(n):
    queue.append(int(input()))

queue.sort()

result = queue[0] * (len(queue) -1)
for i in range(1, len(queue)):
    result += queue[i] * (len(queue)-i) 
print(result)