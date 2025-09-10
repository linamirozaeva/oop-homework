# Task 1
import json
cook_book = {}
with open('recipes.txt', 'rt', encoding='utf-8') as file:
    current_dish = None
    for line in file:
        line = line.strip()
        if line.isdigit():
            continue
        elif '|' not in line:
            current_dish = line
            cook_book[current_dish] = []
        else:
            ingredient_name, quantity, measure = line.split('|')
            ingredient = {
                'ingredient_name': ingredient_name.strip(),
                'quantity': int(quantity),
                'measure': measure.strip()
            }
            cook_book[current_dish].append(ingredient)

print(json.dumps(cook_book, indent=4, ensure_ascii=False))


# Task 2
def get_shop_list_by_dishes(dishes_list, person_count, cook_book):
    shop_list = {}
    for dish in dishes_list:
        if dish not in cook_book:
            print(f"Блюдо '{dish}' отсутствует в кулинарной книге.")
            continue
        ingredients = cook_book[dish]
        for ingredient in ingredients:
            ing_name = ingredient["ingredient_name"]
            if ing_name in shop_list:
                shop_list[ing_name]["quantity"] += ingredient["quantity"] * person_count
            else:
                shop_list[ing_name] = {"measure": ingredient["measure"],
                                       "quantity": ingredient["quantity"] * person_count}
    return shop_list

shop_list = get_shop_list_by_dishes(["Фахитос", "Омлет"], 2, cook_book)
print(json.dumps(shop_list, indent=4, ensure_ascii=False))


# Task 3
import os
def sort_and_write_files_to_result(*filenames):
    files_data = []
    for filename in filenames:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            content = ''.join(lines)
            num_lines = len(lines)
            files_data.append((filename, num_lines, content))
    sorted_files = sorted(files_data, key=lambda x: x[1])
    with open('result.txt', 'w', encoding='utf-8') as output_file:
        for filename, num_lines, content in sorted_files:
            output_file.write(f"{filename}\n")
            output_file.write(f"{num_lines}\n")
            output_file.write(content)
            output_file.write("\n")

sort_and_write_files_to_result('1.txt', '2.txt', '3.txt')