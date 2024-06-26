# Даны два упорядоченных по возрастанию
# списка чисел. Нужно слить их в один
# также упорядоченный список чисел

lst_1 = [1,4,10,25,28]
lst_2 = [2,5,8,11,24]
lst = []

idx1 = 0
idx2 = 0
while idx1 < 5 or idx2 < 5:
    if idx1 == 5:
        lst.append(lst_2[idx2])
        idx2 = idx2 + 1
    elif idx2 == 5:
        lst.append(lst_1[idx1])
        idx1 = idx1 + 1
    elif lst_1[idx1] <= lst_2[idx2]:
        lst.append(lst_1[idx1])
        idx1 = idx1 + 1
    else:
        lst.append(lst_2[idx2])
        idx2 = idx2 + 1
        
print(lst)

