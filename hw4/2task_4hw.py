from random import randint


def create_my_list():
    my_list = []
    len_list = randint(5, 40)
    i = 0
    while i < len_list:
        i += 1
        my_list.append(randint(1, 999))
    return my_list


my_list = create_my_list()
print(my_list)
len_my_list = len(my_list)
new_list = [my_list[el] for el in range(1, len_my_list) if my_list[el] > my_list[el - 1]]
print(new_list)
