# слить два упорядоченных списка в один также упорядоченный

# [1,2,4,8,10,12]

# [2,3,4,9,11,13,15]

# [1,2,2,3,4,4,8,9,10,11,12,13,15]


lst1 = [1,2,4,8,10,12]

lst2 = [2,3,4,9,11,13,15]

idx1 = 0
idx2 = 0
lst = []

while idx1 < len(lst1) or idx2 < len(lst2):
    if idx1 == len(lst1):
        lst.append(lst2[idx2])
        idx2 = idx2 + 1
    elif  idx2 == len(lst2):
        lst.append(lst1[idx1])
        idx1 = idx1 + 1
    elif lst1[idx1] > lst2[idx2]:
        lst.append(lst2[idx2])
        idx2 = idx2 + 1
    else:
        lst.append(lst1[idx1])
        idx1 = idx1 + 1
    
print(lst)