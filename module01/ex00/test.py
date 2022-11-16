"""Test pogram"""
from recipe import Recipe
from book import Book


# Test program
def main():
    """Test program"""
    try:
        # OK test
        print("\n\033[1;35m--Test 1: Recipe creation and print--\033[0m")
        tourte = Recipe("tourte", 3, 10, ['Pate', 'oeufs'], "lunch",
                        "facile")
        print(tourte)

    except AttributeError as exc:
        print(f'ERROR: {exc}')
    except TypeError as exc:
        print(f'ERROR: {exc}')
    
    try:
        # KO test
        print("\n\033[1;35m--Test 2: Recipe type error--\033[0m")
        error_tourte = Recipe("tourte", 3, 10, 'Pate', "tarte", "Pas dur")
        print(error_tourte)

    except AttributeError as exc:
        print(f'ERROR: {exc}')
    except TypeError as exc:
        print(f'ERROR: {exc}')
    
    try:
        # Book creation but recipe ERROR
        print("\n\033[1;35m--Test 3: Book creation and error on print recipe "
              "that is not in it--\033[0m")
        book = Book('Les recettes a la sauce Thomas')
        book.get_recipe_by_name('tourte')
        
    except AttributeError as exc:
        print(f'ERROR: {exc}')
    except TypeError as exc:
        print(f'ERROR: {exc}')

    try:
        # Book add recipe
        print("\n\033[1;35m--Test 4: Recipe addition in book--\033[0m")
        tourte = Recipe("tourte", 3, 10, ['Pate', 'oeufs'], "lunch",
                        "facile")
        book.add_recipe(tourte)
        
    except AttributeError as exc:
        print(f'ERROR: {exc}')
    except TypeError as exc:
        print(f'ERROR: {exc}')

    try:
        # Book print recipe
        print("\n\033[1;35m--Test 5: Recipe lookup in book and print--\033[0m")
        book.get_recipe_by_name('tourte')
        
    except AttributeError as exc:
        print(f'ERROR: {exc}')
    except TypeError as exc:
        print(f'ERROR: {exc}')

    try:
        # Add another lunch and print all lunches
        print("\n\033[1;35m--Test 6: Add a new lunch and print all "
              "lunches--\033[0m")
        cake = Recipe("cake", 1, 5, ['Pate', 'oeufs'],
                    "lunch", "dur")
        book.add_recipe(cake)
        book.get_recipes_by_types('lunch')
        
    except AttributeError as exc:
        print(f'ERROR: {exc}')
    except TypeError as exc:
        print(f'ERROR: {exc}')

    try:
        # Error test on adding a recipe
        print("\n\033[1;35m--Test 7: Adding wrong type to the book--\033[0m")
        book.add_recipe('fries')

    except AttributeError as exc:
        print(f'ERROR: {exc}')
    except TypeError as exc:
        print(f'ERROR: {exc}')

main()
