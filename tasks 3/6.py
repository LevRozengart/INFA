def converter(time):
    res = ''
    if time[len(time) -2:] == 'AM':
        print(time[:len(time) - 2])
        return time[:len(time) - 2]
    else:
        res = str(int(time[:2]) + 12) + time[2:len(time) - 2]
        print(res)
converter('11:34 AM')
