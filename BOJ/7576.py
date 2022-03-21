import sys
from collections import deque
sys = sys.stdin.readline

m,n = map(int, input().split())
tomato = [[int(x) for x in input().split()] for y in range(n)]


def check