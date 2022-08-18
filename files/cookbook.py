from pprint import pprint

def read_recipes():
    with open('recipes.txt','r', encoding='UTF8') as f:
        cook_book = {}
        for n in f:
            list_ingr = []
            name = n.strip('\n')
            if name != '':
                count = f.readline()
                for i in range(int(count)):
                    ingredient_str = f.readline().strip('\n').split('|')
                    ingredient = {'ingredient_name': ingredient_str[0], 'quantity' : int(ingredient_str[1]), 'measure' : ingredient_str[2] }
                    list_ingr.append(ingredient)
                cook_book[name] = list_ingr
        return(cook_book)

def get_shop_list_by_dishes(list_cook,person):
    cook_book = read_recipes()
    cook_dict = {}
    for cook in list_cook:
        for ingredient in cook_book[cook]:
            cook_dict[ingredient['ingredient_name']] = {'measure': ingredient['measure'],
                                                        'quantity': 0}
    for cook2 in list_cook:
        for ingredient in cook_book[cook2]:
            quantity = cook_dict[ingredient['ingredient_name']]['quantity'] + ingredient['quantity'] * person
            cook_dict[ingredient['ingredient_name']] = {'measure': ingredient['measure'],
                                                        'quantity': quantity  }
    return(cook_dict)


pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Фахитос'], 1))