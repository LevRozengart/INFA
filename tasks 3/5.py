def sosedi(a):
    i = 0
    res = ''
    flag = True
    while i < len(a):
        if a[i] == '+':
            flag = True
        else:
            flag = False
        i += 2
    print(flag)
    return flag