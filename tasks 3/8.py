def intostr(num_to_str):
    hd = ['сто', 'двести', 'триста', 'четыреста', 'пятьсот', 'шестьсот', 'семьсот', 'восемьсот', 'девятьсот']
    tn = ['десять', "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесять", "девяносто"]
    on = ["один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]

    on_i = num_to_str % 10
    tn_i = (num_to_str // 10) % 10
    hd_i = num_to_str // 100

    length = len(str(num_to_str))
    if length <= 3:
        if length == 1 and on_i != 0:
            res = on[on_i - 1]

        elif length == 2 and (num_to_str == 10 or num_to_str >= 20):
            res = tn[tn_i - 1] + ' '
            if on_i != 0:
                res = res + on[on_i - 1]

        elif length == 3:
            res = hd[hd_i - 1] + ' '
            if tn_i != 0:
                res = res + tn[tn_i - 1] + ' '
            if on_i > 0:
                res = res + on[on_i - 1]

        elif 10 < num_to_str < 20:
            dop = 'надцать'
            dop_array = ['один', "две", "три", "четыр", "пят", "шест", "сем", "восем", "девят"]
            res = dop_array[on_i - 1] + dop

        else:
            res = 'ноль'
        return res
    else:
        print('Введите число, которое не превышает 999')
    return
