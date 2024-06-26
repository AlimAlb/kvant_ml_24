# Проверить число на простоту 

n = int(input())

# 1012310231230

i = 2
flag = False
while i < n: 
    if n % i == 0:
        flag = True
    i = i + 1
    
if flag:
    print("не простое")
else: 
    print("число простое")