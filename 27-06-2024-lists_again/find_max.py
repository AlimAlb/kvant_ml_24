# Дан список - нужно найти в нем максимум. Список нужно считать с консоли

lst = [1,-5, 10, 23, 25, 100, 20, -10]

maxx = lst[0]
n = len(lst)
for i in range(n):
    if lst[i] > maxx:
        maxx = lst[i]

print(maxx)


