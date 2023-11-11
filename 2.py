array = ['гость 1', 'гость 2', 'гость 3']
def greeting(array):
    for i in range(len(array)):
        print(f'Привет, {array[i]}')
greeting(array)