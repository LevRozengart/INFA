def cleaned_str(st):
    res = ''
    for char in st:
        if char != '@':
            res = res + char
    print(res)
    return res
cleaned_str('asd@fdas@fdsa')
