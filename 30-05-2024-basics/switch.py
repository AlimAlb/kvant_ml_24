s1 = 'Twenty'
s2 = 'One'


print("s1 -> " + s1)
print("s2 -> " + s2)
print()

s = s1 # запомним в переменную значение s1
s1 = s2 # перезапишем значение s1 значением из s2
s2 = s # теперь в s2 положим ранее запомненное значение из s1

print("s1 -> " + s1)
print("s2 -> " + s2)
