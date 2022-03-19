n, k = map(int, input().split())
circle = [i for i in range(1,n+1)]
queue = []
cnt, idx = 1, 0
while cnt <= n:
    j = 1
    while j <= k:
        if circle[idx] != 0:
            j += 1 
        idx += 1
        if idx == len(circle):
                idx = 0
    cnt += 1
    queue.append(circle[idx-1])
    circle[idx-1] = 0
print('<', end='')
for i in range(len(queue)):
    if i == len(queue)-1:
        print(f'{queue[i]}',end='')
    else:
        print(f'{queue[i]},',end=' ')

print('>', end='')
