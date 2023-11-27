def find_opps(array, opps):
    i = 0
    while i < len(array):
        a = array[i] in opps
        if a == True:
            array = array[:i] + array[i + 1:]
        else:
            i += 1
    print(array)
    return array

find_opps(['David', 'Denis', 'Bogdan'], ['H', 'Denis'])