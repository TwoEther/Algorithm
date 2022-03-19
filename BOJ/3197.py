import sys
input = sys.stdin.readline

r,c = map(int, input().split())
lake = [[x for x in input().rstrip()] for y in range(r)]
lPos = []
# 서로다른 L의 좌표 찾기
for y in range(r):
    for x in range(c):
        if lake[y][x] == 'L':
            lPos.append((x,y))



def meltLake():
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    for y in range(r):
        for x in range(c):
            if lake[y][x] == '.':
                for i in range(4):
                    ddx = x + dx[i]
                    ddy = y + dy[i]

                    if ddx >= c or ddx < 0 or ddy >= r or ddy < 0:
                        continue
                    
                    if lake[ddy][ddx] == 'X':
                        lake[ddy][ddx] = 'O'
        
    for y in range(r):
        for x in range(c): 
            if lake[y][x] == 'O':
                lake[y][x] = '.'

def findRoot(xPos1, yPos1, xPos2, yPos2):
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    visited = [[False for x in range(c)] for y in range(r)]

    stack = [(xPos1, yPos1)]

    while stack:
        # print(f'stack = {stack}')
        xPos, yPos = stack.pop()
        visited[yPos][xPos] = True
        for i in range(4):
            ddx = xPos + dx[i]
            ddy = yPos + dy[i]

            if ddx >= c or ddx < 0 or ddy >= r or ddy < 0:
                continue
                
            if lake[ddy][ddx] == '.' and not visited[ddy][ddx]:
                stack.append((ddx, ddy))
                visited[ddy][ddx] = True
            
            if ddx == xPos2 and ddy == yPos2:
                return True
            
    return False

xpos1, ypos1 = lPos.pop()
xpos2, ypos2 = lPos.pop()


for d in range(1,100000):
    meltLake()
    '''
    print('---------- day{} -----------'.format(d))
    for y in range(r):
        for x in range(c): 
            print(lake[y][x], end=' ')
        print()
    '''

    if findRoot(xpos1, ypos1, xpos2, ypos2):
        print(d)
        break


    

