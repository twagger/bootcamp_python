cookbook = {
	"sandwitch" : {
		"ingredients" : ["ham", "bread", "cheese", "tomatoes"],
		"meal" : "lunch",
		"prep_time" : 10,
	},
	"cake" : {
		"ingredients" : ["flour", "sugar", "eggs"],
		"meal" : "dessert",
		"prep_time" : 60,
	},
	"salad" : {
		"ingredients" : ["avocado", "arugula", "tomatoes", "spinach"],
		"meal" : "lunch",
		"prep_time" : 15,
	},
}

def print_recipe(name: str):
	if cookbook.get(name) == None:
		print("\nRecipe for " + name + " is not in the cookbook\n")
	else:
		print("\nRecipe for " + name + ":")
		print("Ingredients list: " + str(cookbook[name]["ingredients"]))
		print("To be eaten for " + cookbook[name]["meal"])
		print("Takes " + str(cookbook[name]["prep_time"]), end='')
		print(" minutes of cooking")

def del_recipe(name: str):
	if cookbook.get(name) == None:
		print("\nRecipe for " + name + " is not in the cookbook\n")
	else:
		cookbook.pop(name, None)
		print("\nRecipe deleted\n")

def add_recipe(name: str, ingredients: list, meal: str, prep_time: int):
	if cookbook.get(name) != None:
		print("\nRecipe for " + name + " already exists in the cookbook\n")
	else:
		cookbook[name] = {}
		cookbook[name]['ingredients'] = ingredients
		cookbook[name]['meal'] = meal
		cookbook[name]['prep_time'] = prep_time
		print('')

def print_all_recipes():
	first = True
	for recipe in cookbook:
		print_recipe(recipe)
	print('')

def display_menu():
	print("Please select an option by typing the corresponding number:")
	print("1: Add a recipe")
	print("2: Delete a a recipe")
	print("3: Print a recipe")
	print("4: Print the cookbook")
	print("5: Quit")

def get_recipe_info():
	print("\nPlease enter the new recipe's name:")
	name = input(">> ")
	print("\nPlease enter the new recipe's ingredients ", end='')
	print("separated by a comma and space):\n(example : bread, milk)")
	ingredients = input(">> ")
	ingredients = list(ingredients.split(', '))
	print("\nPlease enter the new recipe's type of meal:")
	meal = input(">> ")
	print("\nPlease enter the new recipe's cooking time in minutes:")
	prep_time = int(input(">> "))
	return name, ingredients, meal, prep_time

while True:
	display_menu()
	choice = input(">> ")
	if not choice.isnumeric() or \
		(choice.isnumeric() and (int(choice) > 5 or int(choice) < 1)):
		print('')
		print("This option does not exist, ", end='')
		print("please type the corresponding number.")
		print("To exit, enter 5.")
	elif int(choice) == 5:
		print("\nCookbook closed.")
		exit()
	elif int(choice) == 4:
		print_all_recipes()
	elif int(choice) == 3:
		print("\nPlease enter the recipe's name to get its details:")
		name = input(">> ")
		print_recipe(name)
		print('')
	elif int(choice) == 2:
		print("\nPlease enter the recipe's name to delete:")
		name = input(">> ")
		del_recipe(name)
	elif int(choice) == 1:
		name, ingredients, meal, prep_time = get_recipe_info()
		add_recipe(name, ingredients, meal, prep_time)
	