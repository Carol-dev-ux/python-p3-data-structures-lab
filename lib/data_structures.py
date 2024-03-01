import io
import sys

spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food['name'] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food['heat_level'] > 5]

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}".strip())

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food['cuisine'] == cuisine:
            return food
    return None

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}".strip())

def get_average_heat_level(spicy_foods):
    if not spicy_foods:
        return None
    total_heat = sum(food['heat_level'] for food in spicy_foods)
    return total_heat / len(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

def test_print_spiciest_foods(self):
    '''contains function print_spiciest_foods that returns foods with heat_level over 5 formatted with 🌶 emojis.'''
    captured_out = io.StringIO()
    sys.stdout = captured_out
    print_spiciest_foods(get_spiciest_foods(spicy_foods))
    sys.stdout = sys.__stdout__
    assert captured_out.getvalue() == "Green Curry (Thai) | Heat Level: 🌶🌶🌶🌶🌶🌶🌶🌶🌶\n" + \
                                      "Mapo Tofu (Sichuan) | Heat Level: 🌶🌶🌶🌶🌶🌶"

