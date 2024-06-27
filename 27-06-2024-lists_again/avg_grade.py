# Посчитать итоговую за четверть для отдельно взятого ученика
# Считать оценки с консоли

grades = []
print('Введите оценки ученика: ')
grade = input()
while grade != 'exit':
    grade = int(grade)
    if grade >= 1 and grade <= 5:
        grades.append(grade)
    else:
        print("Введите число от 1 до 5")
        print()
    grade = input()

# сумма оценок / количество

n = len(grades)
s = 0
for i in range(n):
    s = s + grades[i]

avg = int(round(s/n, 0))
print()
print(f"Средняя оценка: {avg}")
