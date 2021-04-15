def my_func(var_a, var_b, var_c):
    var_list = sorted([var_a, var_b, var_c])
    return (f'Сумма наибольших чисел = {var_list[1] + var_list[2]}')


print(my_func(int(input('Введите первое число: ')), int(input('Введите второе число: ')),
              int(input('Введите третье число: '))))
