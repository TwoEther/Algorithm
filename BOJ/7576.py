import sys
from collections import deque
sys = sys.stdin.readline

m,n = map(int, input().split())
tom = [[int(x) for x in input().split()] for y in range(n)]

def checkPossible():
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    for y in range(n):
        for x in range(m):
            for j in range(4):
                ddx = x + dx[j]
                ddy = y + dy[j]

                if ddx < 0 or ddx >= m or ddy < 0 or ddy >=n:
                    continue

                if tom[y][x] == -1 or tom[ddy][ddx] == -1:
                    break

                if tom[ddy][ddx] != -1:
                    break
                print(f'ddx,ddy = ({ddx}, {ddy})')
                return False
    return True

def checkComplete():
    for y in range(n):
        for x in range(m):
            if tom[y][x] == 0:
                return False
    return True

queue = deque([])
tmp = deque([])
time = 0
for y in range(n):
    for x in range(m):
        if tom[y][x] == 1:
            queue.append((x,y))


if not checkPossible():
    print(-1)

else:
    while not checkComplete():
        # print(f'------------- day{time+1} -------------')
        # for t in tom:
        #     print(t)
        dx = [1,0,-1,0]
        dy = [0,1,0,-1]
        size = len(queue)
        # print(f'queue = {queue}')

        while queue:
            x,y = queue.pop()

            for j in range(4):
                ddx = x + dx[j]
                ddy = y + dy[j]

                if ddx < 0 or ddx >= m or ddy < 0 or ddy >=n:
                    continue

                if tom[ddy][ddx] == 0:
                    tmp.append((ddx,ddy))
                    tom[ddy][ddx] = 1
        
        while tmp:
            x, y = tmp.popleft()
            queue.append((x,y))

        time += 1
    print(time)
        
