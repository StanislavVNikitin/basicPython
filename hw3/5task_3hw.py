def f_input_user():
    return input(
        "Введите строку чисел резделенных пробелым, для получения суммы нажмите Enter, если нужно выйти по завершению наберите - q: ")


def f_print_sum(var_s):
    print(f' Сумма введенных чисел: {var_s}')


var_sum = 0
mark_cicle = True

while mark_cicle:
    sum_tmp = var_sum
    list_input_user = f_input_user().split()
    for item_input in list_input_user:
        if item_input.isdigit():
            var_sum += int(item_input)
        elif item_input == 'q' or item_input == 'Q':
            mark_cicle = False
    if sum_tmp != var_sum:
        f_print_sum(var_sum)
