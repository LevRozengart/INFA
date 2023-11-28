def summa_v_stroke(s):
    c = '1234567890'
    res = ''
    array = []
    i = 0
    for char in s:
        if (char in c) == True:
            res = res + char
            i += 1
            if i == (len(s)):
                array.append(res)
        else:
            array.append(res)
            res = ''
            i += 1

    i = 0
    for char in array:
        if char == '':
            array = array[:i] + array[i + 1:]
        else:
            i += 1

    i = 0
    for char in array:
        array[i] = int(char)
        i += 1

    res = 0
    for char in array:
        res += char
    print(res)

    return res
summa_v_stroke('123jfds54ngfdbnj53')
