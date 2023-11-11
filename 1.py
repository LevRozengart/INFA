a = [1, 2, 6, 6]
b = [3, 5, 7, 4, 7]
c = []
def third_massiv(a, b):
    c = []
    for i in range(len(a)):
        c.append([a[i], b[i]])
    return c
    
print(third_massiv(a, b))