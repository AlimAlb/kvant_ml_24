# Решим следующую задачу: пусть пользователь вводит свой вес
# а мы по весу должны опеределить здоровый он (вес) или нет. 
# Будем считать здоровым вес в промежутке от 60 до 100 килограмм

print("Введите вес:")
weight_s = input()
weight = int(weight_s)

res = weight >= 60 and weight <= 100

print()
print('Вес здоровый: ')
print(res) 