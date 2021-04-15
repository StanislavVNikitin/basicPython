from itertools import count
from math import factorial


def fg(n):
    var_tmp = 1
    if n == 0:
        yield '!0 = 1'
    else:
        for i in range(1, n + 1):
            var_tmp *= i
            yield f'!{i} = {var_tmp}'


for el in fg(int(input("Укажите число для расчета факториала: "))):
    print(el)
