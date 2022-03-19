import sys
input = sys.stdin.readline
p = int(input())
pz1, pz2 = [], []
a,b = map(int, input().split())

for i in range(a+b):
    if i == a:
        pz2.append(int(input()))
    else:
        pz1.append(int(input()))

def bt():
    
