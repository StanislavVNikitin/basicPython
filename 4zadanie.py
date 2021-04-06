user_string = input('Введите строку раздленную пробелами: ')

my_list = user_string.split(' ')

for ind, el in enumerate(my_list):
    print(ind, el[:10])
