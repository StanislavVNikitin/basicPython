class MyTestDigit(Exception):
    def __init__(self, text):
        self.text = text


list_num = []
booltest = True
while booltest:
    tmp_list = (input("введите  список чисел через пробел, дле прекращения работы ввведите stop: ")).split()
    for en_num in tmp_list:
        if en_num == "stop":
            print('Введена команда stop, программа завершает свою работу!')
            booltest = False
        else:
            try:
                if not (str.isdigit(en_num)):
                    raise MyTestDigit(f'Введен элемент {en_num} который не число!!!')
            except (MyTestDigit) as err:
                print(err)
            else:
                print(f'в список добавляем число: {en_num}')
                list_num.append(en_num)
print()
print(f'*********Вывод полученого списка! **********')
print(list_num)
