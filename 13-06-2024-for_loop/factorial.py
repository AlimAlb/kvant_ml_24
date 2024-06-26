# Факториал
# 5! = 1*2*3*4*5

print("Введите число:")
n = int(input())
# 5! = 1*2*3*4*5 = 120
factorial = 1

for i in range(n): # [0,1,2,3,4]
    factorial = factorial * (i+1) #[1,2,3,4,5]

print(factorial)



