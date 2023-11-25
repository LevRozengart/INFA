def is_grow(array):
    flag = True
    lastchar = -10000000000000
    for char in array:
        if char > lastchar:
            lastchar = char
            continue
        else:
            flag = False
            break
    if flag == True:
        print('Возрастает')
    else:
        print('Не возрастает')
    
a = [1, 2, 4, 5]
is_grow(a)