def hn(length):
    i = 0
    if length % 2 != 0:
        return 0
    for num in range(10 ** (length // 2 - 1), 10 ** (length // 2)):
        left = sum(int(digit) for digit in str(num))
        right = sum(int(digit) for digit in str(num * 2))
        if left == right:
            i += 1
    return i
print(hn(5326532))
