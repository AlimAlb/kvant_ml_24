#[10,4,2,1,5,8,3,7]

#[4,2,1,5,8,3,7,10]

#[4,2,1,5,3,7,8,10]

#[4,2,1,5,3,7,8,10]

#[4,2,1,3,5,7,8,10]

#[2,1,3,4,5,7,8,10]

#[2,1,3,4,5,7,8,10]

#[1,2,3,4,5,7,8,10]


lst = [10,4,2,1,5,8,3,7]

for i in range(len(lst)):
    m = lst[0]
    for i in range(len(lst)-i):
        if lst[i] > m:
            m = lst[i]
    lst[len(lst)-i] = m