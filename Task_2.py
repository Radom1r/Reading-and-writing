import os
from pprint import *
full_path = os.path.join(os.getcwd(), 'recipe.txt')
with open(full_path, 'rt', encoding='utf-8') as recipe:
    cook_book = {}
    for line in recipe:
        dish_name = line.strip()
        ing_count = int(recipe.readline().strip())
        ing = []
        for index in range(ing_count):
            ingredient_name, quantity, measure = recipe.readline().strip().split(' | ')
            ing.append({'ingredient_name': ingredient_name,
                              'quantity' : quantity,
                              'measure' : measure})
        recipe.readline()
        cook_book[dish_name] = ing

def get_shop_list_by_dishes(dishes, person_count):
    for value in dishes:
        for index in range(len(cook_book[value])):
            cook_book[value][index]['quantity'] = str(int(cook_book[value][index]['quantity'])*person_count)+" "+cook_book[value][index]['measure'] if value in cook_book.keys() else print('Error')
            print({cook_book[value][index]['ingredient_name']:cook_book[value][index]['quantity']})
get_shop_list_by_dishes(['Фахитос', 'Омлет'], 10)