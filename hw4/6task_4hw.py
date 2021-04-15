from itertools import count, cycle
from random import randint

for i in count(int(input('Введите начальное число '))):
    print(i, end='')
    quit = input()
    if quit == 'q':
        break

my_list = input('Введите список чисел разделяя пробелом ').split()
iter = cycle(my_list)

for _ in range(randint(5, 10)):
    print(next(iter), end='')
