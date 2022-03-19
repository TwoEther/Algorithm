'''
    sqrt(max)까지의 소수를 구하고 제곱수를 뺌
'''
import math
min, max = map(int, input().split())
LEN = int(math.sqrt(max))
visited = [True for i in range(LEN+1)]
primes = []
isSquare = [True for x in range(max-min+1)]

def Eratosthenes():
    for i in range(2,LEN+1):
        if visited[i] == False:
            continue
        for j in range(i+i,LEN+1,i):
            visited[j] = False

    for i in range(2, LEN+1):
        if visited[i]:
            primes.append(i)

Eratosthenes()

def notSquare():
    result = max-min+1
    idx = -1
    cnt = 0
    for target in range(min, max+1):
        idx += 1
        if not isSquare[idx]:
            continue 
        for prime in primes:
            square = prime ** 2
            if target % square == 0:
                addValue = square
                pidx = idx
                while pidx < len(isSquare):
                    isSquare[pidx] = False
                    pidx += square
                    addValue += square
    
    for i in isSquare:
        if i:
            cnt += 1
    
    return cnt

print(notSquare())








