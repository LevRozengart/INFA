dictt = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
fk = list(dictt.keys())[0]
lk = list(dictt.keys())[-1]
fv = dictt[fk]
lv = dictt[lk]
dictt[fk] = lv
dictt[lk] = fv
del dictt[list(dictt.keys())[1]]
dictt["new_key"] = "new_value"
print(dictt)
