def file_insert_string():
    out_f = open("1task5hw.txt", "w")
    user_string = "start"
    next_str = ""
    while user_string != "":
        user_string = input(f"Введите {next_str}строку: ")
        out_f.writelines(user_string + '\n')
        next_str = "следующую "

    out_f.close()


file_insert_string()
