# Написать программу, которая считывает оценки учеников всего класса с консоли и затем
# считает для всех итоговую оценку: итоговая оценка считается как среднее арифметическое

# Петров - 5, 4, 2, 5, 5 --> (5+4+2+5+5)/5 = 4.2 ~ 4
# Сидоров - 3, 4, 5, 3, 2 --> (3+4+5+3+2)/5 = 3.4 ~ 3

# Хранить данные необходимо в двумерном списке

def read_grade():
    pass
    #TODO: считывание и проверка оценок
    


def read_grades():
    lst = []
    print('Введите имя ученика: ')
    name = input()
    while name != 'stop':
        grades = []
        grades.append(name)
        print("Введите оценки")
        grade =input()
        while grade != 'stop':
            grade = int(grade)
            grades.append(grade)
            grade = input()
        lst.append(grades)

        print('Введите имя ученика: ')
        name = input()
    return lst

def calculate_grades(lst):
    for i in range(len(lst)):
        s = 0
        for j in range(len(lst[i])):
            if j != 0:
                s = s + lst[i][j]
        avg = s/(len(lst[i])-1)
        print(f"{lst[i][0]} - {avg}")


calculate_grades(read_grades())
