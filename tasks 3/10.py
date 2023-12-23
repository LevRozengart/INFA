def dengi(coins, kolvo):
    flag = True
    sumi_coins = sum(coins)
    if sumi_coins % kolvo == 0:
        flag = True
    else:
        flag = False
    print(flag)
    return flag
dengi([1, 2, 5, 2], 2)