def int_func(slovo):
    list_slovo = list(slovo)
    temp_slovo = ''
    latin_simvol = False
    for simvol_slovo in list_slovo:
        if 97 <= int(ord(simvol_slovo)) <= 122:
            latin_simvol = True
            temp_slovo += simvol_slovo
        else:
            latin_simvol = False
            break
    if latin_simvol:
        return temp_slovo[0].upper() + temp_slovo[1:]
    else:
        return False


var_list = input(
    'Введите строку раздленную пробелами, первые буквы слова состоящие из латинских букв выведутся в верхнем регистре: ').split()
new_stroka = ''

for item_list in var_list:
    temp_stroka = int_func(item_list)
    if temp_stroka:
        if new_stroka != '':
            new_stroka += " " + temp_stroka
        else:
            new_stroka = temp_stroka

print(f'Вывод строки латинских слов с большой буквы: {new_stroka}')
