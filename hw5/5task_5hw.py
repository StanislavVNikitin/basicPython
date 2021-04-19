import random


def new_write_file(file_name):
    with open(file_name, 'w', encoding='utf8') as my_file:
        my_list = {str(random.randint(1, 50)) for _ in range(1, random.randint(10, 25))}
        my_file.writelines(' '.join(my_list))


def read_file(file_name):
    sum_dig = 0
    with open(file_name, 'r', encoding='utf8') as my_file:
        for el in my_file.readline().split():
            sum_dig += int(el)
    return sum_dig


file_name = "5task_5hw.txt"

new_write_file(file_name)
print(f'Сумма чисел в файле {file_name} равна {read_file(file_name)}')
