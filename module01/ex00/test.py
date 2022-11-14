"""Test pogram"""
from recipe import Recipe
from book import Book


# Test program
def main():
    """Test program"""
    # OK test
    print("\n\033[1;35m--Test 1: Recipe creation and print--\033[0m")
    tourte = Recipe("tourte", 3, ['Pate', 'oeufs'], "lunch", "c'est pas dur")
    print(tourte)

    # KO test
    print("\n\033[1;35m--Test 2: Recipe type error--\033[0m")
    error_tourte = Recipe("tourte", 3, 'Pate', "tarte", "c'est pas dur")
    try:
        print(error_tourte)
    except TypeError:
        print(">> ERROR : Type Error")

    # Book creation
    print("\n\033[1;35m--Test 3: Book creation--\033[0m")
    book = Book('Les recettes a la sauce Thomas')
    book.get_recipe_by_name('tourte')

    # Book add recipe
    print("\n\033[1;35m--Test 4: Recipe addition in book--\033[0m")
    book.add_recipe(tourte)

    # Book print recipe
    print("\n\033[1;35m--Test 5: Recipe lookup in book and print--\033[0m")
    book.get_recipe_by_name('tourte')

    # Add another lunch and print all lunches
    print(
        "\n\033[1;35m--Test 6: Add a new lunch and print all lunches--\033[0m")
    cake = Recipe("cake", 1, ['Pate', 'oeufs'],
                  "lunch", "c'est pas dur non plus")
    book.add_recipe(cake)
    book.get_recipes_by_types('lunch')

    # Error test on adding a recipe
    print("\n\033[1;35m--Test 7: Adding wrong type to the book--\033[0m")
    try:
        book.add_recipe('fries')
    except AttributeError:
        print(">> ERROR : wrong type, please provide a proper recipe")


main()
