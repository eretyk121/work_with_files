with open('C:/igor/recipes.txt') as f:
    cook_book = {}
    while True:
        cook = f.readline().strip()
        cook_book[cook] = []
        count = f.readline().strip()
        i = 0
        while i < int(count):
            a = f.readline().strip().split("|")
            cook_book[cook].append({'ingredient_name': a[0], 'quantity': a[1],'measure': a[2]})
            i += 1
        if f.readline() == '\n':
            continue
        else:
            break

def get_shop_list_by_dishes(person, dishes):
    prod_list = {}
    if type(dishes) == list:
        for one_dish in dishes:
            for dish, ingredients in cook_book.items():
                if one_dish in dish:

                    for q in ingredients:
                        old_quan = 0
                        if q['ingredient_name'] in prod_list.keys():
                            old_quan = prod_list[q['ingredient_name']]['quantity']

                        ingred = {'measure': q['measure'], 'quantity': int(q['quantity']) * person + old_quan}
                        prod_list[q['ingredient_name']] = ingred
        print(prod_list)

get_shop_list_by_dishes(5, ['Омлет', 'Омлет'])
# def get_shop_list_by_dishes(dishes, person):
#     prod_list = {}
#     for dish, ingredients in cook_book.items():
#         if dishes in dish:
#             for q in ingredients:
#                 print(q['ingredient_name'])
#                 print(prod_list.keys())
#                 if q['ingredient_name'] in prod_list.keys():
#                     old_quan = prod_list['ingredient_name']['quantity']
#                     print(old_quan)
#                 ingred = {'measure': q['measure'], 'quantity': int(q['quantity']) * person}
#                 prod_list[q['ingredient_name']] = ingred
#             print(prod_list)
# # get_shop_list_by_dishes('Омлет', 3)
# def count(*args):
#     p = int(input('Введите количество персон: '))
#     for i in args:
#         get_shop_list_by_dishes(i, p)
# count('Омлет', 'Омлет')

# def get_shop_list_by_dishes(dishes, person):
#     prod_list = {}
#     for dish, ingredients in cook_book.items():
#         if dishes in dish:
#             for q in ingredients:
#                 ingred = {'measure': q['measure'], 'quantity': int(q['quantity']) * person}
#                 prod_list[q['ingredient_name']] = ingred
#             print(prod_list)
# get_shop_list_by_dishes(['Омлет', 'Запеченный картофель'], 5)




