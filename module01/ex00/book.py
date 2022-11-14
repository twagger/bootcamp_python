"""Book class"""
from datetime import date


class Book:
    """Recipe book class"""

    def __init__(self, name):
        self.name = name
        self.creation_date = date.today()
        self.last_update = self.creation_date
        self.recipe_list = {
            "starter": [],
            "lunch": [],
            "dessert": []
        }

    def get_recipe_by_name(self, name):
        """Prints a recipe with the name \texttt{name} \
        and returns the instance"""
        for _, recipes in self.recipe_list.items():
            if len(recipes) != 0:
                for recipe in recipes:
                    if recipe.name == name:
                        print(recipe)
                        return recipe
        print(">> ERROR : recipe not found")

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        for recipe_type, recipes in self.recipe_list.items():
            if recipe_type == recipe_type:
                for recipe in recipes:
                    print(f'- {recipe.name}')

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        try:
            for recipe_type, recipes in self.recipe_list.items():
                if recipe_type == recipe.recipe_type:
                    recipes.append(recipe)
                    return
            print(">> ERROR : type not found")
        except TypeError as exc:
            raise TypeError("This is not a recipe") from exc
