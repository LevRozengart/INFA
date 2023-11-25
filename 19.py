arr = [13, 4, 543, 53]
arrdop = []
def ha(arr):
    lastchar = 0
    for char in arr:
        arrdop.append(lastchar + char)
        lastchar = char
    print(arrdop)
    return arrdop
ha(arr)
        