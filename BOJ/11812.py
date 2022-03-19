n,k,q = map(int, input().split())

def kTree():
    tree = [[] for _ in range(n+1)]
    target = 2

    for i in range(1, n+1):
        for j in range(target, target+k):
            tree[i].append(j)
        target += k
    return tree

t = kTree()
print(t)