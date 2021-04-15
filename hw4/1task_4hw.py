from sys import argv


def payroll():
    try:
        script_name, output_in_hours, rate_per_hour, bonus = argv
    except ValueError:
        print('Нужно запускать программу с параметрами programm.py "выработка_в_часах" "ставка_в_час" "премия"')
    else:
        print(f'{(float(output_in_hours) * float(rate_per_hour) + float(bonus))}')


payroll()
