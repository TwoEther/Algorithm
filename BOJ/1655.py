import sys, heapq
input = sys.stdin.readline

minheap = []
maxheap = []

t = int(input())


for i in range(1, t+1):
    target = int(input())
    
    if len(minheap) == len(maxheap):
        heapq.heappush(maxheap, (-target,target))
    else:
        heapq.heappush(minheap, (target, target))
    
    if minheap and minheap[0][1] < maxheap[0][1]:
        v_min = heapq.heappop(minheap)[1]
        v_max = heapq.heappop(maxheap)[1]
        heapq.heappush(minheap, (v_max, v_max))
        heapq.heappush(maxheap, (-v_min, v_min))
    # print(f'maxheap = {maxheap}   minheap = {minheap}')
    print(maxheap[0][1])

    


