n = int(input())
k = int(input())
array = []
for i in range(1, n+1):
    for j in range(1, n+1):
        array.append(i*j)

array.sort()
print(array[k])