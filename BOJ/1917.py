# 정육면체 전개도
import sys
input = sys.stdin.readline
MAX = 6

def IsPossible(ary):
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    
    for y in range(6):
        for x in range(6):
            count = 2
            if ary[y][x] == 0:
                continue
            else:
                for i in range(4):
                    idx = i
                    ddx = x + dx[i]
                    ddy = y + dy[i]
                    
                    if ddx < 0 or ddy < 0 or ddx >= MAX or ddy >= MAX:            
                        continue
                    else:
                        if ary[ddy][ddx] == 1:
                            for j in range(2): 
                                ddx += dx[idx]
                                ddy += dy[idx]
                                # print(f'x = {x}  y = {y}')
                                # print(f'ddx = {ddx}  ddy = {ddy}')
                                # print(f'count = {count}')
                                if ddx < 0 or ddy < 0 or ddx >= MAX or ddy >= MAX or ary[ddy][ddx] == 0:            
                                    break
                                else:
                                    count += 1
                                
                                if count == 4:
                                    return "yes"
    return "no"


for test_case in range(3):
    six_square = [[int(x) for x in input().split()] for y in range(MAX)]
    print(IsPossible(six_square))
    