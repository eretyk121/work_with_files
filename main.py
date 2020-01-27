with open('recipes.txt', encoding='cp1251') as f:
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


def get_shop_list_by_dishes(dishes, person):
    prod_list = {}
    for dish, ingredients in cook_book.items():
        if dishes in dish:
            for q in ingredients:
                ingred = {'measure': q['measure'], 'quantity': int(q['quantity']) * person}
                prod_list[q['ingredient_name']] = ingred
            print(prod_list)

def count(*args):
    p = int(input('Введите количество персон: '))
    for i in args:
        get_shop_list_by_dishes(i, p)
count('Омлет', 'Запеченный картофель')