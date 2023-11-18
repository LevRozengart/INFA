a = 'ds  ad   adsa     d'
def del_space(a):
    a =  a.lower()
    lst_char1 = ''
    lst_char2 = ''
    i = 0
    for char in a:
        lst_char2 = lst_char1
        lst_char1 = char
        if lst_char1 == lst_char2 and lst_char1 == ' ':
            a = a[:i] + a[i+1:]
        else:
            i += 1
    print(a)
    return a
del_space(a)
