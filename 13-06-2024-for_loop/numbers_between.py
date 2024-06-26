# Вывести все кратные 3-м числа между
# двумя введенными

print("Введите число а:")
a = int(input()) # 5
print("Введите число b:")
b = int(input()) # 10
print()
delta = b - a + 1# 6

# [5,6,7,8,9,10]

for i in range(delta): # [0,1,2,3,4,5]
    num = a + i
    if num % 3 == 0:
        print(num)
    