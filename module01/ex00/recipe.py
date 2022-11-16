"""Recipe class"""


class Recipe:
    """Recipe class"""

    def __init__(self, name, cooking_lvl, cooking_time, ingredients,
                 recipe_type, description=''):
        """Constructor of therecipe"""

        # Emptyness check
        if (name is None
            or cooking_lvl is None
            or ingredients is None
            or recipe_type is None):
            raise AttributeError("All attributes but description "
                                 "are mandatory")

        # Type check
        if (not isinstance(name, str)
            or not isinstance(cooking_lvl, int)
            or not isinstance(cooking_time, int)
            or not isinstance(ingredients, list)
            or not isinstance(description, str)
            or not isinstance(recipe_type, str)):
            raise TypeError("Wrong type on recipe creation attributes")

        # Range check
        if (cooking_lvl < 1 or cooking_lvl > 5
            or cooking_time < 0
            or recipe_type not in ['starter', 'lunch', 'dessert']):
            raise AttributeError("An attibute constraint is not ok")

        # Creation of the recipe
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = ""
        txt += f'{self.name}: \n'
        txt += f'> Level : {self.cooking_lvl} / Type : {self.recipe_type}\n'
        txt += '> Ingredients : \n'
        for ingredient in self.ingredients:
            txt += f'  - {ingredient}\n'
        txt += f'> Description : \n - {self.description}'
        return txt
