def my_func(var_a, var_b):
    if var_b < 0:
        return (f"Возведение в степень: {1 / (var_a ** abs(var_b))}")
    else:
        print('Передано не отрицательное число степени!')


print(my_func(float(input('Введите число для возведение в степень: ')), int(input('Введите отрицательную степень: '))))
