from audioop import reverse
from collections import deque
from ntpath import join

n = int(input())
j = True


for i in range(n):
    process = deque([x for x in input()])
    l = int(input())
    s = input()[1:-1]
    r = 0
    
    if not s:
        print('error')
        continue
    
    ex = deque(map(int, s.split(',')))
    for p in process:
        # print(p)
        if p == 'R':
            r += 1
        else:
            if len(ex) == 0:
                j = False
                break
            else:
                if r % 2 == 0:
                    ex.popleft()
                else:
                    ex.pop()
                
   
    if not j:
        print('error')
        j = True
    else:
        if r % 2 == 1:
            ex.reverse()
        print("[" + ",".join(map(str,ex)) + "]")
            
