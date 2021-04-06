result_now = int(input('Введите текущйи результат спортмена в км: '))
result_end = int(input('Введите цель спортсмена в км: '))
count_day = 1
if result_now < result_end:
    while result_now <= result_end:
        result_now *= 1.1
        count_day += 1
    else:
        print(f'Спортсмен на {count_day} день будет пробегать не менее {result_end} км')
else:
    print('Цель меньше или равна текущему результату, спортсменну не нужно время тренеровок для ее достижения.')
