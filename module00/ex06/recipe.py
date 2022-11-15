"""Cookbook"""

# GLOBAL DATA
sandwitch = {
    "ingredients": [
        "ham",
        "bread",
        "cheese",
        "tomatoes"
    ],
    "meal": "lunch",
    "prep_time": 10
}

cake = {
    "ingredients": [
        "flour",
        "sugar",
        "eggs"
    ],
    "meal": "dessert",
    "prep_time": 60
}

salad = {
    "ingredients": [
        "avocado",
        "arugula",
        "tomatoes",
        "spinach"
    ],
    "meal": "lunch",
    "prep_time": 15
}

cookbook = {
    "sandwitch": sandwitch,
    "cake": cake,
    "salad": salad
}


# FUNCTIONS
def print_all_recipe_names():
    """Print all receipe names"""
    print("\033[1;35m-- Cookbook recipes --\033[0m")
    for recipe_name in list(cookbook):
        print(recipe_name)


def print_recipe_details(recipe_name):
    """Print recipe details"""
    if recipe_name in cookbook:
        for key, value in cookbook[recipe_name].items():
            print(f'\n\033[1;32m{key}:\033[0m')
            if isinstance(value, list):
                for item in value:
                    print(f' - {item}')
            else:
                print(f' - {value}')
    else:
        print("\033[1;31m>> Error : unknown recipe\033[0m")


def delete_recipe(recipe_name):
    """Delete recipe"""
    if recipe_name in cookbook:
        del cookbook[recipe_name]
    else:
        print("\033[1;31m>> Error : unknown recipe\033[0m")


def prep_time_check(prep_time):
    """Checks if the preparation time is in the proper format"""
    if (prep_time.isdigit() is True
            or ((prep_time[0] == '+') and prep_time[1:].isdigit() is True)):
        return True
    return False


def add_recipe_from_input():
    """Add recipe from input"""
    name = input("\033[1;35m>>> Enter a name:\n\033[0m")
    ingredients = []
    ingredient_item = input("\033[1;35m>>> Enter ingredients:\n\033[0m")
    while ingredient_item != "":
        ingredients.append(ingredient_item)
        ingredient_item = input()
    meal = input("\033[1;35m>>> Enter a meal type:\n\033[0m")
    prep_time = input("\033[1;35m>>> Enter a preparation time:\n\033[0m")
    while prep_time_check(prep_time) is False:
        prep_time = input(
            "\033[1;35m>>> Enter a proper preparation time:\n\033[0m")
    cookbook[name] = {
        "ingredients": ingredients,
        "meal": meal,
        "prep_time": prep_time
    }
    print("\033[1;32m~~ The recipe has been added ~~\033[0m")


def print_menu():
    """Print menu"""
    print("\033[1;32m********************************\033[0m")
    print("\033[1;35mWelcome to the Python Cookbook !")
    print("\033[1;32m********************************\033[0m")
    print("List of available options:")
    print("\t1: Add a recipe")
    print("\t2: Delete a recipe")
    print("\t3: Print recipe")
    print("\t4: Print the cookbook")
    print("\t5: Quit\n")


if __name__ == "__main__":
    choice = '0'
    while choice != '5':
        try:
            print_menu()
            choice = input("\033[1;35mPlease select an option:\n\033[0m>> ")
            while choice not in ['1', '2', '3', '4', '5']:
                choice = input(
                    "\033[1;35mPlease select an option (1 to 5):\n\033[0m>> ")
            if choice == '1':
                add_recipe_from_input()
            elif choice == '2':
                recipe_name = input(
                    "\033[1;35mPlease enter the recipe name to delete:\n"
                    "\033[0m>> ")
                delete_recipe(recipe_name)
            elif choice == '3':
                recipe_name = input(
                    "\033[1;35mPlease enter a recipe name to get its details:"
                    "\n\033[0m>> ")
                print_recipe_details(recipe_name)
            elif choice == '4':
                print_all_recipe_names()
            elif choice == '5':
                print("\033[1;32mBye 👋\033[0m")
            if choice != '5':
                input("\n(Press <enter> to display menu)\n")
        except EOFError:
            print('\n')
            continue
