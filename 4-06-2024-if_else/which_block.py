# В первом подъезде квартиры с 1 по 20.
# Во втором с 21 по 48. В третьем с 49 по 90. 
# Пользователь вводит номер квартиры.
# Программа должна указать в каком подъезде находится данная квартира. 


# Пункт 1: Находится ли квартира в первом подъезде или нет? 

number_s = input()
number = int(number_s)

if number >= 1 and number <= 20:
    print("Квартира находится в первом подъезде")
else: 
    if number >= 21 and number <= 48:
        print("Квартира находится во втором подъезде")
    else: 
        if number >= 49 and number <= 90:
            print("Квартира находится в третьем подъезде")
        else: 
            print("Нет такого подъезда")
