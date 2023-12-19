def changer(array):
    x = array[0]
    y = array[len(array) - 1]
    array[0] = y
    array[len(array) - 1] = x
    return array
print(changer([1, 2, 3, 4]))