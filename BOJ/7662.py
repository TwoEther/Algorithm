import heapq
import sys

input = sys.stdin.readline

test_case = int(input())

for t in range(test_case):
    priority_queue = []
    n = int(input())
    for i in range(n):
        o, number = map(str, input().split())
        number = int(number)

        if o == 'I':
            heapq.heappush(priority_queue, number)
        
        else:
            if len(priority_queue) == 0:
                continue
            if number == -1:
                heapq.heappop(priority_queue)
            else:
                priority_queue = heapq.nlargest(len(priority_queue), priority_queue)[1:]
                heapq.heapify(priority_queue)
        # print('----------------------')


    if len(priority_queue) == 0:
        print('EMPTY')
    else:
        print(priority_queue)
        maxV, minV = priority_queue[0], int(heapq.nlargest(len(priority_queue), priority_queue)[0])
        print(minV, maxV)

