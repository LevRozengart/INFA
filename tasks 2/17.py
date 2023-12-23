def find_s(a, b):
    y = a['yb'] - a['ya']
    x = b['xb'] - b['xa']
    S = pow((pow(y, 2)) + pow(x, 2), 0.5)
    print(S)
    return S
find_s({'yb': 5, 'ya': 2}, {'xb': 7, 'xa': 2})