'''
def findRoute(v, n):        # 이분탐색을 이용한 경로 구하기

    start, end = 0, 2**n-1
    result = ''
    
    for i in range(n):
        mid = (end + start) // 2
        if mid < v:
            result += 'u'       
            start = mid + 1
        else:
            result += 'd'
            end = mid - 1
    return result

n,r,c = map(int, input().split())
u_route, d_route = findRoute(r,n), findRoute(c,n)
value, add = 0, 2**(2*n-1)
route = ''

for i in range(len(u_route)):
    route += u_route[i] + d_route[i]

for r in route:
    if r == 'u':
        value += add
    add //= 2
print(value)
'''

dices = [int(x) for x in input().split()]

if dices[0] == dices[1] and dices[1] == dices[2] and dices[2] == dices[0]:
    print(dices[0]*1000 + 10000)
elif dices[0] == dices[1] or dices[1] == dices[2] or dices[2] == dices[0]:
    if dices[0] == dices[1] or dices[0] == dices[2]:
        print(1000 + dices[0]*100)
    else:
        print(1000 + dices[1]*100)
elif dices[0] != dices[1] and dices[1] != dices[2] and dices[2] != dices[0]:
    print(max(dices)*100)
else:
    pass