def umn(string):
    res = ''
    array = []
    array2 = []
    i = 0
    for char in string:
        if  char == ',':
            array.append(res)
            res = ''
            i += 1
            continue
        elif char == ' ':
            i += 1
            continue
        else:
            res = res + char
            if i == len(string) - 1:
                array.append(res)
            i += 1
    j = 0
    while j < len(array):
        array2.append(int(array[j]))
        j += 1
    res = 1
    i = 0
    while i < len(array2):
        res = res * array2[i]
        i += 1
    return res
print(umn('1123, 124, 325, 543'))
