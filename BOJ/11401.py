import sys

n,k = map(int, input().split())
P = 10**9+7

def power(x, y):
    ret = 1
    while y > 0:
        if y % 2: 
            ret *= x
            ret %= P
        
        x *= x
        x %= P
        y //= 2
    
    return ret;

def factorial(n):
    ans = 1
    for i in range(2, n+1):
        ans *= i
        ans %= P
    return ans

result = (factorial(n) * power(factorial(k) * factorial(n-k), P-2)) % P
print(result)