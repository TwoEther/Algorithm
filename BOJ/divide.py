n, k = map(int, input().split())    # n의 k승

div = k
r = 1

def divideConquer(a,b,c):
    if b == 0:
        return 1
    elif b % 2 == 1:
        return divideConquer(a,b-1,c)
    else:
        v = divideConquer(a,b/2,c)