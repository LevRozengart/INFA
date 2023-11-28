a = [3, 4, 6]
b = [2, 2, 6]
c = [12, 3, 6]
def oo(a, b, c):
    resa = 1
    resb = 1
    resc = 1
    for char in a:
        resa = char * resa
    for char in b:
        resb = char * resb
    for char in c:
        resc = char * resc
    return resa + resb + resc
print(oo(a, b, c))