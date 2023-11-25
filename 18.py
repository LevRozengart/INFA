a = 'привет как'
def yazik(a):
    i = 0
    for char in a:
        if char == 'а':
            a = a[:i] + '4' + a[i + 1:]
        elif char == 'е':
            a = a[:i] + '3' + a[i + 1:]
        i += 1
    print(a)
    return a
yazik(a)