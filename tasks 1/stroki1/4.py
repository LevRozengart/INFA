def camel(st):
    res = ''
    upper = True 
    for char in st:
        if char.isalpha():
            if upper:
                res += char.upper()
            else:
                res += char.lower()
            upper = not upper
        else:
            res += char 
    return res
print(camel('fsakfaksfkasjfka, fskaf  fskafisaf  f fjashk'))
