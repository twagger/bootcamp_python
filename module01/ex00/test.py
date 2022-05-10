from recipe import Recipe
from book import Book


# Test program

# OK test
print("\n\033[1;35m--{}: {}--\033[0m"
      .format("Test 1", "Recipe creation and print"))
tourte = Recipe("tourte", 3, ['Pate', 'oeufs'], "lunch", "c'est pas dur")
to_print = str(tourte)
print(to_print)

# KO test
print("\n\033[1;35m--{}: {}--\033[0m"
      .format("Test 2", "Recipe type error"))
error_tourte = Recipe("tourte", 3, 'Pate', "tarte", "c'est pas dur")
try:
    to_print_err = str(error_tourte)
except TypeError:
    print(">> ERROR : Type Error")

# Book creation
print("\n\033[1;35m--{}: {}--\033[0m"
      .format("Test 3", "Book creation"))
book = Book('Les recettes a la sauce Thomas')
book.get_recipe_by_name('tourte')

# Book add recipe
print("\n\033[1;35m--{}: {}--\033[0m"
      .format("Test 4", "Recipe addition in book"))
book.add_recipe(tourte)

# Book print recipe
print("\n\033[1;35m--{}: {}--\033[0m"
      .format("Test 5", "Recipe lookup in book and print"))
recipe = book.get_recipe_by_name('tourte')

# Add another lunch and print all lunches
print("\n\033[1;35m--{}: {}--\033[0m"
      .format("Test 6", "Add a new lunch and display all lunches"))
cake = Recipe("cake", 1, ['Pate', 'oeufs'], "lunch", "c'est pas dur non plus")
book.add_recipe(cake)
book.get_recipes_by_types('lunch')

# Error test on adding a recipe
print("\n\033[1;35m--{}: {}--\033[0m"
      .format("Test 7", "Adding a wrong type to the book"))
try:
    book.add_recipe('fries')
except TypeError:
    print(">> ERROR : Type Error")
