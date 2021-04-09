def fun_div(var_a, var_b):
    '''
    Функия возвращает деление двух переменных
    :param var_a:
    :param var_b:
    :return: возвращает деление двух переменных var_a и var_b
    '''
    try:
        var_div = var_a / var_b
    except ZeroDivisionError:
        print('Упс, похоже мы делим на ноль!')
        return 'Бесконечность'
    else:
        return var_div


try:
    var_print = (
        f"Результат Деления: {fun_div(int(input('Введите делимое число: ')), int(input('Введите делитель: ')))}")
except ValueError:
    print('Упс, похоже вы ввели не число!')
else:
    print(var_print)
