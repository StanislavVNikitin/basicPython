translate_dist = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}


def file_read(file_name):
    my_dict = {}
    with open(file_name, 'r', encoding='utf8') as my_file:
        for line in my_file:
            tmp_list = (line).split()
            if not (tmp_list[0] == ""):
                my_dict[translate_dist.get(tmp_list[0])] = tmp_list[2]
    return my_dict


def file_write(file_name, get_dict):
    with open(file_name, 'w', encoding='utf8') as my_file:
        for key, value in get_dict.items():
            my_file.writelines(f"{key} - {value}\n")


get_dict = file_read("text_4.txt")
file_write("new_text_4.txt", get_dict)
