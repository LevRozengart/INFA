def reverse(array):
    res = ''
    for char in array:
        res = str(char) + res
    return res
print(reverse([1, 2, 3, 5]))
