print('камень - к, ножницы - н, бумага - б')
def knb(a, b):
    ar = ['к', 'н', 'б']
    if a == b:
        print('ничья')
    elif a == ar[0] and b == ar[1]:
        print("игрок 1 победил")
    elif a == ar[0] and b == ar[2]:
        print("игрок 2 победил")
    elif a == ar[1] and b == ar[0]:
        print("игрок 2 победил")
    elif a == ar[1] and b == ar[2]:
        print("игрок 1 победил")
    elif a == ar[2] and b == ar[0]:
        print("игрок 1 победил")
    elif a == ar[2] and b == ar[1]:
        print("игрок 2 победил")
    else:
        print('Получен некорректный символ')
    return
knb('к', "н")