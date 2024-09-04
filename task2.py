cook_book = {
  'Омлет': [
    {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
  'Утка по-пекински': [
    {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
    {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
    {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
    {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'},
    {'ingredient_name': 'Помидор', 'quantity': 6, 'measure': 'шт'}
    ],
  'Запеченный картофель': [
    {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
    {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
    {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ]
  }

############################## main function
def get_shop_list_by_dishes(dishes, person_count):
    products_dict = {}
    for name in dishes:

        str_curr = cook_book[name]

        for l in range(len(str_curr)):
            curr_ingredient = str_curr[l]['ingredient_name']
            curr_quantity = str_curr[l]['quantity']*person_count
            curr_measure = str_curr[l]['measure']

            if (curr_ingredient in products_dict) :
                products_dict[curr_ingredient]={'measure': curr_measure,
                                                'quantity': products_dict[curr_ingredient]['quantity'] + curr_quantity}
            else:
                products_dict[curr_ingredient] = {'measure': curr_measure, 'quantity': curr_quantity}

    return (products_dict)


print( get_shop_list_by_dishes(['Омлет','Утка по-пекински'],3) )
print( get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2) )
