# 1-21 - первый подъезд 
# 22-35 - второй подъезд 
# 36-41 - третий подъезд 

print('Введите номер квартиры:')
number_s = input()
number = int(number_s)

if number >= 1 and number <= 21:
    print("Квартира с первого подъезда")
else:
    if number >= 22 and number <= 35:
        print('Квартира с второго подъезда')
    else:
        if number >= 36 and number <= 41:
            print("Квартира с третьего подъезда")
        else:
            print("Квартира не с этого дома")
