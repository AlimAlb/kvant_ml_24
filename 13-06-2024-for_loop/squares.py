# Вывести квадраты всех четных чисел 
# от 1 до n, где n вводится с консоли

n = int(input())
print()

for i in range(n):
    if (i+1) % 2 == 0:
        sq = (i+1)**2
        out = str(i+1) + " - " + str(sq)
        print(out)

    


