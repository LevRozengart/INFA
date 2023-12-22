def mediana(array):
    array.sort()
    if len(array) % 2 == 0:
        print(array[int((len(array)) / 2) - 1], array[int(len(array) / 2)])
    else:
        print(array[int((len(array)) / 2) - 1])
    return