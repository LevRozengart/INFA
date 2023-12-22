def search_substr(subst, st):
    if st in subst:
        print('Есть контакт!')
        return
    else:
        print('Mimo!')
        return

search_substr('123', '12')
