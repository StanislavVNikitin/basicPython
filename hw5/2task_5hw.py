def file_insert_string(file_name):
    out_f = open(file_name, "w")
    user_string = "start"
    next_str = ""
    while user_string != "":
        user_string = input(f"Введите {next_str}строку: ")
        out_f.writelines(user_string + '\n')
        next_str = "следующую "

    out_f.close()


def file_read(file_name):
    my_file = open(file_name, "r")
    len_line_file = 0
    for line in my_file:
        len_line_file += 1
        if not line == "\n":
            print(f"Строка № {len_line_file}: {line}", sep="")
            len_list = len(line.split())
            print(f'Слов в строке {len_line_file}: {len_list}', sep="")


file_insert_string("2task5hw.txt")
file_read("2task5hw.txt")
