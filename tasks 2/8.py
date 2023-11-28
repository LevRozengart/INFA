def reverse(a):
    res = ''
    for char in a:
        if char.istitle() == True:
            res = char.lower() + res
        else:
            res = char.upper() + res
    print(res)
    return res
reverse('FGeesd')