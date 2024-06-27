# Дан список - нужно найти в нем минимальных положительный. Список нужно считать с консоли

lst = [-5, 10, 23, 1, 25, 100, 20, -10]

i = 0
while lst[i] < 0:
    i = i + 1
minn = lst[i]

n = len(lst)
for i in range(n):
    if lst[i] < minn and lst[i] > 0:
        minn = lst[i]

print(minn)

