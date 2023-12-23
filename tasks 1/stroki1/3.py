def top3(st):
    st = st.replace(" ", "")
    array = []
    for char in st:
        flag = False
        for entry in array:
            if entry[0] == char:
                entry[1] += 1
                flag = True
                break
        if not flag:
            array.append([char, 1])
    sorted_chars = sorted(array, key=lambda x: x[1], reverse=True)[:3]
    result_str = ", ".join(f"{char} - {count}" for char, count in sorted_chars)
    return result_str
print(top3('3fdsfsdfdsfdsgsse'))
