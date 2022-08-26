from pprint import pprint
cook_book = {}
def cook_book_init():
    with open('recipes.txt', 'r', encoding='utf-8') as recipes:
        for line in recipes:
            dish = line.strip()
            list_products = []
            quantity_product = recipes.readline().strip()
            for position in range(int(quantity_product)):
                product = recipes.readline().strip().split(' | ')
                products = {'ingredient_name': product[0], 'quantity': int(product[1]), 'measure': product[2]}
                list_products.append(products)
            cook_book.update({dish: list_products})
            recipes.readline()
        return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for products in cook_book_init()[dish]:
            product = products.pop('ingredient_name')
            products['quantity'] = int(products['quantity']) * int(person_count)
            if product in shop_list:
                products['quantity'] += shop_list[product]['quantity']
            shop_list.update({product: products})
    return shop_list



pprint(cook_book_init())
pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
