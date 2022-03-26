num = str(input())
result = ''
table = ['000', '001', '010', '011', '100', '101', '110', '111']

for n in num:
    s = int(n)
    result += str(table[s])

if result[0] == '0':
    if int(num) == 0:
        print(0)
    else:
        idx = 0
        while result[idx] == '0':
            idx += 1
        result = result[idx:]
        print(result)
        
else:
    print(result)
            