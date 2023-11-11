a = 'dsadSsadsad'
def is_even(a:str):
    a =  a.lower()
    lst_char1 = ''
    lst_char2 = ''
    flag = False
    for char in a:
        lst_char2 = lst_char1
        lst_char1 = char
        if lst_char1 == lst_char2:
            flag = True
            break
    return flag
print(is_even(a))