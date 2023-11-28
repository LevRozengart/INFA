def ne_ori(s: str):
    res = ''
    for char in s:
        res = char + res
    i = 0
    while res[i] == '?' or res[i] == '!':
        i += 1
    if i > 1:
        s = s[:len(s) + 1 - i]
    print(s)
    return s
