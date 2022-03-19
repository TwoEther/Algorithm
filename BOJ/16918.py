import sys
input = sys.stdin.readline

'''
    실제로는 N == 1 일 때,

    N % 2 == 0 일 때,

N > 1이고 N % 4 == 1일때, N % 4 == 3일때.
'''

r,c,n = map(int, input().split())
bomb = [[x for x in input().rstrip()] for y in range(r)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]

if n == 1:
    pass

elif n%2 == 0:
    for y in range(r):
        for x in range(c):
            bomb[y][x] = 'O'

else:
    for y in range(r):
        for x in range(c):
            if bomb[y][x] == 'O':
                for i in range(4):
                    ddx = x + dx[i]
                    ddy = y + dy[i]

                    if ddx < 0 or ddx >=c or ddy < 0 or ddy >= r:
                        continue
                    if bomb[ddy][ddx] == '.':
                        bomb[ddy][ddx] = 'X'

    for y in range(r):
        for x in range(c):
            if bomb[y][x] == 'O' or bomb[y][x] == 'X':
                bomb[y][x] = '.'
            else:
                bomb[y][x] = 'O'

        
for y in range(r):
    print(''.join(bomb[y]))
