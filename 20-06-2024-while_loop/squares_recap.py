# вывести квадраты всех четных чисел от 1 до n
# n - вводится с консоли

n = int(input())
print()

for i in range(n): # [0,1,2,3,...,n-1]
    tmp = i + 1 
    if tmp % 2 == 0:
        result = tmp**2
        out = str(tmp) + " - " + str(result)
        print(out)
    

