# Вводятся числа a и b (b > a). Необходимо вывести все числа кратные 3
# между a и b
# кратное трем = делиться на три без остатка


a = int(input())
b = int(input())
print()
# a = 5 
# b = 10

# b - a + 1

# 5, 6, 7, 8, 9, 10

n = b - a + 1 # 6
for i in range(n): # [0,1,2,3,4,5]
    tmp = a + i
    if tmp % 3 == 0:
        print(tmp)
    
    
    