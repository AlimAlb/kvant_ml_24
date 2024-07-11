# [10, 2, 4, 3, 5, 8, 1]
# [1, 2, 4, 3, 5, 8, 10]
# [1, 2, 4, 3, 5, 8, 10]
# [1, 2, 3, 4, 5, 8, 10]
# [1, 2, 3, 4, 5, 8, 10]

lst = [10, 2, 4, 3, 5, 8, 1]

i = 0
while i < len(lst) - 1:
    j = i
    m = i
    while j < len(lst):
        if lst[j] < lst[m]:
            m = j
        j = j + 1
    
    c = lst[i]
    lst[i] = lst[m]
    lst[m] = c
    
    i = i + 1

print(lst)