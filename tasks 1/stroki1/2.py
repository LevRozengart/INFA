def first_last(letter, st):
    i = 0
    frst = 0
    last = 0
    array = []
    for char in st:
        if char == letter:
            frst = i
            break
        i += 1
    i = 0
    for char in st:
        if char == letter:
            last = i
        i += 1
    array.append(frst)
    array.append(last)
    print(tuple(array))
    return tuple(array)

first_last('1', '12321321312312321')