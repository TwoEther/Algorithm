x = int(input())
result = 1
while x != 1:
    if x % 2 == 1:
        result += 1
    x //= 2
print(result)