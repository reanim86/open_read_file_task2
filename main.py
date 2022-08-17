with open('recipes.txt', encoding='utf-8') as file:

    def add_ingridients():
        numbers_ingridients = int(file.readline().strip())
        ingridients = []
        while numbers_ingridients != 0:
            ingr = file.readline().strip().split(' | ')
            ingridients.append({'ingredient_name': ingr[0], 'quantity': int(ingr[1]), 'measure': ingr[2]})
            numbers_ingridients -= 1
        return ingridients

    def add_cook_book():
        c_book = {}
        while True:
            dish = file.readline().strip()
            c_book[dish] = add_ingridients()
            empty_str = file.readline()
            if not empty_str:
                break
        return c_book

    def get_shop_list_by_dishes(dishes, person_count):
        shop_list = {}
        for dish in dishes:
            for dish_menu, ingridients in cook_book.items():
                if dish_menu == dish:
                    for ingridient in ingridients:
                        quantity_unit = {
                            'measure': ingridient['measure'],
                            'quantity': (ingridient['quantity'] * person_count)
                        }
                        if ingridient['ingredient_name'] in shop_list.keys():
                            quantity_unit['quantity'] += (ingridient['quantity'] * person_count)
                            shop_list[ingridient['ingredient_name']] = quantity_unit
                        else:
                            shop_list[ingridient['ingredient_name']] = quantity_unit
        return shop_list

    cook_book = add_cook_book()
    answer = get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2)

    print(answer)
















