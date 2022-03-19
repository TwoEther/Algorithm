from collections import deque
import sys
n = int(input())
queue = deque()

for i in range(n):
    s = sys.stdin.readline().split()
    if s[0] == 'push_back':
        queue.append(int(s[1]))

    elif s[0] == 'push_front':
        queue.appendleft(int(s[1]))

    elif s[0] == 'pop_front':
        if not queue:
            print(-1)
        else:
            print(queue.popleft())

    elif s[0] == 'pop_back':
        if not queue:
            print(-1)
        else:
            print(queue.pop())

    elif s[0] == 'size':
        print(len(queue))
    
    elif s[0] == 'empty':
        if not queue:
            print(1)
        else:
            print(0)

    elif s[0] == 'front':
        if not queue:
            print(-1)
        else:
            print(queue[0])

    elif s[0] == 'back':
        if not queue:
            print(-1)
        else:
            print(queue[-1])
    else:
        pass