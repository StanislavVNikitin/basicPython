with open('text_6.txt', 'r', encoding='utf8') as file:
    onstring = file.read().split("\n")[:-1]
    print(onstring)

    dict = {}

    for item in onstring:
        key_name, value = item.split(':')
        name_sum = sum(map(int, "".join([i for i in value if i == ' ' or '9' >= i >= '0']).split()))
        dict[key_name] = name_sum

    print(dict)
