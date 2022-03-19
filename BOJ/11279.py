import heapq, sys
n = int(input())
queue = []

for i in range(n):
    k = int(sys.stdin.readline().rstrip())

    if not queue and k == 0:
        print(0)
    
    elif k == 0:
        j = heapq.heappop(queue)[1]
        print(j)
    
    else:
        heapq.heappush(queue, (-k,k))
    
