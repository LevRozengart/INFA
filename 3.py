
def black(a):
    f = 0
    s = sum(a)
    print(s)
    if s > 21:
        print(True)
        return True
    else:
        print(False)
        return False
black([2,3,4,5,6,10,10])
