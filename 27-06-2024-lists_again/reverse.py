lst = [1,2,10,2,3,4]
# --> [4,3,2,10,2,1]

reversed_lst = []

i = len(lst)-1
while i >= 0:
    reversed_lst.append(lst[i])
    i = i-1

print(reversed_lst)