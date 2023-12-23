def shortener(st):
    res = ''
    i = 0

    for char in st:
        if char == '(':
            i += 1
        elif char == ')' and i > 0:
            i -= 1
        elif i == 0:
            res += char
    print(res)
    return res
