# Считайте вес человека. Если он в пределах от 60 до 100 кг
# То вес здоровый. Иначе - вес не здоровый

print("Введите свой вес:")
weight_s = input()
weight = int(weight_s)


print()
if weight >= 60 and weight <= 100: 
    print("Вес здоровый")
else: 
    print('Вес не здоровый')

