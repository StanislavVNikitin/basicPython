my_list = [7, 5, 3, 3, 2]
while True:
    user_rating = int(input('Введите новый рейтинг: '))
    len_list = len(my_list)
    i = 0
    while (i < len_list):
        if (my_list[i] < user_rating):
            if (i == 0):
                my_list.insert(0, user_rating)
                break
            else:
                my_list.insert(i, user_rating)
                break
        i += 1
    else:
        my_list.append(user_rating)
    print(my_list)
