alpha = input()
found = ['a', 'e', 'i', 'o', 'u']
print(sum(map(lambda x : alpha.count(x), found)))