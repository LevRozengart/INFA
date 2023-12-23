def all_eq(array):
    maxi = 0
    res = []
    for char in array:
        if len(char) >= maxi:
            maxi = len(char)
    for char in array:
        if len(char) < maxi:
            res.append(char + ('_' * (maxi - len(char))))
        else:
            res.append(char)
    print(res)
    return res
all_eq(['123', '124142'])
