def file_read(file_name):
    sumcach = 0
    person = 0
    with open(file_name, 'r', encoding='utf8') as my_file:
        for line in my_file:
            tmp_list = (line).split()
            if float(tmp_list[1]) < 20000:
                print(f"Сотрудник {tmp_list[0]} получает меньше 20т {tmp_list[1]}")
            sumcach += float(tmp_list[1])
            person += 1
    print(f'Средняя величина дохода сотрудников: {sumcach / person}')


file_read("text_3.txt")
