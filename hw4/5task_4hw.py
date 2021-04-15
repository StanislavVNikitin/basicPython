from functools import reduce

my_list = [num for num in range(100, 1001, 2)]
print(f'Начальный список {my_list}\nПроизведение всех элементов {reduce((lambda a, b: a * b), my_list)}')
