# Дан список - нужно найти в нем минимум. Список нужно считать с консоли

lst = [1,-5, 10, 23, 25, 100, 20, -10]

minn = lst[0]
n = len(lst)
for i in range(n):
    if lst[i] < minn:
        minn = lst[i]

print(minn)

