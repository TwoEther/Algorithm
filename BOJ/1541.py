import sys
input = sys.stdin.readline

exp = input().strip().split('-')    # -로 분리
result = 0

for idx, e in enumerate(exp):
    try:
        eval(e)
            
    except SyntaxError:
        p = list(map(lambda x : int(x) , e.split('+')))
        addnum = sum(p)
        
    else:
        addnum = eval(e)
    
    if idx == 0:
        result += addnum
    else:
        result -= addnum


print(result)
   