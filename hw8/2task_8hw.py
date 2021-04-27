class MyDivZeroError(Exception):
    def __init__(self, text):
        self.text = text


num1 = input("Введите первое число: ")
num2 = input("Введите второе число: ")

try:
    num1 = float(num1)
    num2 = float(num2)
    if num2 == 0:
        raise MyDivZeroError("Ошибка деления на ноль!!!")
except (ValueError, MyDivZeroError) as err:
    print(err)
else:
    print(f'Результат деления двух чисел = {num1 / num2}')
