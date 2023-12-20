def mul_to_int(a, b):
    if (a * b) / int(a * b) == 1:
        afsa = a * b
        print(int(afsa))
        return int(afsa)
    else:
        print(a * b)
        return a * b
mul_to_int(1, 123)
