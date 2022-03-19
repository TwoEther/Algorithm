n = int(input())
my_list = [int(x) for x in input().split()]
p_list = list(set(my_list))
p_list.sort()

a_dict = {i:v for v,i in enumerate(p_list)}

for i in my_list:
    print(a_dict[i], end=' ')
