products_list = []
product_triple = {}
product_item = 0

while True:
    menu_num = int(input('Меню: 0 - выход, 1 - посмотреть сколько товаров есть, 2 - добавить товар, 3 - удалить товар, 4 - показать аналитику: '))
    if(menu_num == 0):
        break
    elif(menu_num == 1):
        print(len(products_list))
        print(products_list)
    elif(menu_num == 2):
        product_name = input('Введите название продукта: ')
        product_cost = input('Введите цену продукта: ')
        product_count = input('Введите количество продукта: ')
        product_em = input('Введите единицы продукта: ')
        product_triple = { 'название': product_name ,'цена': product_cost, 'количество' : product_count, 'ед': product_em }
        product_item += 1
        product_new_list = (product_item, product_triple)
        products_list.append(product_new_list)
    elif(menu_num == 3):
        print('удаление')
    elif(menu_num == 4):
        print('Аналитика')
        if(len(products_list) > 0):
            i=0
            while(len(products_list)>i):
                product_list_dict = products_list[i]
                i += 1
                for key in product_list_dict[1]:
                    analitic_db = {key:list.append(product_list_dict.get(key))}
                print(analitic_db)





