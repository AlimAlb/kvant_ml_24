# 5! = 1*2*3*4*5 = 120
# n! = 1*2*3*...*n

n = int(input())
print()

factorial = 1

for i in range(n):# 
    tmp = i+1 # [1,2,3,4,5,6,7,8,9,10]
    factorial = factorial * tmp
    
print(factorial)