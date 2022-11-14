"""Recipe class"""


class Recipe:
    """Recipe class"""

    def __init__(self, name, cooking_lvl, ingredients,
                 recipe_type, description=''):
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

    def __str__(self):
        """Return the string to print with the recipe info"""
        if not isinstance(self.ingredients, list):
            raise TypeError
        txt = ""
        txt += f'{self.name}: \n'
        txt += f'> Level : {self.cooking_lvl} / Type : {self.recipe_type}\n'
        txt += '> Ingredients : \n'
        for ingredient in self.ingredients:
            txt += f'  - {ingredient}\n'
        txt += f'> Description : \n - {self.description}'
        return txt
