import re
def password_1(password):
    i = 0
    if len(password) >= 8:
        i += 1
    if re.search(r'[a-z]', password):
        i += 1
    if re.search(r'[A-Z]', password):
        i += 1
    if re.search(r'\d', password):
        i += 1
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        i += 1
    print(i)
    return i
check_password_complexity('nfkjsdtghjwdhege%W^&W$yduiwdhiw')
