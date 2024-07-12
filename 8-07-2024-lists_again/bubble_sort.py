# сортировка списка "пузырьком"

# step1
# [10,4,2,1,5,8,3,7] --> [4,10,2,1,5,8,3,7] --> [4,2,10,1,5,8,3,7] --> [4,2,10,1,5,8,3,7] 
# --> [4,2,1,10,5,8,3,7] --> [4,2,1,5,10,8,3,7] --> [4,2,1,5,8,10,3,7] --> [4,2,1,5,8,3,10,7]
# --> [4,2,1,5,8,3,7,10]  

# step2 
# --> [4,2,1,5,8,3,7,10] --> [2,4,1,5,8,3,7,10]   --> [2,1,4,5,8,3,7,10] --> [2,1,4,5,3,8,7,10]
# --> [2,1,4,5,3,7,8,10] 

# step3
# [2,1,4,5,3,7,8,10] --> [1,2,4,5,3,7,8,10] --> [1,2,4,3,5,7,8,10] 

# step4
#[1,2,4,3,5,7,8,10] --> [1,2,3,4,5,7,8,10]

# step5
# [1,2,3,4,5,7,8,10]


lst = [10,4,2,1,5,8,3,7]
flag = True
while flag:
    print(lst)
    flag = False
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            c = lst[i]
            lst[i] = lst[i+1]
            lst[i+1] = c
            flag = True

print()
print(lst)
        