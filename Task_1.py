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
    pprint(cook_book, sort_dicts=False)