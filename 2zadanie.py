var_list = []
i = 1
modif_list = []

while (int(input("Меню: Хотите добавить элемент в список(1 - да; 0 - нет):")) or not (len(var_list))):
    var_list.append(input("Введите значение для добавления в список: "))

print(f'Вы ввели список', var_list)

if (len(var_list) >= 2):
    while (i < (len(var_list) // 2 * 2)):
        modif_list.append(var_list[i])
        modif_list.append(var_list[i - 1])
        i += 2
    if (len(var_list) % 2):
        modif_list.append(var_list[-1])
    print(f'Измененный список', modif_list)
else:
    print("размер списка меньше двух элементов:", var_list)
