user_num = int(input('Введите целое число: '))
num_max = 0
count = 0
while user_num > 0 :
    num = user_num % 10
    if num_max < num:
        num_max = num
    user_num = user_num // 10
    count += 1

print(f'Наибольшое число {num_max}, всего было чисел {count}')
